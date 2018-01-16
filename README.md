# Web-Opinion-Miner-DeepLearning
![Version](https://img.shields.io/badge/Version-0.01-brightgreen.svg?style=for-the-badge)   ![We Get This](https://img.shields.io/badge/We%20Got%20This-Yes-brightgreen.svg?style=for-the-badge)  ![Tests](https://img.shields.io/badge/Tests-1%2F1-brightgreen.svg?style=for-the-badge)  ![Lines Count](https://img.shields.io/badge/Lines-152444-brightgreen.svg?style=for-the-badge)
Webscraping &amp; Word-to-Vectors: Making sense of democratic opinions

*Early-Stage Project Subject to Change of Liscence and Contents*

Project Description
---- 

The idea of this project is to use Deep Neural Nets that implement *Word-to-Vector* analysis solutions in order to make sense of text formulated in natural language. For example, public policy reforms like in health care and taxes consist of a large variety of issues and opinions. The idea is to explore how deep neural nets can be used to analyze written text to map out the qualitative opinion landscape of the different issues involved in these issues.

Goals of this Project includes:
-  <Current Stage> Integrate and implement upon Frameworks such as *beautifulSoup* and *Scrapy* to develope a robust automated web article scrapper module that can filter and fetch non-repetitive newspaper Articles/Text Content from pre-approved sources according to pre-configured topics and keywords. 
-  <Current Stage> Integrate and Explore *Word2Vector* with *TensorFlow* deep neural nets for analysis, categorization, and summurization of Online Opinions presented in forms of (includes but not limited to) Newspaper Articles, Blogs, Social Media
-  Implement and train Deep Neural Nets that perform necessary analysis, categorization, and implicit summurization with input from Word2Vector module
-  Integrate and Implement upon Frameworks such as *TextRank* to develop robust deeplearning and NLP solutions to Localize Opinions/thesis sentences inside a text Articles.
-  Develope NLP deep learning for extraction and summarization with Natural Language Genration of Articles/Text Content, 
-  Develope non-technical user friendly Website integration of our backend service with modern and pragmatic UI design.
-  *Optional* Develope Cross-Platform Xamarin app with .Net Frameworks for iOS/Android/Winphone and Desktop.


List of library Sources and Licenses
---- 
*TensorFlow*
Licensed under the Apache License, Version 2.0 (the "License") from https://www.tensorflow.org/

*Scrapy* 
Open source library by Scrapy developers from https://scrapy.org/

*BeautifulSoup*
CCl icense Library by Leonard Richardson from https://www.crummy.com/software/BeautifulSoup/

*Word2Vector*
Mdel by Mikolov et al.

*TextRank*
Python Implementation of TextRank by Paco Nathan at https://github.com/ceteri/pytextrank
Algorithm based on the 
`Mihalcea 2004 <http://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf>`

*Article Extractor*

*Data Parser*


Dependencies and Installation
---- 
TensorFlow with Anaconda:
``
conda install -c conda-forge tensorflow
``

Scrapy with Anaconda:
``
conda install -c conda-forge scrapy
``

License
---- 
