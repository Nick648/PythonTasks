"""
Вариант 1
data[offset + n: offset + n + m] - обычные срезы
little-endian: < , big-endian: >
"""
import struct


def parse_array(data, size, typ, offset):  # Unpacking an array
    n = struct.calcsize(typ)
    return list(struct.unpack(f'>{size}{typ}',
                              data[offset: offset + size * n]))


def parse_array_struct_c(data, size, offset):  # Unpacking a struct-array C
    arr = list()
    for count in range(size):
        arr.append(parse_c(data, offset + count * 19))  # 19 = size of struct C
    return arr


def parse_d(data, offset):
    d1_size, d1_offset = struct.unpack('>II',
                                       data[offset: offset + 4 + 4])
    d1 = parse_array(data, d1_size, 'I', d1_offset)
    d2 = struct.unpack('>B', data[offset + 8: offset + 8 + 1])[0]
    d3_size, d3_offset = struct.unpack('>II',
                                       data[offset + 9: offset + 9 + 4 + 4])
    d3 = parse_array(data, d3_size, 'I', d3_offset)
    return {'D1': d1, 'D2': d2, 'D3': d3}  # d = 17


def parse_c(data, offset):
    c1 = parse_d(data, offset)  # d = 17
    c2 = parse_array(data, 2, 'b', offset + 17)  # b = 1
    return {'C1': c1, 'C2': c2}  # c = 19


def parse_b(data, offset):
    b1 = struct.unpack('>Q', data[offset: offset + 8])[0]
    b2 = struct.unpack('>H', data[offset + 8: offset + 8 + 2])[0]
    b3 = struct.unpack('>H', data[offset + 10: offset + 10 + 2])[0]
    b4 = struct.unpack('>H', data[offset + 12: offset + 12 + 2])[0]
    b5 = struct.unpack('>b', data[offset + 14: offset + 14 + 1])[0]
    b6 = struct.unpack('>I', data[offset + 15: offset + 15 + 4])[0]
    b7_size, b7_offset = struct.unpack('>IH',
                                       data[offset + 19: offset + 19 + 4 + 2])
    b7 = parse_array_struct_c(data, b7_size, b7_offset)
    b8 = struct.unpack('>H', data[offset + 25: offset + 25 + 2])[0]
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5,
            'B6': b6, 'B7': b7, 'B8': b8}  # b = 27


def parse_a(data, offset):
    # print("data[offset: offset + 4]:", data[offset: offset + 4])
    a1 = struct.unpack('>f', data[offset: offset + 4])[0]
    # print("a1:", a1, type(a1))
    a2 = struct.unpack('>f', data[offset + 4: offset + 4 + 4])[0]
    a3_offset = struct.unpack('>H', data[offset + 8: offset + 8 + 2])[0]
    a3 = parse_b(data, a3_offset)
    a4_size, a4_offset = struct.unpack('>II',
                                       data[offset + 10: offset + 10 + 4 + 4])
    a4 = parse_array(data, a4_size, 'Q', a4_offset)
    a5 = struct.unpack('>f', data[offset + 18: offset + 18 + 4])[0]
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}  # a = 22


def main(data):
    # Данные начинаются с сигнатуры 0x43 0x45 0x4b
    return parse_a(data, 3)  # offset = 3


inp_1 = (b'CEK\xbfRO\x00?h\xb4[\x00o\x00\x00'
         b'\x00\x03\x00\x00\x00\x8a\xbf?\xa7'
         b'6\x93\x10\xc1\xaa\nG\xbf2d:\'\xa3'
         b'\xe1\n>"\x80\x17\xad\t\xd9\xd7]\xeeg\xda}'
         b'\xea\xe7\xf4\x92\x95\x10bt{\xfeE,\x8a'
         b'\xb6\xbc\x124\xef\xde\xd6I\x00\x00\x00'
         b'\x03\x00\x00\x00\x19\xea\x00\x00'
         b'\x00\x03\x00\x00\x00%\x95\x08'
         b'\x00\x00\x00\x02\x00\x00\x001k\x00'
         b'\x00\x00\x04\x00\x00\x009\xd9:\xda'
         b"\x7fY\x1b'Z\xa3\xb7\xc9C\xcb\x1c"
         b"\x12r\xb3\x86P\xbd\xd1\x00\x00\x00\x02\x00I"
         b'\xae\x13A\xaf\xa8\xd0\xb3\x85!\xe9W'
         b'\xeek\xaeF\x04\xa9\xfdm\xc4lF\xad\xd2'
         b'5\xa5')

main(inp_1)


# For CAP, you only need what is above, having checked in advance for PEP8


def output_data(dic, number=0):  # output dictionary
    print(dic, '\n', 'DICT_' + str(number) + ':\n')
    for i in dic:
        if i == 'A3':
            print('A3:')
            for ib in dic[i]:
                if ib == 'B7':
                    print(" " * 4, 'B7:')
                    for ibc_l in range(len(dic[i][ib])):
                        for ibc_d in dic[i][ib][ibc_l]:
                            if ibc_d == 'C1':
                                print(" " * 8, 'C1:')
                                for ibcd in dic[i][ib][ibc_l][ibc_d]:
                                    print(" " * 12, str(ibcd) + str(":"), dic[i][ib][ibc_l][ibc_d][ibcd])
                            else:
                                print(" " * 8, str(ibc_d) + str(":"), dic[i][ib][ibc_l][ibc_d])
                else:
                    print(" " * 4, str(ib) + str(":"), dic[i][ib])
        else:
            print(str(i) + str(":"), dic[i])
    print('\n', '-' * 120, '\n')


inp_2 = (b'CEK?\x00\xcf\x95\xbf,E\x91\x00k\x00\x00\x00\x03\x00\x00\x00\x86=\xbeB'
         b"\x0cNx\x99N\x9e\x01#\r?\x03\x9f \xcb'\xe3>*^\x0b\xf6\x83\x01\xd1rgb\x0c"
         b'+/\xe5\x98;\n1\xf5\xe3\x17\x92\xbb\x85\x8f\xcb\x12\xf9\x00\x00\x00'
         b'\x03\x00\x00\x00\x19\xac\x00\x00\x00\x04\x00\x00\x00%\xd6`\x00\x00\x00\x02'
         b'\x00\x00\x005\x18\x00\x00\x00\x02\x00\x00\x00==\xde\x85\xda\xbd\xfej'
         b'\xc0L>\xf2\r\x05\xe6oY\x9a|\x8c\x84\x00\x00\x00\x00\x02\x00E\x03!\xd1\x18'
         b"\x9b\xafhX\x86\xe1\x138A\xb2<J\xf6?\x8d\xbd\xf4G'\xaf\n\xd8")

if __name__ == '__main__':  # Start
    print('\nResult:\n')
    print('-' * 120, '\n')
    dic_1 = main(inp_1)
    output_data(dic_1, 1)
    dic_2 = main(inp_2)
    output_data(dic_2, 2)
    print('Done!')
