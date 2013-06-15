# encoding:utf-8
# 统计词频，按频率排序，并写到文档里
import re
from collections import Counter

#\S
file = open('filepath','r+')
try:
    fcontent = file.read()
finally:
    file.close()
words = re.findall(r'\S+',fcontent) #  剔除空格和回车符
freqlist = Counter(words) # 按序列统计出频次

text = open('filepath','w+')
try:
    for key in freqlist:
        text.write(key+':'+repr(freqlist[key])+'\n')
finally:
    text.close()
    

