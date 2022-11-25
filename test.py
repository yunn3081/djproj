from kkbox_developer_sdk.auth_flow import KKBOXOAuth
import requests
import json
import time
from datetime import datetime

# class ClientInfo():
#     client_id = "ff0f283b37d7e3544c29eb274f80617c"
#     client_secret = "b62b7214891171ec6b478368c3b9642f"

# auth = KKBOXOAuth('ff0f283b37d7e3544c29eb274f80617c', 'b62b7214891171ec6b478368c3b9642f')
# token = auth.fetch_access_token_by_client_credentials()

# from kkbox_developer_sdk.api import KKBOXAPI
# kkboxapi = KKBOXAPI(token)
# # artist_id = '8q3_xzjl89Yakn_7GB'
# # artist = kkboxapi.artist_fetcher.fetch_artist(artist_id)
# # print(artist)

# search_results = kkboxapi.search_fetcher.search('workout', types=['playlist'], terr='TW')
# playlists = search_results['playlists']['data']

# first = playlists[0]
# from pprint import pprint
# pprint(first, depth=2)

# tracks_paging = kkboxapi.shared_playlist_fetcher.fetch_tracks_of_shared_playlists('Otv4S0erPHGatlMkoJ')
# tracks = tracks_paging['data']
# pprint(tracks, depth=2)

# KKBOX華語新歌日榜
url = "https://kma.kkbox.com/charts/api/v1/daily?category=297&lang=tc&limit=50&terr=tw&type=newrelease"
# 取得歌曲資訊json檔
response = requests.get(url)
# 將json字串轉為Python的字典型態
data = json.loads(response.text)

song_list = data["data"]["charts"]["newrelease"]
my_dict={}

# 取得每首歌的排名、曲名、連結、作者、時間
for song in song_list:
    song_rank = song["rankings"]["this_period"]
    song_name = song["song_name"]
    song_url = song["song_url"]
    song_artist = song["artist_name"]
    song_timestamp = int(song["release_date"])
    # 從timestamp轉為日期格式
    song_date = time.strftime(
        "%Y-%m-%d", time.localtime(song_timestamp))

    # print("排名:", song_rank)
    # print("歌名:", song_name)
    # print("連結:", song_url)
    # print("作者:", song_artist)
    # print("發行日期:", song_date)



# song_rank = song_list[0]["rankings"]["this_period"]
# song_name = song_list[0]["song_name"]
# song_url = song_list[0]["song_url"]
# song_artist = song_list[0]["artist_name"]
# song_timestamp = int(song_list[0]["release_date"])
# song_date = time.strftime(
#         "%Y-%m-%d", time.localtime(song_timestamp))
# print("排名:", song_rank)
# print("歌名:", song_name)
# print("連結:", song_url)
# print("作者:", song_artist)
# print("發行日期:", song_date)

    musicdetail = {'song_rank': song_rank, 'song':song_name, 'singer':song_artist, 'release_date':song_date}
    my_dict[song_name] = musicdetail


data = my_dict
# print(data)
for item in data.items():
    ranking = item[1]['song_rank']
    song = item[1]['song']
    singer = item[1]['singer']
    release_date = item[1]['release_date']

    # print(song_rank, song, singer, release_date)
    print(song_name)

# print(my_dict)