import math
from typing import List

class ETERNetwork:
    """Simplified ETER neural network without external dependencies."""

    def __init__(self, input_size: int = 16, hidden_size: int = 8, output_size: int = 2):
        self.input_size = input_size
        # Pesos inicializados de forma determinista para mantener estabilidad
        self.W1 = [[(i + j) * 0.01 for j in range(hidden_size)] for i in range(input_size)]
        self.b1 = [0.0] * hidden_size
        self.W2 = [[(i + j) * 0.01 for j in range(output_size)] for i in range(hidden_size)]
        self.b2 = [0.0] * output_size

    def _tanh(self, x: float) -> float:
        e_pos = math.exp(x)
        e_neg = math.exp(-x)
        return (e_pos - e_neg) / (e_pos + e_neg)

    def encode(self, text: str) -> List[float]:
        """Converts text to a fixed-size numeric vector."""
        codes = [float(ord(c)) for c in text][: self.input_size]
        if len(codes) < self.input_size:
            codes += [0.0] * (self.input_size - len(codes))
        return codes

    def forward(self, x: List[float]) -> List[float]:
        """Propagates the input through two dense layers."""
        h = []
        for j in range(len(self.W1[0])):
            s = sum(x[i] * self.W1[i][j] for i in range(self.input_size)) + self.b1[j]
            h.append(self._tanh(s))
        out = []
        for j in range(len(self.W2[0])):
            s = sum(h[i] * self.W2[i][j] for i in range(len(h))) + self.b2[j]
            out.append(self._tanh(s))
        return out
