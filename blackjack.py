import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16


####### DO NOT EDIT ABOVE ########

def deal_card():
    card_value = random.choice(CARD_LABELS)
    return card_value

def get_card_value(card_label):

    if card_label == 'A':
        return ACE_VALUE
    elif card_label == '2':
        return 2
    elif card_label == '3':
        return 3
    elif card_label == '4':
        return 4
    elif card_label == '5':
        return 5
    elif card_label == '6':
        return 6
    elif card_label == '7':
        return 7
    elif card_label == '8':
        return 8
    elif card_label == '9':
        return 9
    elif card_label == '10':
        return FACE_CARD_VALUE
    elif card_label == 'J':
        return FACE_CARD_VALUE
    elif card_label == 'Q':
        return FACE_CARD_VALUE
    elif card_label == 'K':
        return FACE_CARD_VALUE

def deal_cards_to_player():

    first_card = deal_card()
    first_card_value = int(get_card_value(first_card))

    second_card = deal_card()
    second_card_value = int(get_card_value(second_card))

    sum_of_cards = first_card_value + second_card_value

    print("Player drew {} and {}.".format(first_card, second_card))
    print("Player's total is {}.\n".format(sum_of_cards))

    if sum_of_cards < BLACKJACK:
        option = True
        while option:
            hit_stay_option = input("Hit (h) or Stay (s)?\n")
            if hit_stay_option == 'h':
                new_card = deal_card()
                new_card_value = int(get_card_value(new_card))
                sum_of_cards = sum_of_cards + new_card_value
                print("Player drew {}.".format(new_card))
                print("Player's total is {}.\n".format(sum_of_cards))
                if sum_of_cards > BLACKJACK:
                    option = False
            elif hit_stay_option == 's':
                option = False
            else:
                option = True
    return sum_of_cards


def deal_cards_to_dealer():

    first_card = deal_card()
    first_card_value = int(get_card_value(first_card))

    second_card = deal_card()
    second_card_value = int(get_card_value(second_card))

    sum_of_cards = first_card_value + second_card_value

    print("The dealer has {} and {}.".format(first_card, second_card))
    print("Dealer's total is {}.\n".format(sum_of_cards))

    while sum_of_cards <= DEALER_THRESHOLD:
        new_card = deal_card()
        new_card_value = int(get_card_value(new_card))
        sum_of_cards = sum_of_cards + new_card_value
        print("Dealer drew {}.".format(new_card))
        print("Dealer's total is {}.\n".format(sum_of_cards))
    return sum_of_cards


def determine_outcome(player_total, dealer_total):

    if dealer_total > 21:
        print("YOU WIN!\n")
    elif player_total < 21 and dealer_total < 21:
        if player_total > dealer_total:
            print("YOU WIN!\n")
        else:
            print("YOU LOSE!\n")
    elif player_total > 21:
        print("YOU LOSE!\n")

def play_blackjack():

    print("Let's Play Blackjack!\n")
    player = deal_cards_to_player()
    if player < 21:
        dealer = deal_cards_to_dealer()
        determine_outcome(player, dealer)
    elif player == 21:
        print("YOU WIN!")
    elif player > 21:
        print("YOU LOSE!")
    option = True
    while option:
        play_again = input("Play again? (Y/N)\n")
        if play_again == 'Y':
            player = deal_cards_to_player()
            if player < 21:
                dealer = deal_cards_to_dealer()
                determine_outcome(player, dealer)
            elif player == 21:
                print("YOU WIN!")
            elif player > 21:
                print("YOU LOSE!")
        elif play_again == 'N':
            print("Goodbye.")
            option = False
        else:
            option = True


def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """

    # call play_blackjack() here and remove pass below

    play_blackjack()

####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    #Remove comments for next 4 lines to run doctests
    #print("Running doctests...")
    #import doctest
    #doctest.testmod(verbose=True)

    #print("\nRunning program...\n")

    main()
