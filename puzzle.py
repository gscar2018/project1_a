import heapq
from typing import List, Optional, Set

# Class to represent the state of the 8-puzzle
class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board  
        self.parent = parent  
        self.move = move  
        self.depth = depth  
        self.cost = cost  

    def __lt__(self, other):
        return self.cost < other.cost

# Function to display the board 
def printBoard(board):
    for i in range(3):
        print(board[i*3], board[i*3+1], board[i*3+2])

# Possible moves for the blank tile 
moves = {
    'U': -3,  # Move up
    'D': 3,   # Move down
    'L': -1,  # Move left
    'R': 1    # Move right
}

# Calculate the heuristic Manhattan Distance
def manhattanDistance(board, goalState):
    distance = 0
    for i, tile in enumerate(board):
        if tile != 0:
            goalPos = goalState.index(tile)
            currentRow, currentCol = i // 3, i % 3
            goalRow, goalCol = goalPos // 3, goalPos % 3
            distance += abs(currentRow - goalRow) + abs(currentCol - goalCol)
    return distance

# Calculate misplaced tiles heuristic
def misplacedTiles(board, goalState):
    count = 0
    for i in range(9):
        if board[i] != 0 and board[i] != goalState[i]:
            count += 1
    return count

# Get the new state after a move
def moveTile(board, move, blankPos):
    newBoard = board[:]
    newBlankPos = blankPos + moves[move]
    newBoard[blankPos], newBoard[newBlankPos] = newBoard[newBlankPos], newBoard[blankPos]
    return newBoard

# A* search algorithm - Alternative implementation
def aStar(startState, goalState, heuristicFunc=manhattanDistance):
    # Initialize frontier and explored set
    frontier = [PuzzleState(startState, None, None, 0, heuristicFunc(startState, goalState))]
    explored = set()
    stats = {'expanded': 0, 'generated': 1, 'maxFrontier': 0}  # Start with 1 generated (initial state)
    
    while frontier:
        stats['maxFrontier'] = max(stats['maxFrontier'], len(frontier))
        
        # Get best node from frontier
        current = heapq.heappop(frontier)
        # Goal test
        if current.board == goalState:
            return current, stats['expanded'], stats['generated'], stats['maxFrontier']
        
        # Add to explored
        explored.add(tuple(current.board))
        stats['expanded'] += 1
        
        # Generate children
        blankIndex = current.board.index(0)
        
        # Try each possible move
        for direction, offset in moves.items():
            if not isValidMove(blankIndex, direction):
                continue
                
            # Create new state
            newBoard = current.board[:]
            newBlankIndex = blankIndex + offset
            newBoard[blankIndex], newBoard[newBlankIndex] = newBoard[newBlankIndex], newBoard[blankIndex]
            
            # Skip if already explored
            if tuple(newBoard) in explored:
                continue
            
            # Create child node
            gCost = current.depth + 1
            hCost = heuristicFunc(newBoard, goalState)
            child = PuzzleState(newBoard, current, direction, gCost, gCost + hCost)
            stats['generated'] += 1  # Count every node generated
            
            heapq.heappush(frontier, child)
    
    return None, stats['expanded'], stats['generated'], stats['maxFrontier']

# Helper function for move validation
def isValidMove(blankPos, direction):
    row, col = blankPos // 3, blankPos % 3
    if direction == 'U' and row == 0: return False
    if direction == 'D' and row == 2: return False
    if direction == 'L' and col == 0: return False
    if direction == 'R' and col == 2: return False
    return True

# print the solution path
def printSolution(solution, heuristicName, nodesExpanded, nodesGenerated, maxFrontierSize):
    if not solution:
        print("No solution found!")
        return
        
    path = []
    current = solution
    while current:
        path.append(current)
        current = current.parent
    path.reverse()

    print(f"\nSolution found using {heuristicName} heuristic!")
    print("=" * 50)
    print(f"Solution length: {len(path) - 1} moves")
    print(f"Nodes expanded: {nodesExpanded}")
    print(f"Nodes generated: {nodesGenerated}")
    print(f"Max frontier size: {maxFrontierSize}")
    print()
    
    print("Solution path:")
    print("-" * 20)

    for i, step in enumerate(path):
        if i == 0:
            print("Initial State:")
        else:
            print(f"Move {i}: {step.move}")
        printBoard(step.board)
        if i < len(path) - 1:
            print("↓")
    
    print("Goal reached!")

# this section is irrelevant since i am using hardcoded values, but if i remove this section, 
# the algorithm breaks so i kept it 
def getUserInput():
    print("8-Puzzle Solver using A* Search")
    print("=" * 40)
    print("Enter the puzzle state as 9 numbers (0 for blank space)")
    print("Example: 1 2 3 4 5 6 7 8 0 represents:")
    print("1 2 3")
    print("4 5 6") 
    print("7 8  ")
    print()
    
    def getState(stateName):
        while True:
            try:
                print(f"Enter {stateName} state (9 numbers separated by spaces, choose numbers 0-8):")
                inputStr = input().strip()
                numbers = [int(x) for x in inputStr.split()]
                
                if len(numbers) != 9:
                    print("Error: enter exactly 9 numbers.")
                    continue
                
                if sorted(numbers) != list(range(9)):
                    print("Error: enter  each numbers 0-8.")
                    continue
                
                return numbers
            except ValueError:
                print("Error: enter valid integers.")
    
    initialState = getState("initial")
    goalState = getState("goal")
    
    return initialState, goalState

def main():
    """Main program execution."""

    try:
        # Hardcoded example puzzle states
        # Example 1
        initialState = [1,2,3,4,5,6,0,7,8]  # Simple example - 3 moves
        goalState = [1,2,3,4,5,6,7,8,0]     # Standard goal state


        print("8-Puzzle Solver using A* Search")
        print("=" * 40)
        print("Demonstrating A* algorithm with hardcoded example:")
        print()
        
        print("Initial State:")
        printBoard(initialState)
        print("Goal State:")
        printBoard(goalState)
        
        #Manhattan Distance heuristic
        print("Solving with Manhattan Distance heuristic...")
        solution1, nodesExpanded1, nodesGenerated1, maxFrontier1 = aStar(initialState, goalState, manhattanDistance)
        printSolution(solution1, "Manhattan Distance", nodesExpanded1, nodesGenerated1, maxFrontier1)
        
        print("\n" + "="*60 + "\n")
        
        #Misplaced Tiles heuristic
        print("Solving with Misplaced Tiles heuristic...")
        solution2, nodesExpanded2, nodesGenerated2, maxFrontier2 = aStar(initialState, goalState, misplacedTiles)
        printSolution(solution2, "Misplaced Tiles", nodesExpanded2, nodesGenerated2, maxFrontier2)
        
        # Compare heuristics
        if solution1 and solution2:
            print("\nHeuristic Comparison:")
            print("=" * 30)
            print(f"Manhattan Distance - Nodes expanded: {nodesExpanded1}, Generated: {nodesGenerated1}, Max frontier: {maxFrontier1}")
            print(f"Misplaced Tiles    - Nodes expanded: {nodesExpanded2}, Generated: {nodesGenerated2}, Max frontier: {maxFrontier2}")
            
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
