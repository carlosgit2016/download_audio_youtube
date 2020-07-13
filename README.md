# Download Audio Youtube
Simple way to download mp3 from youtube videos

## Pre-requisites
[Docker Desktop](https://docs.docker.com/desktop/) or [Docker Engine](https://docs.docker.com/engine/) installed

## How to use
Pull docker image
```
docker pull carlosflor25/download_audio_youtube:latest
```
Just run using the following command
```
docker run -it --rm -v c:\users\myuser\music:/usr/audios download_audio_youtube "https://www.youtube.com/watch?v=YnU2kGGyalE"
```
The audios are downloaded in the path `/usr/audios`, you can use bind mount how the example above or create a [volume](https://docs.docker.com/engine/reference/run/#volume-shared-filesystems).
## How this works
This image use python [pafy](https://pypi.org/project/pafy/) to download the best audio available and convert to mp3 using [ffmpeg](https://ffmpeg.org/)
