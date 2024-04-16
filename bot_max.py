def choice(round_score, my_score, opponent_score):
    highest  = 20
    if round_score + my_score >=100:
        return False
    if opponent_score >= my_score + 40:
        highest = 34
    if opponent_score >= my_score+20:
        highest = 23
    if round_score >= highest:
        return False
    return True
