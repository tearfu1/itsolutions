FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update -y \
    && apt-get install ffmpeg -y \
    && apt-get install imagemagick -y

RUN > /etc/ImageMagick-6/policy.xml

COPY . .

CMD ["python", "itsolutions/manage.py", "runserver", "0.0.0.0:8000"]
