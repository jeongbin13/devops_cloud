# 문제
# artist 글자수가 3글자 이상인 곡에 대해서
# 좋아요 수와 제목글자수의 곱을 출력

# 1) for/if로 구현

# 2) filter/map 위주로 구현
"""
"""
from pprint import pprint
from typing import List  # Type Hinting
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
"""
"artist"의 글자수가 3글자 이상으로 구성된 리스트를 만들어보세요.
"""
value_list: List[dict] = []
for song_dict in song_list:
    artist: str = song_dict["artist"]
    if len(artist) >= 3:
        value: int = song_dict["like"] * len(song_dict["title"])
        value_list.append

for song_dict in value_list:
    print(value_list)
