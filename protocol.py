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

def plDataToByte(data):
    if isinstance(data, int):
        result = numToBytes(data)
        return result

    elif isinstance(data, str) or isinstance(data, bytes):
        result = plStrToBytes(data)
        return result

    raise TypeError('invalid tag ' + type(data))

def plByteToData(data):
    if not isinstance(data, bytes):
        raise TypeError('invalid tag ' + type(data))

    btag = data[:1]
    if btag == b's' or btag == b'b':
        result = plBytesToStr(data)
        return result

    result, data = bytesToNum(data)
    return result



a = plDataToByte(b"aaaaaaaaa")
b = (a)

c = plDataToByte("中文測試中文測試中文測試")
d = plByteToData(c)

e = plDataToByte(999999994654654165)
f = plByteToData(e)
k = 1