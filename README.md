# Python-Programming

Created a graph color python program using A Start Search Algorithm.

Task:-

Write the map color function as above. It calls A Star Search. Its output is a dictionary assigning colors to locations, for example

{'WA': 'red', 'Q': "blue", ...}

Given:-

#  Here is the example 
locations = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

colors = ["red", "green", "blue"]

adjacencies = [('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), ('NT', 'Q'), 
               ('SA', 'Q'), ('Q', 'NSW'), ('SA', 'NSW'), ('SA', 'V'),
               ('NSW', 'V')]

mapColor(locations, colors, adjacencies)
