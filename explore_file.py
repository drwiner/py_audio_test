
# Load various imports 
import pandas as pd
import os
import librosa
import librosa.display

from wav_file_helper import WavFileHelper
wavfilehelper = WavFileHelper()

audiodata = []
# file_name =  os.path.join(os.path.abspath('./output.wav'),'fold'+str(row["fold"])+'/',str(row["slice_file_name"]))
data = wavfilehelper.read_file_properties("/Users/drw/client/pyaudio/output.wav")
audiodata.append(data)

# Convert into a Panda dataframe
audiodf = pd.DataFrame(audiodata, columns=['num_channels','sample_rate','bit_depth'])

print(audiodf.bit_depth.value_counts(normalize=True)

