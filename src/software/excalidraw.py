import subprocess
import os

def save ():
    try :
        path = os.getenv("OBSIDIAN_PATH_FILE_SAVE")
        subprocess.call(["sh", path])
        return "Excalidraw salvo com sucesso!"
    except Exception as e:
        return str(e)