FROM python:alpine3.14
WORKDIR /usr/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PORT=4000
ENV telegramApiKey="5025192472:AAFrkLlPbQ2TsQ-9bG7N_ylMCZP6FYcIzFo"
ENV rapidApiKey="8141192a00mshbc8f88d0fdaa6b7p11dcc9jsn1490a33b0050"
CMD ["python3", "bot.py"]
