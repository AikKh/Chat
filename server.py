import socket, threading
import jsonpickle
from Profile import Profile

profiles = []

def getProfileByConnection(connection):

    for profile in profiles:
        if profile._connection == connection:
            return profile

    return None

def getProfileByNicname(nickname):
    for profile in profiles:
        if profile._nickname == nickname:
            return profile
        
    return None

def commandExecute(command: str, msg: str, connection: socket.socket):
    profile = getProfileByConnection(connection)
    
    if command == 'reg':
        profile.setNickname(msg)
    elif command == '*':
        msg_to_sent = 'From {} - {}'.format(profile._nickname, msg)
        broadcast(msg_to_sent, connection)
    else:
        try:
            msg_to_sent = 'From {} - {}'.format(profile._nickname, msg)
            profile = getProfileByNicname(command)
            if profile:
                profile._connection.send(msg_to_sent.encode())
            
            else:
                msg_to_sent = 'No such a nickname'
                profile = getProfileByConnection(connection)
                profile._connection.send(msg_to_sent.encode())
        except Exception as e:
            print('Error broadcasting message: {e}')
            remove_connection(profile)
            

def handle_user_connection(connection: socket.socket, address: str):

    while True:
        try:

            msg = connection.recv(1024)

            if msg:
                
                # decode socet message
                jsonString = msg.decode()
                commandObj = jsonpickle.decode(jsonString)
                commandObj._msg = commandObj.getMessage()
                
                commandExecute(commandObj._cmd, commandObj._msg, connection)
                
            else:
                remove_connection(getProfileByConnection(connection))
                break

        except Exception as e:
            print(f'Error to handle user connection: {e}')
            remove_connection(getProfileByConnection(connection))
            break


def broadcast(message: str, connection: socket.socket):

    for profile in profiles:
        if profile._connection != connection:
            try:
                profile._connection.send(message.encode())

            except Exception as e:
                print('Error broadcasting message: {e}')
                remove_connection(profile)


def remove_connection(prof: Profile):

    prof._connection.close()
    profiles.remove(prof)


def server():

    LISTENING_PORT = 12000
    
    try:

        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen(4)

        print('Server running!')
        
        while True:

            socket_connection, address = socket_instance.accept()
            
            profile = Profile(socket_connection)
            profiles.append(profile)
            
            threading.Thread(target=handle_user_connection, args=[socket_connection, address]).start()

    except Exception as e:
        print(f'An error has occurred when instancing socket: {e}')
    finally:
        if len(profiles) > 0:
            for prof in profiles:
                remove_connection(prof)

        socket_instance.close()


if __name__ == "__main__":
    server()