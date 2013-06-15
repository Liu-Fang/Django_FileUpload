# encoding:utf-8
# from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render

from segment import word_segment
import os,re,codecs
from collections import Counter


import tempfile, zipfile 
from django.http import HttpResponse 
from django.core.servers.basehttp import FileWrapper 
# @csrf_protect
def index(request):
    """docstring for index"""
    return render(request,'index.html', {'title':'test page'})

def upload(request):
    if request.method == 'POST':
        f = handle_uploaded_file(request.FILES['pic'])
    return render_to_response('upload.html',{'file':f})

def handle_uploaded_file(f):
    with open(f.name,'wb+') as info:
        try:
            for chunk in f.chunks():
                info.write(chunk)
        finally:
            info.close()
    with codecs.open(f.name,'r+',encoding='utf-8') as files:
        try:
            fcontent = files.read() 
        finally:
            files.close()
    fresult = word_segment(fcontent) # 调用结果，实现分词
    fresult = ' '.join(fresult)
    fresult = fresult.encode('utf-8')
    words = re.findall(r'\S+',fresult) # 删除空格和回车符
    freqlist = Counter(words) # 统计出频次，colletions还有一个功能：可以做出出现频率最高的前N个结果
    freq = freqlist.most_common(10000)
    segment_files = open('/home/liufang/upload/seg_result/result', 'wb+')
    try:
        for i in range(len(freq)):
            segment_files.write(freq[i][0]+':'+repr(freq[i][1])+'\n')
    finally:
        segment_files.close()
    return f




#使用zip的形式，将某个文件夹下的所有文件进行下载（下载大文件和压缩zip文件）
def send_file(request):  
    """                                                                          
    Send a file through Django without loading the whole file into               
    memory at once. The FileWrapper will turn the file object into an            
    iterator for chunks of 8KB.                                                  
    """  
    filename = __file__ # Select your file here.                                  
    wrapper = FileWrapper(file(filename))  
    response = HttpResponse(wrapper, content_type='text/plain')  
    response['Content-Length'] = os.path.getsize(filename)  
    return response 

def download_conf_zipfile(request):
    """create a ZIP file on disk and transmit it in chunks of 8KB,                  
    without loading the whole file into memory. A similar approach can           
    be used for large dynamic PDF files."""  
    temp = tempfile.TemporaryFile() 
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED) 
   # fpath = os.path.join('/home/liufang/upload/seg_result',filename)
    fpath = '/home/liufang/upload/seg_result/result'
 
    
    archive.write(fpath,'happy')# 此处为里面文件名 
    archive.close() 
    wrapper = FileWrapper(temp) 
    response = HttpResponse(wrapper, content_type='application/zip') 
    response['Content-Disposition'] = 'attachment; filename=happy.zip'#此处为外面文件名
    response['Content-Length'] = temp.tell() 
    temp.seek(0) 
    return response


