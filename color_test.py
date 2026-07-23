import cv2
import numpy as np

# Front camera
cap_front = cv2.VideoCapture(0)

# Wrist camera
cap_wrist = cv2.VideoCapture(2)

print("Green and Red detection test started. Press 'q' to quit.")

# HSV range for green
lower_green = np.array([40, 70, 40])
upper_green = np.array([90, 255, 255])

# HSV range for red
lower_red1 = np.array([0, 150, 50])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 150, 50])
upper_red2 = np.array([180, 255, 255])


def detect_colors(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create masks
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = mask_red1 + mask_red2

    # Detect green objects
    contours_g, _ = cv2.findContours(
        mask_green,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours_g:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)

            center_x = x + w // 2
            center_y = y + h // 2

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

            cv2.putText(
                frame,
                f"Green ({center_x}, {center_y})",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

    # Detect red objects
    contours_r, _ = cv2.findContours(
        mask_red,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours_r:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)

            center_x = x + w // 2
            center_y = y + h // 2

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            cv2.putText(
                frame,
                f"Red ({center_x}, {center_y})",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2,
            )

    return frame


while True:
    ret_f, frame_front = cap_front.read()
    ret_w, frame_wrist = cap_wrist.read()

    if not ret_f or not ret_w:
        break

    frame_front = detect_colors(frame_front)
    frame_wrist = detect_colors(frame_wrist)

    cv2.imshow("Front Camera", frame_front)
    cv2.imshow("Wrist Camera", frame_wrist)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap_front.release()
cap_wrist.release()
cv2.destroyAllWindows()
