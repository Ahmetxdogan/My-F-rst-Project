import sounddevice as sd
print(sd.__version__)
# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 4410

duration = 5

recording = sd.rec(int(duration * freq),
				   samplerate=freq, channels=2)

sd.wait()

write("recording0.wav", freq, recording)

wv.write("recording1.wav", recording, freq, sampwidth=2)