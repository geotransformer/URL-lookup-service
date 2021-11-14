# URL-lookup-service
## Part 1 - URL lookup service

This is a small web service that responds to the following GET request.

```javascript
GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}
```

The JSON response contains information about that URL, i.e., is it safe to access that URL. The information is from the check against a local file consisting of known malware URLs.

```bash
curl localhost:8888/urlinfo/1/test2:8080/good?malware=true
```

```json
{"safe":false,"url":"test2:8080/good?malware=true"}
```

#### Setup

**1 Prerequisites**
- Docker
- Internet access

**2 Install**
- Checkout or download this git repository to the local development environment.

- In the URL-lookup-service directory, run install.sh to deploy the web service into a container.

  ```bash
  cloud-user@fasheng:~/URL-lookup-service$ ./install.sh 
  73623fe5d0ba
  Building
  Sending build context to Docker daemon  84.99kB
  Step 1/6 : FROM ubuntu:18.04
   ---> 5a214d77f5d7
  Step 2/6 : RUN mkdir -p /opt/run/url-lookup-service
   ---> Using cache
   ---> 7cb539d711c3
  Step 3/6 : RUN apt-get update      && apt-get install -y --no-install-recommends python3-flask python3-yaml      && apt-get clean
   ---> Using cache
   ---> 9916f9b50d8d
  Step 4/6 : WORKDIR /opt/run/url-lookup-service
   ---> Using cache
   ---> 2f8c04a96c3f
  Step 5/6 : COPY /bin/* /opt/run/url-lookup-service/
   ---> Using cache
   ---> d3ad19d37576
  Step 6/6 : CMD [ "python3", "/opt/run/url-lookup-service/app.py" ]
   ---> Using cache
   ---> c4c8b2e8eaa4
  Successfully built c4c8b2e8eaa4
  Successfully tagged url-lookup:latest
  Install
  fdf2b11722a54dd2d86582861eb7b31b403a3fc18bd9362c7eddfbcd5aadd30e
  CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                  PORTS                    NAMES
  fdf2b11722a5        url-lookup          "python3 /opt/run/ur…"   1 second ago        Up Less than a second   0.0.0.0:8888->8888/tcp   url-lookup
  ```
- The web service is listening on 8888 port by default. If there is a port conflict, change the port to an available port in the following two files.
```bash
bin/URLLookupService.py
install.sh
```
- To test the web service, use the curl command or the API client Postman or Insomnia. Try the urls in the config/malware_url.txt, it should return {"safe":false,"url":"xxxxxx"}. Any other urls, the response should be {"safe":true,"url":"xxxxxx"}

## Part 2 - Questions

Describe how you would accomplish the following:

1 The size of the URL list could grow infinitely. How might you scale this beyond the memory capacity of the system? 
- Scale up. Move to a more powerful machine with more memory and disk
- Scale out. Split the database into multiple partitions. Deploy multiple web service instances and to provide the service for different partitions. Add reverse proxy server to web services instances to cache the response and route the request to the mateched web service instance in need.

2 Assume that the number of requests will exceed the capacity of a single system, describe how might you solve this, and how might this change if you have to distribute this workload to an additional region, such as Europe. 
- scale up
- Scale out. Save the malware urls into a database management system. The web service connects to the database management system to check the URL. Deploy the stateless web service instances so that the instances numbers can be scaled in/out dynamically, based on the number of requests. Add a load balancer to distribute the request accordingly to the web service instances.
- Deploy the web service and the database into multiple datacenters, e.g., datacenter in North America, Europe, etc. Configure the database to replicate data across datacenters. Add a DNS-based traffic load balancer to distribute incoming requests from Europe to the web service instances in Europe.

3 What are some strategies you might use to update the service with new URLs? Updates may be as much as 5 thousand URLs a day with updates arriving every 10 minutes.
- Persist the update before updating the runtime 
- Add a message queue for the update request
- Database replication, only leader replica can write, the follower replica is read-only

4 [On-Call] You’re woken up at 3am, what are some of the things you’ll look for? Does that change anything you’ve done in the app?
- Recent change history
- Symptoms of the issue. Check the knowledge base for it. misconfiguration, human error, hardware issue
- Logs for the system to investigate what is the root cause
- A good system design and implementation can help to form a hypothesis about what's gone wrong. 

5 What are some considerations for the lifecycle of the app?
- Design with operability, scalability, reliability, and evolvability
- Ensure security within the lifecycle of the app
- Test-driven development, automated testing, and CI/CD 
- Responsive support 

6 You need to deploy a new version of this application. What would you do?
- Rolling deployment. No downtime for the service
- Canary deployments. New deployment might fail, but won't impact the whole system
- Blue-green deployment. Easy to roll back to the previous deployment

