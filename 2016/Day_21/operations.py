from typing import List, Tuple

def swap_position(password: List[str], positions: Tuple[int, int], **kwargs) -> str:
    x, y = positions
    password[x], password[y] = password[y], password[x]
    return password

def swap_letters(password: List[str], letters: Tuple[str, str], **kwargs) -> str:
    a, b = letters
    a_indices = [i for i, char in enumerate(password) if char == a]
    b_indices = [i for i, char in enumerate(password) if char == b]
    for i in a_indices:
        password[i] = b
    for i in b_indices:
        password[i] = a
    return password

def rotate_letter(password: List[str], letter: str, **kwargs) -> str:
    index = password.index(letter)
    steps = index + 1
    if index >= 4:
        steps += 1
    return rotate_steps(password, "right", steps)

def rotate_steps(password: List[str], direction: str, steps: int, **kwargs) -> str:
    steps %= len(password)
    if direction == "right":
        password = password[-steps:] + password[:-steps]
    else:
        password = password[steps:] + password[:steps]
    return password

def reverse(password: List[str], positions: Tuple[int, int], **kwargs) -> str:
    x, y = positions
    password[x:y+1] = list(reversed(password[x:y+1]))
    return password

def move(password: List[str], positions: Tuple[int, int], **kwargs) -> str:
    x, y = positions
    a = password[x]
    password = password[:x] + password[x+1:]
    password = password[:y] + [a] + password[y:]
    return password


OPERATIONS = {
    "swap_position": swap_position,
    "swap_letters": swap_letters,
    "rotate_letter": rotate_letter,
    "rotate_steps": rotate_steps,
    "reverse": reverse,
    "move": move
}


def inverse_swap_position(password: List[str], positions: Tuple[int, int], **kwargs) -> str:
    return swap_position(password, positions)

def inverse_swap_letters(password: List[str], letters: Tuple[str, str], **kwargs) -> str:
    return swap_letters(password, letters)

def inverse_rotate_letter(password: List[str], letter: str, **kwargs) -> str:
    index = password.index(letter)

    if index % 2:       # original index must be < 4
        
        index = password.index(letter)
        steps = 0
        while index >= 4 or index != (steps - 1) % len(password):
            password = rotate_steps(password, "left", 1)
            index = password.index(letter)
            steps += 1

    else:               # original index must be >= 4

        index = password.index(letter)
        steps = 0
        while index < 4 or index != (steps - 2) % len(password):
            password = rotate_steps(password, "left", 1)
            index = password.index(letter)
            steps += 1
    
    return password

def inverse_rotate_steps(password: List[str], direction: str, steps: int, **kwargs) -> str:
    inverse_direction = "left" if direction == "right" else "right"
    return rotate_steps(password, inverse_direction, steps)

def inverse_reverse(password: List[str], positions: Tuple[int, int], **kwargs) -> str:
    return reverse(password, positions)

def inverse_move(password: List[str], positions: Tuple[int, int], **kwargs) -> str:
    x, y = positions
    return move(password, (y, x))


INVERSE_OPERATIONS = {
    "swap_position": inverse_swap_position,
    "swap_letters": inverse_swap_letters,
    "rotate_letter": inverse_rotate_letter,
    "rotate_steps": inverse_rotate_steps,
    "reverse": inverse_reverse,
    "move": inverse_move
}