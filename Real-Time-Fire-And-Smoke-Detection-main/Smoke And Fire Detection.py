import cv2
import numpy as np
from collections import deque

def main():
    video_path = r'C:\Users\SYaM\Documents\fire\fire3.mp4'  # Replace with your video file path
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return


    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(f"Processing video: {width}x{height} at {fps:.2f} fps")


    frame_buffer = deque(maxlen=10)


    lower_fire = np.array([0, 120, 70])
    upper_fire = np.array([20, 255, 255])
    lower_smoke = np.array([0, 0, 100])
    upper_smoke = np.array([180, 50, 220])

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Reached end of video")
                break

         
            frame = cv2.resize(frame, (640, 480))
            blurred = cv2.GaussianBlur(frame, (21, 21), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

     
            frame_buffer.append(frame.copy())

        
            fire_mask = cv2.inRange(hsv, lower_fire, upper_fire)
            fire_mask = cv2.morphologyEx(fire_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
            fire_mask = cv2.dilate(fire_mask, None, iterations=2)

            fire_contours, _ = cv2.findContours(fire_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in fire_contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    cv2.putText(frame, "Fire", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

          
            if len(frame_buffer) == 10:
                gray_current = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray_old = cv2.cvtColor(frame_buffer[0], cv2.COLOR_BGR2GRAY)
                frame_diff = cv2.absdiff(gray_current, gray_old)
                _, motion_mask = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)

                smoke_mask_color = cv2.inRange(hsv, lower_smoke, upper_smoke)
                smoke_mask = cv2.bitwise_and(motion_mask, smoke_mask_color)
                smoke_mask = cv2.morphologyEx(smoke_mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
                smoke_mask = cv2.dilate(smoke_mask, None, iterations=3)

                smoke_contours, _ = cv2.findContours(smoke_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for contour in smoke_contours:
                    if cv2.contourArea(contour) > 1000:
                        x, y, w, h = cv2.boundingRect(contour)
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 200, 200), 2)
                        cv2.putText(frame, "Smoke", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)

            cv2.imshow('Fire and Smoke Detection', frame)
            
          
            key = cv2.waitKey(int(1000/fps)) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('p'):  # Pause/play with 'p' key
                while True:
                    key2 = cv2.waitKey(1)
                    if key2 == ord('p'):
                        break
                    elif key2 == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        return

    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()