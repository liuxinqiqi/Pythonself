#coding=utf-8
f = open('file','r+')

s = f.read(6)

print f.tell()       #测定文件的偏移量,以字节为单位
# f.seek(3)
f.seek(10,1)    # 第一个参数表示偏移量，第二个参数表示起始位置(只有三种选择0(当前位置),1(偏移后位置),2(末尾))
# f.seek(-7,2)    #第二个参数为2表示从末尾开始，第一个参数则为负

print f.read(6)    #再次开始以上次的偏移位置为准
