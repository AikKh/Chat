import socket, threading
from Command import Command



def handle_messages(connection: socket.socket):
    
    while True:
        try:
            msg = connection.recv(1024)

            if msg:
                print(msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Error handling message from server: {e}')
            connection.close()
            break
        
def correctMessage(msg: str):
    count = 0
    for l in msg:
        if '-' == l:
            count += 1
            
    return count > 0 and count < 2

def client():
    
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000

    try:

        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
        
        threading.Thread(target=handle_messages, args=[socket_instance]).start()

        print('Connected to chat!')

        while True:
            
            msg = input()

            if msg == 'quit':
                break
            
            if correctMessage(msg):
            
                commands = msg.split('-')
 
                json = Command.CreateCommand(commands[0], commands[1])

                msg = json 

                socket_instance.send(msg.encode())
            else:
                print('Write correct command')

        socket_instance.close()

    except Exception as e:
        print(f'Error connecting to server socket {e}')
        socket_instance.close()


if __name__ == "__main__":
    client()
