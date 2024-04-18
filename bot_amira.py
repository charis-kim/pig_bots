def choice(round_score, my_score, opponent_score):
    if round_score + my_score >= 100:
        return False
    if round_score >= 17:
        return False
    if round_score < 17:
        return True
