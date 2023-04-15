#define BLYNK_TEMPLATE_ID "TMPL6LfvZeYXF"
#define BLYNK_TEMPLATE_NAME "raspberry光線"
#define BLYNK_AUTH_TOKEN "95nPoiUKpcr1n4w7xzX0qDfOcJnoVFUh"
   
import gpiozero    #增加LM35溫度量測
from time import sleep 
# https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3008
import requests


mcp3008_light = gpiozero.MCP3008(channel=7)
mcp3008_temperature = gpiozero.MCP3008(channel=6)
buzzer = gpiozero.Buzzer(25) #設定25pin BZ

while(True):    
    lightValue = round(mcp3008_light.value*1000)
    #temperature = (mcp3008_temperature.value*1000)
    temperature = round(mcp3008_temperature.value* (3.3*100),ndigits=3)
    print(temperature) 
    print(lightValue)

    #單一
    #url = f'https://blynk.cloud/external/api/update?token=95nPoiUKpcr1n4w7xzX0qDfOcJnoVFUh&A0={lightValue}'
    #response = requests.get(url)

    #單一
    #url_temperature = f'https://blynk.cloud/external/api/update?token=95nPoiUKpcr1n4w7xzX0qDfOcJnoVFUh&V1={temperature}'
    #response_temperature = requests.get(url_temperature)

    #傳兩個數值網頁要多batch
    url_ALL = f'https://blynk.cloud/external/api/batch/update?token=95nPoiUKpcr1n4w7xzX0qDfOcJnoVFUh&A0={lightValue}&V1={temperature}'
    response_ALL = requests.get(url_ALL)

    #if response.ok :
    #    print('Light連線成功')

    #if response_temperature.ok :
    #    print('溫度連線成功')

    if response_ALL.ok :
        print('溫度連線成功')

    if lightValue < 20:  #燈源不足的會觸發
        buzzer.on()
    else:
        buzzer.off()
    sleep(1)
