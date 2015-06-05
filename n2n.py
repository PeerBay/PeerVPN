
#~ two default edges on local supernode 
#~ The one with publicedge with an ip based on the domain name 
#~ default anonymous domain uuid4.random
#~ the other one is private protected with a password that changes 
#~ every half an hour and is distributed among the peers
#~ other public and private edges are created to reach other supernodes



#~IDEA: To n2n source code: add code that will return the subnet of the network on register and will use it to generate an local IP address

import subprocess
# import couchdb
import json
import miniupnpc
# server=couchdb.Server()
# n2n_state=server["n2n"]
n2n_state={}
try:
	with open("edges","r") as f:
		domains=json.loads(f.read())
		f.close()
except:
	with open("edges","wb") as f:
		f.write(json.dumps({}))
		f.close()
#~ class remoteSupernode:
		#~ If upnp doesnt work and ports are blocked the user must
		#~ either find a friend's node(upnp capable) and host their domain
		#~ or use a public supernode that accepts domain hosting
		#~ either way a public and a private edge are required to the supernode's
		#~ address based on the domain name
		#~ when this happens the remotesupernode must announce with kadnode the requested domain name 
		#~ and the local node must start a public edge to the remote supernode with the domain name as network name.
		def requestSupernodeForDns(supernode):
		def edges(supernode):
			publicedge(domain,supernode)
			gateway=n2n.gateway(supernode)
			edge(domain,password,supernode)
class Supernode:
	def init(self):
		u = miniupnpc.UPnP()
		u.discoverdelay = 200;
		ndevices = u.discover()
		print ndevices, 'device(s) detected'
		if ndevices>=1:
			u.selectigd()
			self.network={"lanaddr":u.lanaddr,
				"externalipaddress":u.externalipaddress()}
			self.u=u
			self.supernode=None
			self.noUPnP=True
		else:
			print "Please enable UPnP on your modem."
			self.noUPnP=False
			return None

	def start(self,port=None):
		self.init()
		if self.noUPnP==False:
			return "Can't start supernode because UPnP is disabled. Try remoteSupernode"
			
		self.stop()
		u=self.u
		if port!=None:
			r = u.getspecificportmapping(port, 'UDP')
			if r!=None:
				print 'Port mapping already in use. Trying to delete it.'
				b = u.deleteportmapping(port, 'UDP')
				if b:
					print 'Successfully deleted port mapping'
					p=u.addportmapping(port, 'UDP', u.lanaddr, port,
	                    'N2N Supernode on port %u' % port, '')
				else:
					print 'Failed to remove port mapping'
					return "Please try another port."
			else:
				p=u.addportmapping(port, 'UDP', u.lanaddr, port,
                    'N2N Supernode on port %u' % port, '')
				
		else:
			port = 15000	
			r = u.getspecificportmapping(port, 'UDP')
			while r != None and port < 65536:
				port = port + 1
				r = u.getspecificportmapping(port, 'UDP')
			p = u.addportmapping(port, 'UDP', u.lanaddr, port,'N2N Supernode on port %u' % port, '')
		if p:
			print "Port mapping success!Starting supernode.."
			self.supernode=subprocess.Popen(["supernode","-l",str(port),"-f"],shell=False)
			self.supernode_port=port
			print "supernode started on port ",	str(port)
			if "supernode" in n2n_state:
				n2n_state["supernode"]["port"]=port
			else:
				n2n_state["supernode"]={"port":port}
			
		else:
			print "Failed to start supernode!"
			
	#~ def startLocalEdge():
				
	def stop(self):
		subprocess.Popen(["killall", "supernode"],shell=False)
		if 	self.supernode:
			self.supernode.terminate()
			print "Supernode terminated."
			b = self.u.deleteportmapping(self.supernode_port, 'UDP')
			self.supernode=None
			self.supernode_port=None
			n2n_state.delete(n2n_state["supernode"])
			if b:
				print 'Successfully deleted port mapping'
		else:	
			print "No supernode found."



