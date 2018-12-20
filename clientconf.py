import os
import all_ip
from process import getoutput
def clientconf():

	ip=all_ip.client_ip()

	getoutput("scp /root/Desktop/project/task0/core-site.xml {}.{}.{}.{}:/etc/hadoop/".format(ip[0],ip[1],ip[2],ip[3]))


	getoutput("scp /root/Desktop/project/task0/mapred-site.xml {}.{}.{}.{}:/etc/hadoop/".format(ip[0],ip[1],ip[2],ip[3]))


	

