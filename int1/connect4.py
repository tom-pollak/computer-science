# Code adapted from Daniel Hernandez and Peter York's MCTS code

import numpy as np
import random

import colorama
from colorama import Fore, Back


class GameState:
    """
    A GameState represents a valid configuration of the 'state' of a game.
    For instance:
        - the position of all the active pieces on a chess board.
        - The position and velocities of all the entities in a 3D world.
    This interface presents the minimal functionality required to implement
    an MCTS-UCT algorithm for a 2 player game.
    """

    def __init__(self):
        self.playerJustMoved = 2  # Game starts with Player 1.

    def Clone(self):
        """
        :returns: deep copy of this GameState
        """
        st = GameState()
        st.playerJustMoved = self.playerJustMoved
        return st

    def DoMove(self, move):
        """
        !! This is the environment's model !!
        Changes the GameState by carrying out the param move.
        :param move: (int) action taken by an agent.
        """
        self.playerJustMoved = 3 - self.playerJustMoved

    def GetMoves(self):
        """:returns: int array with all available moves at this state"""
        pass

    def IsGameOver(self):
        """:returns: whether this GameState is a terminal state"""
        return self.GetMoves() == []

    def GetResult(self, player):
        """
        :param player: (int) player which we want to see if he / she is a winner
        :returns: winner from the perspective of the param player
        """
        pass


