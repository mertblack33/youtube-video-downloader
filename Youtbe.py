import pytube

video_url = 'https://www.youtube.com/watch?v=2RAbPC9aKQ0&list=RDJIO9WevEOtA&index=2&ab_channel=Motive'

yt = pytube.YouTube(video_url)

print(yt.title)
lk = yt.streams.filter()
for i in lk:
    print(i)
#video =yt.streams.get_by_itag(140)
#video.download("./")