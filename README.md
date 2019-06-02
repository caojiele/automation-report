# Automation report

### [中文文档](README_zh.md)

Automation report is a set can solve many areas of industry involves the report generation requirements, the project is the first purpose is to simplify the manual process inside the company of a link, the main purpose is to the plane of the laboratory tests show data results combined with the corresponding report template batch generate a report(.pdf)。

The project running environment is suitable for all major operating systems, the author mainly introduces the production environment is Linux, use Python compiled languages, using PDFTK, WKHTML format conversion software format on the processing; Using Jinja2 template engine and MarkupSafe templates for HTML escape and tags automatically, at the same time efficient transform source into Python bytecode, speed up the template execution time;The existing table data batch rapidly into a database and combined with the Java file upload download page data, and other functions of system development.Finally realize the detecting data and combined with the matching report template, and generate the final report in PDF format.

## **Steps**

1、To convert data source after the `csv` file (file - save as file type (csv (comma separated) (*.csv) - save), with special programming code editor will confirm for utf-8 (in the case of the notebook, file - coding - utf-8 - save), csv file to be included in the data folder;

![show_1](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_1.png)

2、`cd <program path>`  

Enter the report file path (< program path > program path, such as：/home/jlcao/TP53/report）；
  
![show_2](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_2.png)

3、`virtualenv -p <path> <file name>`  

(such as：/usr/local/bin/python3.5 report）In the current directory to create the report folder, the folder is created in the virtual environment.Just create once;
  
![show_3](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_3.png)

4、`source report/bin/activate`      

Activate the virtual environment（virtualenv）；

![show_4](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_4.png)

5、`pip install -r requirements.txt`  

With `pip` installation depends on the environment, operation requirements.txt, just run once;

![show_5](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_5.png)

6、`python gen_report.py --result-dir results data/xxx.csv` 

（xxx.csv data file for the data folder，such as：TP53-10个口腔拭子交付报告-20170710.csv） Executing this command, you can in the results folder to generate xxx.csv specified in the patients with all reports, report is stored in a separate folder, the folder name and read xxx.csv data source name.

![show_6](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_6.png)

![show_7](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_7.png)

![show_8](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_8.png)

### After input the above command execution：

![show9](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/Dynamic_figure1.gif)

## **Warning**

* ##### Read from the data source, "NO, the name, number" in the header of the data does not have any openings;
* ##### The Data in the file name can't name repetition;
* ##### The test data in the data folder can only be used for the objective of the test data, cannot be used for any other commercial way!!!!!!
* ##### Templates, TP53_pdf_templates two folders in the report template can only be used for the project report template, cannot be used for any other commercial way!!!!!!

## **About**

Hey, I'm Jack Cao, Java engineer, as a member in Apache Dubbo Committer, such as the Apache & Alibaba open source contributor, found in all the year round lot, Github, Gitee, zhihu, jianshu. At present is mainly responsible for group APP back-end development and maintenance, micro services infrastructure, infrastructure construction, Had the opportunity with Alibaba Health & PICC participate in large-scale project development; and my first [studio](https://caojiele.com/cooperation/) was founded in 2017, solve all kinds of company 「incurable diseases」, to achieve the demand of 「imagination」.Have been torn between the demand and development of struggle, as in a line of powerhouse, is still in development.

home：https://caojiele.com

jianshu：https://www.jianshu.com/u/faa01fa59ea3

zhihu：https://www.zhihu.com/people/wang-le-6-62/activities

imooc：https://www.imooc.com/u/4024769/articles

segmentfault：https://segmentfault.com/u/xiaomage_5c10d17d26987
    
Wechat:

 ![Wechat](https://raw.githubusercontent.com/caojiele/resume/master/img-folder/qrcode.jpg)

## **Resources**

* [Report automatic generation program](https://www.jianshu.com/p/86d4ef73ca72)
