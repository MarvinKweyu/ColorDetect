import cv2


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
    def get_segmented_image(image, lower_bound=(0, 70, 0), upper_bound=(80, 255, 255), erode_iterations=3,
                            dilate_iterations=3):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        output_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        img2 = image.copy()

        img2 = cv2.GaussianBlur(img2, (11, 11), 0)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(img2, lower_bound, upper_bound)
        mask = cv2.erode(mask, None, iterations=erode_iterations)
        mask = cv2.dilate(mask, None, iterations=dilate_iterations)
        extracted = cv2.bitwise_and(image, image, mask=mask)

        for i in range(len(mask)):
            for j in range(len(mask[i])):
                if mask[i][j] != 0:
                    output_image[i][j] = image[i][j]

        return output_image, gray, extracted, mask
