import private
import requests
url = f'https://maker.ifttt.com/trigger/button_press/with/key/{private.iftttkey}?value1=32c&value2=54'
#print(url)

r = requests.get(url)
if r.status_code == 200:
    print("發送成功")