import networkx
import matplotlib.pyplot as plt

def start_nx():
	global fuel_for_path
	fuel_for_path = {}
	G = networkx.Graph()
	for planet in planets:
		G.add_node(planet)
	for route in space_map:
		start, end, fuel = route.split(' ')
		#While we're at it, I'm saving some info on the routes.
		fuel_for_path[start+end] = int(fuel)
		fuel_for_path[end+start] = int(fuel)
		G.add_edge(start, end, fuel=int(fuel))
	return G

#VARIABLES
available_fuel = int(input('How much fuel do we have? '))
space_map = ['A B 1', 'A C 1', 'B C 2', 'B D 2', 'C D 1', 'C E 2', 'D E 2', 'D F 2', 'D G 1', 'E G 1', 'E H 1', 'F I 4', 'F G 3', 'G J 2', 'G H 3', 'H K 3', 'I J 2', 'I K 2']
planets = list('ABCDEFGHIJK')

#Start graphing lib
G = start_nx()

for planet in planets:
	#Find the shortest path:
	path_fuel = networkx.shortest_path_length(G, 'A', planet, weight='fuel')
	path = networkx.shortest_path(G, 'A', planet, weight='fuel')
	#Not the same way back:
	for i in range(len(path)-1):
		G.remove_edge(path[i], path[i+1])
	#Find another way back:
	second_path_fuel = networkx.shortest_path_length(G, planet, 'A', weight='fuel')
	second_path = networkx.shortest_path(G, planet, 'A', weight='fuel')
	#If we ever want to try again, we better put those routes back:
	for i in range(len(path)-1):
		G.add_edge(path[i], path[i+1], fuel=fuel_for_path[path[i]+path[i+1]])
	if path_fuel + second_path_fuel > available_fuel: #Then we can't make it home.
		break
	else:
		ok_fuel = path_fuel
		ok_second_fuel = second_path_fuel
		ok_path = path
		ok_second_path = second_path
		ok_planet = planet

print('Planet:', ok_planet)
print('To:', '-'.join(ok_path), '(using', ok_fuel, 'fuel)')
print('Back:', '-'.join(ok_second_path), '(using', ok_second_fuel, 'fuel)')


networkx.draw(G)
plt.savefig('path.png')