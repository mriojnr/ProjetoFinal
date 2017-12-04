#
# Trabalho Final
# 
# Aluno      : Mário Júnior de Sales Pimentel - 11218796
# Disciplina : Analise e Projeto de Algoritmos - 2017.1
# Professor  : GILBERTO FARIAS DE SOUSA FILHO 
#
#
# uso : 
#       utilizando pipe de arquivo:
#           > python3 app.py 100 < nome_do_arquivo.txt
#           
#           OBS 100 = numero de iteracoes do grasp
#           
from City import City
from TSP import TSP

import random
import time
import itertools
import urllib
import csv
import functools
import pprint 
import sys
import timeit

def main(argv):
		
	number_exec = int(argv[1])
	filename = ""

	cities = []

	while True:
		try:
			line = input().strip()

			if "NAME" in line:
				filename = line

			elif line == "NODE_COORD_SECTION":
			   
				while True:
					try:
						
						line = input().split()
						city = City(line[0], line[1], line[2])
						cities.append(city)
					except Exception as e:
						#print ("1 " + str(e) + " city :" + str(city.id))
						break;

		except Exception as e:
			#print ("2 " + str(e) + " city :" + str(city.id))
			break;
	
	tsp = TSP()
	M = tsp.get_distance_matrix(cities)
	
	#tsp.pretty_print(M)
	#exit()

	#print ("\nCusto NN : " + str(custo_nn))
	#tsp.print_tour_simple(nn_tour)

	print ("Executing " + str(number_exec) + " times on : " + str(filename) )

	start_time = timeit.default_timer()

	minimo = float("inf")
	for i in range(number_exec):
		#alpha = random.uniform(0, 1)
		alpha = 0.5
		grasp_tour = tsp.GRASP_TSP(cities, M, alpha)
		custo_final = tsp.get_cost(grasp_tour, M)

		if custo_final < minimo:
			print ("\nAlpha : " + str(alpha) + " Custo GRASP: " + str(custo_final))
			tsp.plot_cities(grasp_tour)
			minimo = custo_final
	
	elapsed = timeit.default_timer() - start_time

	print ("Elapsed time : " + str(elapsed) + " s")
	print ("---------------------------------------------\n\n")

if __name__ == "__main__":
  	main(sys.argv)



