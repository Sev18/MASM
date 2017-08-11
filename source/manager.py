import re
import requests
import urllib2
from bs4 import BeautifulSoup
from time import localtime, strftime
import time
from operator import itemgetter
import sys
import os
import shutil
import ctypes, sys
import subprocess
from win32com.client import GetObject
import shlex
from subprocess import Popen, PIPE, CREATE_NEW_CONSOLE
import _winreg


#aglo: 'Cryptonight', 'Ethash', 'Equihash', 'Groestl', 'Lyra2RE2', 'Myriad-Groestl', 'NeoScrypt', 'Skein'
targetalgo = []
algominer = {'Cryptonight':'ccminer-x64.exe', 'Ethash':'EthDcrMiner64.exe', 'Equihash':'miner.exe', 'Groestl':'ccminer-x64.exe', 'Lyra2RE2':'ccminer-x64.exe', 'Myriad-Groestl':'ccminer-x64.exe', 'NeoScrypt':'ccminer-x64.exe', 'Skein':'ccminer-x64.exe'}
url = "https://masmanager.info/"
url_price = "https://blockchain.info/tobtc?currency=USD&value=1"
#Hashrate(GTX1060*4way)
# 'Cryptonight':2094, 'Ethash':96500000, 'Equihash':1210, 'Groestl':91600000, 'Lyra2RE2':89500000, 'Myriad-Groestl':169100000, 'NeoScrypt':2478000, 'Skein':856500000
algohash = {}

#miners
EthDcrMiner64 = ["C:\\Users\\JScoin\\Desktop\\miner\\Claymore's Dual Ethereum+Decred_Siacoin_Lbry_Pascal AMD+NVIDIA GPU Miner v9.5\\EthDcrMiner64.exe"]
miner = ["C:\\Users\\JScoin\\Desktop\\miner\\Zec Miner 0.3.4b\\miner"]
ccminer = ["C:\\Users\\JScoin\\Desktop\\miner\\ccminer-2.0-release-x64-cuda-8.0\\ccminer-x64"]

batchpath = 'batch\\'

lastalgo = ''

#EthTotal = 0
#PytTotal = 0

zecsetlist = ['Equihash', 'Groestl', 'Lyra2RE2', 'Myriad-Groestl', 'NeoScrypt', 'Skein']
ethsetlist = ['Cryptonight', 'Ethash']

def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

def copy_ow(from_path, to_path): #overwrite folder
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)
	
def getProcessesList():
    PROCESSES_LIST_ = []
    getObj_ = GetObject('winmgmts:')
    processes_ = getObj_.InstancesOf('Win32_Process')
    for ps_ in processes_:
        PROCESSES_LIST_.append(ps_.Properties_('Name').Value)
    return PROCESSES_LIST_

def kill_miners():
	os.system('taskkill /F /IM ccminer-x64.exe /T')
	os.system('taskkill /F /IM EthDcrMiner64.exe /T')
	os.system('taskkill /F /IM miner.exe /T')

