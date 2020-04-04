from pathlib import Path

import cv2
import imutils
import numpy as np
from sklearn.cluster import KMeans


class ColorDetect:
    """
    Detect and write the number of colors in an image
    """

    def __init__(self, image):
        """Class constructor"""
        self.image = cv2.imread(image)
        self.color_description = {}

    def get_color_count(self, color_id=5) -> dict:
        """
        Count the number of different colors
        """

        # convert image from BGR to HSV for better accuracy
        rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        reshape = rgb.reshape((rgb.shape[0] * rgb.shape[1], 3))
        cluster = KMeans(n_clusters=color_id).fit(reshape)
        import pdb;
        pdb.set_trace()
        unique_colors = self.find_unique_colors(cluster, cluster.cluster_centers_)

        return self.color_description

    def find_unique_colors(self, cluster, centroids):

        # Get the number of different clusters, create histogram, and normalize
        labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
        (hist, _) = np.histogram(cluster.labels_, bins=labels)
        hist = hist.astype("float")
        hist /= hist.sum()

        # Create frequency rect and iterate through each cluster's color and percentage
        rect = np.zeros((50, 300, 3), dtype=np.uint8)
        colors = sorted([(percent, color) for (percent, color) in zip(hist, centroids)])
        start = 0
        print(colors)
        for (percent, color) in colors:
            # print(color, "{:0.2f}%".format(percent * 100))
            end = start + (percent * 300)
            color.astype("uint8").tolist()
            start = end
        return colors

    def write_color_count(self):
        """
        Write the number of colors found to the image
        """
        y_axis = 200
        for k, v in self.color_description.items():
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, y_axis)
            fontScale = 1
            fontColor = (0, 0, 0)
            lineType = 1

            cv2.putText(self.image, k + ':' + str(v),
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
            y_axis += 23

    def save_color_count(self, location=".", file_name="out.jpg"):
        """
        Save the resultant image file to the local directory
        
        Parameters
        ----------
        location: str
            The file location of the image
        file_name:str
            The name of the new image

        """
        # write image colors to the image
        self.write_color_count()

        image_folder = Path(location)
        image_to_save = image_folder / file_name

        # Save image
        cv2.imwrite(str(image_to_save), self.image)

        print("Image processed and saved successfully")
