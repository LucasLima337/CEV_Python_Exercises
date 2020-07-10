# Tocando um MP3
import emoji
e = emoji.emojize(':wink:', use_aliases=True)
from pygame import mixer
mixer.init()
mixer.music.load('intheend.mp3')
mixer.music.play()
input('Aperte a tecla enter quando desejar parar {}'.format(e))
