def choice(round_score, my_score, opponent_score):
    if round_score + my_score >= 100:
        return False
    if opponent_score >= 85:
        if my_score <= 80:
            return True
    if my_score + round_score >= 90:
        return False
    if round_score >= 20:
        return False
    if round_score <= 20:
        return True
