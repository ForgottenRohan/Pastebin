FROM python:3.12.4-slim

COPY requirments.txt requirments.txt
RUN pip install -r requirments.txt
COPY . .


CMD [ "fastapi", "run", "main.py" ]