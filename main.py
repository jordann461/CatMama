import cv2
import numpy as np


def detect_track_count_on_region(frame, results, labels, class_id, left_upper, left_down, right_upper, right_down):
    """
    Task of the function:
    Draws a box on the objects detected in a given area. Instantly writes the score,
    the ID and the number of objects on the box. Within a given area (coordinates are taken from the user)
    This function starts a loop for each detection in `results`. Inside the loop, the delimiter
    the box of the detected object is drawn and the class name and confidence score are written
    above the box. If the score of a detected object is below a certain threshold (e.g. score < 0.5)
    or if the detected object does not belong to a desired class (e.g. object), detection
    is ignored and no drawing is made on it.

    Args:
    - frame: The image on which to draw.
    - results: The detection results from the YOLO model.
    - labels: The list of class labels.
    - class_id: Object id(e.g. 2: 'cat' & 'bowl')
    - left_upper: The top-left coordinate of the defined region.
    - left_down: The bottom-left coordinate of the defined region.
    - right_upper: The top-right coordinate of the defined region.
    - right_down: The bottom-right coordinate of the defined region.

    The function works in the following steps:
    1. For each detection in `results`, a loop is started using `enumerate`. `enumerate` is both the index
       and the bounding box information of the detected object.
    2. For each detection, the coordinates of the bounding box (`x1`, `y1`, `x2`, `y2`) are converted to integers.
       This is the drawing operations because OpenCV expects the coordinates to be integers.
    3. The confidence score and class ID of the detected object are retrieved. This information is used to determine how much the detected object
       is reliable and which class it belongs to.
    4. If the score of the detected object is below a certain threshold or belongs to an undesirable class, this detection
       no drawing is performed and the next iteration of the loop is started.
    5. For detections with a score above the threshold and belonging to the desired class, the bounding box is drawn and the class name
       and score information is written.
    6. Object counts are made over an area based on the coordinates received from the user.

    Details:
    result[0].boxes : stores the coordinates, ID and score of the detected objects (tensor or array object)
    result[0].boxes.xyxy: Contains the coordinates (x1, y1, x2, y2) of the bounding box for each detection.
    result[0].boxes.conf: Contains the confidence score of each detected object (between 0 and 1)
    result[0].boxes.cls: Contains the class ID of each detected object.(2= 'car')
    count: Counts selected objects instantly

    """
    count = 0
    region = np.array([left_upper, left_down, right_down, right_upper])
    region = region.reshape((-1, 1, 2))

    # Loop for each detection object
    # ennumerate:  getting both of them index and value of coordinates
    for i, box in enumerate(results[0].boxes.xyxy):
        # Get the coordinates and convert to integer
        # Coordinates must be int because of no float in OpenCV coordinate list
        x1, y1, x2, y2 = map(int, box[:4])
        # Check it out - print(x2)

        # Get score as float (conf[i])
        score = float(results[0].boxes.conf[i])
        # Check it out - print(score)

        # Get class id as int (conf[i])
        cls = int(results[0].boxes.cls[i])
        # Check it out - print(cls)

        # Get label name
        name = labels[cls]
        # Check it out - print(name)

        if (score > 0.2) and (name == class_id):

            # Drow it box(rectangle) on detected object
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Display object ID and Score above box instantly
            text = f'ID:{name}, Score:{score:.2f}'
            cv2.putText(frame, text, (x1, y1 - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # Get bottom center of objects (gets feet)
            px = int(x1 / 2 + x2 / 2)
            py = y2

            # Check it out person is inside region or not. if that inside region count it
            inside_region = cv2.pointPolygonTest(region, (px, py), False)
            if inside_region > 0:
                # If detect object(same class_id) and inside region increas 1
                count += 1

    # Display total object number top left on frame
    cv2.putText(frame, f'Total: {count}', (45, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.polylines(frame, [region], True, (0, 0, 255), 4)


import cv2
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

target_classes = ['cat', 'bowl']
class_ids = [key for key, value in model.names.items() if value in target_classes]

video_path = "test_video2.mp4"
cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    success, frame = cap.read()

    if success:
        start_time = time.time()
        results = model(frame)
        filtered_results = []
        for result in results[0].boxes:
            if int(result.cls) in class_ids:
                filtered_results.append(result)

        annotated_frame = frame.copy()
        for result in filtered_results:
            xyxy = result.xyxy[0].cpu().numpy().astype(int)
            conf = result.conf[0].cpu().numpy()
            cls = int(result.cls[0].cpu().numpy())

            cv2.rectangle(annotated_frame, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)
            label = f"{model.names[cls]} {conf:.2f}"
            cv2.putText(annotated_frame, label, (xyxy[0], xyxy[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        elapsed_time = time.time() - start_time
        cv2.putText(annotated_frame, f'Time: {elapsed_time:}s', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        out.write(annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
