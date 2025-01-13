import random
import keyboard
from chromosomes import Chromosome

population = 1000
noteRange = (26, 127)

class GeneticAlgorithm:
    def __init__(self, targetSequence, populationSize=population):
        self.populationSize = populationSize
        self.targetSequence = targetSequence
        self.numOfRows = len(targetSequence)

        # Creating an initial random population of Chromosomes
        self.population = [Chromosome(self.targetSequence, self.numOfRows, noteRange) for _ in range(self.populationSize)]

    def tournament(self):
        # Selecting the two best chromosomes based on fitness
        sortedPopulation = sorted(self.population, key=lambda x: x.fitnessScore, reverse=True)
        return sortedPopulation[:2]

    def evolve(self):
        generation = 0

        while True:
            print(f"\nGeneration {generation + 1}")

            # Sorting population by fitness (best at the top)
            self.population.sort(key=lambda x: x.fitnessScore, reverse=True)

            # Checking if the best chromosome matches the target sequence (perfect match)
            bestChromosome = self.population[0]
            print("Best fitness score in generation:", bestChromosome.fitnessScore, "/", self.numOfRows)
            if bestChromosome.fitnessScore == self.numOfRows:
                print("Perfect match found!")
                print("Best Sequence:", bestChromosome.genes)
                break
            
            if keyboard.is_pressed('|'):
                print("Stopped")
                break

            nextGeneration = [bestChromosome]

            # Creating the rest of the next generation
            while len(nextGeneration) < self.populationSize:
                # Selecting parents using tournament selection
                parent1, parent2 = self.tournament()

                # Crossovering to create children
                child1 = parent1.crossover(parent2)
                child2 = parent2.crossover(parent1)

                # Mutating the children
                child1.mutate()
                child2.mutate()

                # Adding children to the next generation
                nextGeneration.append(child1)
                if len(nextGeneration) < self.populationSize:
                    nextGeneration.append(child2)

            # Replacing old population with the new generation
            self.population = nextGeneration
            generation += 1

        return bestChromosome