def find_enclosing_chars(line, brackets_to_skip, enclosing_chars):
    """Find positions of enclosing characters, skipping the first few pairs."""
    positions = []
    brackets_to_skip *= 2  # Since we have opening and closing brackets
    
    for i, char in enumerate(line):
        if char == enclosing_chars[0]:
            if brackets_to_skip == 0:
                positions.append(i)
            else:
                brackets_to_skip -= 1
        elif char == enclosing_chars[1]:
            if brackets_to_skip == 0:
                positions.append(i)
            else:
                brackets_to_skip -= 1
    
    return positions

def find_contents_between_indexes(line, indices):
    """Extract contents from a line between given indices."""
    return line[indices[0]:indices[1] + 1]

def generate_replacement_text(tag_contents, stats):
    """Generate replacement text using stats dictionary."""
    difficulty = tag_contents[0]
    if difficulty in stats:
        stat_values = stats[difficulty]
        return f'{{{stat_values[1]}/{stat_values[0]} (Beats 80.69\\%)}}'
    return tag_contents[1]

def replace_stats(filename, stats):
    """Replace stats in the given file with updated values from stats dictionary."""
    with open(filename, 'r') as file:
        file_contents = ""
        for line in file:
            if 'Beats' in line:
                tag_contents = [line.split()[0].replace(':', ""),
                                find_contents_between_indexes(line, find_enclosing_chars(line, 1, ['{', '}']))]
                file_contents += line.replace(tag_contents[1], generate_replacement_text(tag_contents, stats))
            else:
                file_contents += line
    
    with open(filename, 'w') as file:
        file.writelines(file_contents)