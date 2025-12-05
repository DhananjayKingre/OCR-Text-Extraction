import cv2
import numpy as np

def enhance_image(img_path):
    img = cv2.imread(img_path)

    # 1. Upscale - blurry images become readable
    img = cv2.resize(img, None, fx=1.8, fy=1.8, interpolation=cv2.INTER_CUBIC)

    # 2. Denoise
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

    # 3. Sharpen
    kernel = np.array([[0, -1,  0],
                       [-1,  5, -1],
                       [0, -1,  0]])
    img = cv2.filter2D(img, -1, kernel)

    # 4. Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 5. Adaptive threshold (helps with faded text)
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        35, 11
    )

    output_path = img_path.replace('.jpg', '_proc.jpg').replace('.png', '_proc.jpg')
    cv2.imwrite(output_path, thresh)

    return output_path
