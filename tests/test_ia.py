from src.ia import ETERNetwork, FinRLRLAgent


def test_eter_forward():
    eter = ETERNetwork()
    vec = eter.encode("hola")
    out = eter.forward(vec)
    assert len(out) == 2


def test_finrl_agent():
    agent = FinRLRLAgent()
    action = agent.select_action(0)
    assert isinstance(action, int)
    assert 0 <= action < agent.q_table.shape[1]


