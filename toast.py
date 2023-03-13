from datetime import datetime, timedelta
import tkinter
import time
import os

passive_aggressive_message = "Please return this laptop to the IT department (room 323). If for any reason you can't use your actual laptop, feel free to talk to Melissa or Ben to check out this computer again. Thank you!"


def show_toast():
    time.sleep(1)
    root = tkinter.Tk()
    root.title('Loaner Laptop Return Reminder')
    root.call('wm', 'attributes', '.', '-topmost', True)
    toast = tkinter.Label(root, text=passive_aggressive_message, font="helvetica 40",wraplength=1000, justify="center", width=500, height=500)
    toast.config(bg="gray63", fg="black")
    toast.pack()
    path = '~/loaner_reminder/toast.py'
    root.mainloop()


def check_date():
    with open('/Users/'+os.getlogin()+'/loaner_reminder/data.log', 'r') as f:
        data = f.read().split('\n')
    execute_date = datetime.fromisoformat(data[0]) + timedelta(days=int(data[1]))
    if execute_date < datetime.now():
        return True


if __name__ == '__main__':
    if check_date():
        show_toast()
#    show_toast()
