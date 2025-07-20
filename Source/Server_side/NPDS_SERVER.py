from ultralytics import YOLO
from PIL import Image
import numpy as np
import easyocr
import socket
import shutil
import time


def server_setup():
    host = 'your sever(laptop) ip address'
    port = 54321
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening...")
    client_socket, client_address = server_socket.accept()
    print("Connection has been established!")
    try:
        while True:
            receive_image(client_socket)
            AI_detection_()
            text = text_converter()
            send_text(text,client_socket)
    except Exception as e:
        print(f'Error: {e}')
    finally:
        client_socket.close()
        server_socket.close()    
    return


def receive_image(client_socket):
    image_size = int(client_socket.recv(1024).decode('utf-8'))
    received_data = b''
    while len(received_data) < image_size:
        packet = client_socket.recv(4096)  
        if not packet:
            break
        received_data += packet
    print("image")
    with open('received_image.jpg', 'wb') as f:
        f.write(received_data)
    recieved_data=None
    image_size = None
    print("receive image")
    return


def AI_detection_():
    image = Image.open("received_image.jpg")
    resized_image = image.resize((640,640))
    results = model(source = resized_image,conf = 0.6,save_crop = True,save = True)
    print("AI")
    return


def text_converter():
    try:
        img = Image.open("runs\\detect\\predict\\crops\\number_plate\\image0.jpg")
        gray = img.convert('L')
        gray_np = np.array(gray)
        bi_np = np.where(gray_np >125,255,0)
        bi = Image.fromarray(bi_np.astype(np.uint8))
        bi.save("runs\\detect\\predict\\crops\\number_plate\\image1.jpg")
        image_path = "runs\\detect\\predict\\crops\\number_plate\\image1.jpg"
        result = reader.readtext(image_path)
        extracted_text = ' '.join([text[1] for text in result])
    except:
       extracted_text = "not detected"
    finally:
        time.sleep(5)
        shutil.rmtree('runs\\detect')
    print("text_converter")
    print(extracted_text)
    return extracted_text


def send_text(text,client_socket):
    text_data = text.encode('utf-8')
    client_socket.sendall(text_data)
    print("send_text")
    return

    
if __name__ == "__main__":
    
    model = YOLO("number_AI.pt")
    reader = easyocr.Reader(['en'])
    server_setup()
        
