# 8-Puzzle Solver using A* Search Algorithm

A Python implementation of the classic 8-puzzle sliding tile game solver using the A* search algorithm with two different heuristic functions.

## Overview

The 8-puzzle is a sliding puzzle that consists of a 3×3 grid with numbered tiles from 1 to 8 and one blank space.

## Features

- **A* Search Algorithm**: Optimal pathfinding algorithm that guarantees the shortest solution
- **Dual Heuristics**: 
  - Manhattan Distance (more efficient)
  - Misplaced Tiles (simpler but less efficient)
- **Performance Metrics**: Tracks nodes expanded, nodes generated, and maximum frontier size
- **Solution Path Display**: Shows step-by-step moves to reach the goal
- **Comprehensive Statistics**: Compares efficiency between heuristics

## Algorithm Components

### Problem Formulation
- **State**: 3×3 grid represented as a flat list of 9 elements (0 represents blank space)
- **Initial State**: Starting configuration of the puzzle
- **Goal State**: Target configuration `[1, 2, 3, 4, 5, 6, 7, 8, 0]`
- **Actions**: Move blank space Up, Down, Left, or Right (when valid)
- **Path Cost**: Number of moves (g-cost = depth)

### Heuristic Functions
1. **Manhattan Distance**: Sum of distances each tile must travel to reach its goal position
2. **Misplaced Tiles**: Count of tiles not in their correct positions

### Search Statistics
- **Nodes Expanded**: Nodes actually processed by the algorithm
- **Nodes Generated**: Total child nodes created (including duplicates)
- **Max Frontier Size**: Maximum number of nodes in the priority queue

## Usage

### Running the Program
```bash
python puzzle.py
```

### Example Output
```
8-Puzzle Solver using A* Search
========================================
Initial State:
1 2 3
4 5 0
7 8 6

Goal State:
1 2 3
4 5 6
7 8 0

Solution found using Manhattan Distance heuristic!
==================================================
Solution length: 3 moves
Nodes expanded: 4
Nodes generated: 12
Max frontier size: 8
```

## Code Structure

- `PuzzleState`: Class representing a puzzle configuration with parent tracking
- `aStar()`: Main A* search algorithm implementation
- `manhattanDistance()`: Manhattan distance heuristic function
- `misplacedTiles()`: Misplaced tiles heuristic function
- `printBoard()`: Display puzzle state in 3×3 grid format
- `printSolution()`: Show complete solution path with statistics
- `isValidMove()`: Validate if a move is legal given current blank position
## Requirements

- Python 3.7+
- Standard libraries: `heapq`, `typing`

## Example Configurations

The program includes hardcoded examples ranging from simple (2-3 moves) to complex puzzles. You can modify the `initialState` and `goalState` variables in the `main()` function to test different configurations.
