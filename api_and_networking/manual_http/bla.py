import os 
import subprocess
response = subprocess.run(
    ["bash","-c","curl http://localhost:58954/"],
    text = True,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)
print(response.stdout)
