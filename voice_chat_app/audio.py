import tempfile
import time
import wave
import io

import pyaudio
import simpleaudio as sa


def play_by_simpleaudio(audio_data):
    """Audio playback by simpleaudio"""
    # TODO 最初に「プツっ」という音が発生するので要修正
    wave_obj = sa.WaveObject(audio_data, 1, 2, 24000)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def play_by_pyaudio(audio_data):
    """Audio playback by PyAudio"""
    audio = io.BytesIO(audio_data)

    with wave.open(audio, 'rb') as f:

        p = pyaudio.PyAudio()

        def _callback(in_data, frame_count, time_info, status):
            data = f.readframes(frame_count)
            return data, pyaudio.paContinue

        stream = p.open(format=p.get_format_from_width(width=f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True,
                        stream_callback=_callback)


        stream.start_stream()
        while stream.is_active():
            time.sleep(0.1)

        stream.stop_stream()
        stream.close()
        p.terminate()


def play_by_simpleaudio_in_temp_file(audio_data):
    """Audio playback with simpleaudio using temporary files"""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
        temp_wav_file.write(audio_data)
        temp_wav_file.flush()

        print(f"Temp file created: {temp_wav_file.name}")

        play_obj = sa.WaveObject.from_wave_file(temp_wav_file.name).play()
        play_obj.wait_done()
