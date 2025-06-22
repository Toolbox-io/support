FROM python:3

RUN curl -fsSL https://ollama.com/install.sh | sh
RUN ollama serve & sleep 10 && ollama pull llama3:8b

WORKDIR /root
COPY requirements.txt /root/
RUN python3 -m venv .venv && \
    ./.venv/bin/pip3 install -r requirements.txt && \
    rm requirements.txt

COPY . /root/model
WORKDIR /root/model

LABEL org.opencontainers.image.source="https://github.com/Toolbox-io/support"
LABEL org.opencontainers.image.description="A custom LLM built to support users of Toolbox.io"

ENTRYPOINT ["bash", "-c", "ollama serve & /root/.venv/bin/python3 main.py"]