import os
import all_ip
from process import getoutput
def tasktrackerconf():
	
	ip=all_ip.slaves_ip()

	for i in range(len(ip)):
		getoutput("scp /root/Desktop/project/task0/mapred-site.xml {}.{}.{}.{}:/etc/hadoop/".format(ip[i][0],ip[i][1],ip[i][2],ip[i][3]))
	