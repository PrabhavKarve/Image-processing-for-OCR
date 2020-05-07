import requests
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
URL = "http://192.X.X.X:8080/shot.jpg"
ker = np.ones((1,1), np.uint8)

def display_img(pic):
    cv2.imshow("pic", pic)
    cv2.waitKey(0)

def get_text(frr):
    print("in here")
    text = pytesseract.image_to_string(frr, lang='eng')
    print(text)
    display_img(frr)

def process_img(im):
    im = cv2.resize(im, (700, 700))
    ret, im = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = cv2.dilate(im, ker, iterations=1)
    im = cv2.erode(im, ker, iterations=1)
    im = cv2.resize(im, (700, 700))
    get_text(im)

#v1 = cv2.VideoCapture(0)

#path = " your path "
#img = cv2.imread(path)


while True:
    #ret, frame = v1.read()
    img_res = requests.get(URL)
    img_arr = np.array(bytearray(img_res.content), np.uint8)
    img = cv2.imdecode(img_arr, -1)

    cv2.imshow('IPWebcam', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyWindow('IPWebcam')
        break
process_img(img)
cv2.destroyAllWindows()