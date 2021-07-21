import speedtest
import os

p = os.popen(f'speedtest-cli --simple')
print(p.read())

