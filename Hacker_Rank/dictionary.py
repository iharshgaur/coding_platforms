def name_count(str):
    str=str.lower()
    count = dict()
    names = str.split(',')
    for name in names:
        name=name.strip()
        if name in count:
            count[name] += 1
        else:
            count[name] = 1

    return count

print(name_count('Alok, amit, suresh , amit, vidya, sindhu, vidya, vidya, alok'))
