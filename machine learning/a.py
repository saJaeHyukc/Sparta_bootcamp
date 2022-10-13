import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img = cv2.imread('result.jpg')
results = model(img)
results.save()

result = results.pandas().xyxy[0].to_numpy()
result = [item for item in result if item[6]=='person']

tmp_img = cv2.imread('result.jpg')
print(tmp_img.shape)
for i in range(len(result)):
    cropped = tmp_img[int(result[i][1]):int(result[i][3]), int(result[i][0]):int(result[i][2])]
    print(cropped.shape)
    cv2.imwrite(f'people{i+1}.png', cropped)
    cv2.rectangle(tmp_img, (int(results.xyxy[0][i][0].item()), int(results.xyxy[0][i][1].item())), (int(results.xyxy[0][i][2].item()), int(results.xyxy[0][i][3].item())), (255,255,255))
    cv2.imwrite('result1.png', tmp_img)
