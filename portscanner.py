import sys
import socket

def ps(address, port):
    """
    A function that prints out whether a port is open or not on a given host address
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print((address, port))
        s.connect((address, port))
        print("port " + str(port) + " is open.")
        s.close()
    except:
        print ("something went wrong! or port " \
        + str(port) + " is not open.")
        

if __name__ == "__main__":
    ps(sys.argv[1], int(sys.argv[2]))