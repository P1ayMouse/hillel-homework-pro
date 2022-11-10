FROM ubuntu
RUN apt-get update; apt-get install -y python3 python3-pip

WORKDIR /flask_app
COPY . .

RUN pip install flask==2.2.2

ENTRYPOINT ["python3"]
CMD ["flask_application.py"]