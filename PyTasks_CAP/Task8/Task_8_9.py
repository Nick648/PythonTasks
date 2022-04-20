# Вариант 9

def main(x):
    x = x.replace('\n', ' ').replace('\t', '')[6:-4]
    x_parts = x.split(')')
    result = dict()
    # print(x_parts)
    for path in x_parts:
        k = path.find('#')
        if k != -1:
            value = int(path[k + 1: path.find('=')])
            key = path[path.find("@'") + 2: path.rfind("'")].strip()
            # print(key, value, len(key))
            result[key] = value

    return result


s_1 = "begin ( set #4484==> @'erquis' ) ( set#-5312==> @'enat_91') (set\n" \
      "#423==> @'reen' ) ( set #5902 ==>@'veaa_615' ) end"
main(s_1)

# For CAP, you only need what is above, having checked in advance for PEP8
if __name__ == "__main__":
    print("Result:\n")
    s_2 = "begin (set#8426 ==> @'enbe' ) ( set#-6155 ==> @'gear' ) end"
    print("Res 1:", main(s_1))
    print("Res 2:", main(s_2))
