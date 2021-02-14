import socket
my_socket=socket.socket()
my_socket.connect(('127.0.0.1',8820))
def run_client():
    handle_opening_screen()
    handle_sign()


def handle_opening_screen():
    opening_message=my_socket.recv(1024).decode()
    input(opening_message)
def handle_sign():
   ask=my_socket.recv(1024).decode()
   sign_type=input(ask)
   while True:
       if sign_type=="up":
           sign_up()
           break
       elif sign_type=="in":
           sign_in()
           break
       eror_message=my_socket.recv(1024).decode()
       input(eror_message)
def sign_up():
    name_request=my_socket.recv(1024).decode()
    my_user_name=input(name_request).encode()
    my_socket.send(my_user_name)
    password_request=my_socket.recv(1024).decode()
    my_password=input(password_request).encode()
    my_socket.send(my_password)
    verify_password_request=my_socket.recv(1024).decode()
    verify_my_password=input(verify_password_request)
    while verify_my_password !=my_password:
        print("please enter the exact same password you entered above.")
        verify_my_password=input()
    verify_my_password=verify_my_password.encode()
    my_socket.send(verify_my_password)
    data = my_socket.recv(1024).decode()
    print(data)
def sign_in():
    while True:
        name_request = my_socket.recv(1024).decode()
        my_user_name = input(name_request).encode()
        my_socket.send(my_user_name)
        password_request = my_socket.recv(1024).decode()
        my_password = input(password_request).encode()
        my_socket.send(my_password)
        data=my_socket.recv(1024).decode()
        if data=="welcome!":
            break



