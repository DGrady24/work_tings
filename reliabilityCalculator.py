#!/usr/local/bin/python3.9

#Version 1.0
#Written by Rob Collins

import tkinter as tk

window = tk.Tk()
window.title("Reliability Calculator")

heading = tk.Label(text="This application can be used to determine the reliability of BW testing.", height=5)
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

spacer2 = tk.Frame(height=10)
spacer2.pack()

equation = ""

def calculate():
    missed = packets_missed.get()
    total = total_packets.get()
    missed = int(missed)
    total = int(total)
    num = (1-(missed/total))*100
    return num


def update_val():
    num = calculate()
    reliability["text"] = num
    if num >= 99.999:
        reliability["background"] = "green"
    else:
        reliability["background"] = "red"


rel = tk.Frame(relief=tk.GROOVE, borderwidth=5)
rel.pack()
reliability = tk.Label(rel, text='Pleae input values and press "Calculate"')
rel_label = tk.Label(text="Reliability")
rel_label.pack()
reliability.pack()

button1 = tk.Frame(relief=tk.GROOVE, borderwidth=5)
button1.pack()
calc = tk.Button(button1, text="Calculate", width=20, command=update_val)
calc.pack()

window.mainloop()
