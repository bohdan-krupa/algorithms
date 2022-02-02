def getTime(word: str) -> int:
    eng_alphabet = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    )

    position = 0
    time = 0

    for letter in word.upper():
        letter_position = eng_alphabet.index(letter)

        gap = abs(letter_position - position)
        step = min(gap, abs(gap - 26))

        position = letter_position
        time += step
    
    return time
