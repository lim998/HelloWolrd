help="help"
start="start"
stop="stop"
quit="quit"
done= False
msg_help='''

Start - to start the car
stop - to stop the car
quit - to quit
'''

while done==False:
 ans = input("hi")
 if ans == help:
    print(msg_help)
 elif ans == start:
    print(start)
 elif ans == stop:
    print (stop)
 elif ans == quit:
    done = True
 else:
    print("I dont't understand...")

