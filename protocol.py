from data_convert import *

def plStrToBytes(s):
    tag, data = strToBytes(s)
    b_len = numToBytes(len(data))
    
    return tag.encode() + b_len + data

def plBytesToStr(bs):
    btag, data = bs[:1], bs[1:]
    if btag != b'b' and btag != b's':
        raise TypeError('invalid tag ' + btag.decode())
    
    size, data = bytesToNum(data)
    data = bytesToStr(btag+data)
    return data


a = plStrToBytes(b"aaaaaaaaa")
b = plBytesToStr(a)

c = plStrToBytes("中文測試中文測試中文測試")
d = plBytesToStr(c)
