from collections import defaultdict
from math import inf
import random
import csv
import sys

def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    dim = len(points[0])
    center = []
    for i in range(dim): 
        i_sum=0
        for p in points:
            i_sum += p[i]
        center.append(i_sum/(len(points)))
    return center


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    with_assign = list(zip(dataset, assignments))
    unique_assigns = []
    for x in assignments:
        if x not in unique_assigns:
            unique_assigns.append(x)

    centers = []
    for x in unique_assigns:
        cluster = []
        for point in with_assign:
            if point[-1]==x:
                cluster.append(point[0])
        center = point_avg(cluster)
        centers.append(center)
    return centers

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    sum_of_sqr = 0
    for x, y in list(zip(a, b)):
        sum_of_sqr += (y-x)** 2
    return sum_of_sqr ** 0.5

def distance_squared(a, b):
    return distance(a, b) ** 2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.sample(dataset, k = k)


def cost_function(clustering):
    sum_sqr = 0
    for assign in clustering:
        center = point_avg(clustering[assign])
        for point in clustering[assign]:
            sum_sqr += distance_squared(point, center)
    return sum_sqr


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centers = []
    centers.append(random.choice(dataset))
    for i in range(1,k):
        dist = []
        probs = []
        cumsum = []
        for point in dataset:   
            d = sys.maxsize
            for j in range(len(centers)):
                temp_dist = distance(point, centers[j])
                dist.append(min(d, temp_dist))
            d2 = sum(dist)
            prob = d/d2
            probs.append(prob)
            cumsum.append(sum(probs))
        rdm = random.randrange(0,1)
        for p in cumsum:
            if rdm < p:
                i = j
                break
        centers.append(dataset[i])
    return centers  

def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering

def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
