import tempfile
import time
import wave
import io

import pyaudio
import simpleaudio as sa


def play_by_simpleaudio(audio_data):
    # TODO 最初に「プツっ」という音が発生するので要修正
    wave_obj = sa.WaveObject(audio_data, 1, 2, 24000)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def play_by_pyaudio(audio_data):
    # メモリ上で展開
    audio = io.BytesIO(audio_data)

    with wave.open(audio, 'rb') as f:
        # 以下再生用処理
        p = pyaudio.PyAudio()

        def _callback(in_data, frame_count, time_info, status):
            data = f.readframes(frame_count)
            return data, pyaudio.paContinue

        stream = p.open(format=p.get_format_from_width(width=f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True,
                        stream_callback=_callback)

        # Voice再生
        stream.start_stream()
        while stream.is_active():
            time.sleep(0.1)

        stream.stop_stream()
        stream.close()
        p.terminate()


def play_by_simpleaudio_in_temp_file(audio_data):
    # 一時ファイルに音声データを保存
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
        temp_wav_file.write(audio_data)
        temp_wav_file.flush()

        print(f"Temp file created: {temp_wav_file.name}")

        # simpleaudioを使用して音声を再生
        play_obj = sa.WaveObject.from_wave_file(temp_wav_file.name).play()
        play_obj.wait_done()
