def choice(round_score, my_score, opponent_score):
    if round_score + my_score >= 100:
        return False
    if my_score > 90:

        return False

    if round_score < 18:
        return True
    else:
        return False
