import subprocess
import sys

DEFAULT_PACKAGES = ['psutil', 'requests']

def banner():
    print (" +------------------------------------------------------------------------------+")
    print (" | ███████╗██╗      █████╗ ███████╗██╗  ██╗███╗   ███╗ █████╗ ████████╗███████╗ |")
    print (" | ██╔════╝██║     ██╔══██╗██╔════╝██║  ██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝ |")
    print (" | █████╗  ██║     ███████║███████╗███████║██╔████╔██║███████║   ██║   █████╗   |")
    print (" | ██╔══╝  ██║     ██╔══██║╚════██║██╔══██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝   |")
    print (" | ██║     ███████╗██║  ██║███████║██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗ |")
    print (" | ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ |")
    print (" +------------------------------------------------------------------------------+")

def install_default_packages():
    installed_packages = []
    failed_packages = []
    try:
        for package in DEFAULT_PACKAGES:
            print(f"[+] Installing package: {package}")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                installed_packages.append(package)
            except subprocess.CalledProcessError:
                failed_packages.append(package)

        print("[+] Default packages installation summary:")
        if installed_packages:
            print("[+] Installed packages:")
            for package in installed_packages:
                print(f"  - {package}")
        if failed_packages:
            print("[+] Failed to install packages:")
            for package in failed_packages:
                print(f"  - {package}")
        if not installed_packages and not failed_packages:
            print("[+] No packages were installed.")

    except Exception as e:
        print(f"[!] An error occurred while installing packages: {e}")

if __name__ == "__main__":
    banner()
    install_default_packages()
