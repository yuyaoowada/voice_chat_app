from voice_chat_app.audio import play_by_simpleaudio
from voice_chat_app.chatgpt import get_chatgpt_response
from voice_chat_app.recognition import recognize_speech
from voice_chat_app.voicevox import get_voicevox_audio


def talk():
    """Consolidates　voice　recognition, response　by　ChatGPT, and even voice playback by Voicevox"""
    while True:
        print('　【待機中】（終了する場合は「バイバイ」と言ってね）')
        prompt = recognize_speech()

        chatgpt_response = get_chatgpt_response(prompt)

        audio_data = get_voicevox_audio(chatgpt_response).content

        print(f"ずんだもん:{chatgpt_response}")
        play_by_simpleaudio(audio_data)

        if prompt == 'バイバイ':
            break
