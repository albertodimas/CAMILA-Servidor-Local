import random
from typing import List
import numpy as np

class FinRLRLAgent:
    """Minimal Q-learning agent without external dependencies."""

    def __init__(self, n_states: int = 10, n_actions: int = 2, alpha: float = 0.1, gamma: float = 0.9, epsilon: float = 0.1):
        # Q-table stored as minimal ndarray to expose `.shape` attribute
        self.q_table = np.array([[0.0 for _ in range(n_actions)] for _ in range(n_states)])
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def select_action(self, state: int) -> int:
        """Epsilon-greedy action selection."""
        if random.random() < self.epsilon:
            return random.randrange(len(self.q_table[state]))
        q_values = self.q_table[state]
        # Selecciona la acción con el valor Q más alto usando numpy
        return int(np.argmax(q_values))

    def update(self, state: int, action: int, reward: float, next_state: int) -> None:
        """Single-step Q-learning update."""
        best_next = max(self.q_table[next_state])
        td = reward + self.gamma * best_next - self.q_table[state][action]
        self.q_table[state][action] += self.alpha * td

    # Added for clarity: expose decision method used by the main application
    def decide(self, state: int) -> int:
        """Return an action for the given state using current policy."""
        return self.select_action(state)
