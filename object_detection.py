import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import math
import argparse

parser = argparse.ArgumentParser(description='Kullanılmak istenen weights ve config')
parser.add_argument('--weights', help='.weights dosyasının yolu')
parser.add_argument('--config', help='.config dosyasının yolu')
args = parser.parse_args()

option = {
    'model': args.config,
    'load': args.weights,
    'threshold': 0.2,
    'gpu': 1.0
}

tfnet = TFNet(option)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
count = 0
f = 1

while True:
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            W = result['topleft']['x']
            print(W)
            H = result['bottomright']['y']
            print(H)
            distancei = (2 * 3.14 * 180) / (W + H * 360) * 1000 + 3
            print(distancei)
            label = result['label']
            confidence = result['confidence']            
            text = '{}: {:.0f}% , uzaklık = {}'.format(label, confidence * 100, distancei)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
