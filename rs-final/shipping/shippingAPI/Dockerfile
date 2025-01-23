FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t shippingapi:1.0 .
# docker run --name shippingapi -p 8000:8000 shippingapi:1.0