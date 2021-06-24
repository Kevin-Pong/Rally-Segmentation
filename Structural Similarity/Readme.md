# Rally Segmentation based on structural similarity

## Introduction
The implematation method is based on what I observed in broadcasting video. When a rally is playing, the perspective seems to be the same in most time. And between rally and rally, the perspective may change. For example, closing up to the players, coaches, audiences, etc. Based on this idea, I use structural similarity to decide whether a frame is in a rally or not, and ragard consecutive frames as the same rally.    
 
## Install
Here are some packages the program needs. Please do the following command before you run the program.
(Or make sure they are already installed)
```sh
pip install opencv-python
pip install scikit-image
```

## How to Run the Program
python rs_ssim.py <input-video-path> <output-csv-filename>
For example :
```sh
python rs_ssim.py CHEN_Long_CHOU_Tien_Chen_Denmark_Open_2019_QuarterFinal.mp4 output.csv
```
After you run the program, it wiil first start to play the video. Please press 'q' at any time when the frame is the perspective when in a rally.

## Constraints
This implementation method only works for broadcasting video.
