# -*- coding: UTF-8 -*-
import json
from socketIO_client import SocketIO
from voduploadsdk.AliyunVodUtils import *
from voduploadsdk.AliyunVodUploader import AliyunVodUploader
from voduploadsdk.UploadVideoRequest import UploadVideoRequest 

host = 'http://39.107.69.190'
port = 7171
VideoFilePath = 'E:/_wark/TestVideo/WeChat_20171221165925.mp4'
accessKeyID = ''
accessKeySecret = ''
securityToken = ''
serverdir = ''

def testUploadLocalVideo(accessKeyId, accessKeySecret, filePath):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadVideoRequest = UploadVideoRequest(filePath, 'test upload local video')
        videoId = uploader.uploadLocalVideo(uploadVideoRequest)
        print "file: %s, videoId: %s" % (filePath, videoId)
    except AliyunVodException,e:
        print e

def onMessage(*args):
    print 'success'

def onData(data):
    DataDict = json.dumps(data)
    print DataDict
    accessKeyID = data.get('accessKeyID')
    print 'accessKeyID : ' + accessKeyID
    accessKeySecret = data.get('accessKeySecret')
    print 'accessKeySecret : ' + accessKeySecret
    securityToken = data.get('securityToken')
    print 'securityToken : ' + securityToken
    serverdir =  data.get('dir')
    print 'dir : ' + serverdir

data = {
    "type":1
}
sk = SocketIO('http://39.107.69.190',7171)
sk.emit('/pc/osstoken/get',data,onData)
sk.wait_for_callbacks(seconds=1)

testUploadLocalVideo(accessKeyID,accessKeySecret,VideoFilePath)
print 'end'