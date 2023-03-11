FROM python:3.11-alpine
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:5000", "app:app"]
