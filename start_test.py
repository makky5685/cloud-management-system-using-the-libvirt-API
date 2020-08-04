import time
import libvirt
from xml_file import xml_files 
import os
from xml_file import VM_IP_addresses
from xml_file import VM_names
import threading

ACTIVE_VM_list = []
NAME_TO_IP_map = {}
NEXT_VM_index = 1

conn = libvirt.open('qemu:///system')
if conn == None:
	print("could not open libvirt connection")
	exit(1)


def cpu_per(t,dom):
	try:
		x = dom.getCPUStats(True)[0]['cpu_time']
		time.sleep(t)
		y = dom.getCPUStats(True)[0]['cpu_time']
		diff = str(int((y-x)/t))
		if(len(diff) < 9):
			return '-1'
		else:
			return diff[0] + diff[1]
	except:
		return '-1'

def look_for_dead_VM():
	time.sleep(120)
	while(True):
		global ACTIVE_VM_list
		global NAME_TO_IP_map
		TO_BE_REMOVED_domains = []
		ACTIVE_domains = []
		for i in ACTIVE_VM_list:
			if(i.isActive() == 0):
				TO_BE_REMOVED_domains.append(i)
			else:
				ACTIVE_domains.append(i)

		for i in TO_BE_REMOVED_domains:
			ACTIVE_VM_list.remove(i)
		if(len(TO_BE_REMOVED_domains) > 0):
			file = open("server_file","w+")
			for i in ACTIVE_domains:
				file.write(NAME_TO_IP_map[i.name()] + "\n")

			file.close()
		time.sleep(5)


def start_monitor():
	global NEXT_VM_index
	global NAME_TO_IP_map
	global ACTIVE_VM_list
	print("Monitor has started!")
	while(True):
		stats = [0,0]

		time_to_monitor = 30
		while(time_to_monitor > 0):
			print(stats)
			flag = 0
			for i in ACTIVE_VM_list:
				if((i.isActive()==1) and int(cpu_per(3,i)) < 50):
					flag = 1 
			if(flag == 0):
				stats[1]+=1
			else:
				stats[0]+=1
			time_to_monitor-=1
		file = open("monitor_log","a+")
		print(stats)
		if(stats[1] >= stats[0]):
			xml_object = None
			print("Time to spawn another VM!!!")
			for j in range(0,len(NAME_TO_IP_map)):
				temp_dom = conn.lookupByName(VM_names[NEXT_VM_index])
				if(temp_dom != None):
					if(temp_dom.isActive() == False):
						xml_object = temp_dom
						NEXT_VM_index = (NEXT_VM_index+1)%len(NAME_TO_IP_map)
						break
				NEXT_VM_index = (NEXT_VM_index+1)%len(NAME_TO_IP_map)
			if(xml_object == None):
				print("Cannot Find a free VM:::SORRY:)")
				continue
			file.write("TIME TO SPAWN ANOTHER VM\n")
			xml_object.create()
			temp_dom_object = xml_object
			while(temp_dom_object.isActive() == False):
				print("waiting for domain to be active!")
				pass
			#time.sleep(60)	
			file.write("NEW VM SPAWN COMPLETE\n")
			print("NEW VM SPAWN COMPLETE")
			file = open("server_file","a+")
			ip = NAME_TO_IP_map[temp_dom_object.name()]
			file.write(ip+'\n')
			file.close()
			print("TRAFFIC DIRECTED SUCCESSFULLY")
			ACTIVE_VM_list.append(temp_dom_object)
		else:
			file.write("NO NEW VM SPAWN REQUIRED\n")
		file.close()

def start_test():#starts the first vm and starts sending LOAD when the vm boots up completely(approx after 60 seconds!)
	
	global NAME_TO_IP_map
	global conn
	dom_m1 = conn.defineXML(xml_files[0])
	for i in range(0,len(VM_names)):
		NAME_TO_IP_map[VM_names[i]] = VM_IP_addresses[i]
	if(dom_m1 == None):
		print("Could not define XML of INITIAL VM")
		exit(1)
	if(dom_m1.create() < 0):
		print("Could not BOOT INITIAL VM")
		exit(1)
	name = dom_m1.name()
	dom_open_m1 = dom_m1
	time.sleep(30)
	while(dom_open_m1.isActive() == False):
		print("waiting for domain to be active!")
		pass
	#time.sleep(30)
	ACTIVE_VM_list.append(dom_open_m1)
	print("Sending LOAD on INITIAL VM")	
	file = open("server_file","a+")
	ip = NAME_TO_IP_map[dom_open_m1.name()]
	NAME_TO_IP_map[name] = ip
	file.write(ip+'\n')
	file.close()
	if(os.fork() > 0):
		threading.Thread(target = look_for_dead_VM,args=()).start()
		start_monitor()
	else:
		os.system("python3 client.py")
start_test()