lettles = 'abcdefghijklmnopqrstuvwxyz'
Lettle = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '''`!@#$%^&*()_+=-~{}|:"<>?[]\;',./'''

bits = int(input('密码的长度'))
addcode = ''
tp=input('''密码类型：
    1：纯数字
    2：纯小写字母
    3：大小写字母混合
    4：数字与字母混合
    5：数字、字母与字符混合
    ''')
if tp == '1':
    strings = numbers
elif tp == '2':
    strings = lettles
elif tp == '3':
    strings = lettles+Lettle
elif tp == '4':
    strings = numbers+lettles+Lettle
elif tp == '5':
    strings = numbers+lettles+Lettle
    
#code =[]

f= open('codes.txt','a')

def ss(begin,ends,addcode):
    #global code
    global strings
    if begin == ends:
        for i in range(len(strings)):
            addcode = addcode[:begin]+strings[i]
            #code.append(addcode)  根据需要写入列表中
            f.write(addcode+'\n')
    else:
        for i in range(len(strings)):
            addcode = addcode[:begin] +strings[i] +addcode[begin+1:]
            ss(begin+1,ends,addcode)
                        
for i in range(bits):
    addcode +=strings[0]

ss(0,bits-1,addcode)

f.close()
