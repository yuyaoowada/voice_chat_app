import threading

import asyncio

from voice_chat_app.opencv import video_playback
from voice_chat_app.talk import talk


def main():
    print('　　　　　~~ずんだもんと話をしよう！~~　　　　　\n',
          '　　　　　　©VOICEVOX:ずんだもん　　　　　　 ')

    talk()

    # asyncio.run(video_playback())
    # asyncio.run(talk())
    # t1 = threading.Thread(target=video_playback)
    # t2 = threading.Thread(target=talk)
    # t1.start()
    # t2.start()


if __name__ == '__main__':
    main()
