# -*- coding: utf-8 -*-
import sys
import os
import codecs
import click

def read_line_count(fname,output):
    count = 0
    with open(output,'a') as f:
        f.write('fname:%s\n' % fname)
    with open(fname,'r',encoding='utf8') as f:
        for file_line in f.readlines():
            file_line = file_line.strip()
            if not len(file_line) or file_line.startswith('//'):
                continue
            count += 1
    with open(output,'a') as f:
        f.write('line count::%s\n' % count)
    return count
@click.command()
@click.option('--path',type=str,help="代码路径,如r'e:\pathname\subpath")
@click.option('--exts',type=str,help="扩展名列表,形式如:.py;.txt") 
@click.option('--output',default=r'code_line_count.txt',type=str,help="输出结果路径") 
def proc(path,exts,output):#r'e:\newjincin\projects\office_proj\python\duguangcai_testdata\src\companysimulatequestion\companysimulatequestion'
    print(path)
    print(exts)
    extlist=exts.split(';')
    with open(output,'w') as f:
        f.write('\n')
    count = 0
    fcount = 0
    for root,dirs,files in os.walk(path):
        for f in files:
            # Check the sub directorys
            print(f)
            fname = (root + '\\'+ f).lower()
            if os.path.splitext(f)[1]:
                ext = f[f.rindex('.'):]
            try:
                if(extlist.index(ext) >= 0):
                    fcount += 1
                    c = read_line_count(fname,output)
                    count += c
                    with open(output,'a') as f:
                        f.write('total count:%s\n' % count)
            except:
                pass

    with open(output,'a') as f:
        f.write('\n')
        f.write('--------------------------------------\n')
        f.write('total file count:%d\n' % fcount)
        f.write('total line count:%d\n' % count)

if __name__ == "__main__":
    proc()