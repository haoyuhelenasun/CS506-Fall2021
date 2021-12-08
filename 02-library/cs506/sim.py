import math
  
def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i, j in zip(x,y):
        res += abs(i-j)
    return res

def jaccard_dist(x, y):
    intersection = len(list(set(x).intersection(y)))
    union = (len(set(x)) + len(set(y))) - intersection
    if union == 0:
        return 0
    return 1 - intersection / union

def cosine_sim(x, y):
    dot = 0
    A_sqr = 0
    B_sqr = 0
    for i, j in zip(x, y):
        dot += i*j
        A_sqr += i*i
        B_sqr += j*j
    if (math.sqrt(A_sqr)*math.sqrt(B_sqr)) == 0:
        return 0
    return dot/(math.sqrt(A_sqr)*math.sqrt(B_sqr))
