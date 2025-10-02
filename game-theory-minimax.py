import math
import time

class MathDuel:
    def __init__(self, start_number=16, allowed_moves=None):
        if allowed_moves is None:
            allowed_moves = [1, 2, 3]
        self.start_number = start_number
        self.allowed_moves = allowed_moves
        self.current_number = start_number
        self.player_turn = 1  # Player 1 starts (MAX)
        self.game_over = False
        self.winner = None
        self.move_history = []

    def reset(self):
        """Reset the game state."""
        self.current_number = self.start_number
        self.player_turn = 1
        self.game_over = False
        self.winner = None
        self.move_history = []

    def make_move(self, move):
        """TODO: Implement making a move.
        - Subtract `move` from current_number
        - Check if the game is over
        - Switch turns
        """
      
        #Subtract `move` from current_number
        self.current_number -= move

        # Check if the game is over
        if self.current_number == 0:
            self.game_over = True
            self.winner = self.player_turn  # the player who made that move to 0, wins
            return

        # switch turns: 
        if self.player_turn == 1:
           self.player_turn = 2
        else:
           self.player_turn = 1

    def evaluate(self):
        """TODO: Implement evaluation function.
        Return:
          +1 if MAX wins
          -1 if MIN wins
           0 if game not over
        """
        if self.winner == 1:
            return +1
        elif self.winner == 2:
            return -1  
        else:
            return 0

    def minimax(self, state, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
        """TODO: Implement minimax with alpha-beta pruning.
        Arguments:
          - state: current number
          - depth: search depth
          - is_maximizing: True if MAX's turn, False if MIN's
        Return:
          Evaluation value for the state
        """
        
        if state == 0:
          if is_maximizing:
            return -1
        else:
          return +1

        #checking for legal moves
        legal_moves = [m for m in self.allowed_moves if m <= state]
        if not legal_moves:
            return -1 if is_maximizing else +1

        if is_maximizing:
            value = -math.inf
            for m in legal_moves:
                child = state - m
                value = max(value, self.minimax(child, depth - 1, False, alpha, beta))
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = math.inf
            for m in legal_moves:
                child = state - m
                value = min(value, self.minimax(child, depth - 1, True, alpha, beta))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    def get_best_move(self):
        """TODO: Use minimax to find the best move for the current player."""
        best_move = None
        best_value = -math.inf if self.player_turn == 1 else math.inf
        legal_moves = [m for m in self.allowed_moves if m <= self.current_number]

        for move in legal_moves:
            next_state = self.current_number - move
            move_value = self.minimax(next_state, depth=10, is_maximizing=(self.player_turn == 2))

            if self.player_turn == 1:  # MAX
                if move_value > best_value:
                    best_value = move_value
                    best_move = move
            else:  # MIN
                if move_value < best_value:
                    best_value = move_value
                    best_move = move

        return best_move

    def print_game_state(self):
        """Print the current state of the game."""
        
        player_name = "Player 1" if self.player_turn == 1 else "AI"
        role = "MAX" if self.player_turn == 1 else "MIN"
        print(f"\nCurrent number: {self.current_number}")
        print(f"{player_name}'s turn ({role})")
        print(f"Allowed moves: {[m for m in self.allowed_moves if m <= self.current_number]}")
        if self.game_over:
            print(f"\nGame over! {player_name} wins!")

