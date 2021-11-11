FROM ubuntu:18.04

RUN mkdir -p /opt/run/url-lookup-service
RUN apt-get update \
     && apt-get install -y --no-install-recommends python3-flask python3-yaml \
     && apt-get clean

WORKDIR /opt/run/url-lookup-service
COPY /bin/* /opt/run/url-lookup-service/

CMD [ "python3", "/opt/run/url-lookup-service/app.py" ]

