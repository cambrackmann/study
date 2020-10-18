
def runner_up_score(scores):
    scores.sort()
    winner = max(scores)
    
    # Pop from scores until max is not winner
    while scores[-1] == winner:
        scores.pop()
    return scores[-1]