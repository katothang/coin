docker rm -f $(docker ps -a -q)
docker rmi coin
docker image build -t coin /root/coin
docker run coin