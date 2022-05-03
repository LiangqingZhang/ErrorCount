# ErrorCount
An algorithm for predicting the error rate of workers.

## Model
![alt model1](https://github.com/LiangqingZhang/ErrorCount/blob/main/model1.png)
![alt model2](https://github.com/LiangqingZhang/ErrorCount/blob/main/model2.png)

## Overview
Here we provide the implementation of a ErrorCount. The repository is organised as follows:
- `` put you data in main derictory;
- `model.py` implementation of ErrorCount;
- `gen_feature.py` generate features from data;


Finally, `run.py` puts all of the above together and may be used to execute a full training run on you data by executing `python run.py 1`, where "1" is the modeltype, the options is 1 or 2.


## Dependencies

The script has been tested running under Python 3.6.3, with the following packages installed (along with their dependencies):

- `numpy`
- `pandas`
- `Chinese_calendar`
- `torch`

## Acknowledge
This work was supported by the National Key R&D Program of China under Grant No. 2020AAA0103804 and partially supported by grants from the National Natural Science Foundation of China (No.72004021). This work belongs to the University of science and technology of China.


