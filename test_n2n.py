import n2n
import time
#start supernode
s = n2n.Supernode()
s.start()
time.sleep(5)
e=n2n.Edge()
e.init(s)


e.start("tun","name","pass","10.0.0.1")
time.sleep(15)
e.stop("tun")
