FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN echo "Current Working Directory: $(pwd)"

CMD ["python", "main.py"]
