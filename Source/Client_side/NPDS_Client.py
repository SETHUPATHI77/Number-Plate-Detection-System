import lcd_display as ld 
import socket
import os

def capture_image():
    image_file = 'img.jpg'
    command = f'fswebcam -r 640x480 --no-banner {image_file}'
    os.system(command)
    print("camera")
    return


def send_image(client_socket):
    image_path = 'img.jpg'
    with open(image_path, 'rb') as file:
        img_data = file.read()
    image_size = len(img_data)
    client_socket.sendall(str(image_size).encode('utf-8')) 
    client_socket.sendall(img_data)
    print("send_image")
    return

def recv_text(client_socket):
    data = client_socket.recv(1024)
    if not data:
        pass
    data = data.decode('utf-8')
    print("receive_text")
    return data

def client_setup():
    host_add = "Your server IP address"
    port_add = 54321
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host_add, port_add))
    print(f"Connection from {host_add}:{port_add} has been established!")
    while True:
            capture_image()
            send_image(client_socket)
            data = recv_text(client_socket)
            displaying(data,1,2,clean=False)
            print("Vehicle No.:",data) 
    client_socket.close()

    return


def displaying(text,line,delay,clean=True,cl_line=3):
    ld.lcd_show(text,line,delay)
    if clean ==True:
        ld.lcd_clean(cl_line)
    print("display")
    return


if __name__ == "__main__":

    con = [16,26,6,5,22,27,17]
    ld.variables(con)

    texts = ["Booting","initiated.......!","Welcome!...... ","..............","number plate","detection","Booting","completed"]

    for num in range (0,len(texts),2):
        displaying(texts[num],1,0,clean=False)
        displaying(texts[num+1],2,2,clean=True,cl_line=3)
    client_setup()
        
