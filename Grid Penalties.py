url = "https://www.reddit.com/r/formula1/comments/xazoz3/how_the_grid_penalties_were_applied/"

#Qualifying order of the 2022 Monza Grand Prix
quali  = ["Leclerc", "Verstappen", "Sainz", "Perez", "Hamilton", "Russell", "Norris", "Ricciardo", "Gasly", "Alonso", "Ocon", "Bottas", "De Vries", "Zhou", "Tsunoda", "Latifi", "Vettell", "Stroll", "Magnussen", "Schumacher"]

#Grid Penalties for the 2022 Monza Grand Prix
penalties = [("Verstappen", 5), ("Sainz", 999), ("Perez", 10), ("Hamilton", 999), ("Ocon", 5), ("Bottas", 15), ("Tsunoda", 999), ("Magnussen", 15), ("Schumacher", 15)]



def gridPenalty(quali, penalties):
    origGridOrder = {}
    newGridOrder = {}
    BOG = []
    slots = []
    finalGrid = []
    for i in range(len(quali)):
        origGridOrder[quali[i]] = i 
    
    for j in penalties:
        if j[1] == 999:
            BOG.append(j[0])
        else:
            newGridOrder[j[0]] = origGridOrder[j[0]] + j[1]
            slots.append(newGridOrder[j[0]])
        quali.remove(j[0])
    
    index = 0
    for i in slots:
        while index < i and index < len(quali):
            finalGrid.append(quali[index])
            index += 1
        pos = [k for k, v in newGridOrder.items() if v == i][0]
        finalGrid.append(pos)

    return finalGrid + BOG


print(gridPenalty(quali, penalties))
        







