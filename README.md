# Infinite Zooming
Homework4 of NTHU CVFX. Feature matching for moving forward and infinite zooming effect.


- V (5%)Take a sequence of moving-forward images in NTHU campus.
- V (5%)Show feature extraction and matching results between two images
- (20%)implement different feature extrators, e.g. SIFT, SURF, and compare the results
- (10%)Perform image alignment and generate infinite zooming effect
- (10%)exploit creativity to add some image processing to enhance effect. You can use photoshop to do some effects, such as bluring or coloring.


## Part 1: Feature Detector Comparison

### 1.1 Benchmark preparation
In below, we will use 4 types of input images to compare the results. The 4 types are depicted in below 4 columns:

|      | Moving forward | Pitch rotation | Roll rotation | Yaw rotation |
| :--: | :------------: | :------------: | :-----------: | :----------: |
| img1 | ![](imgs/input_compare/source.png) | ![](imgs/input_compare/source.png) | ![](imgs/input_compare/source.png) | ![](imgs/input_compare/source.png)
| img2 | ![](imgs/input_compare/forward.png) | ![](imgs/input_compare/pitch.png) | ![](imgs/input_compare/roll.png) | ![](imgs/input_compare/yaw.png) |

Among the 4 types, the source image are all the same but the target images for feature matching are taken such that they micmic the camera *moving forward, pitch rotation, roll rotation, yaw rotation* respectively.

### 1.2 Comparing different detectors and matching algorithms setting
The source codes generating all the below results is `feature_matcher.py`. We draw 50 matched features with the lowest distance for easier comparing the results by human eyes.

#### Case: Moving forward
| | Brute Force Matching w/ Cross Check | Brute Force Matching w/ Ratio Test |
| :--: | :------------------: | :-----------------: |
| SIFT | ![](imgs/output_compare/forward_sift_bf_crosscheck.jpg) | ![](imgs/output_compare/forward_sift_bf_ratiotest.jpg) |
| SURF | ![](imgs/output_compare/forward_surf_bf_crosscheck.jpg) | ![](imgs/output_compare/forward_surf_bf_ratiotest.jpg) |
| SURF extended | ![](imgs/output_compare/forward_surfext_bf_crosscheck.jpg) | ![](imgs/output_compare/forward_surfext_bf_ratiotest.jpg) |
| ORB | ![](imgs/output_compare/forward_orb_bf_crosscheck.jpg) | ![](imgs/output_compare/forward_orb_bf_ratiotest.jpg) |

#### Case: Pitch rotation
| | Brute Force Matching w/ Cross Check | Brute Force Matching w/ Ratio Test |
| :--: | :------------------: | :-----------------: |
| SIFT | ![](imgs/output_compare/pitch_sift_bf_crosscheck.jpg) | ![](imgs/output_compare/pitch_sift_bf_ratiotest.jpg) |
| SURF | ![](imgs/output_compare/pitch_surf_bf_crosscheck.jpg) | ![](imgs/output_compare/pitch_surf_bf_ratiotest.jpg) |
| SURF extended | ![](imgs/output_compare/pitch_surfext_bf_crosscheck.jpg) | ![](imgs/output_compare/pitch_surfext_bf_ratiotest.jpg) |
| ORB | ![](imgs/output_compare/pitch_orb_bf_crosscheck.jpg) | ![](imgs/output_compare/pitch_orb_bf_ratiotest.jpg) |

#### Case: Roll rotation
| | Brute Force Matching w/ Cross Check | Brute Force Matching w/ Ratio Test |
| :--: | :------------------: | :-----------------: |
| SIFT | ![](imgs/output_compare/roll_sift_bf_crosscheck.jpg) | ![](imgs/output_compare/roll_sift_bf_ratiotest.jpg) |
| SURF | ![](imgs/output_compare/roll_surf_bf_crosscheck.jpg) | ![](imgs/output_compare/roll_surf_bf_ratiotest.jpg) |
| SURF extended | ![](imgs/output_compare/roll_surfext_bf_crosscheck.jpg) | ![](imgs/output_compare/roll_surfext_bf_ratiotest.jpg) |
| ORB | ![](imgs/output_compare/roll_orb_bf_crosscheck.jpg) | ![](imgs/output_compare/roll_orb_bf_ratiotest.jpg) |

#### Case: Yaw rotation
| | Brute Force Matching w/ Cross Check | Brute Force Matching w/ Ratio Test |
| :--: | :------------------: | :-----------------: |
| SIFT | ![](imgs/output_compare/yaw_sift_bf_crosscheck.jpg) | ![](imgs/output_compare/yaw_sift_bf_ratiotest.jpg) |
| SURF | ![](imgs/output_compare/yaw_surf_bf_crosscheck.jpg) | ![](imgs/output_compare/yaw_surf_bf_ratiotest.jpg) |
| SURF extended | ![](imgs/output_compare/yaw_surfext_bf_crosscheck.jpg) | ![](imgs/output_compare/yaw_surfext_bf_ratiotest.jpg) |
| ORB | ![](imgs/output_compare/yaw_orb_bf_crosscheck.jpg) | ![](imgs/output_compare/yaw_orb_bf_ratiotest.jpg) |
