import os
import all_ip
from process import getoutput
def jobtrackerconf():
	getoutput("clear")
	
	ip=all_ip.jobtracker_ip()

	getoutput("scp /root/Desktop/project/task0/mapred-site.xml {}.{}.{}.{}:/etc/hadoop/".format(ip[0],ip[1],ip[2],ip[3]))

	getoutput("scp /root/Desktop/project/task0/core-site.xml {}.{}.{}.{}:/etc/hadoop/".format(ip[0],ip[1],ip[2],ip[3]))
	


	#getoutput("hadoop namenode -format")

def checktt():
	
	ip=all_ip.jobtracker_ip

	getoutput("ssh {}.{}.{}.{} hadoop job -list-active-trackers".format(ip[0],ip[1],ip[2],ip[3]))


