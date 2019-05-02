from collections import defaultdict


def make_set(node, parent, size):
    parent[node] = node
    size[node] = 1

def find_set(node, parent):
    if parent[node] == node:
        return node
    return parent[node] = find_set(parent[node])

def union(node_1, node_2):
    parent_node_1 = find_set(node_1, parent)
    parent_node_2 = find_set(node_2, parent)

    if parent_node_1 != parent_node_2:
        if size[parent_node_1] < size[parent_node_2]:
            parent_node_1, parent_node_2 = parent_node_2, parent_node_1
        parent[parent_node_2] = parent_node_1
        size[parent_node_1] += size[parent_node_2]
    
if __name__ == "__main__":
    pass