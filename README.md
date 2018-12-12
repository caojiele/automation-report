# 自动化生成报告(Automation report)
>自动化生成报告程序是可以解决很多行业领域中设涉及到报告生成的需求，本项目最开始的初衷是公司内部简化人工流程的一个环节，主要实现目的是将实验室检测得出的下机数据结果与对应的报告模版批量结合生成报告(.pdf)。
#
>该项目的运行环境适合所有主流操作系统，笔者主要介绍的生产环境是Liunx，使用的是Python编译语言，运用了pdftk、wkhtml等格式转化软件进行格式上的处理；并采用Jinja2模板引擎和MarkupSafe模板对html自动转义和标记，同时高效的将源码转换成Python字节码，加快模板执行时间；对现有表格数据批量快速带入数据库中并结合java页面数据文件上传下载等功能对系统开发实现。最终实现了检测数据与与之对应的报告模板相结合，并生成最后的pdf格式报告。
## 一、操作步骤
1、将数据源转换完csv文件后（文件-另存为-文件类型（CSV(逗号分隔）（*.csv）-保存），用编程专用编辑器将编码确认为UTF-8（以小黑记事本为例，文件-编码-UTF-8-保存），将csv文件放入data文件夹中；
![show_1](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_1.png)
2、cd <program path>  进入报告程序路径 （<program path>程序路径，如：/home/jlcao/TP53/report）；
![show_2](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_2.png)
3、virtualenv -p <path> <文件夹名>  (如：/usr/local/bin/python3.5 report）在当前目录创建report文件夹，该文件夹即为创建的虚拟环境。只需创建一次；
![show_3](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_3.png)
4、source report/bin/activate      激活虚拟环境（virtualenv）；
![show_4](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_4.png)
5、pip install -r requirements.txt  用pip安装依赖环境，运行requirements.txt，只需运行一次；
![show_5](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_5.png)
6、python gen_report.py --result-dir results data/xxx.csv （xxx.csv为data文件夹数据文件，如：TP53-10个口腔拭子交付报告-20170710.csv） 执行此命令，即可在results文件夹里生成xxx.csv中指定的患者所有报告，报告保存在独立文件夹中，该文件夹名与读取的xxx.csv数据源名对应。
![show_6](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_6.png)
![show_7](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_7.png)
![show_8](https://raw.githubusercontent.com/caojiele/Automation-report/master/img_folder/show_8.png)

## 二、注意事项
1、读取的数据源中，表头中“NO,name,number”所对应的数据不能有空缺；
2、Data中的数据源文件名称不能重名；
### 3、test data文件夹中的数据只能用于本项目的测试数据，不能用于其他任何商业途径！！！
### 4、templates、TP53_pdf_templates两个文件夹中报告模板只能用于本项目的报告模板，不能用于其他任何商业途径！！！
### 特此申明，概不负责

## **三、关于作者**
#### 微信公众号：
![微信公众号](https://raw.githubusercontent.com/caojiele/resume/master/img-folder/qrcode.jpg)
#### 简书链接：[简书个人主页](https://www.jianshu.com/u/faa01fa59ea3)
## **7、参考资料**
