def choice(round_score, my_score, opponent_score):
    if my_score + round_score >= 100:
            return False
    if opponent_score >= 90:
        if round_score >= 25:
            return True
    if opponent_score + 20 >= my_score:
        if round_score >= 15:
            return False
    if round_score >= 23:
        return False
    else:
        return True
pass
