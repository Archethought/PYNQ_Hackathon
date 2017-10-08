import zmq
import time

# trigger the sound collectors by sending a message
# content of the message does not matter, the
# message simply clears the block
# ZeroMQ pattern is PUB-SUB

port = "5556"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

time.sleep(20)

messagedata = 1
socket.send("%s %d" % ('', messagedata))
