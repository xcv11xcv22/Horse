def strToBytes(s):
    if isinstance(s, bytes):
        tag = 'b'
        data = s
    elif isinstance(s, str):
        tag = 's'
        data = s.encode('utf-8')
    else:
        raise TypeError('invalid tag ' + tag)
    return (tag, data)

def bytesToStr(bs):
    if not isinstance(bs, bytes):
        raise TypeError('invalid tage ' + type(bs))
    data = bs.decode()
    tag, _str = data[0], data[1:]
    
    return _str
    

def numToBytes(n):
    data = b''
    size = 0
    while n > 0:
        d = n%256
        data += bytes([d])
        n >>= 8
        size += 1
        
    return bytes([size]) + data

def bytesToNum(bs):
    data = 0
    exp = 0
    size = bs[0]
    for i in range(1, 1+size):
        data += bs[i] << exp
        exp += 8

    return size, data

    

