import tkinter as tk
import requests
import threading
import psutil
import customtkinter as ctk
from sys import exit
import time

ip_address = "192.168.157.68"
ll = ""
ul = ""
def u_submit(root, name, lb, ub):
    if lb.get().isnumeric() and ub.get().isnumeric() and int(ub.get()) > int(lb.get()):
        requests.post(f"http://{ip_address}:8080/change-bounds", {
            "lower_limit": int(lb.get()),
            "upper_limit": int(ub.get())
        })

        for widget in root.winfo_children():
            widget.pack_forget()

        ans1 = ctk.CTkLabel(root, text=f'The laptop will charge when it is below {lb.get()}%',
                             font=("bahnschrift", 18))
        ans1.pack(padx=(30, 0), pady=(30, 10))
        ans2 = ctk.CTkLabel(root, text=f'The laptop will stop charging when it is below {ub.get()}%',
                             font=("bahnschrift", 18))
        ans2.pack(padx=(30, 0), pady=10)
        quit_button = ctk.CTkButton(root, text='Stop', command=lambda: quit())
        quit_button.pack(pady=(10, 0))

def increase_trigger(root, popupLabel, stop_button, continue_button):
    # Perform necessary actions when continuing charging

    requests.post(f"http://{ip_address}:8080/change-bounds", {
        "lower_limit": int(1),
        "upper_limit": int(100)
    })

    # Remove popup elements from the root window
    popupLabel.pack_forget()
    stop_button.pack_forget()
    continue_button.pack_forget()

    u_home(root)

def update_ll(event,):
    global ll
    if event.keysym == 'BackSpace':
        ll = ll[:-1]
    else:
        ll += event.char

def update_ul(event):
    global ul
    if event.keysym == 'BackSpace':
        ul = ul[:-1]
    else:
        ul += event.char

def check_bounds():
    battery = psutil.sensors_battery()
    percent = battery.percent
    data = requests.post(f"http://{ip_address}:8080/update-battery", {
        "laptop_battery": percent
    })
    data = data.json()
    return data

def check_ifcharge():
    data = check_bounds()
    return data["should_charge"]

def clear_widgets(root):
    for widget in root.winfo_children():
        print(widget)
        widget.pack_forget()
def check_upper_limit(root):
    s = "Your device has stopped charging, click continue to charge anyways"
    popupLabel = ctk.CTkLabel(root, text=s,font=("bahnschrift", 18))
    popupLabel.pack(pady=(10,25))
    stopButton = ctk.CTkButton(root, text="Stop Charging", command=exit)
    stopButton.pack(pady=(0,20))
    continueButton = ctk.CTkButton(root, text="Continue Charging", command=lambda: increase_trigger(root, popupLabel, stopButton, continueButton))
    continueButton.pack()

def u_home(root):
    global ll, ul
    data = check_bounds()
    heading = ctk.CTkLabel(root, text="Smart charger", font=("bahnschrift", 24, "bold"))
    heading.pack(padx=10, pady=10, anchor='center')

    frame_h = tk.Frame(root, background='White')
    frame_h.pack(anchor='w')

    frame_tf = tk.Frame(frame_h, background='White')
    frame_tf.pack(anchor='w')

    ins_1 = ctk.CTkLabel(frame_tf, text='Enter the Percentage below which you want to charge',
                         font=("bahnschrift", 18))
    ins_1.pack(side='left', padx=(30, 0), pady=10)

    my_entry1 = ctk.CTkEntry(frame_tf, placeholder_text=data["ll"], width=80)
    if ll:
        my_entry1.insert(0, ll)  # Set lb text box value

    my_entry1.pack(side='left', padx=(90, 0))
    my_entry1.bind("<Key>", update_ll)

    ins_2 = ctk.CTkLabel(frame_h, text='Enter the Percentage Above which you want to stop charging',
                         font=("bahnschrift", 18))
    ins_2.pack(side='left', padx=(30, 0), pady=10)

    my_entry2 = ctk.CTkEntry(frame_h, placeholder_text=data["ul"], width=80)
    my_entry2.pack(side='left', padx=(33, 0))
    my_entry2.bind("<Key>", update_ul)

    if ul:
        my_entry2.insert(0, ul)  # Set lb text box value

    name = 'hello'

    sub_button = ctk.CTkButton(root, text='submit', command=lambda: u_submit(root, name, my_entry1, my_entry2))
    sub_button.pack(side='top', fill="both", pady=(10, 0))

def ui():
    global ll, ul
    root = tk.Tk()
    root.geometry("700x200")
    root.title("Folder organizer")
    root.configure(bg="white")
    root.resizable(False, False)


    def update_ui():
        global ll, ul
        clear_widgets(root)
        frame = tk.Frame(root)
        frame.pack()


        if check_ifcharge():
            u_home(frame)
        else:
            ll = ""
            ul = ""
            check_upper_limit(root)
        root.after(15000, update_ui)  # Run every 5000 milliseconds (5 seconds)

    update_ui()

    root.mainloop()

ui()