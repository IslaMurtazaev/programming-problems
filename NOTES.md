# LeetCode Notes:

* **When facing a Hard problem, try to divide it into multiple steps, eg Alien Dictionary could be thought of 3 processes:**
  1. Extracting dependency rules from the input. For example "A must be before C", "X must be before D", or "E must be before B".
  2. Putting the dependency rules into a graph with letters as nodes and dependencies as edges (an adjacency list is best).
  3. Topologically sorting the graph nodes.

* **To traverse graph iteratively use DFS with Stack and BFS with queue**
