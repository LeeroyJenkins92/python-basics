from vosk import Model, KaldiRecognizer
import wave
import json
import datetime as dt
from pydub import AudioSegment


def waver():
    sound = AudioSegment.from_mp3("C:\\scripts\\NLP\\files\\somevoicefile.mp3")
    sound = sound.set_channels(1)
    sound.export("C:\\scripts\\NLP\\files\\somevoicefile-Mono.wav", format="wav")


def saver(outgoing, res):
    with open(outgoing, 'w', encoding="utf-8") as out:
        out.write(res)


waver()
today = dt.datetime.now().date()
in_file = "C:\\scripts\\NLP\\files\\somevoicefile-Mono.wav"
out_file = f"C:\\scripts\\NLP\\files\\{today}-text.txt"
stream = wave.open(in_file, "rb")
results = ""
last_line = False
model = Model(r"C:\scripts\NLP\model")
recognizer = KaldiRecognizer(model, stream.getframerate())
recognizer.SetWords(True)

while True:
    data = stream.readframes(4000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        result_db = json.loads(recognizer.Result())
        for key, value in result_db.items():
            if value != "" and key == 'text':
                results += f"[phrase]: '{result_db['text']}'"
                last_line = False
            elif not last_line:
                results += "\n"
                last_line = True
saver(out_file, results)
