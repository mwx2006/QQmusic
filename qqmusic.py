import json
import os
import re
import urllib
import socket
import easygui as ui
import requests
ui.msgbox(msg="作者:MWX",title="制作:MWX",ok_button="确定")
#word = input('输入名称:')
word=ui.enterbox(msg="输入歌名(获取可能会需要一定时间，时间因网而异)",title="搜索")
res1 = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w='+word)
jm1 = json.loads(res1.text.strip('callback()[]'))
jm1 = jm1['data']['song']['list']
mids = []
songmids = []
srcs = []
songnames = []
singers = []
songid=[]
xz=[]
xx=[]
for j in jm1:
    try:
        mids.append(j['media_mid'])
        songmids.append(j['songmid'])
        songnames.append(j['songname'])
        singers.append(j['singer'][0]['name'])
        songid.append(j['songid'])
    except:
        print('错误')

js=-1
for n in range(0,len(mids)):
    js=js+1
    res2 = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid='+songmids[n]+'&filename=C400'+mids[n]+'.m4a&guid=6612300644')
    jm2 = json.loads(res2.text)
    vkey = jm2['data']['items'][0]['vkey']
    srcs.append('http://dl.stream.qqmusic.qq.com/C400'+mids[n]+'.m4a?vkey='+vkey+'&guid=6612300644&uin=0&fromtag=66')
    try:
        #print(str(js)+":"+songnames[n]+' - '+singers[n])
        xx.append(str(js)+"-"+songnames[n]+'-'+singers[n])
        xz.append('http://dl.stream.qqmusic.qq.com/C400' +mids[n]+'.m4a?vkey='+vkey+'&guid=6612300644&uin=0&fromtag=66"')
    except:
        js=js+1
        print('Download wrong~')
       # print(songnames[m]+' - '+singers[m]+':', srcs[m])
#jd=input("请选择:")
jdy=ui.choicebox(msg="请选择",choices=xx)
jdy=jdy[:3]
pp=re.search("-",jdy, flags=0).span()
pp=pp[0]
jdy=jdy[:pp]
jd=int(jdy)

try:
    jd = int(jd)
    jg = xz[jd]
except:
    ui.msgbox(msg="错误！",title="错误",ok_button="确定")
    #print("错误!是不是你输错了?")
lj=xx[jd]+':"'+jg
print(xx[jd])
#yxtj=input("\n选择运行命令:\n1:获取链接\n2:下载\n3:播放")
yxtj=ui.indexbox(msg="请选择操作",title="选择操作",choices=("获取链接","下载","播放"))
yxtj=int(yxtj)
if (yxtj==0):
    #print(lj)
    ui.msgbox(msg=lj,title="链接",ok_button="确定")
elif (yxtj==1):
    wjj=os.path.exists('./qqmusic')
    if wjj== False:
        os.makedirs("./qqmusic")
    try:
        urllib.request.urlretrieve(jg,'./qqmusic/'+xx[jd][pp+1:]+".m4a")
    except:
        ui.msgbox(msg="下载失败!",title="下载失败",ok_button="确定")
    else:
        ui.msgbox(msg="下载完成!",title="下载完成",ok_button="确定")
    #print("下载完成")
elif(yxtj==2):
    jg=jg[:-1]
    try:
        urllib.request.urlretrieve(jg,'./qqmusic/'+xx[jd][pp+1:]+".m4a")
    except:
        ui.msgbox(msg="下载失败!",title="下载失败",ok_button="确定")
    else:
        os.system('".\\qqmusic\\'+xx[jd][pp+1:]+".m4a\"")
