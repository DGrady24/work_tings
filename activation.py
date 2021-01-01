#!/usr/bin/env python3.9
# Version 1.0
# Written by Rob Collins

from tkinter import *
from os import *
import tkinter as tk

window = tk.Tk()
window.title("Activation Suite v1.0")

heading_label = tk.Label(text="LTN Appliance Activation Suite.")
heading_label.pack()

host_name = tk.Entry()
host_name_label = tk.Label(text="Hostname")
host_name.pack()
host_name_label.pack()

ip_addr = tk.Entry()
ip_addr_label = tk.Label(text="IP Address")
ip_addr.pack()
ip_addr_label.pack()

flowc = StringVar()
sprd = StringVar()
schd = StringVar()
videqctl = StringVar()
encdr = StringVar()
decdr = StringVar()

software = tk.Frame(relief=tk.GROOVE, borderwidth=5)
software_label = tk.Label(software, text="Check the desired software to deploy.")
flowc_chkbox = tk.Checkbutton(software, text="Flowclient", variable=flowc, onvalue='-f', offvalue='')
sprd_chkbox = tk.Checkbutton(software, text="Spread", variable=sprd, onvalue='-s', offvalue='')
schd_chkbox = tk.Checkbutton(software, text="Schedule Agent", variable=schd, onvalue='-a', offvalue='')
videqctl_chkbox = tk.Checkbutton(software, text="Video Equipment Control", variable=videqctl, onvalue='-c', offvalue='')
encdr_chkbox = tk.Checkbutton(software, text="LTN Encoder", variable=encdr, onvalue='-e', offvalue='')
decdr_chkbox = tk.Checkbutton(software, text="LTED Decoder", variable=decdr, onvalue='-G', offvalue='')
software.pack()
software_label.pack()
flowc_chkbox.pack()
sprd_chkbox.pack()
schd_chkbox.pack()
videqctl_chkbox.pack()
encdr_chkbox.pack()
decdr_chkbox.pack()

chan = tk.Entry()
chan_label = tk.Label(text="Channel")
chan.pack()
chan_label.pack()

rp = tk.Entry()
rp_label = tk.Label(text="Receive Port")
rp.pack()
rp_label.pack()

ovly = tk.Entry()
ovly_label = tk.Label(text="Overlay")
ovly.pack()
ovly_label.pack()

fc = tk.Entry()
fc_label = tk.Label(text="Flowclient ID")
fc.pack()
fc_label.pack()


def software_deploy():
    selection = flowc.get(), sprd.get(), schd.get(), videqctl.get(), encdr.get(), decdr.get()
    selected_software = ''
    for i in selection:
        if i != '':
            selected_software += i + ' '
    selected_software += "-H"
    return "/usr/local/sbin/deploy_software.sh " + selected_software + " " + host_name.get() + " " + ip_addr.get()


def run_activation():
    return "~/work_tings/activate_appliance %s %s %s %s %s" % (host_name.get(), rp.get(),
                                                               chan.get(), ovly.get(), fc.get())


def connect():
    system("ssh -p 3993 col-control.livetimenet.net " + software_deploy())


run = tk.Frame(relief=tk.RAISED, borderwidth=5)
run_button = tk.Button(run, text="Run Activation", command=connect)
run.pack()
run_button.pack()
window.mainloop()
