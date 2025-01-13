Chiptune music is recognizable by its striking 8-bit aural characteristic. It is
often associated with the classic gaming era, whereby technical limitations led to
the production of simple yet memorable musical pieces. This genre can be typified
by using waveforms such as square, triangle, and sawtooth that render coarse,
synthesized sounds. This evokes nostalgia and represents some parts of retro
gaming culture.
The project used genetic algorithms for chiptune creation. Applying concepts
like crossover, mutation, and evaluation of fitness, the algorithm evolves a
population of audio samples over a number of generations to achieve an output
that fits the input audio.

### Project Overview

This project aims to generate nostalgic 8-bit chiptune music reminiscent of retro video games, where technological constraints sparked creative solutions. By blending artificial intelligence with creativity, the project uses a genetic algorithm to evolve melodies over generations, optimizing them for melodic and rhythmic similarity to an input MIDI file.

Why MIDI?

MIDI was chosen for its structured representation of music through discrete note-duration pairs, making it ideal for manipulation by genetic algorithms. Unlike raw audio, MIDI is lightweight and allows faster experimentation with pitch, rhythm, and tempo.

Why Square Waves?

Square waveforms are iconic to chiptune music, creating the sharp, coarse sounds associated with classic gaming consoles. They preserve the stylistic integrity of 8-bit music and are easy to generate and manipulate. Other waveforms like triangle and sawtooth waves were considered, but square waves dominate the retro gaming sound palette.

Why This Matters

This project highlights the intersection of AI and creative expression, offering a new way to appreciate and produce music. It invites listeners to revisit the past while exploring questions about creativity, authorship, and the future of music production.

### Method

This project uses a **genetic algorithm** to generate 8-bit chiptune music from an input MIDI file. The algorithm evolves melodies and rhythms over multiple generations to match the input while adhering to 8-bit aesthetics.

1. **Initialization**:  
   - Parse the MIDI file into `(note, duration)` pairs (e.g., `[(67, 0.5), (71, 0.25)]` where `67` is G4).  
   - Generate a random population of these pairs, constrained to common MIDI notes and rhythms for chiptune style.  

2. **Fitness Evaluation**:  
   - Compare generated notes and durations to the input MIDI.  
   - Assign scores based on melodic and rhythmic similarity, ensuring square wave aesthetics.  

3. **Selection and Crossover**:  
   - Select high-scoring pairs through tournament selection.  
   - Create new offspring by combining parts of parent pairs.  

4. **Mutation**:  
   - Randomly adjust notes or durations to introduce diversity while staying within chiptune constraints.  

5. **Evolution**:  
   - Repeat fitness evaluation, selection, crossover, and mutation until a close match to the input is achieved.  

6. **Output**:  
   - Convert the best result into an 8-bit audio file using Python waveform synthesis with square waves.

