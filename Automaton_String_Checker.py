'''Teoría de la Computación - Acompañamiento
		Validación de cadenas pertenecientes a un Lenguaje Libre de Contexto 
		a travéz de un Autómata de Pila.
			Realizado en Python3 usando la definicion formal del automata en formato JSON (Java Script Object Notation) propuesta.
			
			El proyecto consta de una unica clase llamada Automaton en la que se procesa toda la informacion proporcionada por el objeto JSON
			y se evaluan las cadenas.

			

			Elabrado por Damian Moreno Mireles'''

import json
from Automaton import Automaton

#This is where the json object is loaded
rawAutomaton = json.loads(open("Raw Automaton.json").read())

#How to instantiate the automaton and automatically evals all the strings
newAutomaton = Automaton(rawAutomaton)
