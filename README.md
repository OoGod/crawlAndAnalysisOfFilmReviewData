# crwalAndAnalysisOfFilmReviewData
基于python的影评数据爬取和分析研究(此项目用于毕业设计)

*由于复制外文pdf文件文本有许多空格，于是制作了del_spa.py用于去复制过去的文本空格*

使用方式
```
# 不制定文件名默认去machine.txt的空格，并输出到output.txt中，这里举例去test.txt中的空格
python del_spa.py test.txt
```
_翻译文件_
```
# 翻译文本并输出到test1.txt中
python translate.py machine.txt
```
_去空格并且翻译文本_
```
# 去掉文本之间的换行符，并且翻译文件最后输出到test1.txt中
python run_tran.py machine.txt
```

代码改进
```
很久前的代码,可以了解String类的split(),lstrip()方法进行改进
```
