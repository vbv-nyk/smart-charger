import serial
import psutil
import time
import tkinter as tk
import customtkinter as ctk





def u_submit(root,name, lb,ub):
    if lb.get().isnumeric() and ub.get().isnumeric() and ub.get()>lb.get():
        print(f'Hello {name} and {lb.get()} and {ub.get()}')
        for widget in root.winfo_children():
            widget.pack_forget()

        ans1 = ctk.CTkLabel(root, text=f'The laptop will charge when it is below {lb.get()}%',
                             font=("bahnschrift", 18))
        ans1.pack(padx=(30, 0), pady=(30,10))
        ans2 = ctk.CTkLabel(root, text=f'The laptop will stop charging when it is below {ub.get()}%',
                             font=("bahnschrift", 18))
        ans2.pack(padx=(30, 0), pady=10)
        quit_button = ctk.CTkButton(root, text='Stop', command=lambda:quit())
        quit_button.pack(pady=(10, 0))





def u_home(root):
    heading = ctk.CTkLabel(root, text="Smart charger", font=("bahnschrift", 24, "bold"),
                           text_color='#FFFFFF')
    heading.pack(padx=10, pady=10, anchor='center')

    frame_h = tk.Frame(root, background='#202020')
    frame_h.pack(anchor='w')

    frame_tf = tk.Frame(frame_h, background='#202020')
    frame_tf.pack(anchor='w')

    ins_1 = ctk.CTkLabel(frame_tf, text='Enter the Percentage below which you want to charge', font=("bahnschrift", 18))
    ins_1.pack(side='left',padx=(30,0), pady=10)

    my_entry1 = ctk.CTkEntry(frame_tf, placeholder_text='Enter value',width=80)
    my_entry1.pack(side='left', padx=(90,0))

    ins_2 = ctk.CTkLabel(frame_h, text='Enter the Percentage Above which you want to stop charging', font=("bahnschrift", 18))
    ins_2.pack(side='left',padx=(30,0), pady=10)

    my_entry2 = ctk.CTkEntry(frame_h, placeholder_text='Enter value',width=80)
    my_entry2.pack(side='left', padx=(33,0))
    name='hello'

    sub_button=ctk.CTkButton(root,text='submit',command=lambda :u_submit(root,name,my_entry1,my_entry2))
    sub_button.pack(pady=(10,0))


def ui():
    root = tk.Tk()
    root.geometry("700x200")
    root.title("Folder organizer")
    root.configure(bg="#202020")
    root.resizable(False, False)
    u_home(root)
    root.mainloop()


ui()
