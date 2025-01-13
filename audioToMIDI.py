from pydub import AudioSegment
from pydub.playback import play
import librosa
import numpy as np

from geneticAlgorithm import GeneticAlgorithm

def extractMelodyFromAudio(audioPath, sampleRateTemp=22050, noteDuration=1.4):
    # Loading the audio file, librosa.load will return the audio signal and sample rate
    audio, sampleRate = librosa.load(audioPath)

    # Calculating the hop length and window size for shorter time frames
    # hopLength is the step size in samples
    # piptrack estimates the frequency and magnitudes
    hopLength = int(noteDuration * sampleRate / 4)
    pitches, magnitudes = librosa.piptrack(y=audio, sr=sampleRate, hop_length=hopLength)

    # To store the detected melody as MIDI note numbers
    melody = []

    # Looping over frames to analyze pitches
    for timeFrame in range(pitches.shape[1]):
        pitchFrame = pitches[:, timeFrame]
        magnitudeFrame = magnitudes[:, timeFrame]

        if magnitudeFrame.max() > np.median(magnitudes): # Only considering significant peaks
            pitch = pitchFrame[magnitudeFrame.argmax()]

            if pitch > 0:
                midiNote = librosa.hz_to_midi(pitch)
                melody.append(int(round(midiNote)))
            else:
                melody.append(None)
        else:
            melody.append(None)

    # Replace "None" values with a default note
    melody = [note if note is not None else 26 for note in melody]

    # Returning the MIDI array as a numpy array for better reading later on
    return np.array(melody)

# This method converts a MIDI note number into its corresponding
# frequency in Hz (A4 = 440Hz)
def midiNoteToFreq(midiNote):
    # This is a formula for mapping MIDI notes to frequencies
    return 440.0 * 2 ** ((midiNote - 69) / 12.0)

def generateSineWave(freq, duration, sampleRate=44100):
    if freq is None:
        return AudioSegment.silent(duration)
    
    # An array of samples per second
    timeArray = np.linspace(0, duration / 1000, int(sampleRate * (duration / 1000)), False)
    
    # Generating a sine wave signal for a given frequency
    sineWave = 0.5 * np.sin(2 * np.pi * freq * timeArray)

    # Converting the wave into 16-bit PCM format
    audioData = (sineWave * 32767).astype(np.int16)

    audioSegment = AudioSegment(
        audioData.tobytes(),
        frame_rate = sampleRate,
        sample_width = 2,
        channels = 1
    )

    return audioSegment

def generateSquareWave(freq, duration, sampleRate=44100):
    if freq is None:
        return AudioSegment.silent(duration)
    
    # Time array for the specified duration
    timeArray = np.linspace(0, duration / 1000, int(sampleRate * (duration / 1000)), False)
    
    # Generating the square wave signal
    squareWave = 0.5 * np.sign(np.sin(2 * np.pi * freq * timeArray))
    
    # Converting the wave into 16-bit PCM format
    audioData = (squareWave * 32767).astype(np.int16)
    
    # Creating an AudioSegment object from the wave
    audioSegment = AudioSegment(
        audioData.tobytes(),
        frame_rate=sampleRate,
        sample_width=2,
        channels=1
    )
    
    return audioSegment

def playMelody(melody, noteDuration=300):
    song = AudioSegment.silent()
    
    # Converting each midi note to a sine wave
    for midiNote in melody:
        freq = midiNoteToFreq(midiNote) if midiNote else None
        sineWave = generateSquareWave(freq, noteDuration)
        song += sineWave

    play(song)

if __name__ == "__main__":
    # Extracting melody
    # melody = extractMelodyFromAudio("MHALL.wav")
    melody = [76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 62, 60]

    # Creating a genetic algorithm object and evolving the population
    ga = GeneticAlgorithm(melody)
    bestChromosome = ga.evolve() 

    print("Original melody: \n")
    playMelody(melody)
    print(melody)

    print("\nBest note sequence found:")
    print(bestChromosome.genes)
    print(f"Fitness score: {bestChromosome.fitnessScore}")
    playMelody(bestChromosome.genes)