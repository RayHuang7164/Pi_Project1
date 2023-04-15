import gpiozero  #增加LM35溫度量測
# https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3008
from signal import pause  #執行完就停
from time import sleep  #執行完就停
from gpiozero import Buzzer  #增加BZ 

mcp3008_light = gpiozero.MCP3008(channel=7)
Buzzer = gpiozero.Buzzer(25) #設定25pin
mcp3008_temperature = gpiozero.MCP3008(channel=6)

while(True):
    lightvalue = round(mcp3008_light.value*1000)
    temperature = (mcp3008_temperature*1000)
    print(lightvalue)
    print(temperature)

    if lightvalue < 40:  #燈源不足的會觸發
        Buzzer.on()
    else:
        Buzzer.off()
    sleep(1)
    
#pause()