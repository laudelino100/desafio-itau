FROM python:3.6.8-alpine3.10
EXPOSE 8080
ARG consumer_key
ARG consumer_secret
ARG token_key
ARG token_secret
ENV consumer_key=$consumer_key
ENV consumer_secret=$consumer_secret
ENV token_key=$token_key
ENV token_secret=$token_secret

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./twitter_analysis.py" ]
