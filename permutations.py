LEFT_TO_RIGHT = True
RIGHT_TO_LEFT = False
import graph_data

def valid_cycles(current_graph):
    """
    given a list of permutations and a graph, return the number of valid permutations that are valid hamiltonian cycles
    """
    def jst_permutations(n):
        permutation = list(range(n))
        permutations = []
        directions = [RIGHT_TO_LEFT] * n

        def get_largest_mobile_element(permutation, directions):
            largest_mobile = -1
            index = -1

            for i in range(n):
                if directions[i] == RIGHT_TO_LEFT and i > 0 and permutation[i] > permutation[i - 1]:
                    if permutation[i] > largest_mobile:
                        largest_mobile = permutation[i]
                        index = i
                elif directions[i] == LEFT_TO_RIGHT and i < n - 1 and permutation[i] > permutation[i + 1]:
                    if permutation[i] > largest_mobile:
                        largest_mobile = permutation[i]
                        index = i

            return index

        while True:
            # Add the current permutation to the list of permutations
            permutations.append(permutation[:])

            # Get the index of the largest mobile element
            largest_mobile_index = get_largest_mobile_element(permutation, directions)
            
            # If no mobile element is found, all permutations have been generated
            if largest_mobile_index == -1:
                break

            # Swap the largest mobile element with the adjacent element in its direction
            if directions[largest_mobile_index] == RIGHT_TO_LEFT:
                new_index = largest_mobile_index - 1
            else:
                new_index = largest_mobile_index + 1

            permutation[largest_mobile_index], permutation[new_index] = (
                permutation[new_index], permutation[largest_mobile_index])
            directions[largest_mobile_index], directions[new_index] = (
                directions[new_index], directions[largest_mobile_index])

            # Reverse the direction of all elements greater than the largest mobile element
            largest_mobile_value = permutation[new_index]
            for i in range(n):
                if permutation[i] > largest_mobile_value:
                    directions[i] = not directions[i]
        return permutations
    
    permutations = jst_permutations(len(graph_data.graph_data[current_graph]))

    def is_valid_hamiltonian_cycle(permutation):
        """
        Given a permutation and an adjacency list, return whether the permutation is a valid Hamiltonian cycle.
        """
        for i in range(len(permutation) - 2):
            if permutation[i + 1] not in graph_data.graph_data[current_graph][permutation[i]][1]:
                return False
            if permutation[0] not in graph_data.graph_data[current_graph][permutation[-1]][1]:
                return False
        return True


    valid_cycles = []
    for permutation in permutations:
        if is_valid_hamiltonian_cycle(permutation):
            valid_cycles.append(permutation)
    
    if len(valid_cycles) == 0:
        return -1
    else:
        return valid_cycles