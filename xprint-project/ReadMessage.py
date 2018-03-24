# -*- coding:utf-8 -*-
import ctypes
import os
import io
import time
import execjs

PROJECT_PATH = os.path.dirname(__file__)
DLL_PATH = os.path.join(PROJECT_PATH,"Termb.dll")
def read_card():
    cardstrarray = []
    myDLL = ctypes.WinDLL(DLL_PATH)

    ref = myDLL.CVR_InitComm(1001)
    if ref == 1:
        while True:
            time.sleep(1)
            ref = myDLL.CVR_Authenticate()
            if ref == 0:
                print ("CVR uninitial!")
            elif ref == 1:
                ref = myDLL.CVR_Read_Content(1)
                if ref == 0:
                    print ("Read card failed!")
                elif ref == 1:
                    print ("Read card success!")
                    break
                elif ref == 99:
                    print ("Read card abnormal!")
            elif ref == 2:
                print ("Find card failed!")
            elif ref == 3:
                print ("Select card failed!")

        ref = myDLL.CVR_Read_Content(1)

        userpath = os.getenv("USERPROFILE")+"\\Appdata\\Local\\Temp\\chinaidcard\\"
        txtfile = open(userpath+"wz.txt")
        line = txtfile.readline()
        while line:
            line = line.replace('\n','')
            line = line.replace(' ','')
            cardstrarray.append(line)
            line = txtfile.readline()

        txtfile.close()
        myDLL.CVR_CloseComm()
        print (cardstrarray)
    else:
        print ("Init CVR Failed!")

def read_call_js():
    jsfile = io.open(PROJECT_PATH+"/ticket-new/js/Test.js").read().encode("utf-8")
    jsfile = str(jsfile).replace('\n','')
    print (jsfile)
    # callfunc = execjs.compile(jsfile)
    #refstr = execjs.compile(jsfile).call('add', 3,4)
    #print execjs.compile(open(dir).read().decode('utf-8')).call('add',3,4)
    # print (refstr)

read_call_js()
print ("Done")