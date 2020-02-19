# USAGE
# python  color_detect.py -i image.png

import numpy as np
import argparse
import imutils
import cv2


def root():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help="path to the image file")
    args = vars(ap.parse_args())

    # load the image
    image = cv2.imread(args["image"])

    # Dictionaries of colors
    colors = {
                'red': [
                        ([0,50,50],[10,255,255]),
                        ([170,50,50],[180,255,255])
                        ],
                'blue':[
                        ([110,50,50],[130,255,255])
                        ],
                'green':[
                        ([50,50,50],[80,255,255])
                        ],
                'yellow':[
                        ([26,100,100],[35,255,255])
                        ],
                'orange':[
                        ([10,50,50],[22,255,255])
                        ],
                'purple':[
                        ([140,50,0],[165,255,255])
                        ],
                'cyan':[
                        ([80,50,50],[100,255,255])
                        ],
                'lightgreen':[
                        ([35,50,50],[45,255,255])
                        ]

    }

    pic_description = {}

    # convert image from BGR to HSV for better accuracy
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    for color, boundaries in colors.items():

        i = 0
        for (lower,upper) in boundaries:

        	# find all the 'color' shapes in the image
            lower = np.array(lower,dtype="uint8")
            upper = np.array(upper,dtype="uint8")
            shapeMask = cv2.inRange(hsv, lower, upper)

            if i == 0:
                result = shapeMask
            else:
                result = cv2.bitwise_or(result,shapeMask)

            i += 1

        # find the contours in the mask
        cnts=cv2.findContours(result.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
        cnts = imutils.grab_contours(cnts)
        print("{} : {} ".format(color,len(cnts)))
        pic_description[color]= len(cnts)
        cv2.imshow(color+"Mask", result)


    write_to_picture(image, pic_description)

    return


def write_to_picture(image,pic_description):
    """write the color count to the image"""
    # Write some Text
    y_axis = 200
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

# main()


def get_input_image():
    """
    Get the image as a command-line argument
    """
    parser = argparse.ArgumentParser(description="Write the color count in an image ontu a copy of the image")
    parser.add_argument("-i", "--image", help="path to the image file",required=True)
    args = parser.parse_args()
    return args



def main():
    image = get_input_image()
    ColorDetect(image)


class ColorDetect():
    def __init__(self, image):
        """Class constructor"""
        self.image = image
    

if __name__ == "__main__":
    main()
