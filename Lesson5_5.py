import gpiozero    #增加LM35溫度量測
from time import sleep 
# https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3008

mcp3008_light = gpiozero.MCP3008(channel=7)
mcp3008_temperature = gpiozero.MCP3008(channel=6)
buzzer = gpiozero.Buzzer(25) #設定25pin BZ

while(True):    
    lightValue = round(mcp3008_light.value*1000)
    #temperature = (mcp3008_temperature.value*1000)
    temperature = round(mcp3008_temperature.value* (3.3*100),ndigits=2)
    print(temperature) 
    #print(lightvalue)
    if lightValue < 20:  #燈源不足的會觸發
        buzzer.on()
    else:
        buzzer.off()
    sleep(1)
