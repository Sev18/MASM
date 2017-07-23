import re, requests, urllib2, os, _winreg, shutil, ctypes, sys, subprocess, shlex, socket
from bs4 import BeautifulSoup
from time import localtime, strftime
import time
from operator import itemgetter
from win32com.client import GetObject
from subprocess import Popen, PIPE, CREATE_NEW_CONSOLE

#benchmark
#Region : asia, us-east, europe
#Nvidia : ClaymoreEth, EWBF, ccminer
#AMD : ClaymoreZec, EWBF, sgminer
ClaymoreEth = "miner\ClaymoreEth\EthDcrMiner64.exe"
EWBF = "miner\EWBF\miner"
ccminer = "miner\ccminer\ccminer-x64"
f = open("nvidiasvc.dat", 'r')
flines = f.readlines()
f.close()

#setting.cfg loading
cfgfile = open('setting.cfg','r')
cfgline = cfgfile.readlines()
cfgdict = {}
for line in cfgline:
	line = line.strip()
	if '=' in line:
		cfgdict[line.split('=')[0]] = line.split('=')[1]
ABdir = cfgdict['ABpath'].replace('MSIAfterburner.exe','')
regionCode = {'0':'asia', '1':'europe', '2':'us-east'}
locale = regionCode[cfgdict['region']]

erralgo = []
targetalgo = ['Ethash', 'Equihash', 'Cryptonight', 'Groestl', 'Lyra2RE2', 'Myriad-Groestl', 'NeoScrypt', 'Skein']

algobatch = {
'Cryptonight':ccminer + ' -r 0 -a cryptonight -o stratum+tcp://'+ locale +'.cryptonight-hub.miningpoolhub.com:17024 -u Sev18.1 -p x --api-bind 127.0.0.1:4068',
'Ethash':ClaymoreEth + ' -epool '+ locale +'.ethash-hub.miningpoolhub.com:17020 -ewal Sev18.1 -eworker Sev18.1 -esm 2 -epsw x -allpools 1 -allcoins 1',
'Equihash':EWBF + ' --server '+ locale +'.equihash-hub.miningpoolhub.com --user Sev18.1 --pass x --port 17023 --api 127.0.0.1:42000',
'Groestl':ccminer + '  -r 0 -a groestl -o stratum+tcp://hub.miningpoolhub.com:17004 -u Sev18.1 -p x --api-bind 127.0.0.1:4068',
'Lyra2RE2':ccminer + '  -r 0 -a lyra2v2 -o stratum+tcp://hub.miningpoolhub.com:17018 -u Sev18.1 -p x --api-bind 127.0.0.1:4068',
'Myriad-Groestl':ccminer + '  -r 0 -a myr-gr -o stratum+tcp://hub.miningpoolhub.com:17005 -u Sev18.1 -p x --api-bind 127.0.0.1:4068',
'NeoScrypt':ccminer + '  -r 0 -a neoscrypt -o stratum+tcp://hub.miningpoolhub.com:17012 -u Sev18.1 -p x --api-bind 127.0.0.1:4068',
'Skein':ccminer + '  -r 0 -a skein -o stratum+tcp://hub.miningpoolhub.com:17016 -u Sev18.1 -p x --api-bind 127.0.0.1:4068'}

zecsetlist = ['Equihash', 'Groestl', 'Lyra2RE2', 'Myriad-Groestl', 'NeoScrypt', 'Skein']
ethsetlist = ['Cryptonight', 'Ethash']

algohash = {}
tryn = 3


def getMedian(a):
	a_len = len(a)
	if (a_len == 0): return None
	a_center = a_len / 2

	if (a_len % 2 == 1):
		return a[a_center]
	else:
		return (a[a_center - 1] + a[a_center]) / 2

def kill_miners():
	os.system('taskkill /F /IM ccminer-x64.exe /T')
	os.system('taskkill /F /IM EthDcrMiner64.exe /T')
	os.system('taskkill /F /IM miner.exe /T')		
		
def copy_ow(from_path, to_path): #overwrite folder
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)
	
def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

