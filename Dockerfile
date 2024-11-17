FROM ubuntu:20.04

COPY sources.list /etc/apt/sources.list

WORKDIR /speech_to_text_bot

RUN apt-get update && \
    apt-get install -y \
                ffmpeg \
                python3 \
                python3-pip \
                git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]