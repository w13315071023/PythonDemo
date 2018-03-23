# -*- coding: utf-8 -*-
import json
import base64
import sys
import getopt
import oss2

Host = 'http://39.107.69.190'
CallBackParamDict = {}
STSDataDict = {}
FilePath = 'E:/UEDownload/'

filename = ''
version = ''
userid = ''
openid = ''
unionid = ''
swingid = ''
filetype = ''
number = ''

accessKeyID = ''
accessKeySecret = ''
bucket = ''
serverpath = ''
endpoint = ''
securityToken = ''
sessionid = ''

opts, args = getopt.getopt(sys.argv[1:], "s:p:", ["filename=", "version=", "userid=", "openid=", "unionid=", "swingid=",
                                                  "type=", "number=", "accessKeyID=", "accessKeySecret=", "bucket=", "serverpath=", "endpoint=", "securityToken=", "sessionid="])

for opt, value in opts:
    if opt == "-s":
        Host = value
    elif opt == "-p":
        FilePath = value
    elif opt == "--filename":
        filename = value
    elif opt == "--version":
        version = value
    elif opt == "--userid":
        userid = value
    elif opt == "--openid":
        openid = value
    elif opt == "--unionid":
        unionid = value
    elif opt == "--swingid":
        swingid = value
    elif opt == "--type":
        filetype = value
    elif opt == "--number":
        number = value
    elif opt == "--accessKeyID":
        accessKeyID = value
    elif opt == "--accessKeySecret":
        accessKeySecret = value
    elif opt == "--bucket":
        bucket = value
    elif opt == "--serverpath":
        serverpath = value
    elif opt == "--endpoint":
        endpoint = value
    elif opt == "--securityToken":
        securityToken = value
    elif opt == "--sessionid":
        sessionid = value


def join_DictTo_HTML_Param(dict):
    tempArray = []
    for dictItem in dict:
        tempArray.append(dictItem + "=" + str(dict[dictItem]))
    return "&".join(tempArray)


def uoload_OSS_Server():

    auth = oss2.StsAuth(
        accessKeyID, accessKeySecret, securityToken)
    oss_bucket = oss2.Bucket(auth, endpoint, bucket)

    callback_param = {}
    callback_param['version'] = version
    callback_param['platform'] = '1'
    callback_param['event_userid'] = userid
    callback_param['event_openid'] = openid
    callback_param['unionid'] = unionid
    callback_param['type'] = filetype
    callback_param['swingid'] = swingid
    callback_param['videoNumber'] = number
    callback_param['sessionid'] = sessionid
    callback_param['bucket'] = bucket
    callback_param['endpoint'] = endpoint
    callback_param['objectKey'] = serverpath + filename

    callback_dict = {}
    callback_dict['callbackUrl'] = Host + "/pc/oss/callback"
    callback_dict['callbackBody'] = join_DictTo_HTML_Param(callback_param)
    # print joinDictToHTMLParam(callback_param)

    callback_str = json.dumps(callback_dict).strip()
    base64_callback_body = base64.b64encode(callback_str)
    headers = {'x-oss-callback': base64_callback_body}

    print serverpath

    state = oss_bucket.put_object_from_file(serverpath+filename, FilePath+filename, headers)
    print state

uoload_OSS_Server()

print 'Done'
