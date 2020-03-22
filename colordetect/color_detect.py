# USAGE
# python  color_detect.py -i image.png

import argparse
import sys
from pathlib import Path

import cv2
import imutils
import numpy as np


def get_input_image():
    """
    Get the image as a command-line argument
    """
    parser = argparse.ArgumentParser(description="Write the color count in an image ontu a copy of the image")
    parser.add_argument("-i", "--image", help="path to the image file",required=True)
    args = parser.parse_args()
    return args.image


def main():
     # load the image
    # image = cv2.imread(args["image"])
    image = cv2.imread(get_input_image())
    user_image = ColorDetect(image)
    user_image.get_color_count()
    user_image.save_picture("../")
    sys.exit()


class ColorDetect():
    """
    Detect and write the number of colors in an image
    """
    def __init__(self, image):
        """Class constructor"""
        self.image = image
            # Dictionaries of colors
        self.colors = {
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

        self.pic_description = {}

    def get_color_count(self):
        """
        Count the number of different colors
        """

        # convert image from BGR to HSV for better accuracy
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        for color, boundaries in self.colors.items():

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
            self.pic_description[color]= len(cnts)
            # cv2.imshow(color+"Mask", result) # display the masks
            self.write_color_count()
            # return self.pic_description
        

    def write_color_count(self):
        """
        Write the number of colors found to the image
        """
        y_axis = 200
        for k,v in self.pic_description.items():

            font                   = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10,y_axis)
            fontScale              = 1
            fontColor              = (0,0,0)
            lineType               = 1

            cv2.putText(self.image,k +':' +str(v),
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                lineType)
            y_axis += 23
        # Display the image
        cv2.imshow("img", self.image)
        
       

    def save_picture(self, location=".", file_name="out.jpg"):
        """
        Save the resultant image file to the local directory
        
        Parameters
        ----------
        location: str
            The file location of the image
        file_name:str
            The name of the new image

        """

        image_folder = Path(location)
        image_to_save = image_folder / file_name
        
         # Save image
        cv2.imwrite(str(image_to_save), self.image)
        
        print("Image processed and saved successfuly")
        # cv2.waitKey(0)
        
    

if __name__ == "__main__":
    main()
