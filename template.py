import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s :")


list_of_files = [
    "src/__init_.py",
    "src/crew/__init__.py",
    "src/crew/agent.py",
    "src/crew/tools.py",
    "src/crew/task.py",
    "src/main.py",
    ".env",
    "setup.py",
    "app.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename =os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating Directory : {filedir} for file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"creating empty file : {filepath}")
    else:
        logging.info(f"{filename} is already exist ")

             