from pytube import Playlist
from pytube import YouTube
import os
from pytube.cli import on_progress
link=input("enter youtube playlist url:")
yt_playlist=Playlist(link)

path="E:/youtube videos/testing"
# print(len(os.listdir(path)))

print(f"total {len(yt_playlist)} videos")

while len(os.listdir(path))!=len(yt_playlist):
    try:
        for video in yt_playlist.videos:
            
            video.register_on_progress_callback(on_progress)
            print(video.title)
            print(str(len(yt_playlist)-len(os.listdir(path))-1)+"  videos remaining to download from youtube playlist")
            video.streams.get_highest_resolution().download(path)
           

    except Exception as e:   
        print(e)
# try:
#     for video in yt_playlist.videos:
#         if len(os.listdir(path))!=len(yt_playlist):
#             print(video.title)
#             print(str(len(yt_playlist)-len(os.listdir(path))-1)+"  videos remaining to download from youtube playlist")
#             video.streams.get_highest_resolution().download(path)
#         elif len(os.listdir(path))==len(yt_playlist):
#             break

# except Exception as e:   
#     print(e)
    


print("\nAll videos are downloaded")


# # from pytube import YouTube ,helpers
# # # proxy_handler = {
# # #     "http": "127.0.0.1:20304",
# # #     'https': '127.0.0.1:20304'
# # # }
# # # helpers.install_proxy(proxy_handler)
# # link=input("link : ")
# # yt=YouTube(link)
# # print(yt.title)
# # video=yt.streams.get_highest_resolution().download()
# # # video.download('F:/python/extra/youtube videos')
# # # video.download()
# # print("done")

# # from pytube import Playlist, YouTube
# # playlist_url = 'https://www.youtube.com/playlist?list=PLHQRYFyK0L02C2zxIlPGOg9KM-XvRBZw0'
# # p = Playlist(playlist_url)
# # for url in p.video_urls:
# #     try:
# #         yt = YouTube(url)
# #     except VideoUnavailable:
# #         print(f'Video {url} is unavaialable, skipping.')
# #     else:
# #         print(f'Downloading video: {url}')
# #         yt.streams.first().download()