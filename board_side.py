import urequests
import ujson
import machine
import time
import network

def smart_charge(charge):
	if(charge == -1):
		print("Device not connected to the internet")
		return
	if charge <= 90:
		print("Charging your device")
		relay_pin = machine.Pin(5, machine.Pin.OUT)
	else:
		print("Battery high, not charging")
		relay_pin = machine.Pin(5, machine.Pin.IN)


def get_battery():
    try:
	response = urequests.get('http://192.168.0.108:8080/battery-stats',timeout=5000)
	if response.status_code == 200:
            data = ujson.loads(response.text)
            print("Response Type:", type(response))
            print("Response Text:", response.text)
            print("Parsed Response Type:", type(data))
            if 'battery' in data:
                print("Battery Level:", data['battery'])
                return data['battery']
            else:
                print("No 'battery' field in the response")
                return -1
        else:
            print("Request failed with status code:", response.status_code)
            return -1

    except Exception as e:
        print("Exception occurred:", e)


ssid = "ACT102618905398_2g"
password = "52996826"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Attempting to connect")
    pass

print("Connected to WiFi")


while(True):
	charge = get_battery()
	print(charge)
	smart_charge(charge)
	time.sleep(2)
