#!/home/other/anaconda3/bin/python3


import serial
from pynput.keyboard import Key ,Controller as Keyboard
from pynput.mouse import Button ,Controller as Mouse

keyboard = Keyboard()
mouse = Mouse()



#Global Variables

# Space, W, A, S, D in order 
buttonStateList = [0,0,0,0,0]

keyMap = [Key.space, 'w', 'a', 's', 'd']

                                                                                                                                                                                                                               

def handleButtonState(buttonStates):
    for i in range(0, len(buttonStates)):
        if buttonStates[i] == 1 and buttonStateList[i] == 0:
            keyboard.press(keyMap[i])
        if buttonStates[i] == 0 and buttonStateList[i] == 1:
            keyboard.release(keyMap[i])
        buttonStateList[i]= buttonStates[i]

def handleMouseMovement(x, y):
    if abs(x) < 10:
        x = 0
    if abs(y) < 10:
        y= 0
    mouse.move(x/64, -y/64)
    


def main():
    arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=.1)
    while True:
        dataRaw = arduino.readline()
        buttonStates = 5 * [0]
        try:
            data = dataRaw.decode('ascii')
            # 'S' acts a seperator
            if len(data) > 0 and data[0] == 'S':
                data = data[1:]
                dataArraySplit = data.split(',')

                # Extract all the button values
                for i in range(0, len(buttonStates)):
                        buttonStates[i] = int(dataArraySplit[i])

                
                x = int(dataArraySplit[5])
                y = int(dataArraySplit[6].split('\\')[0])
                handleButtonState(buttonStates)
                handleMouseMovement(x,y)

        except:
            continue
        
		
main()