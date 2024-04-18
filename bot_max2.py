def choice(round_score, my_score, opponent_score):
  score_difference = my_score - opponent_score
  if my_score+round_score >= 100:
    return False
  if opponent_score >= 90:
    return True
  if score_difference <= -40:
    return round_score < 35
  if -40 < score_difference < -20:
    return round_score < 30
  if -20 < score_difference < 0:
    return round_score < 20
  if 0 < score_difference < 20:
    return round_score < 20
  if score_difference >= 20:
    return round_score < 15
  
  
