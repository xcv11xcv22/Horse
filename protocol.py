from data_convert import *

def plStrToBytes(s):
    tag, data = strToBytes(s)
    b_len = numToBytes(len(data))
    
    return tag.encode() + b_len + data

def plBytesToStr(bs):

    b_size, str_len = bytesToNum(bs[1:])
    data = bytesToStr(bytes([bs[0]])+ bs[2+b_size:])
    return data


a = plStrToBytes(b"aaa")
b = plBytesToStr(a)

c = plStrToBytes(b)
d = plBytesToStr(c)
