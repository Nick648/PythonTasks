import re

pattern = re.compile(r"123")
string = "123zzb123"

pos = 0
while pos < len(string):
    print("pos1:", pos)
    match =pattern.match(string, pos)
    print(pattern.match(string, pos))
    if match:
        pos = match.end()
    else:
        pos += 1
    print("pos2:", pos)
# Out: <_sre.SRE_Match object; span=(0, 3), match='123'>

match = re.match(pattern, string)
#print(re.match(pattern, string, 6))
print(match.group())
# Out: '123'
