Multi-algorithm Switching Manager v0.0.3(2017.07.22) by Sev18

**********************************************************
If you find this tool useful, please consider a donation.

ETH - 0xd7A9FA6448a9c7a3192A8D762e6bC04858E1dc7d
BTC - 1P4eov4yk2abZgHvBbgnn35AqGCEozJgjt
**********************************************************


---Introduction---

This is a tool for managing multi-algo switch mining.
(Supports MiningPoolHub/NVIDIA/WINDOWS systems)

* Features *
- Multi-algo switch mining based on self-benchmark
- Solved EWBF 0 sol/s bug on port-based multi-algo switch mining
- Auto switching of AfterBurner overclock settings with algorithm switching(administrator privileges needed)
- Showing expected daily profit
- Setting on GUI program, mining on console-based program

- Supporting algorithms: Ethash, Equihash, Cryptonight, Groestl, Lyra2RE2, Myriad-Groestl, NeoScrypt, Skein
- Miners included :
	Claymore's Dual Ethereum AMD+NVIDIA GPU Miner v9.7 (Windows/Linux)
	https://bitcointalk.org/index.php?topic=1433925.13480
	EWBF's CUDA Zcash miner Version 0.3.4b.
	https://bitcointalk.org/index.php?topic=1707546.0
	ccminer-2.0-release-x64-cuda-8.0.7z
	https://github.com/tpruvot/ccminer/releases
	You can update miners by replacing miner files on \miner\

* Download link *
https://mega.nz/#F!F2RRiR4K!QYicOif89SCQm9vzDjPAMQ​


* Get started * (setting.exe -> benchmark.exe -> manager.exe)
1. Download and extract zip file.

2. Start setting.exe.(run as administrator if you want AfterBurner auto-switch mode)

3. Fill in the blanks and choose algorithms to switch(Ethash + Equihash (or + other 1 more algo) recommended)
* See 'Algorithm selection tip' below for more information

	- For Afterburner auto-switch mode(Run as administrator!)
This is a function that the manager program automatically changes the AfterBurner overclock settings. It isn't going to be applied on Afterburner right after you complete settings, overclock settings are applied only during benchmark and mining.

	(1) Click 'Enable Afterburner Auto-switch
	(2) Fill in overclock settings
Equihash,  Groestl, Lyra2RE2, Myriad-Groestl, NeoScrypt, Skein - Core clock dependent algorithms
Cryptonight, Ethash - Memory clock dependent algorithms
Hashrate of core-clock dependent algorithms mainly affected by overclock of core clock, you should use overclock settings for Zcash mining for these algorithms. For memory-clock dependent algorithms, you can use settings for Ethereum mining.

Example settings, For GTX 1060 Samsung RAM)
Core-clock dependent:
Power limit : 75%, Core clock : +150MHz, Mem clock : +400MHz, Fan speed: 75%
Memory-clock dependent:
Power limit : 75%, Core clock : -100MHz, Mem clock : +800MHz, Fan speed: 75%

	(3) Press 'Save OC settings' button.(after about 3 seconds messagebox will come out)
* The setting goes same for all of your GPUs of your mining rig. You can adjust settings for each card by modifying 'VEN_xxxx&DEV......cfg' files in \OCsets\Profile_z for core-dependent setting, \OCsets\Profile_e for memory-dependent settings.
* Press 'Restore settings' to restore previous settings before using this tool.

4. Press 'Save settings'.

5. Press 'Start Benchmark' on your first time of installation.
* See 'If you have a problem with benchmark' below for any problem.

6. benchmark.exe starts and automatically run benchmarks for 8 algorithms(It will take about 15 minutes).

7. After benchmark completed, manager.exe will start with multi-algorithm switch mining!

* Once you had your benchmarks done, you don't need to run it again unless there is hardware or overclock setting change on your mining rig.

8. If you are done with setting and benchmark, you can just run manager.exe or use start_manager.bat to start mining immediately.(Run as administrator for Afterburner auto switch mode)




* Algorithm selection tips *

This tool provides algo-switching between maximum 8 algorithms, but too many algorithms may cause ineffective mining due to too frequent miner program changes. Also time gap between mining and auto exchange also cause decrease of total profit. So I recommend you to select 2-3 major algorithms like Ethash + Equihash.
You can combine simple coin mining modes by changing port written in batch files on \batch directory.

Example)
Select Ethash, Equihash and Cryptonight on setting
-> auto-switch between [Ethereum, Ethereum-classic, Expanse, Musicoin], [Zcash, Zclassic] and Monero

Select Ethash, Equihash and Cryptonight on setting, change port to 20535(Ethrereum simple mining) on  Ethash batch file
-> auto-switch between Ethereum, [Zcash, Zclassic] and Monero

Select Ethash and Equihash on setting, change port to 20535(Ethrereum simple mining) on  Ethash, 20570(Zcash simple mining) on Equihash batch file.
-> auto-switch between Ethereum and Zcash




* If you have a problem with benchmark *

You can pass benchmark by modifying nvidiasvc.dat file, write down hashrates of your mining rig.(on Hash/s unit)
Example, GTX 1060 Samsung RAM)

Multi-algorithm switch manger
Benchmark Results
[Hashrate]
devCode=MASManager
Cryptonight=2094
Ethash=91430000
Equihash=1210
Groestl=91600000
Lyra2RE2=89500000
Myriad-Groestl=169100000
NeoScrypt=2478000
Skein=856500000

Save nvidiasvc.dat file and you can run manager.exe


* Other features *
- You can modify batch files in \batch directory for miner options. Such as dual mining, failover settings on Claymore's miner. Only be careful not to change %1, %2, %3 on batch file command.
- For new versions on Claymore's, EWBF or ccminer, you can upgrade it by replace files in \miner\ClaymoreEth, \miner\EWBF or \miner\ccminer.




*Release note

v0.0.3(2017.07.22)
- program stabilization
- increased visibility of icon

v0.0.2(2017.07.20)
- benchmark stabilization
- auto start mining after benchmark
