"""
noise: a small library that applies various kinds of noise to bitmaps
"""

import numpy as np
import cv2
import io
from PIL import Image


def add_gaussian_noise(image, mean=0, std=25):
    """
    add gaussian noise to an image.

    parameters:
    -----------
    image : numpy.ndarray
        input image (grayscale or rgb)
    mean : float
        mean of the gaussian noise
    std : float
        standard deviation of the gaussian noise

    returns:
    --------
    numpy.ndarray
        image with added gaussian noise
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy array")

    # generate gaussian noise
    noise = np.random.normal(mean, std, image.shape).astype(np.float32)

    # add noise to the image
    noisy_image = np.clip(image.astype(np.float32) + noise, 0, 255).astype(np.uint8)

    return noisy_image


def add_salt_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    """
    add salt-and-pepper noise to an image.

    parameters:
    -----------
    image : numpy.ndarray
        input image (grayscale or rgb)
    salt_prob : float
        probability of adding salt noise (white pixels)
    pepper_prob : float
        probability of adding pepper noise (black pixels)

    returns:
    --------
    numpy.ndarray
        image with added salt and pepper noise
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy array")

    noisy_image = np.copy(image)

    # add salt (white) noise
    salt_mask = np.random.random(image.shape[:2]) < salt_prob
    if len(image.shape) == 3:  # color image
        for i in range(image.shape[2]):
            noisy_image[salt_mask, i] = 255
    else:  # grayscale image
        noisy_image[salt_mask] = 255

    # add pepper (black) noise
    pepper_mask = np.random.random(image.shape[:2]) < pepper_prob
    if len(image.shape) == 3:  # color image
        for i in range(image.shape[2]):
            noisy_image[pepper_mask, i] = 0
    else:  # grayscale image
        noisy_image[pepper_mask] = 0

    return noisy_image


def rotate_image(image, angle, scale=1.0):
    """
    rotate an image by a specified angle.

    parameters:
    -----------
    image : numpy.ndarray
        input image (grayscale or rgb)
    angle : float
        rotation angle in degrees (positive values for counterclockwise rotation)
    scale : float
        scaling factor

    returns:
    --------
    numpy.ndarray
        rotated image
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy array")

    # get image dimensions
    height, width = image.shape[:2]
    center = (width // 2, height // 2)

    # create rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # apply rotation
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return rotated_image


def rotate_image_random(image, min_angle=-10, max_angle=10, scale=1.0):
    """
    rotate an image by a random angle between the given bounds.

    parameters:
    -----------
    image : numpy.ndarray
        input image (grayscale or rgb)
    min_angle : float
        minimum rotation angle in degrees
    max_angle : float
        maximum rotation angle in degrees
    scale : float
        scaling factor

    returns:
    --------
    tuple
       (angle, rotated_image) - returns both the randomly selected angle and the randomly rotated image
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy array")

    # generate random angle within the specified range
    random_angle = np.random.uniform(min_angle, max_angle)

    # perform rotation using the existing function
    rotated_image = rotate_image(image, random_angle, scale)

    # return both the random angle that was used and the rotated image
    return random_angle, rotated_image


def add_compression_artifacts(image, quality=50):
    """
    add jpeg compression artifacts to an image.

    parameters:
    -----------
    image : numpy.ndarray
        input image (grayscale or rgb)
    quality : int
        jpeg compression quality (0-100), lower values introduce more artifacts

    returns:
    --------
    numpy.ndarray
        image with compression artifacts
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy array")

    # convert numpy array to pil image
    pil_image = Image.fromarray(image)

    # create an in-memory binary stream
    buffer = io.BytesIO()

    # save image with specified jpeg quality
    pil_image.save(buffer, format="JPEG", quality=quality)

    # reset buffer position
    buffer.seek(0)

    # load compressed image
    compressed_image = np.array(Image.open(buffer))

    return compressed_image


def apply_motion_blur(image, kernel_size=15, angle=0):
    """
    apply motion blur to an image.

    parameters:
    -----------
    image : numpy.ndarray
        input image (grayscale or rgb)
    kernel_size : int
        size of the motion blur kernel (should be odd)
    angle : float
        angle of motion blur in degrees

    returns:
    --------
    numpy.ndarray
        blurred image
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy array")

    # ensure kernel size is odd
    kernel_size = kernel_size if kernel_size % 2 == 1 else kernel_size + 1

    # create motion blur kernel
    kernel = np.zeros((kernel_size, kernel_size))

    # convert angle to radians
    angle_rad = np.deg2rad(angle)

    # calculate line coordinates
    x0 = (kernel_size - 1) // 2
    y0 = (kernel_size - 1) // 2

    # calculate line endpoints
    length = kernel_size // 2
    x1 = x0 - int(np.sin(angle_rad) * length)
    y1 = y0 - int(np.cos(angle_rad) * length)
    x2 = x0 + int(np.sin(angle_rad) * length)
    y2 = y0 + int(np.cos(angle_rad) * length)

    # draw line on kernel
    cv2.line(kernel, (y1, x1), (y2, x2), 1, thickness=1)

    # normalize kernel
    kernel = kernel / np.sum(kernel)

    # apply motion blur
    blurred_image = cv2.filter2D(image, -1, kernel)

    return blurred_image


# example usage
if __name__ == "__main__":

    # load sample image
    sample_image = cv2.imread("sample.png")
    if sample_image is None:
        # create a sample image if file doesn't exist
        sample_image = np.ones((300, 400, 3), dtype=np.uint8) * 128

        # add some shapes for visualization
        cv2.rectangle(sample_image, (50, 50), (150, 150), (255, 0, 0), -1)
        cv2.circle(sample_image, (300, 150), 50, (0, 255, 0), -1)

    # apply various noise types
    gaussian_noisy = add_gaussian_noise(sample_image, std=40)
    salt_pepper_noisy = add_salt_pepper_noise(sample_image, salt_prob=0.03, pepper_prob=0.03)
    _, rotated = rotate_image_random(sample_image, min_angle=-20, max_angle=20, scale=1)
    compressed = add_compression_artifacts(sample_image, quality=8)
    motion_blurred = apply_motion_blur(sample_image, kernel_size=20, angle=45)

    # display results (if running in a graphical environment)
    try:
        cv2.imshow("original", sample_image)
        cv2.imshow("gaussian noise", gaussian_noisy)
        cv2.imshow("salt & pepper noise", salt_pepper_noisy)
        cv2.imshow("randomly rotated image", rotated)
        cv2.imshow("compressed image", compressed)
        cv2.imshow("motion blurred", motion_blurred)
        cv2.waitKey(0)  # wait until a key is pressed
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"unable to display images, running in non-graphical environment: {e}")
