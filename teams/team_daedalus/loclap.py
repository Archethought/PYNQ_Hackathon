import json
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

print("load from json")
msg_dict = {}
while len(msg_dict) < 3:
    #  Wait for next request from client
    message = socket.recv()
    print(message)
    msg_dict.update(json.loads(message))
    socket.send(b"ACK")
print("finished loading from json")

print("load from json")
print(len(msg_dict))
print(msg_dict)
time_data = {}
for k,d in msg_dict.items():
    print(k)
    print(d)
    bt = d[0]
    times = []
    for dt in d[1]:
        times.append(bt+dt)
    time_data[k] = times
print("finished calculating times")
print(time_data)

t_A = list()
t_B = list()
t_C = list()
dt_AB = list()
dt_CB = list()
for k in msg_dict:
    t_A.append(data_A[1]+data_A[2][idx])
    t_B.append(data_A[1]+data_B[2][idx]+0.001)
    t_C.append(data_A[1]+data_C[2][idx]-0.001)
    dt_AB.append(t_A[-1] - t_B[-1])
    dt_CB.append(t_C[-1] - t_B[-1])
    print(t_A[-1])
    print(t_B[-1])
    print(t_C[-1])
    print(dt_AB[-1])
    print(dt_CB[-1])
    print()
