import sys

#cache = [0] * 1000000
cache = {}

def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    # <your code>

    if i > j:
        temp = i
        i = j
        j = temp

    if i < j//2:
        i = j//2


    max_length = 1;
    for a in range(i, j+1):
        n = a
        count = 1

        if n in cache:
        #if cache[n] != 0:
            count = cache[n]

        else:
            while n != 1:
                if n % 2 == 0:
                    n = n // 2
                    count = count +1
                elif n % 2 != 0:
                    n = n + n//2 +1
                    count = count + 2
                if n in cache:
                    count += cache[n]-1
                    break;
            cache[a] = count;

        if max_length < count:
            max_length = count
        

    return max_length

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)



collatz_solve(sys.stdin, sys.stdout)
