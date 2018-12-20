import os
import all_ip
from process import getoutput

def set_m1_hostname():

	ip=all_ip.master_ip()

	getoutput("ssh {}.{}.{}.{} hostnamectl set-hostname m1.com".format(ip[0],ip[1],ip[2],ip[3]))
	#getoutput("ssh {0}.{1}.{2}.{3} echo '{0}.{1}.{2}.{3} m1.com' >> /etc/hosts".format(ip[0],ip[1],ip[2],ip[3]))
	getoutput("echo '{0}.{1}.{2}.{3} m1.com' >> /root/Desktop/project/task0/hosts".format(ip[0],ip[1],ip[2],ip[3]))

def set_m2_hostname():
	ip=all_ip.jobtracker_ip()

	getoutput("ssh {}.{}.{}.{} hostnamectl set-hostname m2.com".format(ip[0],ip[1],ip[2],ip[3]))
	#getoutput("ssh {0}.{1}.{2}.{3} echo '{0}.{1}.{2}.{3} m1.com' >> /etc/hosts".format(ip[0],ip[1],ip[2],ip[3]))
	getoutput("echo '{0}.{1}.{2}.{3} m2.com' >> /root/Desktop/project/task0/hosts".format(ip[0],ip[1],ip[2],ip[3]))
def set_slaves_hostname():
	ip=all_ip.slaves_ip()

	for i in range(len(ip)):

		print(ip[i])
		getoutput("ssh {}.{}.{}.{} hostnamectl set-hostname s{}.com".format(ip[i][0],ip[i][1],ip[i][2],ip[i][3],i+1))
		#getoutput("ssh {0}.{1}.{2}.{3} echo '{0}.{1}.{2}.{3} m{4}.com' >> /etc/hosts".format(ip[0],ip[1],ip[2],ip[3],i+1))
		getoutput("echo '{}.{}.{}.{} s{}.com' >> /root/Desktop/project/task0/hosts".format(ip[i][0],ip[i][1],ip[i][2],ip[i][3],i+1))

def set_client_hostname():
	ip=all_ip.client_ip()
	getoutput("ssh {}.{}.{}.{} hostnamectl set-hostname c1.com".format(ip[0],ip[1],ip[2],ip[3]))
	#getoutput("ssh {0}.{1}.{2}.{3} echo '{0}.{1}.{2}.{3} m1.com' >> /etc/hosts".format(ip[0],ip[1],ip[2],ip[3]))
	getoutput("echo '{0}.{1}.{2}.{3} c1.com' >> /root/Desktop/project/task0/hosts".format(ip[0],ip[1],ip[2],ip[3]))


def send_hosts_to_all_ip():

	ip1=all_ip.master_ip()
	ip2=all_ip.jobtracker_ip()
	ip3=all_ip.slaves_ip()
	ip4=all_ip.slaves_ip()

	getoutput("scp /root/Desktop/project/task0/hosts {}.{}.{}.{}:/etc/hosts".format(ip1[0],ip1[1],ip1[2],ip1[3]))
	
	getoutput("scp /root/Desktop/project/task0/hosts {}.{}.{}.{}:/etc/hosts".format(ip2[0],ip2[1],ip2[2],ip2[3]))

	getoutput("scp /root/Desktop/project/task0/hosts {}.{}.{}.{}:/etc/hosts".format(ip4[0],ip4[1],ip4[2],ip4[3]))
	
	for i in range(len(ip3)):
		getoutput("scp /root/Desktop/project/task0/hosts {}.{}.{}.{}:/etc/hosts".format(ip3[i][0],ip3[i][1],ip3[i][2],ip3[i][3]))
	
