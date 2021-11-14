#! /bin/bash
docker rm -f $(docker ps -a -f name=url-lookup -q) || true
echo "Building" 
docker build -t url-lookup .

echo "Install"
docker run -d --name url-lookup -v $(pwd)/config:/opt/run/url-lookup-service/config -p 8888:8888 url-lookup
docker ps -a -f name=url-lookup
