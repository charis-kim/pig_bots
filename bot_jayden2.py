def choice(round_score, my_score, opponent_score):
    if round_score+my_score>=100:
        return False
    return round_score < 19
