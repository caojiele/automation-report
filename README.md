# Automation Report

### [中文文档](README_zh.md)

Automation report is a set can solve many areas of industry involves the report generation requirements, the project is the first purpose is to simplify the manual process inside the company of a link, the main purpose is to the plane of the laboratory tests show data results combined with the corresponding report template batch generate a report(.pdf)。

The project running environment is suitable for all major operating systems, the author mainly introduces the production environment is Linux, use Python compiled languages, using PDFTK, WKHTML format conversion software format on the processing; Using Jinja2 template engine and MarkupSafe templates for HTML escape and tags automatically, at the same time efficient transform source into Python bytecode, speed up the template execution time;The existing table data batch rapidly into a database and combined with the Java file upload download page data, and other functions of system development.Finally realize the detecting data and combined with the matching report template, and generate the final report in PDF format.

## **Steps**

1、To convert data source after the `csv` file (file - save as file type (csv (comma separated) (*.csv) - save), with special programming code editor will confirm for utf-8 (in the case of the notebook, file - coding - utf-8 - save), csv file to be included in the data folder;

![show_1](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289304927-cd6366de-c156-4791-9ae8-14ec07acbf9e.png)

2、`cd <program path>`  

Enter the report file path (< program path > program path, such as：/home/jlcao/TP53/report）；
  
![show_2](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289310105-18cb3818-dc51-4dad-93eb-48aee6c8f725.png)

3、`virtualenv -p <path> <file name>`  

(such as：/usr/local/bin/python3.5 report）In the current directory to create the report folder, the folder is created in the virtual environment.Just create once;
  
![show_3](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289314650-7665ada7-dabf-4134-a136-6495142ed617.png)

4、`source report/bin/activate`      

Activate the virtual environment（virtualenv）；

![show_4](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289320059-a0fc4d29-3c8f-427b-8668-bd39704e9e6e.png)

5、`pip install -r requirements.txt`  

With `pip` installation depends on the environment, operation requirements.txt, just run once;

![show_5](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289328528-52c41177-3dac-4dd4-a3b4-5467d1b3e685.png)

6、`python gen_report.py --result-dir results data/xxx.csv` 

（xxx.csv data file for the data folder，such as：TP53-10个口腔拭子交付报告-20170710.csv） Executing this command, you can in the results folder to generate xxx.csv specified in the patients with all reports, report is stored in a separate folder, the folder name and read xxx.csv data source name.

![show_6](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289332975-c5ad43d0-8465-45e4-854b-e4339c7e9856.png)

![show_7](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289337742-61fe2ec5-2392-481b-bda8-10a15e68cfad.png)

![show_8](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289346397-ea3420b5-75c7-403d-aaaa-3b31c33851c6.png)

### After input the above command execution：

![show9](https://cdn.nlark.com/yuque/0/2019/gif/338441/1563290227027-bddb1241-f498-4750-aa54-e10778199fd6.gif)

## **Warning**

* ##### Read from the data source, "NO, the name, number" in the header of the data does not have any openings;
* ##### The Data in the file name can't name repetition;
* ##### The test data in the data folder can only be used for the objective of the test data, cannot be used for any other commercial way!!!!!!
* ##### Templates, TP53_pdf_templates two folders in the report template can only be used for the project report template, cannot be used for any other commercial way!!!!!!

## **About**

Hey, I'm Jack Cao, Java engineer, such as the Apache & Alibaba open source contributor, found in all the year round lot, Github, Gitee, zhihu, jianshu. At present is mainly responsible for group App backend development and maintenance, micro services infrastructure, infrastructure construction, Had the opportunity with Alibaba Health & PICC participate in large-scale project development; and my first [studio](https://caojiele.com/cooperation/) was founded in 2017, solve all kinds of company 「incurable diseases」, to achieve the demand of 「imagination」.Have been torn between the demand and development of struggle, as in a line of powerhouse, is still in development.

home：https://caojiele.com

jianshu：https://www.jianshu.com/u/faa01fa59ea3

zhihu：https://www.zhihu.com/people/wang-le-6-62/activities

imooc：https://www.imooc.com/u/4024769/articles

segmentfault：https://segmentfault.com/u/xiaomage_5c10d17d26987
    
Wechat: xiaomage_freestyle

 ![Wechat](https://cdn.nlark.com/yuque/0/2019/jpeg/338441/1562681958344-f9b0d53f-2be5-42d0-bdb6-b043d04fd856.jpeg)

More details, please scan qrcode：
  
 ![qrcode](https://cdn.nlark.com/yuque/0/2019/png/338441/1562683998026-42937005-a1e6-43cb-b51e-6aacf2952a56.png)
 
## **Resources**

* [Report automatic generation program](https://www.jianshu.com/p/86d4ef73ca72)
