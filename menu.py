import os
def uper_menu():
	#print("Enter all master,jobtrack,slaves ip")
	import all_ip
	all_ip.all_ip()
	os.system("clear")
	


def menu():
	print("""\t\t\t\tMenu\t\t\t\t\n
		1.press 1 to install java
		2.press 2 to install hadoop
		3.press 3 to setup hadoop cluster
		4.ssh key generate for all ips
		5.Exit
		""")


def hadoop_menu():
	os.system("clear")
	hadoop_ch=int(input("""\t\t\t\tMenu\n
		1.Master configuration
		2.jobtracker configuration
		3.slave configuration
		4.tasktracker configuration
		5.client configuration
		6.set host name
		7.run namenode and jobtracker and datanode and tasktrackers
		8.check live datanode
		9.check live tasktracaker
		10.Open hdfs portal
		11.open jobtracker portal 
		12.Main menu
		"""))

	if hadoop_ch==1:
		import masterconf
		masterconf.masterconf()

	elif hadoop_ch==2:
		import jobtrackerconf
		jobtrackerconf.jobtrackerconf()
	elif hadoop_ch==3:
		import slaveconf
		slaveconf.slaveconf()
	elif hadoop_ch==4:

		import tasktrackerconf
		tasktrackerconf.tasktrackerconf()
	
	elif hadoop_ch==5:

		import clientconf
		clientconf.clientconf()

	
	elif hadoop_ch==6:
		pass
		
	elif hadoop_ch==7:
		import run_nodes


	elif hadoop_ch==8:
		import masterconf
		masterconf.checkdn()

	elif hadoop_ch==9:
		import jobtrackerconf
		jobtrackerconf.checktt()

	elif hadoop_ch==10:
		import run_hdfs_portal
		run_hdfs_portal.master_portal()
	elif hadoop_ch==11:
		import run_hdfs_portal
		run_hdfs_portal.jobtracker_portal()

	elif hadoop_ch==12:
		os.system("clear")
		menu()
	else:
		print("Invalid Character")
