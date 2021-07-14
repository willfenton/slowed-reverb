FROM python:3

RUN apt-get update && apt-get install -y \
    libsox-fmt-all \
    sox

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./slowed-reverb.py" ]
