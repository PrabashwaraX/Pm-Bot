FROM python:latest
 
WORKDIR /bot
COPY . /bot
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "bot"]
