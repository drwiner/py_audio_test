
# Load various imports 
import pandas as pd
import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
# import IPython.display as ipd

from wav_file_helper import WavFileHelper
wavfilehelper = WavFileHelper()

filename = "/Users/drw/pyaudio/output.wav"

audiodata = []
# file_name =  os.path.join(os.path.abspath('./output.wav'),'fold'+str(row["fold"])+'/',str(row["slice_file_name"]))
data = wavfilehelper.read_file_properties(filename)
audiodata.append(data)

# Convert into a Panda dataframe
audiodf = pd.DataFrame(audiodata, columns=['num_channels','sample_rate','bit_depth'])

print(audiodf.bit_depth.value_counts(normalize=True))

plt.figure(figsize=(12,4))
data,sample_rate = librosa.load(filename)
librosa.display.waveshow(data,sr=sample_rate)

# This only works in notebooks
# ipd.Audio(filename) 

plt.show()

print("OK")