import subprocess
import webbrowser
import time
import os

def start_mern_stack():

    # Change directory to MERN stack project directory
    project_path = input("Enter Path to your project:\n")
    os.chdir(project_path)

    # Start Node.js server
    node_process = subprocess.Popen(["npm", "start"], cwd=f"{project_path}/server", shell=True)

    # Start React server
    react_process = subprocess.Popen(["npm", "start"], cwd=f"{project_path}/client", shell=True)

    # Wait for the servers to start
    time.sleep(20)

    # Open the web page in a browser
    webbrowser.open("http://localhost:5173")

    a = 0
    while a != 1:
        a = int(input("Servers have been started. Press 1 to kill the process"))
    else:
        node_process.terminate()
        react_process.terminate()

if __name__ == "__main__":
    start_mern_stack()
