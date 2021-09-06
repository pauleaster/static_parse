# static_parse.py
'''A hacked python file that looks for '="assets/' or '="js/' or '="img/' and
encapsulates the quoted text with {% static '<quoted text>' %}  '''



def alt_find(line):
    str1 = '="assets/'
    str2 = '="js/'
    str3 = '="img/'
    idx1 = line.find(str1)
    idx2 = line.find(str2)
    idx3 = line.find(str3)
    if idx1 > -1:
        return idx1
    elif idx2 > -1:
        return idx2
    elif idx3 > -1:
        return idx3
    else:
        return -1

sout = []

print('*************************** start **********************************************')
counter = 0
for _ in (True,):
    with open('index.html', 'r') as f:
        counter += 1
        read_data = f.readlines()
for line in read_data:

    idx1 = alt_find(line)

    if idx1 > -1:
        # idx2 = line.find('"')
        # print(line[idx1:idx2])
        # print(line[idx1+2:])
        rel_idx2 = line[idx1+2:].find('"')
        idx2 = idx1 + 2 + rel_idx2
        # print("s1")
        s1 = line[:idx1+2]
        # print(s1)
        
        # print("s2")
        s2 = line[idx1+2:idx2]
        # print(s2)
        
        # print("s2new")
        s2new = r"{% static '" + s2 + r"' %}"
        # print(s2new)

        # print("s3")
        s3 = line[idx2:]
        # print(s3)

        newline = s1 + s2new + s3
        # print(line)
        # print(newline)
        sout += [newline]
    else:
        sout += [line]
    #     print()
        # print(line)

print(sout)
print('**************************** end *********************************************')

f = open(r'new_index.html', 'w')
f.writelines(sout)
f.close()