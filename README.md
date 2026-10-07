# DVA340 — Artificial Intelligence (Mälardalen University, spring 2025)

My five laboratory projects from the Erasmus semester in Västerås: code and the report I handed in for each.
(Private archive. The reports of projects 1, 3, 4 and 5 are also public in
[youyou354/Projects](https://github.com/youyou354/Projects).)

| # | Project | Code | Report |
|---|---------|------|--------|
| 1 | 0/1 knapsack as a search tree (BFS and DFS) · shortest path Málaga → Valladolid (greedy best-first and A*) | [`knapsack_bfs_dfs.py`](project1-search/knapsack_bfs_dfs.py), [`shortest_path_greedy_astar.py`](project1-search/shortest_path_greedy_astar.py) | [report](project1-search/report.pdf) |
| 2 | Sudoku by backtracking, ten grids | [`sudoku_backtracking.py`](project2-sudoku/sudoku_backtracking.py) | [report](project2-sudoku/report.pdf) |
| 3 | Travelling salesman on 52 cities: genetic algorithm and ant colony | [`tsp_genetic_algorithm.py`](project3-tsp/tsp_genetic_algorithm.py), [`tsp_ant_colony.py`](project3-tsp/tsp_ant_colony.py) | [report](project3-tsp/report.pdf) |
| 4 | Mancala client for the course tournament (minimax, depth 2) | [`mancala_client.py`](project4-mancala/mancala_client.py) | [report](project4-mancala/report.pdf) |
| 5 | MNIST digit classifier, Keras (784-128-64-32-10, SGD) | [`mnist_keras.py`](project5-mnist/mnist_keras.py) | [report](project5-mnist/report.pdf) |

The code files are the originals, unchanged (they were handed in as `.txt`). Notes:

- Project 5 reads `assignment5.csv` (42,000 labelled digit images, 785 columns); the data is not part of this archive.
- Project 4 expects the course's Mancala server on `127.0.0.1:30000`.

## On the portfolio

Each project runs in the browser on [my portfolio](https://youyou354.github.io/) — knapsack, the map of Spain,
sudoku, the travelling salesman, Mancala and the digit classifier — ported to JavaScript from these files
(for MNIST the network is retrained with the same recipe, since the original model was not saved).
