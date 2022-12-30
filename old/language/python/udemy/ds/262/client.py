import zmq
import time

context = zmq.Context()

socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:5555")

id = 0
while True:
    id += 1
    socket.send(('sub1:' + str(id)).encode())
    print("Sended: %s." % id)
    time.sleep(1)
