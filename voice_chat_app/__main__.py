import numpy as np

from voice_chat_app.audio import play_by_simpleaudio
from voice_chat_app.chatgpt import get_chatgpt_response
from voice_chat_app.recognition import recognize_speech
from voice_chat_app.voicevox import get_voicevox_audio

if __name__ == '__main__':
    prompt = recognize_speech()

    chatgpt_response = get_chatgpt_response(prompt).choices[0].text

    audio_data = get_voicevox_audio(chatgpt_response).content

    play_by_simpleaudio(audio_data)

    print(f"ずんだもん: {chatgpt_response}")
    print("Voicevox: 音声を再生しました。")
