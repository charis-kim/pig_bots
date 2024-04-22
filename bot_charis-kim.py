def choice(round_score, my_score, opponent_score):
        if my_score >= 90:
            return True

        if round_score < 12:
            return True
        else:
            return False
