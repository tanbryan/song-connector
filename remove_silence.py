
# 用于移除音频文件中的静音部分。
from pydub import AudioSegment
from pydub.silence import split_on_silence

def remove_silence(audio_path, silence_thresh=-50, min_silence_len=500):
    """
    移除音频文件中的静默部分。
    
    参数:
    audio_path: 音频文件的路径。
    silence_thresh: 静默的阈值（分贝）。
    min_silence_len: 被认为是静默的最小长度（毫秒）。
    
    处理后的音频文件的路径。
    """
    try:
        # 加载音频文件
        audio = AudioSegment.from_file(audio_path)

        # 分割音频，移除静默部分
        chunks = split_on_silence(audio, silence_thresh=silence_thresh, min_silence_len=min_silence_len)

        # 重新连接音频片段
        processed_audio = AudioSegment.silent(duration=0)
        for chunk in chunks:
            processed_audio += chunk

        # 保存处理后的音频
        output_path = audio_path.replace('.mp3', '_no_silence.mp3')
        processed_audio.export(output_path, format='mp3')

        return output_path

    except Exception as e:
        print(f"Error processing file {audio_path}: {e}")
        return None
