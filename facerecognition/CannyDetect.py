import cv2

__author__ = "boboa"

def edge_demo(image):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    xgrad = cv2.Sobel(gray, cv2.CV_16SC1, 1, 0)
    ygrad = cv2.Sobel(gray, cv2.CV_16SC1, 1, 0)
    # edge_output = cv2.Canny(xgrad, ygrad, 50, 150)
    # cv2.imshow("Vannt_edge",edge_output)
    edge_output = cv2.Canny(gray, 50, 150)
    cv2.imshow("canny edge", edge_output)
    dst = cv2.bitwise_and(image, image, mask=edge_output)
    cv2.imshow("color edge", dst)


if __name__ == "__main__":
    img = cv2.imread("img/a.jpg")
    cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input image", img)
    edge_demo(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
