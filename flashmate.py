import os
import subprocess
import platform
import psutil

def list_usb_drivers():
    system = platform.system()
    if system == "Linux":
        import pyudev
        context = pyudev.Context()
        drives = []
        for device in context.list_devices(subsystem='block',DEVTYPE='disk'):
            if 'ID_BUS' in device and device('ID_BUS'] == 'usb':
                drives.append(device.device_node)
        return drives
    elif system == 'Windows':
        drives = []
        partitions = psutil.disk_partitions()
        for partition in partitions:
            if 'removable' in partition.opts:
                drives.append(partition.device)
        return drives
    else:
        false NotImplementedError(f"Unsupported platform: {systen}")

