# Title
### Project: Number-Plate-Detection-System
### Product: SmartVision

# Abstract
The aim of this project was to learn and implement:

* Real-time number plate detection using YOLOv8
* Text extraction using OCR (EasyOCR)
* Socket communication between client and server
* Display of extracted number plate on LCD screen
* End-to-end AI + IoT integration

SmartVision is a Number plate detection system. A Raspberry Pi captures vehicle images using webcam and sends them to a laptop server running a YOLOv8 model. The number plate is detected and cropped, then passed to an OCR engine (EasyOCR) to extract the text, which is sent back to the Raspberry Pi for display on an LCD screen.

# Components
| Item                                  | Quantity |
| ------------------------------------- | -------- |
| Raspberry Pi 4                        | 1        |
| USB Webcam                            | 1        |
| LCD Display (16x2)                    | 1        |
| YOLOv8 Model (Trained)                | 1        |
| EasyOCR (OCR Engine)                  | 1        |
| Laptop (Server)                       | 1        |
| Power Supply                          | 1        |

# PHASE 1
## Electronics Aspect
### Main Algorithm
1. The Raspberry Pi captures an image using the webcam.
2. The image is sent via socket protocol to the server (laptop).
3. The image is passed to EasyOCR, which extracts the alphanumeric text.
4. The text is sent back to the Raspberry Pi, which displays it on the LCD screen.

### Other Algorithm
* LCD interface using GPIO pins.

### Controllers
* Raspberry Pi 4 handles image capture, communication and display.
* Laptop (server) handles OCR operations.

### Sensor
* USB Webcam: Captures vehicle image.

### Display
* 16x2 LCD: Show extracted number plate text

### Power
* Power Supply for Raspberry Pi

## Conclusion
* The webcam works well, but improper camera placement limits the accuracy.
* EasyOCR does not reliably extract text from the captured images as expected.
* The LCD display effectively shows the number plate results in a readable format.
* Client-server model greatly reduced time.
* Overall, the system performed poorly.

# PHASE 2
## Electronics Aspect
### Main Algorithm
1. The Raspberry Pi (client) captures an image using the webcam.
2. Camera angle optimized for clearer image capture.
3. The image is sent via socket protocol to the server (laptop).
4. The server runs the YOLOv8 model was trained with a custom dataset for number plate detection to improve accuracy.
5. The cropping logic was enhanced to tightly bound number plates, improving OCR accuracy.
6. The cropped image is passed to EasyOCR, which extracts the alphanumeric text.
7. The text is sent back to the Raspberry Pi, which displays it on the LCD screen.

### Other Algorithms
* LCD interface using GPIO pins.

### Controller
* Raspberry Pi 4 handles client-side image capture, communication and display.
* Laptop (server) handles YOLO and OCR operations.

### Sensor
* USB Webcam: Captures vehicle image.

### Display
* 16x2 LCD: Show extracted number plate text

### Power
* Power Supply for Raspberry Pi and server(laptop).

## Client-Server Workflow
* Camera (webcam) captures image
* Image sent to server using Python socket protocol
* Server processes image:
* * YOLOv8 detects number plate → crops it
* * EasyOCR extracts text
* * Result text sent to Raspberry Pi
* Raspberry Pi receives text and displays on LCD

## Dataset Preparation & Model Training
* Images of number plates were downloaded using the simple_image_download Python module
* Annotation was done on the Roboflow website, labeling the number plate region
* Dataset was exported in YOLO format
* YOLOv8 training was carried out on Google Colab, leveraging GPU for fast training
* Trained model was deployed on the server machine

## Conclusion
* Trained YOLOv8 model offered accurate and fast number plate localization
* YOLOv8 model perfectly crop the exact number plate region
* EasyOCR extracted clear and usable text in real-time
* System was stable and efficient for real-world testing
* Display output was accurate and user-friendly
