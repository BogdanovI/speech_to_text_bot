"""Module convert ogg voice message by the segment to wav format."""

import os
from pydub import AudioSegment

def transcoding_ogg_to_wav(path_to_file):
    """Function conver saved audio ogg file to wav."""
    if os.path.splitext(path_to_file)[1] != ".ogg":
        return "error"
    dest_song = os.path.splitext(path_to_file)[0]+'.wav'

    song = AudioSegment.from_ogg(path_to_file)
    song.export(dest_song, format="wav")
    return dest_song
