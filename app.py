from pytube import YouTube


video: str = input("Digite o link do vídeo o Youtube: ")
yt = YouTube(video)
print("Start Download")
video = yt.streams.get_highest_resolution()
video.download()
print("Fininsh Download...")
