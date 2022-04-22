FROM python:alpine3.14
WORKDIR /usr/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PORT=4000
CMD ["python3", "bot.py"]
