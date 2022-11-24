docker rmi -f $(docker images -aq)
docker rm -f $(docker ps -a -q)
docker rmi coin
docker image build -t coin /home/ec2-user/coin
docker run -d -p 80:80 coin
