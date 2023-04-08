import private
import requests

from gpiozero import Button
from signal import pause
from gpiozero import RGBLED,Buzzer


state = False
counter = 0

def user_press():  #按下按鈕事件
    global state,counter
    state = not state
    buzzer.on()
    
    if state == True:
        print("開燈")
        counter += 1
        if counter % 7 == 1:
            led.color=(0, 1, 0)  #full green
            url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttkey}?value1=green&value2=1'
        elif counter % 7 == 2:
            led.color=(0, 0, 1)  #full blue
            url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttkey}?value1=blue&value2=2'
        elif counter % 7 == 3:
            led.color=(1, 0, 1)  # magenta 紅紫
            url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttkey}?value1=紅紫&value2=3'
        elif counter % 7 == 4:
            led.color=(1, 1, 0)  # yellow
            url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttkey}?value1=yellow&value2=4'
        elif counter % 7 == 5:
            led.color=(0, 1, 1)  # cyan  藍綠色  
            url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttkey}?value1=藍綠色&value2=5'       
        elif counter % 7 == 6:
            led.color=(1, 1, 1)  # white
            url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttkey}?value1=白&value2=6' 
        elif counter % 7 == 0:
            led.color=(1, 0, 0)  #full red
            url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttkey}?value1=danger&value2=100'

            r = requests.get(url)
            if r.status_code == 200:
                print("發送成功")

    else:
        print("關燈")
        led.color=(0,0,0)

def user_release():
    buzzer.off()



button = Button(18)
led = RGBLED(red=17, green=27, blue=22)
buzzer = Buzzer(25)

button.when_pressed = user_press        #按下按鈕時 user_press
button.when_released = user_release     #釋放按鈕時觸發事件 user_release

pause()