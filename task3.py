#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

def calculate_cluster_points(cluster):
    return sum(int(point) for point in cluster)

def find_cluster_with_largest_sum(filename):
    largest_sum = 0
    current_cluster = []
    
    with open(filename, 'r') as file:
        clusters = file.read().strip().split('\n\n')
        for cluster in clusters:
            points = cluster.strip().split('\n')
            cluster_sum = calculate_cluster_points(points)
            if cluster_sum > largest_sum:
                largest_sum = cluster_sum
                current_cluster = points

    return current_cluster, largest_sum

filename = "task03.txt"  
largest_cluster, largest_sum = find_cluster_with_largest_sum(filename)

print("Largest cluster with sum:", largest_sum)
for point in largest_cluster:
    print(point)
