def Truth_Expectation(v):
    return (v[1] * (v[0] - 0.5) + 0.5)

def Truth_Projection(v, originalTime, targetTime):
    return (v[0], v[1] * (0.8**abs(targetTime - originalTime)))
