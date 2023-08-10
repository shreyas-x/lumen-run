import serial

PORT = "/dev/ttyS10"
BAUD = 9600

def init():
    ser = serial.Serial(PORT, BAUD)
    print("BlueRobotics Lumen Control Utility")
    return ser

def loop(ser):
    print("Enter a value from 0 to 6: ", end="")
    val = input()
    if val == '0':
        ser.write(b'0')
        print("Lights are now off")
    elif val == '1':
        ser.write(b'1')
        print("Lights are now at brightness level 1, lowest brightness")
    elif val == '2':
        ser.write(b'2')
        print("Lights are now at brightness level 2")
    elif val == '3':
        ser.write(b'3')
        print("Lights are now at brightness level 3")
    elif val == '4':
        ser.write(b'4')
        print("Lights are now at brightness level 4")
    elif val == '5':
        ser.write(b'5')
        print("Lights are now at brightness level 5")
    elif val == '6':
        ser.write(b'6')
        print("Lights are now at brightness level 6, max brightness")
    else:
        ser.write(b'6')
        print("Lights are now at brightness level 6, max brightness")

def die():
    ser.close()

if __name__ == "__main__":
    try:
        ser = init()
        while(True):
            loop(ser)
    except KeyboardInterrupt:
        die()


