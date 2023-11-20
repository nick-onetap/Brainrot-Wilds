# Win Detection

def flip_horizontal(result):
    horizontal_values = []
    for value in result.values():
        horizontal_values.append(value)
    rows, columns = len(horizontal_values), len(horizontal_values[0])
    hvals2 = [[""] * rows for _ in range(columns)]
    for x in range(rows):
        for y in range(columns):
            hvals2[y][rows - x - 1] = horizontal_values[x][y]
        hvals3 = [item[::-1] for item in hvals2]
        return hvals3
    
def longest_sequence(hit):
    subSeqLength, longest = 1, 1
    start, end = 0, 0
    for i in range(len(hit) - 1):
        if hit[i] == hit[i + 1] - 1:
            subSeqLength += 1
            if subSeqLength > longest:
                longest = subSeqLength
                start = i + 2 - subSeqLength
                end = 1 + 2
        else:
            subSeqLength = 1
    return hit[start:end]