From alpine:latest

RUN apk add --no-cache py-pip
RUN pip3 install --upgrade pip

COPY ./job-board /job-board
WORKDIR /job-board

RUN pip3 install -r requirements.txt

EXPOSE 5000

WORKDIR /job-board/demo-ui
ENTRYPOINT ["python3"]
CMD ["__init__.py"]