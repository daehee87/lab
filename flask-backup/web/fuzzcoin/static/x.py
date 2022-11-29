import os, sys, time, subprocess

host = os.getenv("H")
port = os.getenv("P")
token = os.getenv("T")

# check if this is first run
if os.path.isdir("./fuzzcoin-worker"):
    print("you already setup/configured the client.")
    print("cd into `fuzzcoin-worker` and run `./run.sh` to start fuzzing")
    os._exit(0)

try:
    docker = subprocess.check_output(["docker", "--version"])
    print("your docker version: %s (recommended 18.09+)" % docker)
except:
    os.system("sudo apt-get install -y docker.io || sudo yum install -y docker")

# install git
os.system("sudo apt-get install -y git || sudo yum install -y git")
# clone fuzzcoin client
os.system("git clone https://gl.gtisc.gatech.edu/ammar/fuzzcoin-worker.git")

# setup config file
with open("fuzzcoin-worker/fuzzcoin.conf", "w") as f:
    f.write("HOST=%s\n" % host)
    f.write("PORT=%s\n" % port)
    f.write("TOKEN=%s\n" % token)

print("\n\n\n\n\n\n\n\n")
print("Install complete. cd into `fuzzcoin-worker` and run `./run.sh`")
