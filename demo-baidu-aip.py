# -*- coding:utf-8 -*-
import json
from aip import AipOcr

APP_ID = "9851066"
API_KEY = "LUGBatgyRGoerR9FZbV4SQYk"
SECRET_KEY = "fB2MNz1c2UHLTximFlC4laXPg7CVfyjV"

aipOcr = AipOcr(APP_ID,API_KEY,SECRET_KEY)

filePath = "C:/Users/Mr.Sun/Desktop/UploadVideo/20170707154412643.jpg"
def get_file_content(filePath):
    with open(filePath,"rb") as fp:
        return fp.read()

options = {
    "detect_direction":"true",
    "language_type":"CHN_ENG"
}

result = aipOcr.basicGeneral(get_file_content(filePath),options)
print json.dumps(result).decode("unicode-escape")