import urequests
import ujson
import machine
import time
import network

def smart_charge(should_charge):
	if should_charge:
		print("Charging your device")
		relay_pin = machine.Pin(5, machine.Pin.OUT)
	else:
		print("Battery high, not charging")
		relay_pin = machine.Pin(5, machine.Pin.IN)


def get_battery():
    try:
	response = urequests.get('http://192.168.157.217:8080/battery-stats',timeout=5000)
	if response.status_code == 200:
            data = ujson.loads(response.text)
            print("Response Type:", type(response))
            print("Response Text:", response.text)
            print("Parsed Response Type:", type(data))
            return data["should_charge"]
	else:
            print("No 'battery' field in the response")
            return False
    except Exception as e:
        print("Exception occurred:", e)


ssid = "moto"
password = "12345678"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Attempting to connect")
    pass

print("Connected to WiFi")


while(True):
	should_charge = get_battery()
	print(should_charge)
	smart_charge(should_charge)
	time.sleep(2)
