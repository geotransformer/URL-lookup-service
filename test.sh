#! /bin/bash
docker rm -f $(docker ps -a -f name=url-lookup -q) || true
echo "Building" 
docker build -t url-lookup .

echo "Run"

docker run -d --name url-lookup --rm -v $(pwd)/config:/opt/run/url-lookup-service/config -p 5003:5003 url-lookup

sleep 5

echo "Testing"
curl localhost:5003/healthy
curl localhost:5003/urlinfo/1/test2:8080/good?malware=true
curl "localhost:5003/urlinfo/1/test2:8080/good?malware=true&safe=false"
curl localhost:5003/urlinfo/1/test3:8080