def ab_zec_set():
	os.system('taskkill /F /IM MSIAfterburner.exe /T')
	time.sleep(1)
	copy_ow('OCsets\Profile_z', ABdir+'\Profiles')
	time.sleep(1)
	subprocess.Popen(cfgdict['ABpath'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	print strftime("[%x %X]", localtime()) + ' ' + 'AfterBurner: Zcash setting loaded for ' + profalgo +'.'
	f.write(strftime("[%x %X]", localtime()) + ' ' + 'AfterBurner: Zcash setting loaded for ' + profalgo +'.'+'\n')

def ab_eth_set():
	os.system('taskkill /F /IM MSIAfterburner.exe /T')
	time.sleep(1)
	copy_ow('OCsets\Profile_e', ABdir+'\Profiles')
	time.sleep(1)
	subprocess.Popen(cfgdict['ABpath'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	print strftime("[%x %X]", localtime()) + ' ' + 'AfterBurner: Ethereum setting loaded for ' + profalgo +'.'
	f.write(strftime("[%x %X]", localtime()) + ' ' + 'AfterBurner: Ethereum setting loaded for ' + profalgo +'.'+'\n')

def start_miner(profalgo):

	batchline = batchpath + profalgo + '.bat ' + cfgdict['workername'] + ' ' + cfgdict['password'] + ' ' +regionCode[cfgdict['region']]
	subprocess.Popen(batchline, creationflags=CREATE_NEW_CONSOLE)
	print strftime("[%x %X]", localtime()) + ' ' + profalgo + ' : ' + algocoin[profalgo] + ' + ' + str(dolperday[profalgo]) + ' $/day - ' + algominer[profalgo] + ' ' + 'Started.'
	f.write(strftime("[%x %X]", localtime()) + ' ' + profalgo + ' : ' + algocoin[profalgo] + ' + ' + str(dolperday[profalgo]) + ' $/day - ' + algominer[profalgo] + ' ' + 'Started.'+'\n')

#intro
print '*******************************************************************************'
print '             Multi-aglorithm Switching Manager v0.0.3 by Sev18'
print '*******************************************************************************'
print 'Donation address'
print 'ETH - 0xd7A9FA6448a9c7a3192A8D762e6bC04858E1dc7d'
print 'BTC - 1P4eov4yk2abZgHvBbgnn35AqGCEozJgjt'
print '*******************************************************************************\n'

	
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
		
#nvidiasvc.dat loading
hashfile = open('nvidiasvc.dat','r')
hashline = hashfile.readlines()
hashdict={}
for line in hashline:
	line = line.strip()
	if '=' in line:
		hashdict[line.split('=')[0]] = line.split('=')[1]



print 'Loading benchmark result..'

#check admin status
if cfgdict['ABswitch'] == '1':
	if is_admin():
		pass
	else:
		print 'Afterburner auto switch needs administrator privileges. Please restart program as admin.'
		os.system('Pause')
		sys.exit(1)
#Check ethash, equihash mining mode
ethashf = open('batch\Ethash.bat','r')
ethashfl = ethashf.readlines()
for line in ethashfl:
	if line.startswith('::'):
		pass
	elif line.startswith('rem'):
		pass
	else:
		if 'miner\ClaymoreEth\EthDcrMiner64.exe' in line:
			etline = line.strip()
for segs in etline.split(' '):
	if 'ethash-hub.miningpoolhub.com'in segs:
		etport = segs.split(':')[1]
ethashf.close()

equihashf = open('batch\Equihash.bat','r')
equihashfl = equihashf.readlines()
for line in equihashfl:
	if line.startswith('::'):
		pass
	elif line.startswith('rem'):
		pass
	else:
		if 'miner\EWBF\miner' in line:
			eqline = line.strip()
			eqport = eqline.split('--port ')[1].split(' --')[0]

equihashf.close()

et_portcoin = {'20535':'Ethereum', '20555':'Ethereum-Classic', '20565':'Expanse' , '20585':'Musicoin'}
eq_portcoin = {'20570':'Zcash', '20575':'Zclassic'}
	

		
#targetalgo, algohash
talgolist = cfgdict['selAlgo'].replace(',',' ').strip(). split(' ')
for algo in talgolist:
	targetalgo.append(algo)
	print 'Selected algorithm: '+algo

for hash in hashdict.keys():
	if hash != 'devCode':
		algohash[hash] = int(hashdict[hash])


now = time.localtime()
s = "%04d%02d%02d_%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

	
while True:
	try:
		f=open('log\\'+s+'.txt', 'w')
		soup_price = BeautifulSoup(requests.get(url_price).content, "html.parser")
		btcprice= 1/float(str(soup_price))
		soup = BeautifulSoup(requests.get(url).content, "html.parser")
		algo_list = soup.find(id="algoList")
		algo_list_td = algo_list.findAll('td')
		
		coin_list = soup.find(id="coinList")
		coin_list_td = coin_list.findAll('td')

		cn = len(coin_list_td)/6		
		coinref = {}
				
		for i in range(0,cn):
			coinline = str(coin_list_td[i*6])
			coin = coinline.split('>')[2].split('<')[0].strip()
			btcline = str(coin_list_td[i*6+3].find('span'))
			bpd = btcline[btcline.find('title="')+7:btcline.find('">')]
			coinref[coin] = re.sub(',','',bpd)
		
		n = len(algo_list_td)/6
		algoref = {}
		algoprof = {}
		algocoin = {}
		dolperday = {}
		
		for i in range(0,n):
			algoline = str(algo_list_td[i*6])
			algo = algoline.split('>')[1].split('<')[0].strip()
			coinline = str(algo_list_td[i*6+1])
			coin = coinline.split('>')[1].split('<')[0].strip()
			btcline = str(algo_list_td[i*6+3].find('span'))
			bpd = btcline[btcline.find('title="')+7:btcline.find('">')]
			algoref[algo] = re.sub(',','',bpd)
			
			if algo in targetalgo:
				if algo == 'Ethash':
					if etport == '17020':
						algoprof[algo] = int(round(float(algoref[algo])*float(algohash[algo])/1000))
						algocoin[algo] = coin
						dolperday[algo] = round(float(algoref[algo])*float(algohash[algo])/1000000000*btcprice,2)
					else:
						algoprof[algo] = int(round(float(coinref[et_portcoin[etport]])*float(algohash[algo])/1000))
						algocoin[algo] = et_portcoin[etport]
						dolperday[algo] = round(float(algoref[algo])*float(algohash[algo])/1000000000*btcprice,2)

				if algo == 'Equihash':
					if eqport == '17023':
						algoprof[algo] = int(round(float(algoref[algo])*float(algohash[algo])/1000))
						algocoin[algo] = coin
						dolperday[algo] = round(float(algoref[algo])*float(algohash[algo])/1000000000*btcprice,2)
					else:
						algoprof[algo] = int(round(float(coinref[eq_portcoin[eqport]])*float(algohash[algo])/1000))
						algocoin[algo] = eq_portcoin[eqport]
						dolperday[algo] = round(float(algoref[algo])*float(algohash[algo])/1000000000*btcprice,2)						

				
		sorted_algoprof = sorted(algoprof.iteritems(), key=itemgetter(1), reverse=True)
		profalgo = str(sorted_algoprof[0]).split("'")[1] #most profitable algorithm name
	except Exception as e:
		print e
		print 'Error occured, retrying after 60 seconds.'
		time.sleep(60)
		continue
	
	proc_list = getProcessesList()
	
	#EthTotal = EthTotal + algoprof['Ethash']
	#PytTotal = PytTotal + algoprof[profalgo]
	
	#PytPer = round((float(PytTotal) - float(EthTotal))/float(EthTotal)*100, 2)

	
	if profalgo == lastalgo:
		if algominer[profalgo] in proc_list:
			print strftime("[%x %X]", localtime()) + ' ' + profalgo + ' : ' + algocoin[profalgo] + ' + ' + str(dolperday[profalgo]) + ' $/day - ' + algominer[profalgo] + ' ' + 'Running.'
			f.write(strftime("[%x %X]", localtime()) + ' ' + profalgo + ' : ' + algocoin[profalgo] + ' + ' + str(dolperday[profalgo]) + ' $/day - ' + algominer[profalgo] + ' ' + 'Running.'+'\n')
		else:
			kill_miners()
			start_miner(profalgo)
	else:
		if profalgo in zecsetlist:
			if cfgdict['ABswitch'] == '1':
				ab_zec_set()
		elif profalgo in ethsetlist:
			if cfgdict['ABswitch'] == '1':
				ab_eth_set()
		kill_miners()
		start_miner(profalgo)
	lastalgo = profalgo
	f.close()
	time.sleep(60)

	#	pass
	
