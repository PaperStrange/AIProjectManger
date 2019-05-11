:ballot_box_with_check: 2019/3/12: complete the structure 

:arrow_forward:(Waiting) TODO 2019/3/18: display the structure tree using mind map

:arrow_forward:(Waiting) TODO 2019/4/1: balance the customer need and programming design (e.g the use of cutomer story method)

:bulb:&:warning: TODO 2019/5/11: (1) modify the template files in each "collector" folder; 

:bulb: TODO 2019/4/22: need a markdown file to display findings by story style

## Proposed project structure (the same as what is shown in "template" branch)<a name="structure"></a>

Name | Description |
------------ | -------------
data/ | a folder containing data and data description
data/collector | a folder containing data description (e.g. data type) files
data/data_processed| a folder containing data files after processed
data/data_raw| a folder containing  raw data obtained by direct downloading or spiders like scrapy and so on
-- | --
model/ | a folder containing jupyter notebooks of different modeling and descriptions (e.g. loss) for modeling
model/collector | a folder containing description files for modeling
model/collector/tricks_collector.md | a markdown file to record tricks applied when modeling as well as the result
model/saved_models | a folder containing files of saved models
model/test.ipynb | a jupyter notebook containing test part of a modeling procedure
model/train_valid.ipynb | a jupyter notebook containing train and validation parts of a modeling procedure
-- | --
submit/ | a folder containing submitted csv files and result record files
submit/results.md | a markdown file to record each submit with model usage, scores etc. 
-- | --
timeline/ | a folder containing governing files to keep trace of competition
timeline/Timeline_Year.Month.Day_who.ppt | a template to show a possible timeline government method
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

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

This repository is distributed under the GNU license.

Must give credit to everyone whoeve commited to the open community! Anyway, feel free to use the code here as you would like!
