[中文版本的 README](README.md)
------------------------------

# The ATIS (Airline Travel Information System) Dataset
This repository contains ATIS Dataset in Python pickle format and Rasa NLU JSON format ([https://rasa.com/docs/nlu/dataformat/#json-format](https://rasa.com/docs/nlu/dataformat/#json-format)), also this project provide codes to show how extract data from pickle file.

## Data Sample
```text
   0:         flight: BOS i want to fly from boston at 838 am and arrive in denver at 1110 in the morning EOS
                              BOS                                        O
                                i                                        O
                             want                                        O
                               to                                        O
                              fly                                        O
                             from                                        O
                           boston                      B-fromloc.city_name
                               at                                        O
                              838                       B-depart_time.time
                               am                       I-depart_time.time
                              and                                        O
                           arrive                                        O
                               in                                        O
                           denver                        B-toloc.city_name
                               at                                        O
                             1110                       B-arrive_time.time
                               in                                        O
                              the                                        O
                          morning              B-arrive_time.period_of_day
                              EOS                                        O
```

## Summary of Data
| Sample Number | Vocabulary Size | Number of Slots | Number of Intents |
| --- | --- | --- | --- |
| 4978(Training set)+893(Testing set) | 943 | 129 | 26 |

## Sample Code
[summary_data.py](summary_data.py) include codes to read data from raw data file，user can learn how to read data.

## Download Data

| Data Format | Training Set | Testing Set |
| --- | --- | --- |
| Python 3 Pickle Format | [atis.train.pkl](data/raw_data/ms-cntk-atis/atis.train.pkl) | [atis.test.pkl](data/raw_data/ms-cntk-atis/atis.test.pkl) |
| Rasa NLU JSON Format | [train.json](data/standard_format/rasa/train.json) | [test.json](data/standard_format/rasa/test.json) |



## Credit
* The origin data set come from [ATIS DataSet by siddhadev](https://www.kaggle.com/siddhadev/atis-dataset)，some codes also copied from here。
    * NOTE: `ATIS DataSet by siddhadev` comes from [MicroSoft CNTK Examples](https://github.com/Microsoft/CNTK/tree/master/Examples/LanguageUnderstanding/ATIS/Data)

## Similar Projects
* https://github.com/mesnilgr/is13 also provide ATIS dataset, but only provide slots data without intent.