#~ class dynamicIP():
	#~ def getmac():
	#~ def convertToIpv6(mac):
		#~ A mac address is 48 bits, an IPv6 address is 128 bits. Here s the conversion process step by step:
		#~ take the mac address: for example 52:74:f2:b1:a8:7f
		#~ throw ff:fe in the middle: 52:74:f2:ff:fe:b1:a8:7f
		#~ reformat to IPv6 notation 5274:f2ff:feb1:a87f
		#~ convert the first octet from hexadecimal to binary: 52 -> 01010010
		#~ invert the bit at index 6 (counting from 0): 01010010 -> 01010000
		#~ convert octet back to hexadecimal: 01010000 -> 50
		#~ replace first octet with newly calculated one: 5074:f2ff:feb1:a87f
		#~ prepend the link-local prefix: fe80::5074:f2ff:feb1:a87f
		#~ done!
	#~ def createSubnet():
		#~ import random   
		#~ M = 16**4
		#~ mac=convertToIpv6(getmac())
		#~ starting_ip=mac[:10] + ":".join(("%x" % random.randint(0, M) for i in range(6)))
		#~ subnet=starting_ip[:20]#remove last 2 octet
		#~ while subnet in couch["subnets"]:
			#~ starting_ip=mac[:10] + ":".join(("%x" % random.randint(0, M) for i in range(6)))
			#~ subnet=starting_ip#remove last 2 octet
		#~ couch["subnets"][subnet]={"used":True}
		#~ return starting_ip
			

#~ class PublicEdge():
	#~ def connect(self,domain):
		#~ to connect to the supernode's public network we derive the ip address of the public edge from the hash of the p2p domain.  
		#~ Connecting here users will be able to leave a friend request with "how to get in touch" data. 
		#~ on friend request put (supernode p2p address , network name,net password , username , public key, message, sign )encrypted
		#~ public edge generates the domain name into an subnet and a network name( tun name is handled by n2n library)

#~edge -d n2n0 -c mynetwork -k encryptme -a 1.2.3.4 -l a.b.c.d:xyw 
class Edge(Supernode):
	def __init__(self,Supernode):
		subprocess.Popen(["killall", "edge"],shell=False)
		if Supernode.supernode_port:
			self.local_supernode="127.0.0.1:"+str(Supernode.supernode_port)
			print "Local supernode running on port ",Supernode.supernode_port
		else:
			self.local_supernode=None	
		self.started=True
		self.edges={}
	def start(self,tuntap,network_name,password,static_ip,supernodes=[]):
		try :
			if  not self.started:
				self.init()
		except:
			print "Edge instance already exists."
		#~ edges=open("edges")
		#~ edges=json.loads(edges)
		#~ edge={tun:1,network:"ksij23djfkos039kf9",password:"",}
		#~  
		
		
		
		if supernodes==[]:
			if self.local_supernode:
				supernodes=[self.local_supernode]
				print "You didn't specify a supernode.Using local supernode."
			else:
				return "No supernode defined.Abort!"
		edgecmd=["edge","-f","-d",tuntap,"-c",network_name,"-k",password,"-a",static_ip]		
		for i in supernodes:
			edgecmd.append("-l")		
			edgecmd.append(i)
		if tuntap in self.edges:
			return "Interface ",tuntap," already in use.Rename tuntap." 			
		self.edges[tuntap]={"network_name":network_name,"password":password,"static_ip":static_ip,"supernodes":supernodes,"edge":subprocess.Popen(edgecmd,shell=False)}
		print "Edge on ",tuntap, " created."	
		n2n_state[tuntap]={"network_name":network_name,"password":password,"static_ip":static_ip,"supernodes":supernodes}
	def stop(self,tuntap):
		if tuntap in self.edges:
			self.edges[tuntap]["edge"].terminate()
			print "Edge with tuntap ", tuntap," terminated."
			self.edges.pop(tuntap)
			n2n_state.delete(n2n_state[tuntap])
		else:
			print "Edge with tuntap ", tuntap,"not found." 	
		
		
			
