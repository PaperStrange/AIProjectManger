## Results
|Preprocessing|Model|Result (metric name)|
|:--:|:--:|:--:|
|[Santander LightGBM Baseline](https://www.kaggle.com/chocozzz/santander-lightgbm-baseline-lb-0-899)|--|0.899(Asserted))|
||lgb_baseline_hzq.csv: LightGBM, recurrent|0.898|
||Submit file B: model, change|score 2|
|[Santander EDA and Prediction](https://www.kaggle.com/gpreda/santander-eda-and-prediction)|--|0.9(Asserted)|
||Santander_EDA_and_Prediction_ori_hzq.csv: model, recurrent|0.9|
||Santander_EDA_and_Prediction_mod_hzq_20190315.csv: LightGBM, over-sampling|0.814|
|[LGB 2 leaves + augment](https://www.kaggle.com/jiweiliu/lgb-2-leaves-augment)|LightGBM|0.901|
|--|Stacking (LightGBM, XGBoost, Catboost)|0.897|
|--|XGBoost|0.899|
|--|CatBoost|0.895|
