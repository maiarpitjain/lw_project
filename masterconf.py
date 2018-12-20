import os
import all_ip
from process import getoutput

def masterconf():
	getoutput("clear")
	ip=all_ip.master_ip()

	#getoutput("ssh 192.168.43.{0} scp /root/Desktop/project/task0/hdfs-site.xml 192.168.43.{0}:/etc/hadoop/".format(ip))

	getoutput("scp /root/Desktop/project/task0/hdfs-site.xml {}.{}.{}.{}:/etc/hadoop/".format(ip[0],ip[1],ip[2],ip[3]))

	getoutput("scp /root/Desktop/project/task0/core-site.xml {}.{}.{}.{}:/etc/hadoop/".format(ip[0],ip[1],ip[2],ip[3]))
	
	getoutput("ssh {}.{}.{}.{} hadoop namenode -format".format(ip[0],ip[1],ip[2],ip[3]))



def checkdn():

	ip=all_ip.master_ip
	getoutput("ssh {}.{}.{}.{} hadoop dfsadmin -report".format(ip[0],ip[1],ip[2],ip[3]))
   
