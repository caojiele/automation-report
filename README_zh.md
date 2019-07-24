# 自动化生成报告

### [英文文档](README.md)

Automation report是一款可以解决很多行业领域中设涉及到报告生成的需求，本项目最开始的初衷是为公司内部简化人工流程的一个环节，主要实现目的是将实验室检测得出的下机数据结果与对应的报告模版批量结合生成报告(.pdf)。

该项目的运行环境适合所有主流操作系统，笔者主要介绍的生产环境是Liunx，使用的是Python编译语言，运用了pdftk、wkhtml等格式转化软件进行格式上的处理；并采用Jinja2模板引擎和MarkupSafe模板对html自动转义和标记，同时高效的将源码转换成Python字节码，加快模板执行时间；对现有表格数据批量快速带入数据库中并结合java页面数据文件上传下载等功能对系统开发实现。最终实现了检测数据与与之对应的报告模板相结合，并生成最后的pdf格式报告。

## **一、操作步骤**

1、将数据源转换完**csv**文件后（文件-另存为-文件类型（CSV(逗号分隔）（*.csv）-保存），用编程专用编辑器将编码确认为UTF-8（以小黑记事本为例，文件-编码-UTF-8-保存），将csv文件放入data文件夹中；

![show_1](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289304927-cd6366de-c156-4791-9ae8-14ec07acbf9e.png)

2、`cd <program path>`  

进入报告程序路径 （<program path>程序路径，如：/home/jlcao/TP53/report）；
  
![show_2](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289310105-18cb3818-dc51-4dad-93eb-48aee6c8f725.png)

3、`virtualenv -p <path> <文件夹名>`  

(如：/usr/local/bin/python3.5 report）在当前目录创建report文件夹，该文件夹即为创建的虚拟环境。只需创建一次；
  
![show_3](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289314650-7665ada7-dabf-4134-a136-6495142ed617.png)

4、`source report/bin/activate`      

激活虚拟环境（virtualenv）；

![show_4](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289320059-a0fc4d29-3c8f-427b-8668-bd39704e9e6e.png)

5、`pip install -r requirements.txt`  

用pip安装依赖环境，运行requirements.txt，只需运行一次；

![show_5](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289328528-52c41177-3dac-4dd4-a3b4-5467d1b3e685.png)

6、`python gen_report.py --result-dir results data/xxx.csv` 

（xxx.csv为data文件夹数据文件，如：TP53-10个口腔拭子交付报告-20170710.csv） 执行此命令，即可在results文件夹里生成xxx.csv中指定的患者所有报告，报告保存在独立文件夹中，该文件夹名与读取的xxx.csv数据源名对应。

![show_6](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289332975-c5ad43d0-8465-45e4-854b-e4339c7e9856.png)

![show_7](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289337742-61fe2ec5-2392-481b-bda8-10a15e68cfad.png)

![show_8](https://cdn.nlark.com/yuque/0/2019/png/338441/1563289346397-ea3420b5-75c7-403d-aaaa-3b31c33851c6.png)

### 输入以上命令后程序执行：

![输入以上命令后程序执行](https://cdn.nlark.com/yuque/0/2019/gif/338441/1563290227027-bddb1241-f498-4750-aa54-e10778199fd6.gif)

## **二、注意事项**

* ##### 读取的数据源中，表头中“NO,name,number”所对应的数据不能有空缺；
* ##### Data中的数据源文件名称不能重名；
* ##### test data文件夹中的数据只能用于本项目的测试数据，不能用于其他任何商业途径！！！
* ##### templates、TP53_pdf_templates两个文件夹中报告模板只能用于本项目的报告模板，不能用于其他任何商业途径！！！

#### 特此申明，概不负责！！！

## **三、关于作者**

Hey，我是小码哥，Java 攻城狮，Apache、Alibaba等开源组织贡献者之一，常年出没于 Github、Gitee、知乎、思否等地带。目前主要负责集团App后端开发以及维护、微服务技术实施、基础设施构建等工作，有幸参与过阿里健康、平安万家医疗等公司大型项目开发；17年有了自己的第一个[工作室](https://caojiele.com/cooperation/)，解决各种公司的「疑难杂症」，实现「天马行空」的需求。一直在需求和开发之间徘徊挣扎，任处于一线开发之中，绝招尚在开发。

个人主页：https://caojiele.com

简书：https://www.jianshu.com/u/faa01fa59ea3

慕课网手记：https://www.imooc.com/u/4024769/articles

segmentfault：https://segmentfault.com/u/xiaomage_5c10d17d26987
    
微信公众号: xiaomage_freestyle

 ![微信公众号](https://cdn.nlark.com/yuque/0/2019/jpeg/338441/1562681958344-f9b0d53f-2be5-42d0-bdb6-b043d04fd856.jpeg)

更多详情，请扫二维码：

 ![qrcode](https://cdn.nlark.com/yuque/0/2019/png/338441/1562683998026-42937005-a1e6-43cb-b51e-6aacf2952a56.png)

## **四、参考资料**

* [自动化生成报告程序](https://www.jianshu.com/p/86d4ef73ca72)
