

def check(s, filename):
    with open(filename, 'w') as fstream:
        map = dict()
        for word in sorted(list(s.lower().split())):
            if word not in map:
                map[word] = 1
            else:
                map[word] += 1

        for key in map:
            print(key, map[key], file=fstream)

check("a aa abC aa ac abc bcd a", "file.txt")