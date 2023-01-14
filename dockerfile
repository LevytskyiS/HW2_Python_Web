FROM python:3.9

COPY . /HWM3

WORKDIR /HWM3

ENTRYPOINT ["python"]
CMD ["bot.py"]