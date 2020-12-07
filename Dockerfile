FROM continuumio/miniconda:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
RUN apt-get update && apt-get upgrade -y && apt-get install -qqy wget

RUN curl -sL https://deb.nodesource.com/setup_13.x | bash - && apt-get install -y nodejs && apt-get install -y npm

# Backend
RUN mkdir -p /backend
COPY ./backend/requirements.yml /backend/requirements.yml
RUN /opt/conda/bin/conda env create -f /backend/requirements.yml
ENV PATH /opt/conda/envs/backend-motion/bin:$PATH

ENV PYTHONDONTWRITEBYTECODE 1
RUN echo "source activate backend-motion" >~/.bashrc

COPY ./scripts /scripts
RUN chmod +x ./scripts*

# Frontend
#
#RUN mkdir -p /frontend_tmp
#RUN mkdir -p /frontend
#WORKDIR /frontend_tmp
#COPY ./frontend/package.json /frontend_tmp/
#COPY ./frontend/package-lock.json /frontend_tmp/
#RUN npm install
#COPY ./frontend /frontend_tmp
#RUN npm run build

COPY backend /backend
WORKDIR /backend
