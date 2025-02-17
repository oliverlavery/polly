FROM python:latest

RUN pip --no-cache-dir install \
	slackbot

COPY app /app
COPY run.sh /run.sh
COPY requirements.txt /requirements.txt

ARG TINI_VERSION=v0.18.0
RUN apt-get update && apt-get install -y nmap
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT [ "/usr/bin/tini", "--" ]

CMD ["/bin/sh", "/run.sh"]
