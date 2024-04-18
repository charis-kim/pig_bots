def choice(round_score, my_score, opponent_score):
  total_score = my_score + round_score
  difference = my_score - opponent_score
  if total_score >= 100:
      return False
  elif difference >= 20:
      stop_point = 25+2
  elif difference >= 40:
      stop_point = 20+2
  elif difference <= -20:
      stop_point = 30+2
  elif difference <= -40:
      stop_point = 35+2
  else:
      stop_point = 25+2
  if round_score >= stop_point:
      return False
