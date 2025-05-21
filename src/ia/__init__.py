"""IA module integrating ETER neural network and FinRL reinforcement learning."""

from .eter import ETERNetwork
from .finrl_agent import FinRLRLAgent

# Instantiate shared components for application-wide use
eter_network = ETERNetwork()
finrl_agent = FinRLRLAgent()

__all__ = ["ETERNetwork", "FinRLRLAgent", "eter_network", "finrl_agent"]
