import requests


def get_voicevox_audio(text=None, speaker=1):  # VOICEVOX:ずんだもん
    """Voice playback by Voicevox"""
    host = "127.0.0.1"
    port = 50021
    query_payload = {"text": text, "speaker": speaker}

    query_response = requests.post(
        f"http://{host}:{port}/audio_query",
        params=query_payload
    )

    if query_response.status_code != 200:
        raise Exception("Audio query failed.")
    audio_query = query_response.json()

    synthesis_payload = {"speaker": speaker}
    synthesis_response = requests.post(
        f"http://{host}:{port}/synthesis",
        params=synthesis_payload,
        json=audio_query
    )

    if synthesis_response.status_code != 200:
        raise Exception("Audio synthesis failed.")

    return synthesis_response

