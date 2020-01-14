# 95555 Diogo Venancio


# 2.1.1
def eh_labirinto(tuple_for_maze):
    """Verifies if the input is a valid maze."""
    # input: universal / output: boolean

    # Verifies if argument is a tuple
    if not isinstance(tuple_for_maze, tuple):
        return False

    # Verifies if input is an empty tuple
    if tuple_for_maze == ():
        return False

    # Verifies if each element of tuple is a tuple. Also verifies the 3 x 3 rule
    for i in range(len(tuple_for_maze)):
        if not isinstance(tuple_for_maze[i], tuple):
            return False
        if len(tuple_for_maze) < 3 or len(tuple_for_maze[i]) < 3:
            return False

    # Verifies if all tuples have the same size
    for i in range(len(tuple_for_maze) - 1, 0, -1):
        if len(tuple_for_maze[i]) != len(tuple_for_maze[i - 1]):
            return False

    # Verifies if each element is an integer, either 1 or 0. Also verifies if is a wall
    for i in range(len(tuple_for_maze)):
        for j in range(len(tuple_for_maze[i])):
            if not isinstance(tuple_for_maze[i][j], int):
                return False
            if tuple_for_maze[i][j] != 0 and tuple_for_maze[i][j] != 1:
                return False
            if tuple_for_maze[0][j] != 1 or tuple_for_maze[-1][j] != 1:
                return False
            if tuple_for_maze[i][0] != 1 or tuple_for_maze[i][-1] != 1:
                return False

    return True  # If everything is alright, returns True


# 2.1.2
def eh_posicao(tuple_position):
    """Verifies if input is a position."""
    # input: universal / output: boolean

    # Verifies if parameter is a tuple
    if not isinstance(tuple_position, tuple):
        return False

    # Verifies if elements from tuple are integers >= 0
    for i in tuple_position:
        if not isinstance(i, int) or i < 0:
            return False

    # Verifies if tuple only has 2 elements
    if len(tuple_position) != 2:
        return False

    return True  # If everything is alright, returns True


# 2.1.3
def eh_conj_posicoes(tuple_set_of_positions):
    """Verifies if input is a set of positions in which, each one will represent an unit."""
    # input: universal / output: boolean

    # Verifies if parameter is a tuple
    if not isinstance(tuple_set_of_positions, tuple):
        return False

    # Verifies if each element from tuple is a position
    for i in range(len(tuple_set_of_positions)):
        if not eh_posicao(tuple_set_of_positions[i]):
            return False

    # Verifies if each value is unique
    validating = []
    for i in tuple_set_of_positions:
        if i not in validating:
            validating.append(i)
        else:
            return False

    return True  # If everything is alright, returns True


# 2.1.4
def tamanho_labirinto(maze):
    """Returns a tuple representing maps size (Nx, Ny)."""
    # input: maze / output: tuple

    # Verifies if input is a maze
    if not eh_labirinto(maze):
        raise ValueError("tamanho_labirinto: argumento invalido")

    # Returns size of maze. Index = 0 was used, but it could be any other because maze is a perfect rectangle/square
    size = (len(maze), len(maze[0]))
    return size


# 2.1.5
def eh_mapa_valido(maze, set_of_positions):
    """Verifies if each unit is not at a wall."""
    # input: maze + set of positions / output: boolean

    # Verifies if arguments are a valid maze and a set of positions
    if not eh_labirinto(maze) or not eh_conj_posicoes(set_of_positions):
        raise ValueError("eh_mapa_valido: algum dos argumentos e invalido")

    # Verifies if each unit from set of positions is inside the map
    for ele in set_of_positions:
        if tamanho_labirinto(maze)[0] < ele[0] or tamanho_labirinto(maze)[1] < ele[1]:
            return False

    # Verifies if coordinates are not at walls
    for i in range(len(set_of_positions)):
        if maze[set_of_positions[i][0]][set_of_positions[i][1]] == 1:
            return False

    return True  # If everything is alright, returns True


# 2.1.6
def eh_posicao_livre(maze, set_of_positions, position):
    """Verifies if input position is neither a wall nor one of the units."""
    # input: maze + set of positions + position / output: boolean

    # Verifies if arguments are valid
    if not eh_labirinto(maze) or not eh_conj_posicoes(set_of_positions) or not eh_posicao(position) \
            or not eh_mapa_valido(maze, set_of_positions):
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")

    # Verifies if position is neither one of the units nor one wall
    if position in set_of_positions or maze[position[0]][position[1]] == 1:
        return False

    return True  # If everything is alright, returns True


# 2.1.7
def posicoes_adjacentes(position):
    """Returns adjacent positions to a given position"""
    # input: position / output: set of positions

    # Verifies if position is valid
    if not eh_posicao(position):
        raise ValueError("posicoes_adjacentes: argumento invalido")

    # Gets coordinates of vicinity respecting the mazes order
    res_adj_pos = ()
    if position[0] >= 0 and position[1] - 1 >= 0:
        res_adj_pos += ((position[0], position[1] - 1),)
    if position[0] - 1 >= 0 and position[1] >= 0:
        res_adj_pos += ((position[0] - 1, position[1]),)
    if position[0] + 1 >= 0 and position[1] >= 0:
        res_adj_pos += ((position[0] + 1, position[1]),)
    if position[0] >= 0 and position[1] + 1 >= 0:
        res_adj_pos += ((position[0], position[1] + 1),)

    return res_adj_pos  # Returns all valid coordinates of vicinity


