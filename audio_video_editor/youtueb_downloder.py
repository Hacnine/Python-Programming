import pytube
urls = input('Give an url: ')
youtube = pytube.YouTube(urls)
stream = youtube.streams.all()
# for i in stream:
#     print(i)
# https://www.youtube.com/watch?v=Q--H5uqHP5s
video = youtube.streams.get_by_itag(136)
video.download()
print('Video is downloaded')
