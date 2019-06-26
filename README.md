### Table of Contents

1. [Installation and Instruction](#installation)
2. [Project Motivation](#motivation)
3. [Branch Description](#branch)
4. [A proposed project structure](#structure)
5. [Instruction to deploy](#instruction)
6. [To-dos](#To-dos)
7. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation and Instruction<a name="installation"></a>

Nothing need to be installed or updated to run this project.

This project mainly focuses on a disciplined and better-arranged AI project structure. By default, project is divided in sicx parts: *data*, *download*, *model*, *submit(for competitions like kaggle)*, *timeline*, *utils*. 

Commonly, whole steps of AI project include three parts such as data pre-processing, model training, testing, deploying and post (by different platforms, like website or APP). Corresponding to different steps, different folder is expected to be used. 

* For the first data processing step, folder *data* is used to store raw (data_raw child folder) or processed data (data_processed child folder) as well as processing description files or tricks (collector child folder). Folder *download* is used to store the downloaded model kernels in each child folders assigned by the correlated kernel name + platform name; 
* For the second training, testing, deploying step, folder *model* is used to store save models (saved_models child folder), jupyter notebooks, model tuning tricks or experiences (collector child folder). 
* For the third post step, folder *submit* is used to store all kinds of posting files. Especially for AI competition, each submit could be recorded in *results.md*. 

Besides, folder *timeline* is used for the project management, for example, storing different versions of project timeline files. Some common-used tools to accelerate the construction of AI project are stored in folder *utils* which is easy to be expanded as you like. Further descriptions for each folder or child folder, child file are listed in the sheet below.

## Project Motivation<a name="motivation"></a>

In this project, I was interested in how to create a common-used file structure to make machine learning projects more organized and more readable.

## Branch Description<a name="branch"></a>

Master branch only contains the general descriptions of this project.

Full version of this file structure is introduced in "template" branch in detail. "develop" branch contains TODOs which haven't been checked and reviewed. The applications of this file structure are displayed in several branches named by "ie_xxx" respectively. 

## A proposed project structure (the same as what is shown in "template" branch)<a name="structure"></a>

Name | Description |
------------ | -------------
data/ | a folder containing data and data description
data/collector | a folder containing data description (e.g. data type) files
data/data_processed| a folder containing data files after processed
data/data_raw| a folder containing  raw data obtained by direct downloading or spiders like scrapy and so on
-- | --
model/ | a folder containing jupyter notebooks of different modeling and descriptions (e.g. loss) for modeling
model/collector | a folder containing description files for modeling
model/save | a folder containing files of saved models
model/submit | a folder containing files of each submit for competition
-- | --
timeline/ | a folder containing files indicating specific time arrangement of different competition period
-- | --
utils/ | a folder containing scripts or jupyter notebooks for the whole data processing
utils/pipeline | a folder containing template python scripts used for a quick start of pipline construction
utils/pipeline | a python script to show the example of [ETL pipeline](https://en.wikipedia.org/wiki/Extract,_transform,_load) using sklearn pakage
utils/pipeline/pipeline.md | a markdown file to record my design thinking of pipeline
utils/spiders | a folder containing spiders used for obtaining data online
utils/test | a folder containing several testing codes 
utils/test/situation_test | a folder containing codes for situational test
utils/test/situation_test/nexus.ipynb | a jupyter notebook containing records for different nexus in a specific business situation
utils/test/unit_test | a folder containing unit test codes for better TDD
utils/test/unit_test/test_data_processing.py | a python script containing unit test codes for data processing procedure
utils/data_process.ipynb | a jupyter notebook containing all needed data processing process during the competition
utils/data_process_tricks.ipynb | a jupyter notebook containing all useful trciks of python packages learned during the competition
-- | --
README.txt | a file containing all descriptions of this repository for new user
requirements.txt | a file containing all required packages of `python` for checking
coding_style.md | a markdown file to record my design thinking of coding style such as name, comment and docstring, re-construction
 
## Instruction to deploy<a name="instructions"></a>

1. clone or download all repository with **master** branch

2. read all descriptions listed in the section "A proposed project structure" of this README.md file carefully, make sure get the idea of the usage of each folder and each file.

3. Guided by the management of your project, use the specific folder and file templates to accelerate the accomplishment of specific tasks. For example , when preprocessing data , use the template notebook "data_process . Ipynb " and "data_process_tricks . Ipynb " located in " utils " folder to assist programming , while building model , the folder " model " and other notebooks in " utils " folder will be helpful .

## To-dos<a name="To-dos"></a>

:memo: Goals which i want to achieve at now:

* minimize the cost of familiar and maximize the flexiblity

:memo: Functions which is not for consideration for the moment

* connects data processing and modeling
* deploy this organizations online by flask, Django .etc

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

This repository is distributed under the GNU license.

Must give credit to everyone whoeve commited to the open community! Anyway, feel free to use the code here as you would like!