# 2.1.8
def mapa_str(maze, set_of_positions):
    """Returns a string which, when printed, represents the maze with its units."""
    # input: maze + set of position / output: string

    # Verifies if input is valid
    if not eh_labirinto(maze) or not eh_conj_posicoes(set_of_positions) or not eh_mapa_valido(maze, set_of_positions):
        raise ValueError("mapa_str: algum dos argumentos e invalido")

    # Changes the maze into a list so that its values can be changed
    map_converted_to_list = []
    for i in range(len(maze)):
        map_converted_to_list += [list(maze[i])]

    # Changes lists values into either 0, . or # to represent each coordinate appropriately
    for ny in range(len(maze[0])):
        for nx in range(len(maze)):
            if map_converted_to_list[nx][ny] == 1:
                map_converted_to_list[nx][ny] = "#"
            else:
                map_converted_to_list[nx][ny] = "."
    for j in set_of_positions:
        map_converted_to_list[j[0]][j[1]] = "O"

    # Converts the list into a string that can be printed
    map_ready_to_be_printed = ""
    for nx in range(len(maze[0])):
        for ny in range(len(maze)):
            map_ready_to_be_printed += str(map_converted_to_list[ny][nx])
        map_ready_to_be_printed += "\n"

    # Returns a string that can be printed to give a representation of the map. [:-1] was used to remove the last \n
    return map_ready_to_be_printed[:-1]


# 2.2.1
def obter_objetivos(maze, set_of_positions, position):
    """Returns all adjacent positions to every unit in the map but not the ones from the input position"""
    # input: maze + set of positions + position / output: set of positions

    # Validates arguments
    if not eh_valid_arguments(maze, set_of_positions, position):
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")

    # Removes the position from the set_of_positions to get the correct output
    filtered_set_of_positions = ()
    for ele in set_of_positions:
        if ele != position:
            filtered_set_of_positions += (ele,)

    # Gets and filters (not in walls) adjacent positions from each unit
    res_adj_pos_filtered = ()
    for ele in filtered_set_of_positions:
        adj_pos_not_filtered = posicoes_adjacentes(ele)
        for i in adj_pos_not_filtered:
            if maze[i[0]][i[1]] != 1:
                res_adj_pos_filtered += (i,)

    # Filters for unique positions and possible units in the result after filtering
    unique_adj_pos_filtered = ()
    for i in res_adj_pos_filtered:
        if i not in unique_adj_pos_filtered and i not in set_of_positions:
            unique_adj_pos_filtered += (i,)

    return unique_adj_pos_filtered  # Returns a tuple with all the valid adjacent positions


# 2.2.2
def obter_caminho(maze, set_of_positions, position):
    """Returns a tuple with the shortest path (according to the Breadth First Search Algorithm) from a unit
    to another, respecting all the mazes rules."""
    # input: maze + set of positions + position / output: set of positions

    # Validates arguments
    if not eh_valid_arguments(maze, set_of_positions, position):
        raise ValueError("obter_caminho: algum dos argumentos e invalido")

    # Gets objectives
    objective_list = obter_objetivos(maze, set_of_positions, position)

    # If the unit is already close to another unit, then it does not need to move
    if position in objective_list:
        return ()

    # Initiates structures
    exploration_list = [(position, ())]
    explored_positions_list = []

    # Cycle to search for the shortest path
    while exploration_list:
        current_position, current_path = exploration_list.pop(0)

        # Gets new position into the queue and saves path
        if current_position not in explored_positions_list:
            explored_positions_list.append(current_position)
            current_path += (current_position,)

            # Ends the cycle because we found our objective
            if current_position in objective_list:
                return current_path

            # Until we find our objective, we search for each elements adjacent positions and save our path
            else:
                for ele in posicoes_adjacentes(current_position):
                    if eh_posicao_livre(maze, set_of_positions, ele):
                        exploration_list += ((ele, current_path),)

    return ()  # Returns () if we are unable to find any path


# 2.2.3
def mover_unidade(maze, set_of_positions, position):
    """Returns a set of positions corresponding to all units coordinates after one of them (position input)
    has moved towards another one."""
    # input: maze + set of positions + position / output: set of positions

    # Verifies if arguments are valid
    if not eh_valid_arguments(maze, set_of_positions, position):
        raise ValueError("mover_unidade: algum dos argumentos e invalido")

    # Gets the shortest path
    path = obter_caminho(maze, set_of_positions, position)

    # If path is empty it means that units do not need to move or they can not move
    if path == () or len(set_of_positions) > 2:
        return set_of_positions

    # Saving positions index for later use
    position_index = 0
    for i in range(len(set_of_positions)):
        if set_of_positions[i] == position:
            position_index = i

    # Removes position from set of positions so that, when added, will not repeat elements
    set_of_positions_filtered = ()
    for ele in set_of_positions:
        if not ele == position:
            set_of_positions_filtered += (ele,)

    # Position is now the second coordinate of the path
    position = path[1]

    # Putting position in the index where it was
    res_set_of_positions = set_of_positions_filtered[:position_index] + \
                           (position,) + set_of_positions_filtered[position_index:]

    return res_set_of_positions  # Result is an changed set of positions


# Extra
def eh_valid_arguments(maze, set_of_positions, position):
    """Verifies if each argument is valid and if position is in set_of_positions."""
    # input: maze + set of positions + position / output: boolean

    # Verifies if arguments are valid
    if not eh_labirinto(maze) or not eh_conj_posicoes(set_of_positions) or not eh_posicao(position) \
            or not eh_mapa_valido(maze, set_of_positions):
        return False

    # Verifies if position is in the set
    if position not in set_of_positions:
        return False

    return True  # If everything is alright, returns True
