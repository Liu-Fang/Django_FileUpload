# encoding:utf-8

def handle_uploaded_file(f):
    name = f.name
    fname = os.path.join('/home/liufang/upload/uploaded_files/',name)
    with open(fname,'wb+') as info:
        try:
            for chunk in f.chunks():
                info.write(chunk)
        finally:
            info.close()
    with codecs.open(fname,'r+',encoding='utf-8') as files:
        try:
            fcontent = files.read() 
        finall# encoding:utf-8y:
            files.close()
    fresult = word_segment(fcontent) # 调用结果，实现分词
    fresult = ' '.join(fresult)
    fresult = fresult.encode('utf-8')
    words = re.findall(r'\S+',fresult) # 删除空格和回车符
    freqlist = Counter(words) # 统计出频次，colletions还有一个功能：可以做出出现频率最高的前N个结果
    freq = freqlist.most_common(10000)
    fdname =  os.path.join('/home/liufang/upload/seg_result/',name)
    segment_files = open(fdname, 'wb+')
    try:
        for i in range(len(freq)):
            segment_files.write(freq[i][0]+':'+repr(freq[i][1])+'\n')
    finally:
        segment_files.close()
    return f
