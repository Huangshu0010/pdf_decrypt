#批量破解pdf密码，使用https://qpdf.sourceforge.io/
import subprocess
import  os
path = r"D:\Tools\qpdf-10.4.0\bin" #设置qpdf.exe所在目录
pre = os.getcwd()  #初始pdf文件夹为当前目录

def get_filelist(dir):
    Filelist = []
    for home, dirs, files in os.walk(pre):
        for filename in files:
            # 文件名列表，包含完整路径
            Filelist.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
    return Filelist

if __name__ =="__main__":
    Filelist = get_filelist(pre)
    for file  in Filelist:
        cmd = ["qpdf","--decrypt","--replace-input","--password=d8e5e",file]  #命令行终端命令
        sub = subprocess.Popen(args=cmd,cwd=path,shell=True)  #不要忘记cwd
        print(file,"done")
        sub.wait()   #最好加上，否则可能由于多个进程同时执行带来机器瘫痪
