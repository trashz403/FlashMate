import os
import subprocess
import platform
import psutil

def list_usb_drives():
    system = platform.system()
    if system == 'Linux':
        import pyudev
        context = pyudev.Context()
        drives = []
        for device in context.list_devices(subsystem='block', DEVTYPE='disk'):
            if 'ID_BUS' in device and device['ID_BUS'] == 'usb':
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
        raise NotImplementedError(f"Unsupported platform: {system}")

def unmount_drive(drive):
    system = platform.system()
    if system == 'Linux':
        subprocess.run(['umount', drive], check=True)
    elif system == 'Windows':
        subprocess.run(['diskpart', '/s', f"""
        select volume {drive.strip(':')}
        remove
        """.strip()], shell=True, check=True)

def flash_iso_to_usb(iso_path, usb_drive):
    system = platform.system()
    if system == 'Linux':
        subprocess.run(['dd', f'if={iso_path}', f'of={usb_drive}', 'bs=4M', 'status=progress', 'conv=fdatasync'], check=True)
    elif system == 'Windows':
        # Using `dd` for Windows from https://www.chrysocome.net/dd
        dd_path = 'path/to/dd.exe'  # Adjust this to where dd.exe is located
        subprocess.run([dd_path, f'if={iso_path}', f'of=\\.\{usb_drive.strip(":")}', 'bs=4M', '--progress'], check=True)

def main():
    print("Detecting USB drives...")
    usb_drives = list_usb_drives()
    
    if not usb_drives:
        print("No USB drives detected.")
        return

    print("Available USB drives:")
    for idx, drive in enumerate(usb_drives, 1):
        print(f"{idx}: {drive}")

    drive_index = int(input("Select the USB drive index to flash the ISO to: ")) - 1
    usb_drive = usb_drives[drive_index]

    iso_path = input("Enter the path to the ISO file: ")

    print(f"Unmounting {usb_drive}...")
    unmount_drive(usb_drive)

    print(f"Flashing {iso_path} to {usb_drive}...")
    flash_iso_to_usb(iso_path, usb_drive)

    print("ISO flashing complete.")

if __name__ == "__main__":
    main()
      
