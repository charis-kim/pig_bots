def choice(round_score, my_score, opponent_score):
    if round_score >= 9 and my_score >= (opponent_score - 10):
        return False
    if round_score<= 7 or my_score <= (opponent_score - 15):
        return True
