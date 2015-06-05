!! Working locally only for now
Create p2p virtual private networks with python and n2n.

How to install:
```
sudo apt-get install libminiupnpc-dev libnatpmp-dev avahi-daemon
sudo pip install miniupnpc
git clone https://github.com/lukablurr/n2n_v2_fork
cd n2n_v2_fork
make 
sudo make install
cd ..
git clone https://github.com/PeerBay/PeerVPN
```
How to use:
```
import n2n
import time
#start supernode
s = n2n.Supernode()
s.start()
time.sleep(5)
e=n2n.Edge()
e.init(s)
e.start("tun","networkname","password","10.0.0.1")
time.sleep(15)
e.stop("tun")
```
