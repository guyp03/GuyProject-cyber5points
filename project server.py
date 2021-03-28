import socket
import sqlite3
server_socket=socket.socket()
server_socket.bind(('0.0.0.0',8820))
server_socket.listen(1)
(client_socket,client_address)=server_socket.accept()
openning_m="welcome to our website!please press any button to continue"
ask_for_sign= "select which kind of sign you want-up or in"
ask_for_username="please enter your username"
ask_for_password="please enter your password"
after_sign_up="Congratulations!Thanks for joining us!Now you can use our services."
ask_for_verify="please verify your password"
countrys=["US"]
ask_for_place="please select the place you're gonna be in"
ask_for_date="please enter the date you're gonna be in the place you entered above"
def main():
    run_server()
def run_server():
   handle_opening_screen()
   handle_sign()
   send_data("welcome!")
   #place,date=place_and_time()


def send_data(data):
    preper_data=str(len(data))+data
    send_d=preper_data.zfill(len(data)+4).encode()
    print(send_d.decode())
    client_socket.send(send_d)
def get_data():
    len_data=client_socket.recv(4).decode()
    len_data=int(len_data)
    data=client_socket.recv(len_data).decode()
    print(data)
    return data
#def place_and_time():

  #  places=""

    #for coun in countrys:
       # place=place+coun+","
   # ask_for_place_f=ask_for_place+coun
    #send_ask_for_place=ask_for_place_f.encode()
  #  client_socket.send(send_ask_for_place)
  #  place=client_socket.recv(1024).decode()
  #  send_ask_for_date=ask_for_date.encode()
    #client_socket.send(send_ask_for_date)
    #date=client_socket.recv(1024).decode()
    #return place,date



def handle_opening_screen():
    send_data(openning_m)
def handle_sign():
    send_data(ask_for_sign)
    data=get_data()
    if data=="in":
        sign_in()
    elif data=="up":
         sign_up()

def sign_in():
    while True:
        print("started")
        done=False
        send_data(ask_for_username)
        user_name=get_data()
        print(user_name)
        send_data(ask_for_password)
        password=get_data()
        print(password)
        c = sqlite3.connect('acounts.db')
        cursor = c.cursor()
        acounts_table = cursor.execute("SELECT*FROM acountsTable")
        rows = acounts_table.fetchall()
        for row in rows:
            if row[0] == user_name:
                if row[1]==password:
                    done=True
                    break
        if done==True:
            break
        send_data("the name or password isn't correct. please try again.")

def sign_up():
    send_data(ask_for_username)
    user_name=""
    while True :
        username=get_data()
        c = sqlite3.connect('acounts.db')
        cursor=c.cursor()
        acounts_table=cursor.execute("SELECT*FROM acountsTable")
        rows=acounts_table.fetchall()
        valid=True
        for row in rows:
            if username==row[0]:
                valid=False
        if valid==True:
            user_name=username
            c.close()
            send_data("done")
            break
        erorr_message="the name you typed is occupied.please enter different name."
        send_data(erorr_message)
    send_data(ask_for_password)
    password=get_data()
    send_data(ask_for_verify)
    get_data()
    c=sqlite3.connect('acounts.db')
    cursor=c.cursor()
    cursor.execute("INSERT INTO acountsTable VALUES ('{}','{}')".format(user_name,password))
    c.commit()
    c.close()
    send_data(after_sign_up)

if __name__ == '__main__':
    main()