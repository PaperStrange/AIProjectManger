# File structure

Name | Description |
------------ | -------------
data/ | a folder containing data and data description
data/collector | a folder containing data description (e.g. data type) files
data/data_processed| a folder containing data files after processed
data/data_raw| a folder containing  raw data obtained by direct downloading or spiders like scrapy and so on
model/ | a folder containing jupyter notebooks of different modeling and descriptions (e.g. loss) for modeling
model/collector | a folder containing description files for modeling
model/save | a folder containing files of saved models
model/submit | a folder containing files of each submit for competition
timeline/ | a folder containing files indicating specific time arrangement of different competition period
utils/ | a folder containing scripts or jupyter notebooks for the whole data processing
utils/spiders | a folder containing spiders used for obtaining data online
utils/test | a folder containing several testing codes 
utils/test/test_edgetech | a folder containing testing codes for the application of edge technology
utils/test/test_situation | a folder containing testing codes for situational testing
utils/test/test_situation/collector | a folder containing description files of the testing
README.txt | a file containing all descriptions of this repository for new user
requirements.txt | a file containing all required packages of `python` for checking

# License

This repository is distributed under the GNU license.
