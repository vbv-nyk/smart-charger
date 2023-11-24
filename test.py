import psutil


def get_battery_percentage():
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = battery.power_plugged
    print(charging)
    status = "Charging" if charging else "Discharging"

    print(f'Battery: {percent}% ({status})')


get_battery_percentage()
