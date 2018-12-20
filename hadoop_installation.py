import os
import all_ip
from process import getoutput

def hadoop_install_in_master():
	ip=all_ip.master_ip()
	
	a=getoutput("ssh {}.{}.{}.{} hadoop version".format(ip[0],ip[1],ip[2],ip[3]))
	if a==0:
		pass
	else:	
		getoutput("scp /root/Desktop/project/task0/hadoop-1.2.1-1.x86_64.rpm {}.{}.{}.{}:".format(ip[0],ip[1],ip[2],ip[3]))
		getoutput("ssh {}.{}.{}.{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip[0],ip[1],ip[2],ip[3]))
		#getoutput("scp /root/Desktop/project/task0/.bashrc {}.{}.{}.{}:".format(ip[0],ip[1],ip[2],ip[3]))


def hadoop_install_in_jobtracker():
	ip=all_ip.jobtracker_ip()
	a=getoutput("ssh {}.{}.{}.{} hadoop version".format(ip[0],ip[1],ip[2],ip[3]))
	if a==0:
		pass
	else:
		getoutput("scp /root/Desktop/project/task0/hadoop-1.2.1-1.x86_64.rpm {}.{}.{}.{}:".format(ip[0],ip[1],ip[2],ip[3]))
		getoutput("ssh {}.{}.{}.{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip[0],ip[1],ip[2],ip[3]))

def hadoop_install_in_slaves():
	ip=all_ip.slaves_ip()


	for i in range(len(ip)):
		a=getoutput("ssh {}.{}.{}.{} hadoop version".format(ip[i][0],ip[i][1],ip[i][2],ip[i][3]))
		if a==0:
			pass
		else: 
			getoutput("scp /root/Desktop/project/task0/hadoop-1.2.1-1.x86_64.rpm {}.{}.{}.{}:".format(ip[i][0],ip[i][1],ip[i][2],ip[i][3]))
			getoutput("ssh {}.{}.{}.{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip[i][0],ip[i][1],ip[i][2],ip[i][3]))


def hadoop_install_in_client():
	ip=all_ip.client_ip()
	a=getoutput("ssh {}.{}.{}.{} hadoop version".format(ip[0],ip[1],ip[2],ip[3]))
	if a==0:
		pass
	else:

		getoutput("scp /root/Desktop/project/task0/hadoop-1.2.1-1.x86_64.rpm {}.{}.{}.{}:".format(ip[0],ip[1],ip[2],ip[3]))
		getoutput("ssh {}.{}.{}.{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip[0],ip[1],ip[2],ip[3]))
		
