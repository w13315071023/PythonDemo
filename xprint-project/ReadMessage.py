# -*- coding:utf-8 -*-
import ctypes
import os
import io
import time
import execjs
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

PROJECT_PATH = os.path.dirname(__file__)
DLL_PATH = os.path.join(PROJECT_PATH,"Termb.dll")

@app.route('/',methods = ['GET','POST'])
def home():
    print 'home'
    # return render_template('home.html')

@app.route('/signin',methods = ['GET'])
def signin_form():
    print 'signin-get'
    # return render_template('form.html')

@app.route('/signin',methods = ['POST'])
def sugnin():
    print 'signin-post'
    # username = request.form['username']
    # password = request.form['password']
    # if username == 'admin' and password == 'password':
    #     return render_template('signin-ok.html',username = username)
    # return render_template('form.html',message = 'Bad username or pasword',username = username )

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

# def read_call_js(array):
#     jsfile = io.open(PROJECT_PATH+"/ticket-new/TicketIndex.html",'r',encoding='UTF-8').read()
#     refstr = execjs.compile(jsfile).call('inputvalue',array[0],array[1],array[2],array[3],array[4],array[5],array[8])
#     print (refstr)

# read_call_js(read_card())

if __name__ == '__main__':
    app.run()
    print ("Done")