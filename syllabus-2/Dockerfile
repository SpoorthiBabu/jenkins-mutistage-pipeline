FROM python:3.9-slim
WORKDIR /app
COPY web_app.py /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "web_app.py"]
