def answer(population, x, y, strength):
    if strength >= population[y][x]:
        population[y][x] = -1
        population = zombify(population, strength)
    return population

def zombify(population, strength):
    flag = False
    height = len(population)
    width = len(population[0])
    for y in range(0, height):
        for x in range(0, width):
            if population[y][x] == -1:
                if 0 <= y-1 and y-1 < height and 0 <= x and x < width:
                    if strength >= population[y-1][x] and population[y-1][x] != -1:
                        population[y-1][x] = -1
                        flag = True
                if 0 <= y and y < height and 0 <= x+1 and x+1 < width:
                    if strength >= population[y][x+1] and population[y][x+1] != -1:
                        population[y][x+1] = -1
                        flag = True
                if 0 <= y and y < height and 0 <= x-1 and x-1 < width:
                    if strength >= population[y][x-1] and population[y][x-1] != -1:
                        population[y][x-1] = -1
                        flag = True
                if 0 <= y+1 and y+1 < height and 0 <= x and x < width:
                    if strength >= population[y+1][x] and population[y+1][x] != -1:
                        population[y+1][x] = -1
                        flag = True
    if not flag:
        return population
    return zombify(population, strength)

test = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
print answer(test, 2, 1, 5)