class Connect4State(GameState):
    """
    GameState for the Connect 4 game.
    The board is represented as a 2D array (rows and columns).
    Each entry on the array can be:
        - 0 = empty    (.)
        - 1 = player 1 (X)
        - 2 = player 2 (O)
    """

    def __init__(self, width=7, height=6, connect=4):
        self.playerJustMoved = 2
        self.winner = 0  # 0 = no winner, 1 = Player 1 wins, 2 = Player 2 wins.

        self.width = width
        self.height = height
        self.connect = connect
        self.InitializeBoard()

    def InitializeBoard(self):
        """
        Initialises the Connect 4 gameboard.
        """
        self.board = []
        for y in range(self.width):
            self.board.append([0] * self.height)

    def Clone(self):
        """
        Creates a deep copy of the game state.
        NOTE: it is _really_ important that a copy is used during simulations
              Because otherwise MCTS would be operating on the real game board.
        :returns: deep copy of this GameState
        """
        st = Connect4State(width=self.width, height=self.height)
        st.playerJustMoved = self.playerJustMoved
        st.winner = self.winner
        st.board = [self.board[col][:] for col in range(self.width)]
        return st

    def DoMove(self, movecol):
        """
        Changes this GameState by "dropping" a chip in the column
        specified by param movecol.
        :param movecol: column over which a chip will be dropped
        """
        assert (
            movecol >= 0
            and movecol <= self.width
            and self.board[movecol][self.height - 1] == 0
        )
        row = self.height - 1
        while row >= 0 and self.board[movecol][row] == 0:
            row -= 1

        row += 1

        self.playerJustMoved = 3 - self.playerJustMoved
        self.board[movecol][row] = self.playerJustMoved
        if self.DoesMoveWin(movecol, row):
            self.winner = self.playerJustMoved

    def GetMoves(self):
        """
        :returns: array with all possible moves, index of columns which aren't full
        """
        if self.winner != 0:
            return []
        return [
            col for col in range(self.width) if self.board[col][self.height - 1] == 0
        ]

    def DoesMoveWin(self, x, y):
        """
        Checks whether a newly dropped chip at position param x, param y
        wins the game.
        :param x: column index
        :param y: row index
        :returns: (boolean) True if the previous move has won the game
        """
        me = self.board[x][y]
        for (dx, dy) in [(0, +1), (+1, +1), (+1, 0), (+1, -1)]:
            p = 1
            while (
                self.IsOnBoard(x + p * dx, y + p * dy)
                and self.board[x + p * dx][y + p * dy] == me
            ):
                p += 1
            n = 1
            while (
                self.IsOnBoard(x - n * dx, y - n * dy)
                and self.board[x - n * dx][y - n * dy] == me
            ):
                n += 1

            if p + n >= (
                self.connect + 1
            ):  # want (p-1) + (n-1) + 1 >= 4, or more simply p + n >- 5
                return True

        return False

    def IsOnBoard(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def GetResult(self, player):
        """
        :param player: (int) player which we want to see if he / she is a winner
        :returns: winner from the perspective of the param player
        """
        return player == self.winner

    def __repr__(self):
        s = ""
        for x in range(self.height - 1, -1, -1):
            for y in range(self.width):
                s += [
                    Back.WHITE + Fore.WHITE + ".",
                    Back.BLACK + Fore.WHITE + "X",
                    Back.BLACK + Fore.WHITE + "O",
                ][self.board[y][x]]
                s += Fore.RESET
                s += Back.RESET
            s += "\n"
        s += "\n\n\n"
        return s


class TreeNode:
    """Single node of game tree"""

    def __init__(self, state):
        # assert isinstance(Connect4State, state)
        self.state = state
        self.childNodes = []
        self.minimax = None
        self.player = 3 - self.state.playerJustMoved

    def __str__(self):
        return str(self.state)

    def AddChildNode(self, childNode):
        # assert isinstance(TreeNode, childNode)
        self.childNodes.append(childNode)

    def GenerateSuccessors(self):
        for move in self.state.GetMoves():
            newState = self.state.Clone()
            newState.DoMove(move)
            childNode = TreeNode(newState)
            self.AddChildNode(childNode)

    def GenerateMinimax(self, player):
        if self.state.IsGameOver():
            if self.state.winner:
                if self.state.GetResult(player):
                    return 1
                return -1
            return 0

        self.GenerateSuccessors()
        for child in self.childNodes:
            newMinimax = child.GenerateMinimax(player)
            if self.minimax is None:
                self.minimax = newMinimax
            elif self.player == player:  # Max player move
                self.minimax = max(self.minimax, newMinimax)
            elif self.player != player:  # Min player move
                self.minimax = min(self.minimax, newMinimax)
        return self.minimax


def PrintGameResults(state):
    """
    Print match results. Function assumes match is over.
    """
    if state.winner != 0:
        if state.GetResult(state.playerJustMoved) == 1.0:
            print(str(state))
            print("Player " + str(state.playerJustMoved) + " wins!")
        else:
            print(str(state))
            print("Player " + str(3 - state.playerJustMoved) + " wins!")

    else:
        print("Nobody wins!")


def PlayGame(initialState):
    state = initialState
    while not state.IsGameOver():
        # Render
        print(str(state))
        # Capture user input
        if state.playerJustMoved == 1:
            # Player 2 turn
            move = random.choice(state.GetMoves())
        else:
            # Player 1 turn
            move = random.choice(state.GetMoves())
        # Update game state
        state.DoMove(move)

    PrintGameResults(state)


def GenerateGameTree(node):
    print(node, node.GenerateMinimax(node.player))
    node.GenerateSuccessors()
    for s in node.childNodes:
        s.GenerateSuccessors()
        GenerateGameTree(s)


def PlayMinimax(initialState):
    state = initialState
    while not state.IsGameOver():
        node = TreeNode(state)
        node.GenerateSuccessors()
        subTree = {s: s.GenerateMinimax(node.player) for s in node.childNodes}
        sortedSubTree = {
            k: v for k, v in sorted(subTree.items(), key=lambda x: x[1], reverse=True)
        }
        move = list(sortedSubTree.keys())[0]
        state = move.state
        print(state)
    PrintGameResults(state)


env = Connect4State(width=5, height=5)
PlayMinimax(env)
# node = TreeNode(env)
# GenerateGameTree(node)
# PlayGame(env)
