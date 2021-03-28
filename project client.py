import socket
my_socket=socket.socket()
my_socket.connect(('127.0.0.1',8820))
def main():
    run_client()
def run_client():
    handle_opening_screen()
    handle_sign()
  #  place_and_time()
def send_data(data):
    preper_data=str(len(data))+data
    send_d=preper_data.zfill(len(data)+4).encode()
    my_socket.send(send_d)
def get_data():
    len_data=my_socket.recv(4).decode()
    len_data=int(len_data)
    data=my_socket.recv(len_data).decode()
    return data
#def place_and_time():
  #  place_request=my_socket.recv(1024).decode()
   # while True:
      #  my_place=input(place_request)

def handle_opening_screen():
    opening_message=get_data()
    input(opening_message)
def handle_sign():
   ask=get_data()
   sign_type=input(ask)
   while True:
       if sign_type=="up":
           send_data(sign_type)
           sign_up()
           break
       elif sign_type=="in":
           send_data(sign_type)
           sign_in()
           break
       else:
           eror_message="please select up or in."
           sign_type=input(eror_message)
def sign_up():
    name_request=get_data()
    my_user_name=input(name_request)
    send_data(my_user_name)
    is_valid=get_data()
    while is_valid !="done":
        print(is_valid)
        my_user_name=input()
        send_data(my_user_name)
        is_valid=get_data()
    password_request=get_data()
    my_password=input(password_request)
    send_data(my_password)
    verify_password_request=get_data()
    verify_my_password=input(verify_password_request)
    while verify_my_password != my_password:
        verify_my_password=input("please enter the exact same password you entered above.")
    send_data("done")
    data = get_data()
    print(data)
def sign_in():
    while True:
        name_request = get_data()
        my_user_name = input(name_request)
        send_data(my_user_name)
        password_request = get_data()
        my_password = input(password_request)
        send_data(my_password)
        data=get_data()
        print(data)
        if data=="welcome!":
            break



if __name__ == '__main__':
    main()