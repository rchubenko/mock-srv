FROM python:3.11-slim
WORKDIR /opt
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "mock_server.py"]
