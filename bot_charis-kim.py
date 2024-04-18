def player_choice(player, round_score):
    # TODO: return True if the player wants to roll again
    #       return False if the player wants to hold
    if player == 0:
        answer = input("Roll or Hold?")
        if answer == "roll":
            return True
        else:
            return False
    else:
        if scores[1] >= 90:
            round_score < 4
            return False

        if round_score < 12:
            return True
        else:
            return False
