import os
import csv
import tabulate
import platform
import psutil
import cpuinfo
import GPUtil
import diskinfo

def main():
	#Path to the dataset.
	path = f"{os.getcwd()}/data_Q3_2023/data_Q3_2023/"
	#List to hold lists which have data of every file.
	superList = []
	
	#For every csv file in the dataset...
	for csvfile in os.listdir(path):
		#Open the file, get the header, then contents in a clean and iteratble format.
		file = open(path + csvfile)
		header = next(file).split(',')
		contents = list(csv.reader(file, delimiter=','))

		#Notable SMART attribute indicators for failure (i.e. these are the indexes for searching the dataset).
		MODEL 			= header.index("model")
		FAILURE			= header.index("failure") 
		REALLOC_SEC_COUNT 	= header.index("smart_5_raw")
		WEAR_LEVEL_COUNT 	= header.index("smart_173_raw")
		ERASE_FAIL_COUNT 	= header.index("smart_176_raw")
		PENDING_SEC_COUNT 	= header.index("smart_197_raw")
		UNCORRECTABLE_SEC_COUNT = header.index("smart_198_raw")
		DRIVE_TEMP 		= header.index("smart_231_raw")
			
		#For every row in the file's contents...
		for row in contents:
			fileList = []

			fileList.append(row[MODEL]) 			#Store model
			fileList.append(row[FAILURE]) 			#Store its failure status
			fileList.append(row[REALLOC_SEC_COUNT]) 	#Store its wear leveling count
			fileList.append(row[WEAR_LEVEL_COUNT]) 		#Store its wear leveling count
			fileList.append(row[ERASE_FAIL_COUNT]) 		#Store its erase failure count
			fileList.append(row[PENDING_SEC_COUNT]) 	#Store its current pending sector count
			fileList.append(row[UNCORRECTABLE_SEC_COUNT]) 	#Store its uncorrectable secotors count
			fileList.append(row[DRIVE_TEMP]) 		#Store its drive temperature

		superList.append(fileList)
	
	print(superList)

"""
	#Demo code for platform, psutil, cputil, GPUtil, and diskinfo modules.

	#Documentation: https://docs.python.org/3/library/platform.html
	print("Platform Module Info:")
	print(f"Machine: 	{platform.machine()}")
	print(f"Architecture: 	{platform.architecture()}")
	print(f"Node: 		{platform.node()}")
	print(f"Platform: 	{platform.platform()}")
	print(f"Processor: 	{platform.processor()}")
	print(f"Release: 	{platform.release()}")
	print(f"System: 	{platform.system()}")
#	print(f"System Alias: 	{platform.system_alias(TODO 3 parameters needed)}")
	print(f"Version: 	{platform.version()}")
	print(f"UName: 		{platform.uname()}")
	print(f"UName Core:	{platform.uname().processor}")
	#Among others
	
	#Documentation: https://github.com/giampaolo/psutil/blob/master/README.rst
	print("\nPSUtil Module Info:")
	print(f"psutil Info: 		{psutil.cpu_times()}")
	print(f"CPU (Logical) Cores: 	{psutil.cpu_count()}")
	print(f"CPU Cores: 		{psutil.cpu_count(logical=False)}")
	print(f"CPU Freq: 		{psutil.cpu_freq()}")
	print(f"Virt Mem: 		{psutil.virtual_memory()}")
	print(f"Swap Mem: 		{psutil.swap_memory()}")
	print(f"Swap Mem: 		{psutil.disk_partitions()}")
	print(f"Disk Usage: 		{psutil.disk_usage('/')}")
	print(f"Disk IO: 		{psutil.disk_io_counters(perdisk=False)}")
	print(f"Sensor Temps: 		{psutil.sensors_temperatures()}")
	#Among others

	#Documentation: https://github.com/workhorsy/py-cpuinfo
	print("\nCPUtil Module Info:")
	print(f"CPU Vendor: 		{cpuinfo.get_cpu_info()['vendor_id_raw']}")
	print(f"CPU Brand: 		{cpuinfo.get_cpu_info()['brand_raw']}")
	print(f"CPU Model: 		{cpuinfo.get_cpu_info()['model']}")
	print(f"CPU Family: 		{cpuinfo.get_cpu_info()['family']}")
	print(f"CPU Freq (Advertised): 	{cpuinfo.get_cpu_info()['hz_advertised_friendly']}")
	print(f"CPU Freq (Real): 	{cpuinfo.get_cpu_info()['hz_actual_friendly']}")
	print(f"CPU Core Count: 	{cpuinfo.get_cpu_info()['count']}")
	#Among others
	
	#Documentation: https://github.com/anderskm/gputil
	print("\nGPUtil Module Info:")
	GPUs = GPUtil.getGPUs()
	for gpu in GPUs:
		print(f"GPU Name: 	{gpu.name}")
		print(f"GPU Load: 	{gpu.load}")
		print(f"GPU Mem Util: 	{gpu.memoryUtil}")
		print(f"GPU Mem Total: 	{gpu.memoryTotal}")
		print(f"GPU Mem Used: 	{gpu.memoryUsed}")
		print(f"GPU Mem Free: 	{gpu.memoryFree}")
		print(f"GPU Driver: 	{gpu.driver}")
		print(f"Display Mode: 	{gpu.display_mode}")
		print(f"Displa Active: 	{gpu.display_active}")
		#Among others
	
	#Documentation: https://diskinfo.readthedocs.io/en/latest/intro.html#how-to-use
	print("\nDiskinfo Module Info:")
	disks = diskinfo.DiskInfo()
	for disk in disks.get_disk_list(sorting=True):
		if ("sd" in disk.get_name()):
			print(f"Disk Name: {disk.get_name()}")
			print(f"Disk Path: {disk.get_path()}")
			print(f"Disk Model: {disk.get_model()}")
			print(f"Disk Type: {disk.get_type()}")
			print(f"Disk Size: {disk.get_size()}")
			print(f"Disk Device ID: {disk.get_device_id()}")
#			print(f"Disk Temp: {disk.get_temperature()}") #Only works if drive is NVME
			print(f"SMART Data: {disk.get_smart_data(sudo='sudo')}")
			print(f"Disk Health: {disk.get_smart_data(sudo='sudo').healthy}")
			#Among others			
	"""

if __name__ == "__main__":
	main()
