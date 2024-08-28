import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="textsummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",  #hidden file; empty folder won't be uploaded on commit; can be deleted later
    f"src/{project_name}/__init__.py", #constructor is used to import components as a local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]
#Splitting filepath into dir and file, creating file directory path and filepath 
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info("Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating emplty file: {filepath} ")

    else:
        logging.info("f{filename} already exists")