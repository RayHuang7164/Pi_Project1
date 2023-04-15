import gpiozero
# https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3008
from signal import pause  #執行完就停
from time import sleep  #執行完就停
from gpiozero import Buzzer  #增加BZ 

mcp3008 = gpiozero.MCP3008(channel=7)
Buzzer = gpiozero.Buzzer(25) #設定25pin

while(True):
    lightvalue = round(mcp3008.value*1000)
    print(lightvalue)
    if lightvalue < 40:  #燈源不足的會觸發
        Buzzer.on()
    else:
        Buzzer.off()
    sleep(1)
    
#pause()