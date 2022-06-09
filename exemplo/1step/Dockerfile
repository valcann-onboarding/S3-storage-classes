FROM alpine:latest
LABEL maintainer="Matheus Silva <malvesa@valcann.com.br>" 

ARG BUCKET_NAME
ARG SUBLOT_TAG

RUN apk --no-cache add \ 
      bash \
      curl \
      less \
      groff \
      jq \
      git \
      python3 \
      py3-pip \
      py-pip && \
      pip install --upgrade pip awscli s3cmd && \
      mkdir /root/.aws

WORKDIR /valcann

COPY ./sublots/ .
COPY ./restore_object.py .

CMD ["python3", "restore_object.py"]