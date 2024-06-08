import subprocess
import sys

def install_packages(requirements_file):
    try:
        with open(requirements_file, 'r') as file:
            packages = file.readlines()
        
        for package in packages:
            package = package.strip()
            if package:
                print(f"Installing package: {package}")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        
        print("All packages installed successfully.")
    
    except FileNotFoundError:
        print(f"The file {requirements_file} does not exist.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")

if __name__ == "__main__":
    requirements_file = 'requirements.txt'
    install_packages(requirements_file)
