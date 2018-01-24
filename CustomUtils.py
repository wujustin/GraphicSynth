#encoding=utf-8

import os
import sys
import codecs
import re
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

# 保存文件的函数
def savefile(savepath,content):
    fp = codecs.open(savepath,'w','utf-8')
    fp.write(content)
    fp.close()

def saveListToFile(savepath, lines):
    fp = codecs.open(savepath,'w','utf-8')
    for line in lines:        
        fp.write(line + "\r\n")
    fp.close()

def loadfile(path):
    fp = codecs.open(path,'r','utf-8')
    lines = fp.readlines()
    
    new_lines = []
    for text in lines:
        text = text.strip()
        if not text:
            continue
        
        text = text.strip('\n')        
        if not text:
            continue
        
        text = text.strip('\r\n')        
        if not text:
            continue
        new_lines.append(text)
        
    fp.close()
    return new_lines

def rmSpecPunct(content):
    content = re.sub("[\.\`！!!“<>\/_,$%^~#*(:)+\"\']+|[［］／＼·～－，?？?《》+——~@#＃＄＾＆＊ ＞：＋＝￥%……&*（）【】]+".decode("utf-8")," ", content)
    return content

def filterNoChs(content):
    pat = re.compile(u'[^\u4E00-\u9FCB]')
    line = pat.sub(r'', content)#replace
    return line

def np_float_div(np_A, np_B):
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide(np_A, np_B)
        c[c == np.inf] = 0.0
        c = np.nan_to_num(c)
        
        return c
    
def enWordSplit(string):
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()
