"""
Project    makeFilesPhot.py |Environment    PyCharm
File_name   04_获取音频时长 |User    Pfolg
2024/7/7   18:05
"""
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.oggopus import OggOpus
from mutagen.oggvorbis import OggVorbis


def get_audio_duration(file_path):
    # 根据文件扩展名选择合适的mutagen类
    if file_path.endswith('.mp3'):
        audio = MP3(file_path)
    elif file_path.endswith('.flac'):
        audio = FLAC(file_path)
    elif file_path.endswith('.opus'):
        audio = OggOpus(file_path)
    elif file_path.endswith('.ogg'):
        audio = OggVorbis(file_path)
    else:
        raise ValueError("Unsupported audio format")

    # 获取音频时长（以秒为单位）
    md_duration = audio.info.length
    return md_duration


# 使用函数获取音频时长
audio_file_path = '.\\平行四界Quadimension,星尘 - I Really Want to Stay At Your House.mp3'
duration = get_audio_duration(audio_file_path)
print(f"The duration of the audio file is {duration} seconds.")
