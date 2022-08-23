# i need to incorporate network scanning for different OS's
#Add a little more functionality to the program
#if all goes well I will be able to use the program to scan for wifi networks and connect to them automatically
#Also could run recon on device
import os
from pyfiglet import Figlet
global cam,call ,video,cap

fig = Figlet(font='slant')
print(fig.renderText('Remote Control'))


target = input('Enter target: ')
os.system('adb tcpip 5555')
os.system(('adb connect ' + target))




def call():
    cell = input('Enter cell number: ')
    os.system('adb shell am start -a android.intent.action.CALL -d tel:'+ cell)


    return True

def cam():
    os.system('adb shell am start -a android.media.action.IMAGE_CAPTURE')
    os.system('timeout 5')
    os.system('adb shell input keyevent 27')

    return True
def video():
    os.system('adb shell am start -a android.media.action.VIDEO_CAMERA')
    os.system('timeout 5')
    os.system('adb shell input keyevent 27')
    return True
def cap():
    os.system('adb shell screencap -p storage/sdcard0/screen.png')
    os.system('adb pull storage/sdcard0/screen.png')
    return True

while True:
    print('1. Call')
    print('2. Camera')
    print('3. Video')
    print('4. Capture')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        call()
    elif choice == '2':
        cam()
    elif choice == '3':
        video()
    elif choice == '4':
        cap()
    elif choice == '5':
        os.system('adb kill-server')
        print('[*]Exiting program...goodbye!!!')
        break
    else:
        print('Invalid choice')
        break
