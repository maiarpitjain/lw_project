
import os

def ip_splitter(ip):
	l=ip.split('.')
	#print(l)
	for i in range(len(l)):
		l[i]=int(l[i])

	return l


def all_ip():

	os.system("touch ip.txt")

	global m1_ip
	global m2_ip
	global l
	global c1_ip
	m1_ip=(input("Enter your master ip"))
	m1_ip=ip_splitter(m1_ip)
	os.system("echo {} >> /root/Desktop/project/task0/ip.txt".format(m1_ip))

	m2_ip=(input("Enter your jobtracker ip"))
	m2_ip=ip_splitter(m2_ip)
	os.system("echo {} >> /root/Desktop/project/task0/ip.txt".format(m2_ip))
	
	total_s=int(input("Enter your total slave"))
	l=[]
	for i in range(total_s):
	
		l.append(input("Enter your slave{} ip".format(i)))
		l[i]=ip_splitter(l[i])
		os.system("echo {} >> /root/Desktop/project/task0/ip.txt".format(l[i]))

	c1_ip=input("Enter your client ip")
	c1_ip=ip_splitter(c1_ip)
	os.system("echo {} >> /root/Desktop/project/task0/ip.txt".format(c1_ip))


	#print(m1_ip)
	#print(m2_ip)
	#print(l)


def master_ip():
	return m1_ip

def jobtracker_ip():
	return m2_ip

def slaves_ip():
	return l

def client_ip():
	return c1_ip



