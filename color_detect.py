# USAGE
# python  color_detect.py -i image.png

import numpy as np
import argparse
import imutils
import cv2


def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help="path to the image file")
    args = vars(ap.parse_args())

    # load the image
    image = cv2.imread(args["image"])

    boundaries = [
                  ([178,179,0],[255,255,255]),  # red
                  ([ 10,244,172],[ 30,254,252]), # orange>blurry on 2
                  ([ 30,244,131],[ 50,254,211]), # light green>>correct
                  # ([33,80,40],[102,255,255]), # green
                  ([110,245,214],[130,255,254]), # blue
                  ([150,245,131],[170,255,211]), # purple>blurry on2
                  ([ 20,245,172],[ 40,255,252]),  # brown>two images on 2
                  ([ 80,245,173],[100,255,253]), # light blue
                  ([ 60,235,45],[ 80,255,125])  # yellow> gives green
                  ]

    colors_names = ['red','orange','blue','green','brown','yellow']
    locate = 0
    pic_description = {}
    for (lower,upper) in boundaries:

        while locate < len(colors_names):
            # color being worked on
            color = colors_names[locate]
        	# find all the 'color' shapes in the image
            lower = np.array(lower,dtype="uint8")
            upper = np.array(upper,dtype="uint8")
            shapeMask = cv2.inRange(image, lower, upper)

        	# find the contours in the mask
            cnts=cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
            cnts = imutils.grab_contours(cnts)
            print("{} : {} ".format(color,len(cnts)))
            pic_description[color]= len(cnts)
            cv2.imshow("Mask", shapeMask)
            locate += 1

        	# loop over the contours
            # for c in cnts:
            #     # draw the contour and show it
            #     cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            #     cv2.imshow("Image", image)
            #     cv2.waitKey(0)
    write_to_picture(image, pic_description)

    return


def write_to_picture(image,pic_description):
    """write the color count to the image"""
    # Write some Text
    y_axis = 330
    for k,v in pic_description.items():

        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10,y_axis)
        fontScale              = 1
        fontColor              = (0,0,0)
        lineType               = 1

        cv2.putText(image,k +':' +str(v),
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            lineType)
        y_axis += 23
    # Display the image
    cv2.imshow("img", image)
    # Save image
    cv2.imwrite("out.jpg", image)
    cv2.waitKey(0)
    return

main()
