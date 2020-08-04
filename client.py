import os
import threading
import time
import random

lock = threading.Lock()
servers = []
def get_active_servers():
	global servers
	while(True):
		file = open("server_file","r")
		a = file.read()
		servers = a.split("\n")
		if('' in servers):
			servers.remove('')
		#print(servers)


def download(thread_id):
	global servers
	file = open("LOAD","r")
	max_downloads = int(file.read())
	
	#print(str(thread_id)+" starts download")
	for x in range(0,max_downloads):
		if(len(servers) > 0):
			os.system("wget "+servers[x%len(servers)]+":8000/file  -O /dev/null")
			#print("LOAD NOW AT "+str(max_downloads))
		else:
			print("No server present to serve!!!")
	#print(str(thread_id)+" stops download")

if __name__ == "__main__":
	print("in main")
	count = 0
	
	threading.Thread(target = get_active_servers,args=()).start()
	time.sleep(5)
	while(True):
		threading.Thread(target = download, args = (count,)).start()
		time.sleep(1)
		count+=1

	




