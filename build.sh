ID="$(basename $PWD)"
mkdir corpus 2>/dev/null
sudo docker build -t "web-$ID" .
sudo docker rm -f "web-$ID-nick"
# add --cap-add=SYS_PTRACE --security-opt seccomp=unconfined to debug nginx
sudo docker run --security-opt \
                seccomp=unconfined \
                -v $PWD/out:/out \
                -p 4000:4000/tcp \
                --name "web-$ID-nick" \
                -it \
                "web-$ID"
 
