#!/usr/bin/env python3.9

#Version 2.0
#Written by Rob Collins

import tkinter as tk

window = tk.Tk()
window.title("Reliability Calculator")

heading = tk.Label(text="This application can be used to determine the reliability and availability of an endpoint/site.", height=5)
heading.pack()

packets_missed = tk.Entry()
packets_missed.pack()
missing_label = tk.Label(text="Packets Missed")
missing_label.pack()

spacer1 = tk.Frame(height=10)
spacer1.pack()

total_packets = tk.Entry()
total_packets.pack()
total_label = tk.Label(text="Total Packets")
total_label.pack()

spacer1 = tk.Frame(height=10)
spacer1.pack()

discon = tk.Entry()
discon.pack()
discon_label = tk.Label(text="Disconnection Time")
discon_label.pack()

dim = tk.Entry()
dim.pack()
dim_label = tk.Label(text="Days in Month")
dim_label.pack()

spacer2 = tk.Frame(height=10)
spacer2.pack()

def cal_rel():
    missed = packets_missed.get()
    total = total_packets.get()
    missed = int(missed)
    total = int(total)
    num1 = (1-(missed/total))*100
    return num1


def cal_avl():
    disconnect = discon.get()
    days = dim.get()
    disconnect = int(disconnect)
    days = int(days)
    discon_seconds = (disconnect/1000000)
    seconds_per_month = (60*60*24*days)
    num2 = (1-(discon_seconds/seconds_per_month))*100
    return num2


def update_val():
    num1 = cal_rel()
    reliability["text"] = num1
    if num1 >= 99.999:
        reliability["background"] = "PaleGreen1"
    else:
        reliability["background"] = "IndianRed1"
    num2 = cal_avl()
    availability["text"] = num2
    if num2 >= 99.999:
        availability["background"] = "PaleGreen1"
    else:
        availability["background"] = "IndianRed1"


rel = tk.Frame(window, relief=tk.GROOVE, borderwidth=5)
rel.pack()
reliability = tk.Label(rel, text='Pleae input values and press "Calculate"')
rel_label = tk.Label(text="Reliability")
reliability.pack()
rel_label.pack()

avl = tk.Frame(relief=tk.GROOVE, borderwidth=5)
avl.pack()
availability = tk.Label(avl, text='Pleae input values and press "Calculate"')
avl_label = tk.Label(text="Availability")
col_code = tk.Label(text="Green indicates 5 9's reliability/availability, Red indicates failure to meet 5 9's.")
availability.pack()
avl_label.pack()
col_code.pack()

button1 = tk.Frame(relief=tk.GROOVE, borderwidth=5)
button1.pack()
calc = tk.Button(button1, text="Calculate", width=20, command=update_val)
calc.pack()

window.mainloop()
