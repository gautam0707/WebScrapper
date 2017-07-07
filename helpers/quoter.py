def states():
	with open("india_states",'r') as f:
		with open("india_states_eng","w") as w:
			for line in f:
				w.write("\""+line.strip()+"\",")

def countries():
	with open("world_countries",'r') as f:
		with open("world_countries_eng","w") as w:
			for line in f:
				w.write("\""+line.strip()+"\",")

if __name__ == "__main__":
	countries()

