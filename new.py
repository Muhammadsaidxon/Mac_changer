#!/usr/bin/env python

import subprocess
interface = input("Interfaceni kiriting : ")
new = input("yangi mac manzil: ")
print("[+] changing mac adress for" + interface + new)

subprocess.call("sudo ifconfig " + interface +" down ", shell=True)
subprocess.call("sudo ifconfig " + interface +" hw ether " + new, shell=True)
subprocess.call("sudo ifconfig " + interface +" up ", shell=True)