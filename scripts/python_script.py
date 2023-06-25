import serial
import pydirectinput

arduino = serial.Serial('COM9', 115200, timeout=.1)     #serial input from arduino.

pydirectinput.PAUSE = 0

keysDown = {}   #list of currently pressed keys


def keyDown(key):               #what to do if key pressed. takes value from handleJoyStickAsArrowKeys
    keysDown[key] = True        #adds key to KeysDown list
    pydirectinput.keyDown(key)  #runs pydirectinput using key from (argument)


def keyUp(key):                     #what to do if key released. takes value from handleJoyStickAsArrowKeys
    if key in keysDown:
        del (keysDown[key])         #remove key from KeysDown
        pydirectinput.keyUp(key)    #runs pydirectinput using key from (argument)


def handleJoyStickAsArrowKeys(x, y, z):
    if y == 0:          #0 is down on joystick, 2 is up on joystick else is neutral
        keyDown('down')   
        keyUp('up')   
    elif y == 2:       
        keyDown('up')
        keyUp('down')
    else:               
        keyUp('up')
        keyUp('down')

    if x == 2:          #2 is left on joystick, 0 is right on joystick else is neutral
        keyDown('left')
        keyUp('right')
    elif x == 0:        
        keyDown('right')
        keyUp('left')
    else:              
        keyUp('left')
        keyUp('right')

    if z == 1:          #1 is button pressed else not pressed
        keyDown('e') 
    else:
        keyUp('e')     


while True:
    rawdata = arduino.readline()            #read serial data from arduino one line at a time
    data = str(rawdata.decode('utf-8'))     #decode the raw byte data into UTF-8
    if data.startswith("S"):                #make sure the read starts in the correct place
        dx = int(data[1])                   #X direction is second digit in data (data[0] is 'S')
        dy = int(data[3])                   #Y direction is fourth digit in data
        JSButton = int(data[5])             #JSButton is sixth digit in data
        handleJoyStickAsArrowKeys(dx, dy, JSButton)     #run body of code using dx, dy and JSButton as inputs
