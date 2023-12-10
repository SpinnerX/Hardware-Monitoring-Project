import os
import platform
import psutil
import GPUtil
import cpuinfo
from tabulate import tabulate

def main():
	LINES_USEFUL_INFORMATION = 11;

	for file in os.listdir(os.getcwd()):
		for row in csvfile:
			list = []
			for i in range(len(LINES_USEFUL_INFORMATION)):
				list.append(

"""
	#Documentation: https://docs.python.org/3/library/platform.html
	print(f"Machine: {platform.machine()}")
	print(f"Architecture: {platform.architecture()}")
	print(f"Node: {platform.node()}")
	print(f"Platform: {platform.platform()}")
	print(f"Processor: {platform.processor()}")
	print(f"Release: {platform.release()}")
	print(f"System: {platform.system()}")
#	print(f"System Alias: {platform.system_alias(TODO 3 parameters needed)}")
	print(f"Version: {platform.version()}")
	print(f"UName: {platform.uname()}")
	print(f"UName: {platform.uname().processor}")

	#Documentation: https://github.com/workhorsy/py-cpuinfo
	print(f"CPU Info: {cpuinfo.get_cpu_info()}")
#	print(f"CPU Info: {cpuinfo.get_cpu_info()['brand_raw']}")

	#Documentation: https://github.com/giampaolo/psutil/blob/master/README.rst
	print(f"psutil Info: {psutil.cpu_times()}")
	
	#Documentation: https://github.com/anderskm/gputil
	GPUs = GPUtil.getGPUs()
	for x in GPUs:
		print(f"GPU Name: {x.name}")
"""
	


if __name__ == "__main__":
	main()
