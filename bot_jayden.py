def choice(round_score, my_score, opponent_score):
    highest = 15
    if opponent_score == 1:
        highest = 20
    if opponent_score >= 50 and round_score <= my_score-opponent_score+10 and my_score < 45:
        highest = 25
    if opponent_score >= 75 and round_score+my_score < opponent_score+10:
        highest = 20
    if opponent_score-my_score<10:
        highest = 15
    if my_score+round_score>=85 and opponent_score<85:
        highest = 100-my_score
    if round_score+my_score>=100:
        return False
    if round_score > highest:
        return False
    return True
