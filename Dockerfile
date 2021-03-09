FROM python:3.6.12-slim-buster
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV PORT 50051
CMD python greeter_server.py
