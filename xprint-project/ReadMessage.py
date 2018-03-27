# -*- coding:utf-8 -*-
import ctypes
import sys
import os
import io
import time
import execjs
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
    time.sleep(2)
    # print request.form["Filename"]
    # return """<img src="""+request.form['Filename']+""">"""
    return render_template("templateindex.html",
                           name="马振虎",
                           sex="男",
                           nation="汉",
                           year="1994",
                           moth="03",
                           day="15",
                           address="河南省濮阳市",
                           idcard="123654789321421247",
                           idcardimg = "img/img1.jpg",
                           photoimg = request.form["Filename"])


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

        cardstrarray.append(str(userpath+"xp.jpg"))
        print cardstrarray[8]
        myDLL.CVR_CloseComm()
        return cardstrarray
    else:
        print ("Init CVR Failed!")
        return []


if __name__ == '__main__':
    app.run()
    print ("Done")
