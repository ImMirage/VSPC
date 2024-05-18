import os
import ctypes
import sys  # Prevents PyCache
sys.dont_write_bytecode = True  # Line above explains.
from getpass import getuser
from traceback import format_exc
from modules.logging import logging

class VSPC:
    def __init__(self, project_directory: str = None):
        self.project_directory = project_directory
    
    def setup(self):
        if not os.path.exists(self.project_directory):
            os.makedirs(self.project_directory)
    
    def start(self):
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(f"VSPC | User: {getuser()} | VSPC Directory: {os.getcwd()} | Creator: @Sacrifice")
            if not self.project_directory:
                logging.info("You must set a project directory!")
                return
            
            project_name = input("Enter your project name > ")
            file_name = input("Enter the main file name > ")
            if not project_name:
                logging.error("Your project name cannot be empty!")
                return
            if not file_name:
                logging.error("Your main file name cannot be empty!")
                return
                
            if "." not in file_name:
                logging.error("The file must have an extension! Example: (main.py)")
                return
                
            project_path = os.path.join(self.project_directory, project_name)
            if not os.path.exists(project_path):
                os.makedirs(project_path)
                
                with open(os.path.join(project_path, file_name), 'w') as f:
                    pass
                
                logging.info(f"Directory and file created: {project_path} | {file_name}")
                logging.info("Loading VSCode...")
                os.system(f'code {project_path}')
            else:
                logging.info(f"Directory already exists: {project_path}")
        except Exception as e:
            logging.error(format_exc())

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    vspc = VSPC(project_directory="./projects")
    vspc.setup()
    vspc.start()