FROM alpine:3.6

LABEL maintainer="adil.mouhssine@gmail.com" \
      description="Base image from alpine for all python container." \
      version="0.1"

# Python
RUN apk add --no-cache python3 \
  && if [[ ! -e /usr/bin/python ]];        then ln -sf /usr/bin/python3 /usr/bin/python; fi \
  && if [[ ! -e /usr/bin/python-config ]]; then ln -sf /usr/bin/python3-config /usr/bin/python-config; fi \
  && if [[ ! -e /usr/bin/idle ]];          then ln -sf /usr/bin/idle3 /usr/bin/idle; fi \
  && if [[ ! -e /usr/bin/pydoc ]];         then ln -sf /usr/bin/pydoc3 /usr/bin/pydoc; fi \
  && if [[ ! -e /usr/bin/easy_install ]];  then ln -sf /usr/bin/easy_install-3* /usr/bin/easy_install; fi \
  && easy_install pip \
  && pip install --upgrade pip \
  && if [[ ! -e /usr/bin/pip ]]; then ln -sf /usr/bin/pip3 /usr/bin/pip; fi

# User and group
ARG USER
ARG GROUP
ARG WORKDIR
ENV USER=${USER:-aslm} GROUP=${GROUP:-aslm}

RUN addgroup -S ${GROUP} && adduser -S -g ${USER} ${GROUP}

RUN apk add --no-cache --virtual build_deps python3-dev ca-certificates libffi-dev gcc g++ musl-dev linux-headers tzdata \
      && cp /usr/share/zoneinfo/America/New_York /etc/localtime \
      && echo "America/New_York" > /etc/timezone \
      && apk del build_deps \
      && rm -r /root/.cache

RUN mkdir -p /${WORKDIR:-app}/logs