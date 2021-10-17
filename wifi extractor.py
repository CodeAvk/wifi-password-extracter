# To See wifi Password in Wiondows
# Basic Process

# open Comand Promt and Type -netsh wlan show profiles

import  subprocess

def get_wifi_profiles():
    # check_output() it's take one output i.e  a list added
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    print(meta_data)  # This gives Information in the form of Binary
    print(type(meta_data))

    # To convert byte into String by using decode function
    data = meta_data.decode("utf-8")
    # print(data)

    # Now we get our information as well as some unnecessary data
    # to print only valid dataf
    data = data.split("\n")
    # print(data)

    names = []

    for line in data:
        if " All User Profile     : " in line:
            # print(line)
            name = line.split(":")[1]
            # names.append(name)
            names.append(name[1:-1])

    return names



passwords= "y"
for name in get_wifi_profiles():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles',name,"key=clear"])
    data = meta_data.decode("utf-8",errors="backslashreplace")
    data=data.split("\n")
    names=[]
    for line in  data:
        if "Key Content " in line:
         passwords= line.split(":")[1]

    print(name," : ",passwords)