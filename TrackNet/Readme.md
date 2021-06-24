# Rally Segmentation based on Predict Result of TrackNet

## Introduction
The implematation method is based on the predict result of TrackNet. If number of frame that ball is visible in prediction > threshold in next fixed amount of frames, I regard it as the start of the rally. Similarily, if number of frame that ball is invisible in prediction > threshold in next fixed amount of frames, I regard it as the end of the rally.
 
## Install
Here are some packages the program needs. Please do the following command before you run the program.
(Or make sure they are already installed)
```sh
pip install numpy
```

## How to Run the Program
python rs_tracknet.py <input-predict-csv-path> <output-csv-filename>
For example :
```sh
python rs_tracknet.py TAI_Tzu_Ying_CHEN_Yufei_Malaysia_Masters_2020_Finals_predict.csv output.csv
```


