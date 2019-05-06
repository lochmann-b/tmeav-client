import os
import tkinter as tk
from tkinter import messagebox
import requests
import json

### action handler

def response_received(response):
    print(response)

def validate_email(email, label):    
    url = os.getenv('TMEAV_URL') if os.getenv('TMEAV_URL') is not None else "http://localhost:5000/api/v1/isEmailAddressValid"
    try:
        response = requests.post(url, json={'emailAddress':email}, headers={"Content-Type":"application/json"})
        if response.status_code == 200:        
            is_email_address = response.json()['isValid']
            label['text'] = 'TMEAV Says: This is an email address' if is_email_address else 'TMEAV says: This is not an email address'
        else:
            label['text'] = 'TMEAV returned status code: {}'.format(response.status_code)
    except Exception as ex:
        label['text'] = ''
        messagebox.showerror("Could not fetch data", ex)


### Main
if __name__ == '__main__':
    root_window = tk.Tk()
    root_window.title("TMEAV")
    root_window.geometry("280x150")

    frame = tk.Frame(root_window)
    frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.9, anchor='n')

    entry = tk.Entry(frame)
    entry.place(relwidth=0.65, height=20)

    validate_button = tk.Button(frame, text="Validate")
    validate_button.place(relx=0.7, height=20, relwidth=0.3)

    result_label = tk.Label(frame, text="Enter an email address and click validate")
    result_label.place(relx=0.0, rely=0.2, relwidth=1.0, relheight=0.45)

    validate_button.config(command=lambda: validate_email(entry.get(), result_label))

    root_window.mainloop()
