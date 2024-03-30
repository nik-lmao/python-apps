def remove_duplicates():
    lines = set()
    duplicates_removed = 0

    with open("token_url.txt", 'r') as file:
        for line in file:
            if line.strip() not in lines:
                lines.add(line.strip())
            else:
                duplicates_removed += 1

    with open("token_url.txt", 'w') as file:
        file.write('\n'.join(lines))

    return duplicates_removed

remove_duplicates()