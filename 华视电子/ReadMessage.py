# -*- coding:utf-8 -*-
import ctypes
import os
import time

PROJECT_PATH = os.path.dirname(__file__)
DLL_PATH = os.path.join(PROJECT_PATH,"Termb.dll")

print DLL_PATH

myDLL = ctypes.WinDLL(DLL_PATH)
print myDLL

ref = myDLL.CVR_InitComm(1002)
if ref != 1:
    print "Init CVR Failed!"

while True:
    time.sleep(1)
    ref = myDLL.CVR_Authenticate()
    if ref == 0:
        print "CVR uninitial!"
    elif ref == 1:
        ref = myDLL.CVR_Read_Content(1)
        if ref == 0:
            print "Read card failed!"
        elif ref == 1:
            print "Read card success!"
            break
        elif ref == 99:
            print "Read card abnormal!"
    elif ref == 2:
        print "Find card failed!"
    elif ref == 3:
        print "Select card failed!"

ref = myDLL.CVR_Read_Content(1)

# myDLL.GetPeopleName(char *strTmp, int *strLen)	    			 	得到姓名信息	
# myDLL.GetPeopleSex(char *strTmp, int *strLen)	    			 	得到性别信息	
# myDLL.GetPeopleNation(char *strTmp, int *strLen)	    			 	得到民族信息	
# myDLL.GetPeopleBirthday(char *strTmp, int *strLen)			 	得到出生日期	
# myDLL.GetPeopleAddress(char *strTmp, int *strLen)			 	得到地址信息	
# myDLL.GetPeopleIDCode(char *strTmp, int *strLen)			 	得到身份证号信息
# myDLL.GetDepartment(char *strTmp, int *strLen)	    			 	得到发证机关信息
# myDLL.GetStartDate(char *strTmp, int *strLen)	    					得到有效开始日期	
# myDLL.GetEndDate(char *strTmp, int *strLen)	        				得到有效截止日期
# myDLL.CVR_GetSAMID(char *SAMID)	        				    得到安全模块号
# myDLL.GetFPDate (unsigned char *pData, int * pLen)			    得到指纹数据，不超过1024字节
# myDLL.GetBMPData (unsigned char *pData, int * pLen)			    得到头像照片bmp数据，不超过38862字节
# myDLL.Getbase64BMPData (unsigned char *pData, int * pLen)	    得到头像照片base64编码数据，不超过38862*2字节
# myDLL.Getbase64JpgData (unsigned char *pData, int * pLen)			得到头像照片jpg数据，不超过38862字节


# //以下为可选API函数,方便二次开发，unicode
# myDLL.GetPeopleNameU(char *strTmp, int *strLen)	    			 	得到姓名信息	
# myDLL.GetPeopleSexU (char *strTmp, int *strLen)	    			 	得到性别信息	
# myDLL.GetPeopleNationU (char *strTmp, int *strLen)	    			 	得到民族信息	
# myDLL.GetPeopleBirthdayU (char *strTmp, int *strLen)			 	得到出生日期	
# myDLL.GetPeopleAddressU (char *strTmp, int *strLen)			 	得到地址信息	
# myDLL.GetPeopleIDCodeU (char *strTmp, int *strLen)			 	得到身份证号信息
# myDLL.GetDepartmentU (char *strTmp, int *strLen)	    			 	得到发证机关信息
# myDLL.GetStartDateU (char *strTmp, int *strLen)  					得到有效开始日期	
# myDLL.GetEndDateU (char *strTmp, int *strLen)      				得到有效截止日期
# myDLL.CVR_GetSAMIDU (char *SAMID)	        			    得到安全模块号
# myDLL.GetFPDate (unsigned char *pData, int * pLen)			    得到指纹数据，不超过1024字节
# myDLL.GetBMPData (unsigned char *pData, int * pLen)			    得到头像照片bmp数据，不超过38862字节
# myDLL.Getbase64BMPDataU (unsigned char *pData, int * pLen)	    得到头像照片base64编码，不超过38862*4字节
# myDLL.Getbase64JpgData U (unsigned char *pData, int * pLen)		得到头像照片jpg的base64编码，不超过38862*2字节


# myDLL.etJpgData(unsigned char * jpgData, int * pLen);				获取jpg二进制数据
# myDLL.etSexCode(unsigned char * sexData, int * pLen);				得到性别代码
# myDLL.etNationCode(unsigned char * nationData, int *pLen);			得到民族代码

myDLL.CVR_CloseComm()