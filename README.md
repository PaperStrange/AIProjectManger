# Introduction

This repository is a try to `design` a proper project structure used for kaggle competition or fun data mining

# :file_folder: Structure
Name | Description |
------------ | -------------
data/ | a folder containing data and data description
data/collector | a folder containing data description (e.g. data type) files
data/data_processed| a folder containing data files after processed
data/data_raw| a folder containing  raw data obtained by direct downloading or spiders like scrapy and so on
 |
model/ | a folder containing jupyter notebooks of different modeling and descriptions (e.g. loss) for modeling
model/collector | a folder containing description files for modeling
model/save | a folder containing files of saved models
model/submit | a folder containing files of each submit for competition
 |
timeline/ | a folder containing files indicating specific time arrangement of different competition period
|
utils/ | a folder containing scripts or jupyter notebooks for the whole data processing
utils/spiders | a folder containing spiders used for obtaining data online
utils/test_edgetech | a folder containing scripts for applying edge technology to this project and evaluate
utils/test_situation | a folder containing scripts for applying other situations which are more likely to happen in dairy life for this project and evaluate
utils/test_situation/collector | a folder containing description files of the above testing
|
README.txt | a file containing all descriptions of this repository for new user
requirements.txt | a file containing all required packages of `python` for checking

# :memo: Goals which i want to achieve:

* a structure containing full procedures of deploying model to a specific reality problem
* a structure containing efficient tools for the whole data processing for convenient code reconstruct

# :memo: Functions which is not for consideration for the moment

* `automatcally` connects data processing and modeling
* deploy online by python package like tensorflow, flask, Django .etc

# :memo: TODOs
* during kaggle completion, beautify the structure

# License

This repository is distributed under the GNU license.