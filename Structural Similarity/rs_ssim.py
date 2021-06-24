import cv2
import csv
import sys
from skimage.metrics import structural_similarity

filename = sys.argv[1]
output_file_name = sys.argv[2]

video = cv2.VideoCapture(filename)
count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        image = frame
        break

cv2.destroyAllWindows()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

video.release()
video = cv2.VideoCapture(filename)

counter = 1
flag = 0
data = []

with open(output_file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Start', 'End'])

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        score = structural_similarity(image_gray, frame_gray)
        if score >= 0.85 and flag == 0:
            data.append(counter)
            flag = 1
        if score < 0.85 and flag == 1:
            data.append(counter)
            writer.writerow(data)
            data.clear()
            flag = 0

        print(str(counter) + '/' + str(count) + ': ' + str(score))
        counter += 1

video.release()
cv2.destroyAllWindows()