import gpiozero
# https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3008
from signal import pause  #執行完就停
from time import sleep  #執行完就停
mcp3008 = gpiozero.MCP3008(channel=7)

while(True):
    lightvalue = round(mcp3008.value*1000)
    print(lightvalue)
    sleep(1)
    
#pause()