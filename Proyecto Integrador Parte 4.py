import os
import readchar

map_oneline = "..###################\n......#.........#...#\n#.#.#.#.#.#.#.###.###\n#.#.#...#.#.#...#...#\n#.#.#.#######.###.#.#\n#.#.#...#.#.....#.#.#\n###.#.###.#.#.#####.#\n#...#.#...#.#.......#\n#######.#.#####.###.#\n#.#.#.#.#.#...#.#...#\n#.#.#.###.#.#####.###\n#.#...#.............#\n#.###.#.#####.#####.#\n#...#.#...#...#.....#\n###.#.#.#.###.#.###.#\n#.....#.#.#...#.#.#.#\n#.#.#######.#####.###\n#.#.#.#.....#.....#.#\n#.#.#.#.#.###.###.#.#\n#.#.....#.......#...\n###################."


map_split = list(map_oneline.split("\n"))

matriz = []

for i in range(len(map_split)):
    matriz.append([])
    for j in range(len(map_split[0])):
        matriz[i].append(map_split[i][j-1])


def imprimir_matriz(mapa):
    os.system("cls" if os.name == "nt" else clear)
    f = ''
    for fila in mapa:
        for columna in fila:
            f += columna
        print(f)
        f = ''



def main_loop(mapa, posicion_inicial, posicion_final):
    px = posicion_inicial[0]
    py = posicion_inicial[1]
    mapa[py][px] = 'p'
    imprimir_matriz(mapa)
    print("\n" + "posicion: " + str(px) + ". " + str(py))

    while True:
        k = readchar.readkey()
        if k == readchar.key.UP:
            if 0 < py <= len(mapa) - 1:
                if mapa [py - 1][px] != "#" and py > 0:
                    mapa[py][px] = "."
                    py -= 1
                else:
                    pass
        elif k == readchar.key.DOWN:
            if 0 <= py < len(mapa) - 1:
                if mapa [py + 1] [px] != "#":
                    mapa[py][px] = "."
                    py += 1
                else:
                    pass
        elif k == readchar.key.LEFT:
            if 0 < px <= len(mapa[py]) - 1:
                if mapa[py][px - 1] != "#" and px > 0:
                    mapa[py][px] = "."
                    px -= 1
                else:
                    pass
        elif k == readchar.key.RIGHT:
            if 0 <= px < len(mapa[py]) - 1:
                if mapa[py][px + 1] != "#":
                    mapa[py][px] = "."
                    px += 1
                else:
                    pass

        mapa[py][px] = "p"
        imprimir_matriz(mapa)
        print("\n" + "posicion: " + str(px) + "." + str(py))

        if px == posicion_final[0] and py == posicion_final[1]:
            print("FELICITACIONES, LO LOGRASTE!!")
            break
    
main_loop(matriz, (0,0), (len(matriz[0])-1, len(matriz)-1))