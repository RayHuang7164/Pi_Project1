import gpiozero
# https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3008
from signal import pause  #執行完就停
mcp3008 = gpiozero.MCP3008(channel=7)
print(mcp3008.value)

pause()