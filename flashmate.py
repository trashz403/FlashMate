from drivepy.main import DrivePy

iso_path = input("Enter the path to the ISO file : ")

DrivePy.flash_iso(iso_path, usb_drive)
DrivePy.make_bootable(usb_drive)
