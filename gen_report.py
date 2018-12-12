#!/usr/bin/env python
#-*-coding:utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import os, sys, argparse, datetime, shutil, time, subprocess

working_dir = os.path.abspath((os.path.dirname(__file__)))
template_dir = os.path.join(working_dir, 'templates')
pdf_template_dir = os.path.join(working_dir, 'TP53_pdf_templates')
env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
pdf_files = ["TP53-0.pdf", "TP53-1.pdf", "TP53-2.pdf", "TP53-3.pdf", "TP53-4.pdf", "TP53-5.pdf", "TP53-6.pdf", "TP53-7.pdf", "TP53-8.pdf", "TP53-9.pdf"]

class HeaderError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def check_header(header, standard_header):
    for item in standard_header:
        if item not in header:
            raise HeaderError("文件(Header)必须包含以下字段： %s" % item)

def render_template(template, **kwargs):
    template = env.get_template(template)
    return template.render(**kwargs)

def copy_template_files(template_dir, result_dir):
    dependence_files = ["TP53-1.css", "TP53-4.css", "TP53-5.css", "picture_1.png", "picture_2.png", "picture_3.png", 
                   "picture_4.png", "picture_5.png", "picture_6.png", "picture_7.png"]
    temp_dependence_files = [ os.path.join(template_dir, item) for item in dependence_files ]
    result_dependence_files = [ os.path.join(result_dir, item) for item in dependence_files ]
    for src, dest in zip(temp_dependence_files, result_dependence_files):
        shutil.copyfile(src, dest)

def copy_pdf_templates(template_dir, result_dir):
    dependence_files = ["TP53-0.pdf", "TP53-2.pdf", "TP53-3.pdf", "TP53-6.pdf", "TP53-7.pdf", "TP53-8.pdf", "TP53-9.pdf"]
    temp_dependence_files = [ os.path.join(template_dir, item) for item in dependence_files ]
    result_dependence_files = [ os.path.join(result_dir, item) for item in dependence_files ]
    for src, dest in zip(temp_dependence_files, result_dependence_files):
        shutil.copyfile(src, dest)    

def check_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def gen_report(data_file_obj, result_dir, data_file_name=None):
    templates = ['TP53-1.html', 'TP53-4.html', 'TP53-5.html']
    file_header = ["NO", "form", "name", "number", "sex", "age", "result"]

    if data_file_name:
        pdf_results_dir = os.path.join(result_dir, os.path.basename(data_file_name).replace('.csv', ''))
    else:
        pdf_results_dir = os.path.join(result_dir, 'pdf')
    check_dir(pdf_results_dir)

    header = data_file_obj.readline()
    header = [i.strip('.\n\r" ') for i in header.split(',')]
    print("header: %s" % str(header))
    check_header(header, file_header)

    for line in data_file_obj:
        content = [i.strip('.\n\r" ') for i in line.split(',')]
        if len(content) != len(header):
            print("列数不相等")
            sys.exit(1)
        else:
            patient_info = dict(zip(header, content))
            print("患者信息：%s" % patient_info)
            filename = patient_info.get('NO') + patient_info.get('name') + patient_info.get('number')
            patient_info['report_date'] = time.strftime("%Y.%m.%d", time.localtime()) 
            for template in templates:
                template_file = render_template(template, patient_info=patient_info)
                patient_result_dir = os.path.join(result_dir, filename)
                if not os.path.exists(patient_result_dir):
                    os.makedirs(patient_result_dir)
                    copy_template_files(template_dir, patient_result_dir)
                result_file = os.path.join(patient_result_dir, template)
                with open(result_file, 'w') as output:
                    output.write(template_file)
                pdf_dir = os.path.join(patient_result_dir, 'pdf')
                if not os.path.exists(pdf_dir):
                    os.makedirs(pdf_dir)
                subprocess.call(["wkhtmltopdf", 
                                 os.path.join(patient_result_dir, template), 
                                 os.path.join(pdf_dir, "%s.pdf" % template.replace('.html', ''))])
            copy_pdf_templates(pdf_template_dir, os.path.join(patient_result_dir, "pdf"))

            path_maker = lambda dir_name: os.path.join(pdf_dir, dir_name)
            input_pdfs = list(map(path_maker, pdf_files))
            
            input_pdfs.insert(0, "pdftk")
            input_pdfs.extend(["cat", "output", os.path.join(pdf_results_dir, "%s.pdf" % filename)])
            print(input_pdfs)
            subprocess.call(input_pdfs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="报告生成器")
    parser.add_argument('--result-dir', default="results", help="结果目录")
    parser.add_argument('data_file', help="患者结果文件")

    args = parser.parse_args()

    result_dir = args.result_dir
    data_file = args.data_file
    with open(data_file, 'r') as data_file_obj:
        gen_report(data_file_obj, result_dir, data_file_name=data_file)



