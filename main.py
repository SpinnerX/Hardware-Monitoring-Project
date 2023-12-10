import platform
import psutil
import cpuinfo
import GPUtil

def main():
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
	print(f"CPU Info: {cpuinfo.get_cpu_info()}");

	#Documentation: https://github.com/giampaolo/psutil/blob/master/README.rst
	

	#Documentation: https://github.com/anderskm/gputil
	


if __name__ == "__main__":
	main()
