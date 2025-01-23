FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]

# docker build -t usersapi:1.0 .
# docker run --name usersapi -p 8080:8080 usersapi:1.0