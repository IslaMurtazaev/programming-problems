class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return self.val

    def __repr__(self):
        return self.val


"""
Given a binary tree of N nodes, however, there’s only one edge breaking the binary tree, find it and eliminate it


Clarifications:

Node {
	val: int (not unique)
	left: Node
	right: Node
}

input: we are given root node
				a
                    b      e
                 d    e (e is the same vertice)


		a
 	   b     c
    	d    e
            a (remove this edge)



Approach:

Traverse a tree and find a breaking edge => remove it

Use bfs to store seen nodes
if curr node is already seen => remove the edge


TC = O(v)
SC = O(v)


Implementation:

  a
 b  c
c
"""
import collections


def remove_breaking_edge(root):  # root = a
    if not root:
        return

    seen = {root}  # = [a, b, c]
    queue = collections.deque([root])  # = [c]

    while queue:
        node = queue.popleft()  # = b

        # check if one of the children is in seen
        if node.left:
            if node.left in seen:  # false
                node.left = None
                return

        seen.add(node.left)
        queue.append(node.left)

        if node.right:
            if node.right in seen:  # second c
                node.right = None
                return

        seen.add(node.right)
        queue.append(node.right)



"""
Return all edges we can remove to make the binary tree work.
Before: a->b, a->c, b->d, c->d. Returning b->d or c->d is fine to me.
After: Return b->d and c->d. [[b, d], [c, d]]

there is only one breaking edge
there are no self loops


There are 3 cases:
1. No loop  
return edges from parent [a,b], [c,b]                a
                                                    / \
                                                   b   c
                                                        \
                                                         b

2. Loop
return only one edge [c,b]              a
                                         \
                                          b <-
                                           \ /
                                            c

3. Loop with root
return edge from root to branch                   a <-
with the loop to root and edge itself            / \ /
[a,b],[b,a]                                     c   b
"""


def dfs(node, parent_nodes, seen):
    if node in seen:
        return node
    seen.add(node)

    right = None
    if node.right:
        parent_nodes[node.right].append(node)
        right = dfs(node.right, parent_nodes, seen)

    left = None
    if node.left:
        parent_nodes[node.left].append(node)
        left = dfs(node.left, parent_nodes, seen)

    return right or left


def find_breaking_edges(root):  # root = a
    """
    store seen nodes to find the breaking edge
    """
    parent_nodes = collections.defaultdict(list)

    # find breaking node
    breaking_node = dfs(root, parent_nodes, set())

    # Handle loop
    has_loop = False
    node = breaking_node
    while node in parent_nodes:
        if breaking_node in parent_nodes[node]:
            has_loop = True
            break
        node = parent_nodes[node][-1]

    # case 1
    if not has_loop:
        return [[parent.val, breaking_node.val] for parent in parent_nodes[breaking_node]]
    # case 2
    if breaking_node != root:
        return [[parent_nodes[breaking_node][1].val, breaking_node.val]]
    # case 3
    else:
        return [[root.val, node.val], [node.val, root.val]]


# case 1
nodeA = Node('a')
nodeB = Node('b')
nodeC = Node('c')

nodeA.right = nodeB
nodeA.left = nodeC
nodeC.left = nodeB

assert find_breaking_edges(nodeA) == [['a', 'b'], ['c', 'b']]

# case 2
nodeA = Node('a')
nodeB = Node('b')
nodeC = Node('c')

nodeA.right = nodeB
nodeB.right = nodeC
nodeC.right = nodeB

assert find_breaking_edges(nodeA) == [['c', 'b']]

# case 3
nodeA = Node('a')
nodeB = Node('b')
nodeC = Node('c')

nodeA.right = nodeB
nodeA.left = nodeC
nodeB.right = nodeA

print('find_breaking_edges', find_breaking_edges(nodeA))
assert find_breaking_edges(nodeA) == [['a', 'b'], ['b', 'a']]
