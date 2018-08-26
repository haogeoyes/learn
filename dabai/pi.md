# 2018-08-26 dueros

> n2n

```
sudo apt-get install n2n
sudo chmod +s /usr/sbin/edge
启动n2n
edge -d edge0 -c 自定义网络名 -k 密码 -u 1000 -g 1000 -a 想设置的本机ip -l 超级节点地址和端口

edge  -d edge0 -c haoge -k haoge -u 1000 -g 1000 -a 1.1.1.1 -l n2n.lucktu.com:10082
1.1.1.1
26/Aug/2018 22:36:13 [     edge.c:1136] Using supernode 167.88.162.244:10082
26/Aug/2018 22:36:13 [tuntap_linux.c:  38] Interface edge0 has MAC FE:A3:48:34:00:A4
26/Aug/2018 22:36:13 [     edge.c:1333] Interface up. Dropping privileges to uid=1000, gid=1000
26/Aug/2018 22:36:13 [     edge.c: 670] Registering with supernode
26/Aug/2018 22:36:13 [     edge.c:1367]
26/Aug/2018 22:36:13 [     edge.c:1368] Ready
26/Aug/2018 22:36:13 [     edge.c:1434] STATUS: pending=0, operational=0
26/Aug/2018 22:36:14 [     edge.c:1035] Received REGISTER_ACK from remote peer [ip=167.88.162.244:10082]


edge -d A1 -a 10.0.0.23 -c test -k 1234567 -l n2n.lucktu.com:10082 -r -b &


mac
git clone https://github.com/meyerd/n2n.git


windows
http://www.vpnhosting.cz/n2nguien.exe
```

> 录音

```
arecord -D“plughw：1,0”-r16000 -f S16_LE -d 2 test.wav
```

