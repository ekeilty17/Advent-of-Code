def can_shapes_fit_in_region(all_orientations, orientation_indexes, region):
    W, L, shape_quantity = region

    def dfs(state, shape_quantity_remaining):
        print(shape_quantity_remaining)
        print("\n".join("".join([str(int(x)) for x in row]) for row in state))
        print()

        key = (hash_array(state), tuple(shape_quantity_remaining))
        if key in cache:
            return cache[key]

        for index, orientation_group in zip(orientation_indexes, all_orientations):
            if shape_quantity_remaining[index] == 0:
                continue
            
            for present_orientation in orientation_group:
                if shape_quantity_remaining[index] == 0:
                    break
                
                w, l = present_orientation.shape
                for i in range(state.shape[0] - w+1):
                    if shape_quantity_remaining[index] == 0:
                        break
                    
                    for j in range(state.shape[1] - l+1):
                        if shape_quantity_remaining[index] == 0:
                            break
                        
                        overlap = (state[i:i+w, j:j+l] != 0) & present_orientation
                        if np.any(overlap):
                            continue
                        updated_state = state.copy()
                        updated_state[i:i+w, j:j+l] += np.where(present_orientation, index, 0)
                        updated_shape_quantity_remaining = list(shape_quantity_remaining)
                        updated_shape_quantity_remaining[index] -= 1

                        updated_key = (hash_array(updated_state), tuple(updated_shape_quantity_remaining))

                        if np.sum(updated_shape_quantity_remaining) == 0:
                            cache[updated_key] = True
                            print("Solution Found")
                            print(updated_state)
                            return True
                        
                        solution_found = dfs(updated_state, updated_shape_quantity_remaining)
                        cache[updated_key] = solution_found

                        if solution_found:
                            return True
        
        cache[key] = False
        return False

    curr_state = np.zeros((W, L))
    return dfs(curr_state, shape_quantity)