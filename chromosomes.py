import random

class Chromosome:
    def __init__(self, targetMelody, numOfRows, noteRange=(26, 127), timeRange=(0.0, 60.0), bestGenes=None):
        self.noteRange = noteRange
        self.timeRange = timeRange
        self.numOfRows = numOfRows
        self.targetMelody = targetMelody
        
        # Initializing genes with random values if no bestGenes are provided
        if bestGenes is not None:
            self.genes = bestGenes
        else:
            self.genes = self.initializeGenes()

        self.fitnessScore = 0
        self.calculateFitness()

    def initializeGenes(self):
        # Generating random pairs of [note, time] within the specified ranges - it is a flatened 1d array ie pairs
        geneArray = []

        for _ in range(self.numOfRows):
            midiNote = random.randint(self.noteRange[0], self.noteRange[1])
            time = round(random.uniform(self.timeRange[0], self.timeRange[1]), 1)

            geneArray.append((midiNote, time))

        return geneArray
    
    def mutate(self, mutationRate=0.5):
        if random.random() < mutationRate:
            randomIndex = random.randint(0, self.numOfRows - 1)
            self.genes[randomIndex] = [
                random.randint(self.noteRange[0], self.noteRange[1]), 
                round(random.uniform(self.timeRange[0], self.timeRange[1]), 1)
            ]

            self.fitnessScore = self.calculateFitness()

    def crossover(self, mate):
        crossoverPoint = random.randint(1, self.numOfRows - 1)
        
        childGenes = self.genes[:crossoverPoint] + mate.genes[crossoverPoint:]

        child = Chromosome(self.targetMelody, self.numOfRows, self.noteRange, self.timeRange)
        child.genes = childGenes
        
        return child
    
    def calculateFitness(self):
        # Calculating the fitness based on matching both note and time.

        fitnessScore = 0

        for i in range(self.numOfRows):
            if (self.genes[i][0] == self.targetMelody[i][0] and (self.genes[i][1] == self.targetMelody[i][1])):
                fitnessScore += 1

        return fitnessScore

    def __repr__(self):
        # Formatting the genes to only one decimal place for the time
        return f"Chromosome(fitness={self.fitnessScore}, genes={self.genes})"



