#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import math
import numpy as np

def histogram_times(filename):

    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)
        hours = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for incident in airplane_data[1:]:
            arrTime = incident[1].split(":")
            
            if arrTime[0] is not '':
                try:
                    index = int(arrTime[0])
                    hours[index] = hours[index] +  1
                except:
                    continue
        return hours


def weigh_pokemons(filename, weight):
	with open(filename) as json_data:
		pokemon = json.load(json_data)
	
		idIndex = 0
		namesOfPokemon = []
		while (idIndex < len(pokemon['pokemon'])):
			value = pokemon['pokemon'][idIndex]['weight'].replace(" kg", "")
			if float(value) == weight:
				namesOfPokemon.append(pokemon['pokemon'][idIndex]['name'])
			idIndex += 1
			 
		return namesOfPokemon
			
def single_type_candy_count(filename):
	with open(filename) as json_data:
		pokemon = json.load(json_data)
		countForCandy = 0
		print("keys")
		print(pokemon["pokemon"][0].keys())
		print()
		print()
		for i in range (0, len(pokemon['pokemon'])): 
			if len(pokemon['pokemon'][i]['type']) == 1:
				if 'candy_count' in pokemon['pokemon'][i].keys():
					countForCandy += pokemon['pokemon'][i]['candy_count']
				
				
	return countForCandy

def reflections_and_projections(points):
	arrTranslation1 = [[1,0],
						[0,0]]
	arr =  np.array([[ math.cos(math.pi / 2), -math.sin(math.pi / 2) ],
					 [math.sin(math.pi / 2), math.cos(math.pi / 2) ]])
	arrTranslation2 = [[1,3],
						[3,9]]
	
	for i in range(len(points)):
		
		points[i] = [points[i][0], 1 - points[i][1] + 1] #np.dot(points[i], arrTranslation1)
		# print(points[i])

		points[i] = np.dot(points[i], arr)
		# print(points[i])

		points[i] = 1/10 * np.dot(points[i], arrTranslation2)
		# print(points[i])
		
	return points

def normalize(image):
	# print(image)
	imgMod = np.copy(image) #image.cop
	print(imgMod)
	print()
	print()
	print()
	imgMod = imgMod.reshape(1, len(imgMod) * len(imgMod[0]))
	maximum = max(image[0])
	minimum = min(image[0])

	for i in range(len(image)):	
		for j in range(len(image[i])):
			image[i][j] = 255/(maximum - minimum) * (image[i][j] - minimum)
		
	return image


def sigmoid_normalize(image):
    pass

#print("Plane Crashes")
#print(histogram_times('airplane_crashes.csv'))
#print()
#print()
#print()
#print("Pokedex")
#print(weigh_pokemons('pokedex.json', 10.0))
#print()
#print()
#print()
#print("Pokedex - Candy")
#print(single_type_candy_count('pokedex.json'))
#print()
#print()
#print()
#print("reflections")
#print(reflections_and_projections([[5,-3] ]))
#print()
#print()
#print()
#print("reflections")
#print(reflections_and_projections([[5,-3],[6,9],[9,5] ]))
#print()
#print()
#print()
#print("arr")
#testArr = np.random.uniform(low=0, high=255, size=(32,32))
#print(normalize(testArr))
#
#
