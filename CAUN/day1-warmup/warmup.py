# coding: utf-8

import time

start_time = time.time()
file = open("input.txt", "r")

# print(file.read())
txt = file.read()
#print(txt[0])
cnt = 0
pos = 0
for parenthesis in txt:
    if parenthesis == '(':
        cnt += 1
    elif parenthesis == ')':
        cnt -= 1
    pos += 1
    
    if cnt < 0:
        print(pos)
        break

print(cnt)

file.close()
print("--- %s seconds ---" % (time.time() - start_time))