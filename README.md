# The ATIS (Airline Travel Information System) Dataset
本仓库包含了 ATIS Dataset(数据集)，并提供了读取脚本和示例代码。

## 数据统计
| 样本数 | 词汇数 | 实体数 | 意图数 |
| --- | --- | --- | --- |
| 4978(训练集)+893(测试集) | 943 | 129 | 26 |

## 下载

| 数据格式 | 训练集 | 测试集 |
| --- | --- | --- |
| Python 3 Pickle 格式 | [atis.train.pkl](data/raw_data/ms-cntk-atis/atis.train.pkl) | [atis.test.pkl](data/raw_data/ms-cntk-atis/atis.test.pkl) |
| Rasa NLU JSON 格式 | [train.json](data/standard_format/rasa/train.json) | [test.json](data/standard_format/rasa/test.json) |



## Credit
* 本项目的原始数据集来自 [ATIS DataSet by siddhadev](https://www.kaggle.com/siddhadev/atis-dataset)，部分代码亦来自此处。
    * NOTE: `ATIS DataSet by siddhadev` 数据集则来自于 [MicroSoft CNTK Examples](https://github.com/Microsoft/CNTK/tree/master/Examples/LanguageUnderstanding/ATIS/Data)

## 同类项目
* https://github.com/mesnilgr/is13 也提供了 ATIS 数据集，但该数据集只有实体数据没有意图数据。
