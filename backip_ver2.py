# coding=utf8
import os
import time

source = ['/home/douxiao/Desktop/gitZip/notes']
target_dir = '/home/douxiao/Desktop/gitZip/backup'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
# 将当前的日期作为主目录 #os.sep 变量的使用方式——它将根据你的操作系统给出相应的分隔
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前的时间作为zip的文件名
now = time.strftime('%H%M%S')
# 给文件名添加一个来自用户的注释
comment = input('Enter a comment --> ')
# 检查是否有评论键入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
# 如果子目录不存在则创建一个

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 运用的的字符串方法 join 来将列表 source 转换成字符串
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

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
