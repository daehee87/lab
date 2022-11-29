import os, sys, time, subprocess

L = os.getenv("LIST")
C = os.getenv("CPUS")
A = os.getenv("AUTO")
URL = "https://fuzzcoin.kr/static/tmp/%s" % L

# get fuzzing pool list
data = subprocess.check_output(["curl", "-s", URL])
pools = data.strip().split("\n")

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
os.system(
    "git clone https://gl.gtisc.gatech.edu/daehee/fuzzcoin-worker2.git fuzzcoin-worker"
)

# setup config file
with open("fuzzcoin-worker/fuzzcoin.conf", "w") as f:
    i = 0
    for pool in pools:
        f.write("HOST[%d]=%s\n" % (i, pool.split("H=")[1].split(" ")[0].strip()))
        f.write("PORT[%d]=%s\n" % (i, pool.split("P=")[1].split(" ")[0].strip()))
        f.write("TOKEN[%d]=%s\n" % (i, pool.split("T=")[1].split(" ")[0].strip()))
        i += 1

    # put CPU usage rate
    f.write("CPUS=%s\n" % str(float(C) / 100.0))

# make crontab entry
if A == "auto":
    print("adding crontab entry")
    cmd = ""
    cmd += "sudo crontab -l > /tmp/z;"
    cmd += 'echo "@reboot `pwd`/fuzzcoin-worker/autorun.sh" >> /tmp/z;'
    cmd += "sudo crontab /tmp/z; rm /tmp/z"
    os.system(cmd)

print("\n\n\n\n\n\n\n\n")
print("Install complete. cd into `fuzzcoin-worker` and run `./run.sh`")
