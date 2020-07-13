import os
import sys
import pafy

videoUrl = sys.argv[1]
video = pafy.new(videoUrl)
bestAudio = video.getbestaudio()
print("Best audtio founded: ", bestAudio.bitrate, bestAudio.extension, bestAudio.filename)
print("Downloading................")
bestAudio.download()
# bestAudioFileName = "".join(str(bestAudio.filename).split())
# os.rename(bestAudio.filename, bestAudioFileName)
print("Downloading................OK")
print("Converting to MP3................")
inputFile = str(bestAudio.filename)
# bestAudioTitle = "".join(str(bestAudio.title).split())
outputFileMp3 = str(bestAudio.title) + ".mp3"
command = f"ffmpeg -i \"{inputFile}\" -vn -ar 44100 -ac 2 -b:a 192k \"{outputFileMp3}\""
os.system(command)
print("Deleting file................")
os.remove(inputFile)
print("Deleting file................OK")