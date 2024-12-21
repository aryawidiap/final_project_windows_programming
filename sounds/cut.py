from pydub import AudioSegment
t1 = 0 #Works in milliseconds
t2 = 2
t2 = t2 * 1000
for i in range(1,4):
    newAudio = AudioSegment.from_wav(f"note_{i}.wav")
    newAudio = newAudio[t1:t2]
    newAudio.export(f"note_{i}_cut.wav", format="wav") #Exports to a wav file in the current path.