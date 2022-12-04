FROM python:latest

COPY . /HWM3

WORKDIR /HWM3

ENTRYPOINT ["python"]
CMD ["bot.py"]