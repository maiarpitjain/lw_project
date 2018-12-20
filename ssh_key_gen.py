import os
import all_ip
def self_key_gen():
	#ip=input("Enter your pc ip")
	#ip=all_ip.ip_splitter(ip)
	os.system("ssh-keygen")

def with_master():
	ip=all_ip.master_ip()
	
	os.system("ssh-copy-id {}.{}.{}.{}".format(ip[0],ip[1],ip[2],ip[3]))


def with_jobtracker():
	ip=all_ip.jobtracker_ip()
	os.system("ssh-copy-id {}.{}.{}.{}".format(ip[0],ip[1],ip[2],ip[3]))
	

def with_slaves():
	ip=all_ip.slaves_ip()
	for i in range(len(ip)):
		os.system("ssh-copy-id {}.{}.{}.{}".format(ip[i][0],ip[i][1],ip[i][2],ip[i][3]))

	

