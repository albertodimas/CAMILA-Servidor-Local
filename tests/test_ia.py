from src.ia import ETERNetwork, FinRLRLAgent


def test_eter_forward():
    eter = ETERNetwork()
    vec = eter.encode("hola")
    out = eter.forward(vec)
    assert len(out) == 2


def test_finrl_agent():
    agent = FinRLRLAgent()
    action = agent.select_action(0)
    assert action in {0, 1}
    agent.update(0, action, reward=1.0, next_state=1)


