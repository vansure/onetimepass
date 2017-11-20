# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:15:35 2017

@author: User
"""
import onetimepass as otp
my_secret = 'MFRGGZDFMZTWQ2LK'

VANSURE_key='NVNDE5TSNBNFUSZU'
VANSURE_token = str(otp.get_totp(VANSURE_key))

YUE_key='LBTWCS2NKJYW4SRP'
YUE_token = str(otp.get_totp(YUE_key))

CashBack_key='IEZXGRDHG42XCWTK'
CashBack_token = str(otp.get_totp(CashBack_key))

if len(VANSURE_token)==5:
	VANSURE_token='0'+VANSURE_token
if len(YUE_token)==5:
	YUE_token='0'+YUE_token
if len(CashBack_token)==5:
	CashBack_token='0'+CashBack_token

print 'VANUSURE:\t',VANSURE_token
print 'YUE:\t\t',YUE_token
print 'CashBack:\t',CashBack_token


