FROM registry.opensource.zalan.do/stups/python:3.5.1-17

WORKDIR /opt

COPY apps /opt/apps
RUN pip3 install -r /opt/apps/requirements.txt

WORKDIR /opt/apps
CMD ["uwsgi","--http",":8080","-w","app"]
