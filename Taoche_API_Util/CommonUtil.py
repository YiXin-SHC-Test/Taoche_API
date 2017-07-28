# -*- coding: UTF-8 -*-
__author__ = 'Maglweb'

import sys
import time
import datetime as dt
import hashlib

reload(sys)
sys.setdefaultencoding('utf-8')

'''获取当前时间戳'''
class get_time():

    def time(self):
        now = time.time();
        return now

    '''获取10位时间戳'''
    def second_stamp(self):
        now = int(time.time())
        return now

    '''获取13位时间戳'''
    def milsecond_stamp(self):
        now = int(round(time.time()*1000))
        return now

'''获取MD5加密字符串'''
class MD5():
    def get_MD5(self,Msg):
        """MD5加密算法，返回32位"""
        word = ''
        if isinstance(Msg,unicode):
            word = Msg.encode("utf-8")
        elif not isinstance(Msg,str):
            word = str(Msg)
        m = hashlib.md5()
        m.update(word)
        #print m.hexdigest()
        return m.hexdigest()

if __name__ == "__main__":
    time1 = get_time()
    print time1.time()
    print time1.second_stamp()
    print time1.milsecond_stamp()
    MD5 = MD5()
    print MD5.get_MD5("123")