## File structure

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

## Good Habits

* Use logging pythob package to create log during the process 

* Use yapf or pylint python package to find bugs and style problems in Python source code

* Use pytest python package to apply unit test or operate TDD 

# License

This repository is distributed under the GNU license.
