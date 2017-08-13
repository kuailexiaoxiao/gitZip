#coding=utf8
import os
import time
source = ['/home/douxiao/Desktop/gitZip/notes']
target_dir ='/home/douxiao/Desktop/gitZip/backup'
#os.sep 变量的使用方式——它将根据你的操作系统给出相应的分隔符
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
#运用的的字符串方法 join 来将列表 source 转换成字符串
zip_command = 'zip -r {0} {1}' .format(target, ' ' .join(source))

print('Zip command is :')
print(zip_command)
print('Running:')
'''os.system 函数的命令，这一函数可以使命令像是从系
统中运行的。也就是说，从 shell 中运行的——如果运行成功，它将返回 0 ，如果运行失
败，将返回一个错误代码。
'''
if os.system(zip_command) == 0:
    print('Successful backup to ', target)
else:
    print('Backup failed')