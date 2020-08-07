from gtts import gTTS
import os
fh = open('text.txt', 'r')
my_text = fh.read().replace('\n', ' ')
language = 'en'
output = gTTS(text=my_text, lang=language, slow=False)
output.save('output.mp3')
fh.close()
os.system('start output.mp3')