def do_they_overlap_at(target, candidate, overlap):
    a = target[-overlap:]
    b = candidate[:overlap]
    return a == b


def largest_overlap(target, candidate):
    if len(target) != len(candidate):
        return -1

    if len(target) == 0 or len(candidate) == 0:
        return -1

    overlap = 0
    for i in range(1, len(target) + 1):
        if do_they_overlap_at(target, candidate, i):
            overlap = i
    return overlap


print(largest_overlap('ABCABCA', 'BCABCAB'))
print(largest_overlap('ABC', 'AB'))
print(largest_overlap('', 'AB'))
print(largest_overlap('', ''))
print(largest_overlap('CCC', 'AAA'))
