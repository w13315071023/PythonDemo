# -*- coding:utf-8 -*-
import ctypes
import sys
import os
import io
import time
import execjs
from PIL import Image
from flask import Flask
from flask import render_template
from flask import request

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


PROJECT_PATH = os.path.dirname(__file__)
DLL_PATH = os.path.join(PROJECT_PATH,"Termb.dll")

app = Flask(__name__ , static_folder=PROJECT_PATH + '/templates/',static_url_path='')
IsGetFrame = False

@app.route('/',methods = ['GET'])
def home():
    print 'index'
    # read_card()
    # jsfile = io.open(PROJECT_PATH+"/ticket-new/TicketIndex.html",'r',encoding='UTF-8').read()
    return render_template("index.html")

@app.route('/file', methods = ['GET','POST'])
def File():
    carddata = read_card()
    return render_template("templateindex.html",
                           name=carddata[0],
                           sex=carddata[1],
                           nation=carddata[2],
                           year=str(carddata[3])[0:4],
                           address=carddata[4],
                           idcarda=(carddata[5])[0:10],
                           idcardb=(carddata[5])[14:18],
                           photoimg = request.form["Filename"])
    # return render_template("templateindex.html",
    #                        datetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
    #                        name='孙晶伟',
    #                        sex='男',
    #                        nation='蒙古',
    #                        year='1994',
    #                        address='河南省天津市北京区内蒙古路上海社区2号110',
    #                        idcarda='1101201994',
    #                        idcardb='1234',
    #                        photoimg=request.form["Filename"])


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
        txtfile = io.open(userpath+"wz.txt")
        line = txtfile.readline()
        while line:
            line = line.replace('\n','')
            line = line.replace(' ','')
            print(line)
            cardstrarray.append(line)
            line = txtfile.readline()

        img = Image.open(str(userpath+"xp.jpg"))
        img.save(PROJECT_PATH + '/templates/img/cardphoto.png')
        myDLL.CVR_CloseComm()
        return cardstrarray
    else:
        print ("Init CVR Failed!")
        return []


if __name__ == '__main__':
    app.run(port=5010)
    print ("Done")
