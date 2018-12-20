import os
import all_ip
from process import getoutput
def slaveconf():
	ip=all_ip.slaves_ip()

	for i in range(len(ip)):
		getoutput("scp /root/Desktop/project/task0/hdfs-site2.xml {}.{}.{}.{}:/etc/hadoop/hdfs-site.xml".format(ip[i][0],ip[i][1],ip[i][2],ip[i][3]))
		getoutput("scp /root/Desktop/project/task0/core-site.xml {}.{}.{}.{}:/etc/hadoop/hdfs-site.xml".format(ip[i][0],ip[i][1],ip[i][2],ip[i][3]))
		
		

