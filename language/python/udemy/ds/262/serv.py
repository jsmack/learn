import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b'sub1:')
socket.bind("tcp://127.0.0.1:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message.decode())

    #  Do some 'work'
    #time.sleep(1)

    #  Send reply back to client
    #socket.send(b"World")