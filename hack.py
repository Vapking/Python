import subprocess
cmdCommand = "shutdown -h now"
process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
