import authentication
import os
import menu
#import java_installation
#import hadoop_installation 

def set_ssh():
	import ssh_key_gen
	ssh_key_gen.self_key_gen()
	ssh_key_gen.with_master()
	ssh_key_gen.with_jobtracker()
	ssh_key_gen.with_slaves()

def set_hostname():
	
	import set_hostname
	set_hostname.set_m1_hostname()
	set_hostname.set_m2_hostname()
	set_hostname.set_slaves_hostname()
	set_hostname.set_client_hostname()

user=input("Enter User name:\n")
passwd=input("Enter Password\n")

r=authentication.auth(user,passwd)


if r:

	menu.uper_menu()
	#set_ssh()
	#set_hostname()


	while True:
		os.system("touch hosts")
		os.system("clear")
		

		menu.menu()

		choice=int(input("Enter your choice"))

		if choice==1:
			import java_installation
			java_installation.java_install_in_master()
			java_installation.java_install_in_jobtracker()
			java_installation.java_install_in_slaves()

		elif choice==2:
			import hadoop_installation
			hadoop_installation.hadoop_install_in_master()
			hadoop_installation.hadoop_install_in_jobtracker()
			hadoop_installation.hadoop_install_in_slaves()

		elif choice==3:
			menu.hadoop_menu()

		elif choice==4:
			pass
		elif choice==5:
			break
		else:
			print("Invalid Character")
			break
			
		ch=input("Do you want to continue y/n")
		if ch=='n':
			break
	

else:
	print("user and password does not exist")
	
