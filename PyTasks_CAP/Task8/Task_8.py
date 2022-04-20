# Вариант 18

def main(x):
    x = x.replace('\n', ' ').replace('\t', '')[2:-2]
    x_parts = x.split('.')
    result = dict()
    # print(x_parts)
    for path in x_parts:
        if path.find(':=') != -1:
            k = path.find(':=')
            key = path[path.rfind(' ', 0, k - 1) + 1: k]
            key = key.replace(' ', '')
            value = path[path.find('q(', k) + 2:path.find(')', k)]
            # print(key, value, len(key), len(value))
            result[key] = value

    return result


s = '[[begin define quinra_57:= q(beisxe). end begin define amaabe\n' \
    ':=q(laar). end begin define edla:= q(tiza_703). end ]]'
main(s)

# For CAP, you only need what is above, having checked in advance for PEP8
if __name__ == "__main__":
    print("Res 1:", main(s))

"""
# Вариант 40
def main_40(x):
    x = x.replace(' ', '').replace('\n', '').replace('\t', '')[1:-1]
    x_parts = x.split(';')
    result = dict()
    for path in x_parts:
        part = part[6:-8].replace('var@', '')
        key, value = part.split('=')
        result[key[1:-1]] = value
    return result

print(main_40("( <data> var @'qubi_571' = inin_783.</data>;<data>var @'esgeza' = inbege. "
              "</data>; <data> var @'enon_506'= onin. </data>;)"))
"""
