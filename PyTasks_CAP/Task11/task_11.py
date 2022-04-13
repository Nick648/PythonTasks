'''
Вариант 40
'''
import struct

def parse_array(data, size, offset, type):
    return list(struct.unpack(f'<{size}{type}',
                              data[offset: offset + size * struct.calcsize(type)]))

def parse_g(data, offset): #Байтовая строка, смещение
    g1 = struct.unpack('<i', data[offset: offset + 4])[0] #LittleAndian <, big: >
    g2 = struct.unpack('<h', data[offset + 4: offset + 4 + 2])[0]
    return {'G1' : g1, 'G2': g2}

def parse_f(data, offset):
    #f1 = list(struct.unpack('<5h', data[offset: offset + 10]))  # LittleAndian <, big: >
    f1 = parse_array(data, 5, offset, 'h')
    f2 = struct.unpack('<q', data[offset + 10: offset + 10 + 8])[0]
    f3 = struct.unpack('<d', data[offset + 18: offset + 18 + 8])[0]
    f4_size, f4_offset = struct.unpack('<II', data[offset + 26: offset + 26 + 8])
    f4 = parse_array(data, f4_size, f4_offset, 'h')
    f5 = struct.unpack('<f', data[offset + 34: offset + 34 + 4])[0]
    f6 = struct.unpack('<q', data[offset + 38: offset + 38 + 8])[0]
    return {'F1': f1, 'F2': f2, 'F3': f3, 'F4': f4, 'F5': f5, 'F6': f6}

def parse_e(data, offset):
    e1 = struct.unpack('<Q', data[offset: offset + 8])[0]
    e2_offset = struct.unpack('<H', data[offset + 8: offset + 8 + 2])[0]
    e2 = parse_f(data, e2_offset)
    e3 = parse_g(data, offset + 10)
    return {'E1': e1, 'E2': e2, 'E3': e3}

#def parse...
#main(parse_a(data, 4)) # offset = 4