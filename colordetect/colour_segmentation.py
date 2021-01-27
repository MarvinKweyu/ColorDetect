import cv2
import numpy as np


class ColourSegmentation:

    @staticmethod
    def get_image_array(image_path: str, resize_h: int = None):
        img = cv2.imread(image_path)
        if resize_h is not None:
            h0, w0, _ = img.shape
            h1 = resize_h
            w1 = int(w0 * h1 / h0)
            img = cv2.resize(img, (w1, h1))
        return img

    @staticmethod
    def get_segmented_image(image, lower_bound, upper_bound, erode_iterations=3, dilate_iterations=3,
                            use_grab_cut=True, gc_iterations=3):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        output_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        img2 = image.copy()

        img2 = cv2.GaussianBlur(img2, (11, 11), 0)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(img2, lower_bound, upper_bound)
        mask = cv2.erode(mask, None, iterations=erode_iterations)
        mask = cv2.dilate(mask, None, iterations=dilate_iterations)

        if use_grab_cut:
            mask[mask == 0] = cv2.GC_BGD
            mask[mask > 0] = cv2.GC_PR_FGD

            fg_model = np.zeros((1, 65), dtype="float")
            bg_model = np.zeros((1, 65), dtype="float")

            mask, bg_model, fg_model = cv2.grabCut(
                image, mask, None, fg_model, bg_model, iterCount=gc_iterations, mode=cv2.GC_INIT_WITH_MASK
            )

            mask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 0, 1)
            mask = (mask * 255).astype("uint8")

        segmented = cv2.bitwise_and(image, image, mask=mask)

        for i in range(len(mask)):
            for j in range(len(mask[i])):
                if mask[i][j] != 0:
                    output_image[i][j] = image[i][j]

        return output_image, gray, segmented, mask