def ab_zec_set():
	os.system('taskkill /F /IM MSIAfterburner.exe /T')
	time.sleep(1)
	copy_ow('OCsets\Profile_z', ABdir+'\Profiles')
	time.sleep(1)
	subprocess.Popen(cfgdict['ABpath'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	print strftime("%x %X", localtime()) + '\t' + 'AfterBurner: Zcash setting loaded.'

def ab_eth_set():
	os.system('taskkill /F /IM MSIAfterburner.exe /T')
	time.sleep(1)
	copy_ow('OCsets\Profile_e', ABdir+'\Profiles')
	time.sleep(1)
	subprocess.Popen(cfgdict['ABpath'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	print strftime("%x %X", localtime()) + '\t' + 'AfterBurner: Ethereum setting loaded.'
	
def ccminer_khs():
	TCP_IP = '127.0.0.1' 
	TCP_PORT = 4068
	BUFFER_SIZE = 1024
	MESSAGE = "summary"
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE)
	data = s.recv(BUFFER_SIZE)
	s.close()
	khs = data.split(';')[5].split('=')[1]
	return khs


def ClaymoreEthBench():
	trynumber = tryn
	while trynumber != 0:
		try:

			subprocess.Popen(algobatch[algo], creationflags=CREATE_NEW_CONSOLE)

			url = "http://127.0.0.1:3333"
			sec =120
			hashlist = []
			
			print 'Ethash benchmark start.'
			time.sleep(10)
			print 'Waiting for API connection.'
			time.sleep(10)
			print 'API connected.'
			time.sleep(10)
			while sec != 0:
				soup = BeautifulSoup(requests.get(url).content, "html.parser")
				soup_list = soup.findAll(text=True)
				hash = float(soup_list[0].split('["')[1].split('", "')[2].split(';')[0])
				print 'Ethash Hashrate : ' + str(hash/1000) +' Mh/s - '+ str(sec)+' seconds left.'
				sec = sec-10
				time.sleep(10)
				if hash != 0:
					hashlist.append(hash)
		
			medhash = getMedian(hashlist)
			print 'Ethash benchmark complete! Average hashrate : ' +str(medhash/1000)+ ' Mh/s'
			algohash['Ethash'] = medhash*1000
			os.system('taskkill /F /IM EthDcrMiner64.exe /T')
			hashlist = []

			trynumber = 0
		except:
			if trynumber > 1:
				print 'Error occured. Trying '+algo+' benchmark again..'
				os.system('taskkill /F /IM EthDcrMiner64.exe /T')
				trynumber = trynumber - 1
			elif trynumber == 1:
				print 'Could not complete '+algo+' benchmark. Please try again later.'
				erralgo.append(algo)
				os.system('taskkill /F /IM EthDcrMiner64.exe /T')
				trynumber = trynumber - 1
				algohash[algo] = 0
	
def EWBFBench():
	trynumber = tryn
	while trynumber != 0:
		try:

			subprocess.Popen(algobatch[algo], creationflags=CREATE_NEW_CONSOLE)

			url = "http://127.0.0.1:42000"
			sec = 120
			hashlist = []
			print 'Equihash benchmark start.'
			time.sleep(10)
			print 'API connected.'
			while sec != 0:
				soup = BeautifulSoup(requests.get(url).content, "html.parser")
				soup_list = soup.findAll(id='total')
				hash = float(str(soup_list[0]).split('W</td><td>')[1].split(' Sol/s</td>')[0])
				print 'Equihash Hashrate : ' + str(hash) +' Sol/s - '+ str(sec)+' seconds left.'
				sec = sec-10
				time.sleep(10)
				if hash != 0:
					hashlist.append(hash)
		
			medhash = getMedian(hashlist)
			print 'Equihash benchmark complete! Average hashrate : ' +str(medhash)+ ' Sol/s'
			algohash['Equihash'] = medhash
			os.system('taskkill /F /IM miner.exe /T')
			hashlist = []

			trynumber = 0
		except:
			if trynumber > 1:
				print 'Error occured. Trying '+algo+' benchmark again..'
				os.system('taskkill /F /IM miner.exe /T')
				trynumber = trynumber - 1
			elif trynumber == 1:
				print 'Could not complete '+algo+' benchmark. Please try again later.'
				erralgo.append(algo)
				os.system('taskkill /F /IM miner.exe /T')
				trynumber = trynumber - 1
				algohash[algo] = 0

def ccminerBench():
	trynumber = tryn
	while trynumber != 0:
		try:

			subprocess.Popen(algobatch[algo], creationflags=CREATE_NEW_CONSOLE)

			url = "http://127.0.0.1:4068"
			if algo == 'Cryptonight':
				sec = 180
			else:
				sec = 120
			hashlist = []
			print algo + ' benchmark start.'
			time.sleep(10)
			print 'API connected.'
			while sec != 0:
				cckhs = float(ccminer_khs())
				print algo + ' Hashrate : ' + str(cckhs) +' Kh/s - '+ str(sec)+' seconds left.'
				sec = sec-10
				time.sleep(10)
				if cckhs != 0:
					hashlist.append(cckhs)
		
			medhash = getMedian(hashlist)
			print algo + ' benchmark complete! Average hashrate : ' +str(medhash)+ ' Kh/s'
			algohash[algo] = float(medhash)*1000
			os.system('taskkill /F /IM ccminer-x64.exe /T')
			hashlist = []
		#	
			trynumber = 0
		except:
			if trynumber > 1:
				print 'Error occured. Trying '+algo+' benchmark again..'
				os.system('taskkill /F /IM ccminer-x64.exe /T')
				trynumber = trynumber - 1
			elif trynumber == 1:
				print 'Could not complete '+algo+' benchmark. Please try again later.'
				erralgo.append(algo)
				os.system('taskkill /F /IM ccminer-x64.exe /T')
				trynumber = trynumber - 1
				algohash[algo] = 0
	
		

if cfgdict['ABswitch'] == '1':
	if is_admin():
		pass
	else:
		print 'Afterburner auto switch needs administrator privileges. Please restart program as admin.'
		os.system('Pause')
		sys.exit(1)
		
print ("Miner benchmark for Cryptonight, Ethash, Equihash, Groestl, Lyra2RE2, Myriad-Groestl, NeoScrypt, Skein. It will take about 15 minutes.")
for algo in targetalgo:
	kill_miners()
	if algo == 'Ethash':
		if cfgdict['ABswitch'] == '1':
			ab_eth_set()
		ClaymoreEthBench()
	elif algo == 'Equihash':
		if cfgdict['ABswitch'] == '1':
			ab_zec_set()
		EWBFBench()
	else:
		if cfgdict['ABswitch'] == '1':
			if algo in zecsetlist:
				ab_eth_set()
			elif algo in ethsetlist:
				ab_zec_set()
		ccminerBench()

f = open('nvidiasvc.dat', 'w')
for line in flines:
	if '=' in line:
		pass
	else:
		f.write(line)

devcode = 'MASManager'
f.write('devCode='+devcode+'\n')
for k, v in algohash.items():
	f.write(k+'='+str(int(v))+'\n')
f.close()
if len(erralgo) != 0:
	print 'Incomplete benchmark for:'
	for line in erralgo:
		print line
	print 'Please retry benchmark later.'
print 'Benchmark Complete! Starting manager.exe.'
subprocess.Popen('manager.exe', creationflags=CREATE_NEW_CONSOLE)
os.system('Pause')
	
			
		
	



