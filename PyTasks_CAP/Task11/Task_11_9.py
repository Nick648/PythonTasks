"""
Вариант 9
data[offset + n: offset + n + m] - обычные срезы
"""
import struct


def parse_array(data, size, typ, offset):  # Unpacking an array
    n = struct.calcsize(typ)
    return list(struct.unpack(f'<{size}{typ}',
                              data[offset: offset + size * n]))


def parse_array_struct_d(data, addresses):  # Unpacking a struct-array D
    arr = list()
    for count in range(len(addresses)):
        arr.append(parse_d(data, addresses[count]))
    return arr


def parse_e(data, offset):
    e1 = parse_array(data, 5, 'i', offset)  # Unpacking an array i(4)*5
    e2_size, e2_offset = struct.unpack('<II',
                                       data[offset + 20: offset + 20 + 4 + 4])
    e2 = parse_array(data, e2_size, 'i', e2_offset)
    e3 = struct.unpack('<Q', data[offset + 28: offset + 28 + 8])[0]
    return {'E1': e1, 'E2': e2, 'E3': e3}  # e = 36


def parse_d(data, offset):
    d1 = struct.unpack('<h', data[offset: offset + 2])[0]  # little-endian: < , big-endian: >
    d2 = struct.unpack('<q', data[offset + 2: offset + 2 + 8])[0]
    d3 = struct.unpack('<h', data[offset + 10: offset + 10 + 2])[0]
    d4 = struct.unpack('<h', data[offset + 12: offset + 12 + 2])[0]
    d5 = struct.unpack('<b', data[offset + 14: offset + 14 + 1])[0]
    d6 = parse_array(data, 4, 'b', offset + 15)  # b(1)*4
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6}  # d = 19


def parse_c(data, offset):
    c1_size, c1_offset = struct.unpack('<HH',
                                       data[offset: offset + 2 + 2])
    c1_array = parse_array(data, c1_size, 'I', c1_offset)
    c1 = parse_array_struct_d(data, c1_array)
    c2 = parse_e(data, offset + 4)  # e = 36
    c3 = struct.unpack('<d', data[offset + 40: offset + 40 + 8])[0]
    return {'C1': c1, 'C2': c2, 'C3': c3}  # c = 48


def parse_b(data, offset):
    b1 = struct.unpack('<b', data[offset: offset + 1])[0]
    b2_offset = struct.unpack('<I', data[offset + 1: offset + 1 + 4])[0]
    b2 = parse_c(data, b2_offset)
    return {'B1': b1, 'B2': b2}  # b = 5


def parse_a(data, offset):
    a1 = struct.unpack('<H', data[offset: offset + 2])[0]
    a2 = struct.unpack('<I', data[offset + 2: offset + 2 + 4])[0]
    a3_offset = struct.unpack('<I', data[offset + 6: offset + 6 + 4])[0]
    a3 = parse_b(data, a3_offset)
    a4 = struct.unpack('<f', data[offset + 10: offset + 10 + 4])[0]
    a5 = struct.unpack('<H', data[offset + 14: offset + 14 + 2])[0]
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}


def main(data):
    # Данные начинаются с сигнатуры 0x4b 0x48 0x43 0x42 0x72
    return parse_a(data, 5)  # offset = 5


inp_1 = (b'KHCBr\xaa\xeaA\xc3h\xaf\x83\x00\x00\x00\xe9'
         b'\x8c\xbf>\x9a\xb2^:2\x050Y\\'
         b"\xd6Ca\x92\x8c\xcfE/\xae\xf4\xe7q_c\x97\x8f'\xbd>*\xf6"
         b'\xf5\x10\xcd\xef\xf1Ah'
         b'\x1duZ\x15\x00\x00\x00(\x00\x00\x00K]\xa0\x16'
         b'\x8fI\x06\xd8H$\x81 \xbb'
         b'\x1bY(\x02\x00;\x00\xfaux\x13\\\x18\x03O\xfb'
         b'\xa53\xea|I\xc1\xb0\rrA\xde\x04'
         b'\x00\x00\x00C\x00\x00\x00\x9c\xd1\xfe(\x90'
         b'\x1d/o\x98\x8b\xba\xed\xfc'
         b'\x16\xdb\xbfMS\x00\x00\x00')

main(inp_1)


# For CAP, you only need what is above, having checked in advance for PEP8

def output_data(dic, number=0):  # output dictionary
    print(dic, '\n', 'DICT_' + str(number) + ':\n')
    for i in dic:
        if i == 'A3':
            print('A3:')
            for ib in dic[i]:
                if ib == 'B2':
                    print(" " * 4, 'B2:')
                    for ibc in dic[i][ib]:
                        if ibc == 'C1':
                            print(" " * 8, 'C1:')
                            for ibcd in range(len(dic[i][ib][ibc])):
                                print(" " * 12, "[")
                                for d_dict in dic[i][ib][ibc][ibcd]:
                                    print(" " * 12, str(d_dict) + str(":"), dic[i][ib][ibc][ibcd][d_dict])
                                print(" " * 12, "]")
                        elif ibc == 'C2':
                            print(" " * 8, 'C2:')
                            for ibce in dic[i][ib][ibc]:
                                print(" " * 12, str(ibce) + str(":"), dic[i][ib][ibc][ibce])
                        else:
                            print(" " * 8, str(ibc) + str(":"), dic[i][ib][ibc])
                else:
                    print(" " * 4, str(ib) + str(":"), dic[i][ib])
        else:
            print(str(i) + str(":"), dic[i])
    print('\n', '-' * 120, '\n')


inp_2 = (b'KHCBrq\xf1r\xb7\xc6\xc6\x9a\x00\x00\x00k\xab'
         b'\x1c?\tW\xbc\xf1\xbe'
         b'\x01\x0f\x830\xb1i\xfe\xaf\xf7\x11\xc6'
         b'\xa4i\x13\x9d\xc3Ti\xfa\xbe8\x7f5\xef'
         b'\x0e\xb3\xf7\x07\xff\x0cR\x035<v\xee'
         b'\xb2f\x14b\xc49\x16\x16\xab\xbb\xce\xdd'
         b'\x12\x9b\xf4\xe4\xb1\x88\x15\x00\x00\x00(\x00'
         b'\x00\x00;\x00\x00\x00\xd2\x1e'
         b'\xa5?)\xc2\x0b6\xd8@\xf1w?8\xa3\x16\x03'
         b'\x00N\x00\x89\xdet\x80Ap\xef\xafK\x12'
         b'\xd9\xfe\xc5\xb2\x96\x9d\xf4e8K\x04\x00'
         b'\x00\x00Z\x00\x00\x00w;P\x1c\xb6\xb6'
         b'\x10\xcc\x0e\xb2\xa7\x91{\x00'
         b'\xe6?\xa7j\x00\x00\x00')

if __name__ == '__main__':  # Start
    print('\nResult:\n')
    print('-' * 120, '\n')
    dic_1 = main(inp_1)
    output_data(dic_1, 1)
    dic_2 = main(inp_2)
    output_data(dic_2, 2)
    print('Done!')
