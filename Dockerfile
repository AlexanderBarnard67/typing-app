FROM python:3.8-slim
WORKDIR /main
COPY venv /main
CMD ["python", "./main.py"]