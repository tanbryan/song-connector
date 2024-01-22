from pydub import AudioSegment
from remove_silence import remove_silence

# 合并片段
def merge_audio(files_list):
    merged_audio = AudioSegment.empty()
    for file in files_list:
        audio = AudioSegment.from_mp3(file)
        audio2= remove_silence(audio, silence_thresh=-20)
        merged_audio += audio2
    return merged_audio
