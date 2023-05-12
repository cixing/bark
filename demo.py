from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
# from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
     你好，我叫张小华。你有什么问题需要问我吗？今天的天气看起来不错[laughs]，要一起出去玩吗？
"""
audio_array = generate_audio(text_prompt, history_prompt="zh_speaker_9")
# save audio to disk
write_wav("zh_speaker_9.wav", SAMPLE_RATE, audio_array)
  
# play text in notebook
# Audio(audio_array, rate=SAMPLE_RATE)