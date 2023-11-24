import urequests
import ujson
import machine
import time


def get_battery():
    try:
        response = urequests.get('http://localhost:8080/battery-stats')
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
        else:
            print("Request failed with status code:", response.status_code)

    except Exception as e:
        print("Exception occurred:", e)


def charge_or_not(charge):
    relay_pin = machine.Pin(5, machine.Pin.OUT)
    relay_pin.value(0)
    while response == 1:
        if charge <= 60 and status == False:
            relay_pin.value(1)
        elif charge == 95 and status == True:
            relay_pin.value(0)


charge = get_battery()
charge_or_not(charge)
