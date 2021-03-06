def perm(a):
    length = len(a)
    if length == 1:
        return [a]
    else:
        visited = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            for j in perm(b):
                j.insert(0,i)
                if j not in visited:
                    visited.append(j)
        return visited