# -*- coding: utf-8 -*-
import json
import base64
import sys
import getopt
import oss2
from socketIO_client import SocketIO

version	="1234"
platform = "1"
host = 'http://39.107.69.190'
port = '7171'
userID = ''
openID = ''
unionID = ''
swingID = ''
uploadType = ''
VideoNumber = ''
VideoFilePath = 'E:/_wark/TestVideo/WeChat_20171221165925.mp4'
VideoFileName = 'WeChat'
session = []

opts, args = getopt.getopt(sys.argv[1:], "s:p:v:f:n:",["userID=","openID=","swingID=","unionID=","type=","number="])
for opt, value in opts:
    if opt == "-s":
        host = value
    elif opt == "-p":
        port = value
    elif opt == "-v":
        version = value
    elif opt == "-f":
        VideoFilePath = value
    elif opt == "-n":
        VideoFileName = value
    elif opt == "--userID":
        userID = value
    elif opt == "--openID":
        openID = value
    elif opt == "--unionID":
        unionID = value
    elif opt == "--swingID":
        swingID = value
    elif opt == "--type":
        uploadType = value
    elif opt == "--number":
        VideoNumber = value

def onMessage(*args):
    return

def joinDictToHTMLParam(dict):
    tempArray = []
    for dictItem in dict:
        tempArray.append(dictItem + "=" + str(dict[dictItem]))
    return "&".join(tempArray)

def onData(data):
    # print json.dumps(data)

    auth = oss2.StsAuth(data['accessKeyID'], data['accessKeySecret'], data['securityToken'])
    bucket = oss2.Bucket(auth, data['endpoint'], data['bucket'])

    callback_param = {}
    callback_param['version'] = version
    callback_param['platform'] = platform
    callback_param['event_userid'] = userID
    callback_param['event_openid'] = openID
    callback_param['unionid'] = unionID
    callback_param['type'] = uploadType
    callback_param['swingid'] = swingID
    callback_param['videonuber'] = VideoNumber
    callback_param['sessionid'] = session[0]
    callback_param['bucket'] = data['bucket']
    callback_param['endpoint'] = data['endpoint']
    callback_param['objectKey'] = data['dir']+VideoFileName

    callback_dict = {}
    callback_dict['callbackUrl'] = host + "/oss/callback"
    callback_dict['callbackBody'] = joinDictToHTMLParam(callback_param)
    # print joinDictToHTMLParam(callback_param)
    
    callback_str = json.dumps(callback_dict).strip()
    base64_callback_body = base64.b64encode(callback_str)
    headers = {'x-oss-callback': base64_callback_body}

    bucket.put_object_from_file(data['dir']+VideoFileName, VideoFilePath,headers)

data = {
    "type": 1
}

connectStr = host+':'+port+'?version='+version+'&platform='+platform

sk = SocketIO(connectStr)
session = sk._get_engineIO_session()
sk.emit('/pc/osstoken/get', data, onData)
sk.wait_for_callbacks(seconds=1)


print 'true'
