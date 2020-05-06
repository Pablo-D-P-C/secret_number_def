from def_num import play_game, get_score_list, get_top_scores

while True:
    selection = input("""Hello, What would you like to do?
    A) Play a new game
    B) Best scores
    C) Exit
    """)

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print("Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were {4}"\
                  .format(score_dict.get("player"),
                          str(score_dict.get("attempts")),
                          score_dict.get("date"),
                          score_dict.get("secret"),
                          score_dict.get("wrong_guesses")))
    else:
        print("Leaving the Game......")
        break