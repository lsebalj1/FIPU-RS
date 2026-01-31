FROM python:3.14-slim

WORKDIR /app

RUN pip install aiohttp

COPY main.py .

EXPOSE 8081

CMD ["python", "main.py"]