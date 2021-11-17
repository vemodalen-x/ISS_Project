# ITSS_Project

## Introduction

This is a competition in Kaggle named [NFL Health & Safety - Helmet Assignment](https://www.kaggle.com/c/nfl-health-and-safety-helmet-assignment). And we use it as our ITSS project topic.

The goal of this competition is to give both position and label to each player in the video.

In this work, we focus on the following three targets.
1. Using computer vision techniques to identify and locate player helmets. 
2. Using optimization methods to match helmet boxes to NGS data based on relative distances.
3. Tracking of helmets throughout the duration of a play and assigning labels to these tracks.

The overall pipeline is shown here.
![overall pipeline](/images/overall.png)


## Dataset and Helper code

Dataset we used is provided by Kaggle.
https://www.kaggle.com/c/nfl-health-and-safety-helmet-assignment/data

Helper code can be found here, including the evaluation code, check submission code, generate video code, etc.
https://github.com/RobMulla/helmet-assignment

## Final Result

The accuracy is about 64%, and the weighted accuracy is about 50%.

## File Structure

```
├── detection
|   ├── data_prepare  
│   ├── output_nfl               
│   ├── train                                                 
│   ├── baseline.csv                              // detection output file
│   ├── baseline_nms95.csv                        // detection output file, nms = 0.95
│   └── 58102_002798_Endzone_fps50_detection.mp4  // detection output video
|
├── mapping
│   ├── gradient-descent.ipynb                    // do mapping use gradient descent         
    ├── km.ipynb                                  // do mapping use KM-algorithm 
│   └── mapping.csv                               // the output csv file of the mapping step
|                   
├── mapping+tracking                   
│   ├── mapping+tracking.ipynb                    // combine the mapping and tracking
│   ├── ground_truth_pred_58102_002798_Endzone.mp4// ground truth
│   ├── labeled_58102_002798_Endzone.mp4          // our predicted, not showing correct or not, just the label
│   └── our_pred_58102_002798_Endzone.mp4         // our predicted, green boxes means correct
|
└── miscellaneous                                 // contains some files like data exploration, 
    ├── ...
    └── NFL_final.ipynb                           // combine three parts together

```

