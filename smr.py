# SM Freechat Remote Recorder v.1.0.0 by Horacio for Python 2.7.13

import sys, os, urllib, urllib3, ssl, re, time, datetime, command
urllib3.disable_warnings()
reload(sys)
sys.setdefaultencoding('utf-8')
from colorama import init, Fore, Back, Style
from termcolor import colored
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.cfg')

init()
print(colored(" => START <= ", 'yellow', 'on_blue'))
print

if __name__=='__main__':
   import sys
model = sys.argv[1]
print (colored(' => SM Model => {} <=', 'yellow', 'on_blue')).format(model)
print

url ='https://streamate.com/cam/{}/'.format(model)
http_pool = urllib3.connection_from_url(url)
r = http_pool.urlopen('GET',url)
enc = (r.data)
dec=urllib.unquote(enc).decode()
sid0 = dec.split("p_sid: '")[1]
sid = sid0.split("'")[0]
if len(sid) > 2:
   srv0 = dec.split("p_srv: '")[1]
   srv = srv0.split("'")[0]
   pid0 = dec.split("p_pid: '")[1]
   pid = pid0.split("'")[0]
   swf0 = dec.split('embedSWF("')[1]
   swf = swf0.split('"')[0]
   cnsg0 = dec.split("p_g: '")[1]
   cnsg = cnsg0.split("'")[0]
   ft0 = dec.split("p_ft: '")[1]
   ft = ft0.split("'")[0]
   fcs0 = dec.split('fcs')[1]
   fcs = fcs0.split('-1')[0]
   print (colored(' => Found: FCS: {} * SRV: {} * SID: {} * PID: {} <=', 'yellow', 'on_blue')).format(fcs,srv,sid,pid)
   print
   timestamp = str(time.strftime("%d%m%Y_%H%M%S"))
   path = config.get('folders', 'output_folder')
   filename = model + '_SM_' + timestamp + '.flv'
   pf = (path + filename)
   rtmpdump = config.get('files', 'rtmpdump')

   print (colored(" => RTMP REC => {} <=", "yellow", "on_red")).format(filename)
   print
   command = 'rtmpdump -r"rtmp://fcs{}-1.streamate.com/reflect/{}" -a"reflect/{}" -W"{}" -p"{}" -CS:0 -CS:{} -CS: -CO:1 -CNS:signupargs:smid={} -CNS:srvav:{} -CNS:sessionType:preview -CNS:pid:{} -CNS:sid:{} -CNS:ft:{} -CNS:lang:en -CNS:sk:streamate.com -CNS:hd:1 -CNS:g:{} -CNN:version:8.000000 -CNS:freecnt:3 -CNS:nickname: -CNS:srv:{} -CO:0 -m 900 --live -y"{}" -o"{}"'.format(fcs,sid,sid,swf,url,sid,pid,srv,pid,sid,ft,cnsg,srv,sid,pf)
   os.system(command)
   print
   print(colored(" => END <= ", 'yellow','on_blue'))
   time.sleep(1)    # pause 1 second
   sys.exit()
else:
   print(colored(" => Model is OFFLINE <= ", 'yellow','on_red'))
   print
   time.sleep(3)    # pause 3 second
   print(colored(" => END <= ", 'yellow','on_blue'))
   sys.exit()
