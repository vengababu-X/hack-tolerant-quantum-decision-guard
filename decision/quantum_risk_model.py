class QuantumRiskModel:
    def __init__(self):
        self.state = {"LOW": 0.4, "MEDIUM": 0.4, "CRITICAL": 0.2}

    def apply_evidence(self, strength: float):
        shift = strength * 0.3
        self.state["CRITICAL"] += shift
        self.state["LOW"] -= shift / 2
        self.state["MEDIUM"] -= shift / 2
        total = sum(self.state.values())
        for k in self.state:
            self.state[k] = max(self.state[k] / total, 0)

    def collapse(self):
        return max(self.state, key=self.state.get)

    def current(self):
        return self.state
