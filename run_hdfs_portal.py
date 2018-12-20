print("will run soon ")
import all_ip
import os


def master_portal():
	ip=all_ip.master_ip()
	os.system("firefox {}.{}.{}.{}:50070".format(ip[0],ip[1],ip[2],ip[3]))


def jobtracker_portal():
	ip=all_ip.jobtracker_ip()
	os.system("firefox {}.{}.{}.{}:50030".format(ip[0],ip[1],ip[2],ip[3]))
