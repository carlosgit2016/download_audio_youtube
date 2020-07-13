FROM python:latest

COPY download_audio_youtube.py /usr/youtube/download_audio_youtube.py

RUN apt-get update && \
	apt-get -y install software-properties-common apt-utils && \
	add-apt-repository ppa:mc3man/trusty-media && \
	apt-get -y install ffmpeg 
	
RUN pip install youtube-dl && \
	pip install pafy

WORKDIR /usr/audios
ENTRYPOINT ["python", "/usr/youtube/download_audio_youtube.py"]