#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

def clusterpoints(cluster):
    return sum(map(int, cluster))

def find_largest(file_path):
    largest_sum = 0
    current_cluster = []
    largest_cluster = []
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            if line:
                current_cluster.append(line)
            else:
                cluster_sum = clusterpoints(current_cluster)
                if cluster_sum > largest_sum:
                    largest_sum = cluster_sum
                    largest_cluster = current_cluster
                current_cluster = []

    
    cluster_sum = clusterpoints(current_cluster)
    if cluster_sum > largest_sum:
        largest_cluster = current_cluster

    return largest_cluster, largest_sum

file_path = "task03.txt"  
largest_cluster, largest_sum = find_largest(file_path)

print("Largest cluster with sum:", largest_sum)
for point in largest_cluster:
    print(point)