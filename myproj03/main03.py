import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
# for song_dick in song_list:
#     title: str = song_dick["title"]
#     title_lenght = len(title)
#     print(title, title_lenght)


def get_title_and_length_for_song(song_dict):
    title: str = song_dict["title"]
    return [title, len(title)]


for title, length in map("get_title_and_length_for_song, song list"):
    print(title, length)

# 방탄소년단의 노래에 대해서만, 곡명과 곡명의 글자수를 출력
for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        title: str = song_dict["title"]
        bts_list.append([title, len(title)])

for title, lenght in bts_list:
    print(title, length)


def check_bts_song(song_dict):
    return song_dict["artist"] == "방탄소년단"


for title, lenght in map(
    get_title_and_lenght_for_song, filter(check_bts_song, song_list)
):
    print(title, length)
