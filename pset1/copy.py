from typing import Type
import random

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print(f'Invalid card: {suit} {rank}')

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return VALUES[self.rank]


# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        ans = "Hand contains "
        for i in range(len(self.cards)):
            ans += str(self.cards[i]) + " "
        return ans
        # return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)
        # add a card object to a hand

    def get_value(self):
        value = 0
        aces = False
        for c in self.cards:
            rank = c.get_rank()
            v = VALUES[rank]
            if rank == 'A': aces = True
            value += v
        if aces and value < 12: value += 10
        return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video


# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        # create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)
        # shuffle the deck

    def deal_card(self):
        return self.deck.pop()
        # deal a card object from the deck

    def __str__(self):
        ans = "The deck: "
        for c in self.deck:
            ans += str(c) + " "
        return ans
        # return a string representing the deck


# define player class
class Player:

    def __init__(self):
        self.matrix = {}
        self.desired_sum = [12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.nums_of_cards = [2, 3, 4, 5, 6, 7]
        for sum in self.desired_sum:
            dict_by_sum = {}
            for num_of_cards in self.nums_of_cards:
                dict_by_num_of_cards = {}
                for face_card_rank in RANKS:
                    dict_by_num_of_cards[face_card_rank] = None
                dict_by_sum[num_of_cards] = dict_by_num_of_cards
            self.matrix[sum] = dict_by_sum
        
        # self.nums_of_cards_list = []
        # to define
        # Scenarios that we can fill without simulating
        # If the sum is 10 or less
        # If the sum is 21
        # Function should check if sum is over 21
        # Function should check if blackjack

    """
    The sim function will perform a boatload of trials and produce as output a matrix of probabilities. 
    For example, in the cell corresponding to a player hand of 18 and a dealer face card of 4, 
    the value may be 235 / 978 meaning that this combination occurred 978 times in the simulation 
    and in only 235 times did the player win if she asked for another card. 
    You would then convert that matrix to boolean values, based on some threshold ratio value. 
    The normal approach would be to use 50%, but you may decide to use a different value.

    You should show the win-loss ratio for every cell in the matrix, not just the overall win-loss ratio from simulation.
    """
    def sim(self, trials: int) -> None:
        # Randomly simulate a game (until it reaches a preset number of trials)

        # Initialize matrix to store win percentages
        percentage_matrix = {}
        for hand_sum in self.desired_sum:
            dict_by_sum = {}
            for num_of_cards in self.nums_of_cards:
                dict_by_num_of_cards = {}
                for face_card_rank in RANKS:
                    dict_by_num_of_cards[face_card_rank] = None
                dict_by_sum[num_of_cards] = dict_by_num_of_cards
            percentage_matrix[hand_sum] = dict_by_sum
        # Initialize matrix to store how many times the scenario has been simulated    
        sim_num_matrix = {}
        for hand_sum in self.desired_sum:
            dict_by_sum = {}
            for num_of_cards in self.nums_of_cards:
                dict_by_num_of_cards = {}
                for face_card_rank in RANKS:
                    dict_by_num_of_cards[face_card_rank] = 0
                dict_by_sum[num_of_cards] = dict_by_num_of_cards
            sim_num_matrix[hand_sum] = dict_by_sum

        num_of_cards_list = [7, 6, 5, 4, 3, 2]
        for num_of_cards in num_of_cards_list:
            for _ in range(trials * (num_of_cards - 1)):
                dealerhand = Hand()
                playerhand = Hand()
                deck = Deck()
                deck.shuffle()
                
                # num_of_cards = round(random_left_skewed)
                # Create playerhand 
                for _ in range(num_of_cards):
                    playerhand.add_card(deck.deal_card())

                hand_sum = playerhand.get_value()
                if hand_sum in self.desired_sum:
                    # Deal card for dealer's facecard
                    face_card = deck.deal_card()
                    face_card_rank = face_card.get_rank()
                    dealerhand.add_card(face_card)

                    # Check if we've simulated checked the combination
                    current_percentage = percentage_matrix[hand_sum][num_of_cards][face_card_rank]
                    
                    stand_win = 0
                    stand_loss = 0
                    hit_win = 0
                    hit_loss = 0
                    
                    # Simulate the dealer's hand
                    while dealerhand.get_value() < 17:
                        dealerhand.add_card(deck.deal_card())
                    stand_win, stand_loss = stand_win_percentage = self.do_stand(dealerhand, playerhand)
                    hit_win, hit_loss = self.do_hit(deck, dealerhand, playerhand, percentage_matrix, num_of_cards, face_card_rank)
                    result = (stand_win/(stand_win + stand_loss), hit_win/(hit_win+hit_loss))

                    if current_percentage is None:
                        # Add the result to the percentage matrix
                        percentage_matrix[hand_sum][num_of_cards][face_card_rank] = result
                        sim_num_matrix[hand_sum][num_of_cards][face_card_rank] += 1
                    else:
                        # sim_num_matrix[hand_sum][num_of_cards][face_card_rank] += 1
                        # Update the value in the percentage matrix (take the average)
                        curr_percentage = percentage_matrix[hand_sum][num_of_cards][face_card_rank] 
                        num = sim_num_matrix[hand_sum][num_of_cards][face_card_rank]
                        updated_result = (((curr_percentage[0] * num) + result[0])/(num+1), ((curr_percentage[1] * num) + result[1])/(num+1))
                        percentage_matrix[hand_sum][num_of_cards][face_card_rank] = updated_result
                        sim_num_matrix[hand_sum][num_of_cards][face_card_rank] += 1
            # print("percentage_matrix:\n", percentage_matrix)

        # Print sim_num_matrix for inspection
        # print("sim_num_matrix:\n", sim_num_matrix)
        # Create boolean matrix based on percentage matrix
        for sum in self.desired_sum:
            dict_by_sum = {}
            for num_of_cards in self.nums_of_cards:
                dict_by_num_of_cards = {}
                for face_card_rank in RANKS:
                    percentages = percentage_matrix[sum][num_of_cards][face_card_rank]
                    if percentages is None:
                        dict_by_num_of_cards[face_card_rank] = False
                    else:
                        stand_win_percentage = percentages[0]
                        hit_win_percentage = percentages[1]
                        if stand_win_percentage >= hit_win_percentage:
                            dict_by_num_of_cards[face_card_rank] = False
                        else:
                            dict_by_num_of_cards[face_card_rank] = True
                dict_by_sum[num_of_cards] = dict_by_num_of_cards
            self.matrix[sum] = dict_by_sum

    def do_stand(self, dealerhand, playerhand):
        player_value = playerhand.get_value()
        if player_value > dealerhand.get_value() or dealerhand.get_value() > 21:
            return 1, 0
        else:
            return 0, 1

    def do_hit(self, deck, dealerhand, playerhand, percentage_matrix, num_of_cards, face_card_rank):
        playerhand.add_card(deck.deal_card())
        current_hand_sum = playerhand.get_value()
        if current_hand_sum > 21:
            return 0, 1
        elif current_hand_sum == 21:
            if dealerhand.get_value() == 21:
                return 0, 1
            else:
                return 1, 0
        else:
            # Look up if the scenario already exists in matrix
            if num_of_cards <= 6:
                current_strat = percentage_matrix[current_hand_sum][num_of_cards + 1][face_card_rank]
                if current_strat is None:
                    # Fall back to default strat of hitting until sum reaches 17
                    while current_hand_sum < 17:
                        playerhand.add_card(deck.deal_card())
                        current_hand_sum = playerhand.get_value()
                    while dealerhand.get_value() < 17:
                        dealerhand.add_card(deck.deal_card())
                    if current_hand_sum > dealerhand.get_value() or dealerhand.get_value() > 21:
                        return 1, 0
                    else:
                        return 0, 1
                else:
                    stand_win_percentage = current_strat[0]
                    hit_win_percentage = current_strat[1]
                    if stand_win_percentage >= hit_win_percentage:
                        return stand_win_percentage, 1 - stand_win_percentage
                    if stand_win_percentage < hit_win_percentage:
                        return hit_win_percentage, 1 - hit_win_percentage
            else:
                # Fall back to default strat of hitting until sum reaches 17
                while current_hand_sum < 17:
                    playerhand.add_card(deck.deal_card())
                    current_hand_sum = playerhand.get_value()
                while dealerhand.get_value() < 17:
                    dealerhand.add_card(deck.deal_card())
                if current_hand_sum > dealerhand.get_value() or dealerhand.get_value() > 21:
                    return 1, 0
                else:
                    return 0, 1

    """
    The hitme function will simply perform a table look-up. 
    You will have a 2 dimensional matrix comprising the optimal strategy for all possible combinations 
    of player hands and dealer face cards. The values in the matrix will simply be true or false. 
    For example,
    hitme(12, 1) ==> true
    If your hand value is 12 and the dealer has an ace, you should ask for another card.
    hitme(18, 4) ==> false
    If your hand value is 18 and the dealer shows a four, you should stay put.
    """
    def hitme(self, playerhand: Type[Hand], dealerfacecard: Type[Card]) -> bool:
        # Calculate the num of cards
        check_hand = playerhand.__str__()
        found_strings = []
        words = check_hand.split()
        for word in words:
            if len(word) == 2:
                found_strings.append(word)
        num_of_cards = len(found_strings)
        #print(found_strings)
        

        # If num of cards is 0 or 1, return True
        if num_of_cards <= 1:
            return True 
        
        # If there are 2 or more cards
        current_value = playerhand.get_value()
        # If the current value of the hand is 11 or less, always hit
        if current_value <= 11:
            return True
        # If the current value of the hand is 21 or more, stand
        elif current_value >= 21:
            return False
        # Else, lookup strategy in matrix and return
        else:
            # self.nums_of_cards_list.append(num_of_cards)
            face_card_rank = dealerfacecard.get_rank()
            return self.matrix[current_value][num_of_cards][face_card_rank]

    """
    Once you have your hitme table installed, run your own simulated games, 
    keeping track of the win/loss ratio. Report your results for simulations of at least 100,000 hands.
    Finally, write a function play(trials) which will play the given number of hands and return your overall winning percentage.
    """
    def play(self, trials: int) -> float:
        # Check if strategy exists
        if not self.matrix:
            raise KeyError("No lookup table found. Run sim first.")
        # Initialize win counter
        win = 0
        # Run simulation
        for _ in range(trials):
            # Initialize player hand and dealer hand
            playerhand = Hand()
            dealerhand = Hand()
            # Initialize deck
            deck = Deck()
            deck.shuffle()

            # Deal initial cards 
            dealerfacecard = deck.deal_card()
            playerhand.add_card(deck.deal_card())
            playerhand.add_card(deck.deal_card())

            # Deal card to player until hit me returns False
            while self.hitme(playerhand, dealerfacecard):
                playerhand.add_card(deck.deal_card())
            
            # Deal dealer's hand
            dealerhand.add_card(dealerfacecard)
            while dealerhand.get_value() < 17:
                dealerhand.add_card(deck.deal_card())
            
            # Compute value of player and dealer
            playervalue = playerhand.get_value()
            dealervalue = dealerhand.get_value()

            # Determine if the player won or not
            if playervalue <= 21 and (playervalue > dealervalue or dealervalue > 21):
                win += 1
        
        # Return the win percentage
        return win/trials * 100

def main():
    score = []
    sim_num = 100000
    play_num = 100000
    # num_of_cards_averages = []
    for i in range (10):
        player = Player()
        player.sim(sim_num)
        score.append(player.play(play_num))
        # num_of_cards_averages.append[sum(player.nums_of_cards_list)/len(player.nums_of_cards_list)]
    print("result for default strat 17 and sim_num", sim_num, "and play_num", play_num)
    print("scores:", score)
    print("average:", sum(score)/len(score))
    # print("average of num of cards passed into hitme for matrix lookup:", sum(num_of_cards_averages)/len(num_of_cards_averages))

if __name__ == "__main__":
    main()

# result for default strat 17 and sim 10000
# scores: [39.47, 40.04, 39.160000000000004, 38.96, 38.6, 38.83, 39.22, 38.92, 38.73, 40.81]
# average: 39.274

# result for default strat 17 and sim 100000
# scores: [39.61, 40.69, 39.879999999999995, 39.23, 39.81, 39.75, 38.85, 40.47, 39.08, 40.64]
# average: 39.800999999999995
    
# result for default strat 18 and sim 10000
# scores: [40.050000000000004, 40.33, 39.17, 39.37, 39.44, 39.12, 39.97, 39.12, 38.62, 39.4]
# average: 39.458999999999996

# result for default strat 18 and sim 100000
# scores: [38.4, 40.45, 39.31, 39.489999999999995, 40.47, 40.1, 37.54, 40.06, 40.25, 41.25]
# average: 39.732
    
# result for default strat 16 and sim 10000
# scores: [40.14, 40.300000000000004, 40.300000000000004, 40.089999999999996, 39.87, 40.1, 41.23, 40.339999999999996, 40.89, 38.940000000000005]
# average: 40.22

# result for default strat 16 and sim 100000
# scores: [40.27, 40.22, 38.879999999999995, 38.35, 39.550000000000004, 40.25, 39.04, 39.5, 39.6, 40.410000000000004]
# average: 39.607000000000006

# FIXED the 
# result for default strat 16 and sim_num 100000 and play_num 100000
# scores: [40.229, 39.668, 40.388000000000005, 40.366, 40.21, 40.319, 39.943, 39.928000000000004, 40.157, 39.45]
# average: 40.065799999999996

# result for default strat 17 and sim_num 100000 and play_num 100000
# scores: [40.696, 41.39, 40.875, 40.933, 40.724, 41.17, 40.809, 40.971999999999994, 40.662, 40.313]
# average: 40.85439999999999

# TODO:
# - improve percentage
    


# from typing import Type
# import random

# # define globals for cards
# SUITS = ('C', 'S', 'H', 'D')
# RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
# VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# # define card class
# class Card:
#     def __init__(self, suit, rank):
#         if (suit in SUITS) and (rank in RANKS):
#             self.suit = suit
#             self.rank = rank
#         else:
#             self.suit = None
#             self.rank = None
#             print(f'Invalid card: {suit} {rank}')

#     def __str__(self):
#         return self.suit + self.rank

#     def get_suit(self):
#         return self.suit

#     def get_rank(self):
#         return self.rank

#     def get_value(self):
#         return VALUES[self.rank]


# # define hand class
# class Hand:
#     def __init__(self):
#         self.cards = []

#     def __str__(self):
#         ans = "Hand contains "
#         for i in range(len(self.cards)):
#             ans += str(self.cards[i]) + " "
#         return ans
#         # return a string representation of a hand

#     def add_card(self, card):
#         self.cards.append(card)
#         # add a card object to a hand

#     def get_value(self):
#         value = 0
#         aces = False
#         for c in self.cards:
#             rank = c.get_rank()
#             v = VALUES[rank]
#             if rank == 'A': aces = True
#             value += v
#         if aces and value < 12: value += 10
#         return value
#         # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
#         # compute the value of the hand, see Blackjack video


# # define deck class
# class Deck:
#     def __init__(self):
#         self.deck = []
#         for s in SUITS:
#             for r in RANKS:
#                 self.deck.append(Card(s, r))
#         # create a Deck object

#     def shuffle(self):
#         random.shuffle(self.deck)
#         # shuffle the deck

#     def deal_card(self):
#         return self.deck.pop()
#         # deal a card object from the deck

#     def __str__(self):
#         ans = "The deck: "
#         for c in self.deck:
#             ans += str(c) + " "
#         return ans
#         # return a string representing the deck


# # define player class
# class Player:

#     def __init__(self):
#         self.matrix = {}
#         self.desired_sum = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#         self.nums_of_cards = [1, 2, 3, 4, 5, 6, 7, 8]
#         for sum in self.desired_sum:
#             dict_by_sum = {}
#             for num_of_cards in self.nums_of_cards:
#                 dict_by_num_of_cards = {}
#                 for face_card_rank in RANKS:
#                     dict_by_num_of_cards[face_card_rank] = None
#                 dict_by_sum[num_of_cards] = dict_by_num_of_cards
#             self.matrix[sum] = dict_by_sum
#         # to define
#         # Scenarios that we can fill without simulating
#         # If the sum is 10 or less
#         # If the sum is 21
#         # Function should check if sum is over 21
#         # Function should check if blackjack

#     """
#     The sim function will perform a boatload of trials and produce as output a matrix of probabilities. 
#     For example, in the cell corresponding to a player hand of 18 and a dealer face card of 4, 
#     the value may be 235 / 978 meaning that this combination occurred 978 times in the simulation 
#     and in only 235 times did the player win if she asked for another card. 
#     You would then convert that matrix to boolean values, based on some threshold ratio value. 
#     The normal approach would be to use 50%, but you may decide to use a different value.

#     You should show the win-loss ratio for every cell in the matrix, not just the overall win-loss ratio from simulation.
#     """
#     def sim(self, trials: int) -> None:
#         # Randomly simulate a game (until it reaches a preset number of trials)
#         # Set convergence criteria
#         # desired_precision = 0.001
#         max_iterations = 10000

#         # Set the parameters for a left-skewed distribution
#         left_bound = 1   # Lower bound
#         mode = 3        # Mode (peak)
#         right_bound = 8  # Upper bound

#         # Generate a random number from a left-skewed distribution
#         random_left_skewed = random.triangular(left_bound, mode, right_bound)
        
#         # Initialize matrix to store win percentages
#         percentage_matrix = {}
#         for hand_sum in self.desired_sum:
#             dict_by_sum = {}
#             for num_of_cards in self.nums_of_cards:
#                 dict_by_num_of_cards = {}
#                 for face_card_rank in RANKS:
#                     dict_by_num_of_cards[face_card_rank] = None
#                 dict_by_sum[num_of_cards] = dict_by_num_of_cards
#             percentage_matrix[hand_sum] = dict_by_sum
#         # sim_num_matrix = Player()

#         num_of_cards_list = [5, 4, 3, 2]
#         for num_of_cards in num_of_cards_list:
#             for i in range(max_iterations):
#                 dealer_hand = Hand()
#                 player_hand = Hand()
#                 deck = Deck()
#                 deck.shuffle()
                
#                 # num_of_cards = round(random_left_skewed)
#                 # Create player_hand 
#                 for _ in range(num_of_cards):
#                     player_hand.add_card(deck.deal_card())
#                 hand_sum = player_hand.get_value()
#                 if hand_sum in self.desired_sum:
#                     # Deal card for dealer's facecard
#                     face_card = deck.deal_card()
#                     face_card_rank = face_card.get_rank()
#                     dealer_hand.add_card(face_card)

#                     # Check if we've simulated checked the combination
#                     print (hand_sum)
#                     current_percentage = percentage_matrix[hand_sum][num_of_cards][face_card_rank]
#                     if current_percentage is None:
#                         stand_win_percentage = self.simulate_stand(deck, dealer_hand, player_hand, trials)
#                         hit_win_percentage = self.simulate_hit(deck, dealer_hand, player_hand, trials, percentage_matrix, num_of_cards, face_card_rank)
#                         result = (stand_win_percentage, hit_win_percentage)
#                         # Add the result to the percentage matrix
#                         percentage_matrix[hand_sum][num_of_cards][face_card_rank] = result

#         # Create boolean matrix based on percentage matrix
#         for sum in self.desired_sum:
#             dict_by_sum = {}
#             for num_of_cards in self.nums_of_cards:
#                 dict_by_num_of_cards = {}
#                 for face_card_rank in RANKS:
#                     percentages = percentage_matrix[sum][num_of_cards][face_card_rank]
#                     if percentages is None:
#                         dict_by_num_of_cards[face_card_rank] = False
#                     stand_win_percentage = percentages[0]
#                     hit_win_percentage = percentages[1]
#                     if stand_win_percentage >= hit_win_percentage:
#                         dict_by_num_of_cards[face_card_rank] = False
#                     else:
#                         dict_by_num_of_cards[face_card_rank] = True
#                 dict_by_sum[num_of_cards] = dict_by_num_of_cards
#             self.matrix[sum] = dict_by_sum

#     def simulate_stand(self, deck, dealer_hand, player_hand, trials):
#         win = 0
#         loss = 0
#         for _ in range(trials):
#             player_value = player_hand.get_value()
#             while dealer_hand.get_value() < 17:
#                 dealer_hand.add_card(deck.deal_card())
#             if player_value > dealer_hand.get_value():
#                 win += 1
#             else:
#                 loss += 1
#         return win/(win+loss)

#     def simulate_hit(self, deck, dealer_hand, player_hand, trials, percentage_matrix, num_of_cards, face_card_rank):
#         win = 0
#         loss = 0
#         for _ in range(trials):
#             player_hand.add_card(deck.deal_card())
#             current_hand_sum = player_hand.get_value()
#             if current_hand_sum > 21:
#                 loss += 1
#             else:
#                 # Look up if the scenario already exists in matrix
#                 current_strat = percentage_matrix[current_hand_sum][num_of_cards + 1][face_card_rank]
#                 if current_strat is None:
#                     # Fall back to default strat of hitting until sum reaches 17
#                     while current_hand_sum < 17:
#                         player_hand.add_card(deck.deal_card())
#                         current_hand_sum = player_hand.get_value()
#                     while dealer_hand.get_value() < 17:
#                         dealer_hand.add_card(deck.deal_card())
#                     if current_hand_sum > dealer_hand.get_value():
#                         win += 1
#                     else:
#                         loss += 1
#                 else:
#                     stand_win_percentage = current_strat[0]
#                     hit_win_percentage = current_strat[1]
#                     if stand_win_percentage >= hit_win_percentage:
#                         win += stand_win_percentage
#                         loss += (1-stand_win_percentage)
#                     if stand_win_percentage < hit_win_percentage:
#                         win += hit_win_percentage
#                         loss += (1-hit_win_percentage)
#         return win/(win+loss)


#     """
#     The hitme function will simply perform a table look-up. 
#     You will have a 2 dimensional matrix comprising the optimal strategy for all possible combinations 
#     of player hands and dealer face cards. The values in the matrix will simply be true or false. 
#     For example,
#     hitme(12, 1) ==> true
#     If your hand value is 12 and the dealer has an ace, you should ask for another card.
#     hitme(18, 4) ==> false
#     If your hand value is 18 and the dealer shows a four, you should stay put.
#     """
#     def hitme(self, playerhand: Type[Hand], dealerfacecard: Type[Card]) -> bool:
#         current_value = playerhand.get_value()
#         if current_value < 11:
#             return True
#         elif current_value >= 21:
#             return False
#         else:
#             num_of_cards = len(playerhand)
#             face_card_rank = dealerfacecard.get_rank()
#             return self.matrix[current_value][num_of_cards][face_card_rank]
#         # use the matrix to decide whether to hit

#     """
#     Once you have your hitme table installed, run your own simulated games, 
#     keeping track of the win/loss ratio. Report your results for simulations of at least 100,000 hands.
#     Finally, write a function play(trials) which will play the given number of hands and return your overall winning percentage.
#     """
#     def play(self, trials: int) -> float:
#         # TODO: REWRITE THIS PART

#         # play out trials with the learned matrix
#         if not self.matrix:
#             raise ValueError("No data to make decisions. Run sim() to obtain strategic data.")
        
#         wins = 0
#         for _ in range(trials):
#             deck = Deck()
#             deck.shuffle()

#             player_hand = Hand()
#             dealer_hand = Hand()

#             # deal
#             player_hand.add_card(deck.deal_card())
#             player_hand.add_card(deck.deal_card())
#             dealer_hand.add_card(deck.deal_card())
#             dealer_hand.add_card(deck.deal_card())

#             # player plays
#             while self.hitme(player_hand, dealer_hand.cards[0]) and player_hand.get_value() <= 21:
#                 player_hand.add_card(deck.deal_card())

#             # dealer plays
#             while dealer_hand.get_value() < 17:
#                 dealer_hand.add_card(deck.deal_card())

#             # determine win
#             if player_hand.get_value() <= 21 and (player_hand.get_value() > dealer_hand.get_value() or dealer_hand.get_value() > 21):
#                 wins += 1

#         return wins / trials * 100

# def main():
#     player = Player()
#     player.sim(1000)
#     player.play(10000)

# if __name__ == "__main__":
#     main()