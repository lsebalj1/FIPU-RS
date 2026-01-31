FROM python:3.14-slim

WORKDIR /app

RUN pip install fastapi uvicorn "pydantic[email]" python-multipart

COPY main.py models.py .
COPY routes/ routes/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]