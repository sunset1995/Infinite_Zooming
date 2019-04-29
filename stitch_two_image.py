import cv2
import numpy as np

from feature_matcher import CreateMethod
from vp_detect import detect_in_image_vp


if __name__ == '__main__':

    import os
    import sys
    import glob
    import argparse

    METHODS = [k for k in CreateMethod.__dict__.keys() if k[:2] != '__']

    # Arguments parser
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--iglob', required=True)
    parser.add_argument('--outdir', required=True)
    parser.add_argument('--method', choices=METHODS, required=True)
    args = parser.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    method = CreateMethod.__dict__[args.method]()

    # Read two images
    img_paths = sorted(glob.glob(args.iglob), reverse=True)
    for path in img_paths:
        assert os.path.isfile(path)

    # Generate matching between adjacency images
    img1 = cv2.imread(img_paths[0], cv2.IMREAD_COLOR)
    for i in range(1, len(img_paths)):
        img2 = cv2.imread(img_paths[i], cv2.IMREAD_COLOR)
        kp1, des1, kp2, des2, matches = method(img1, img2)

        # Draw match result
        match_img = cv2.drawMatches(
            img1, kp1, img2, kp2, matches,
            None, flags=2)

        # Estimate homography
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        # Save result
        k1 = os.path.split(img_paths[i-1])[1][:-4]
        k2 = os.path.split(img_paths[i])[1][:-4]
        cv2.imwrite(os.path.join(args.outdir, '%s_%s_match.png' % (k1, k2)), match_img)

        # Prepare for next iteration
        img1 = img2
