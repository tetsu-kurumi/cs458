from typing import Type
import random
import time

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
        self.nums_of_cards = [2, 3, 4, 5, 6]
        self.ace_counts = [0, 1, 2, 3, 4]
        for sum in self.desired_sum:
            dict_by_sum = {}
            for num_of_cards in self.nums_of_cards:
                dict_by_num_of_cards = {}
                for face_card_rank in RANKS:
                    dict_by_face_card_rank = {}
                    for ace_count in self.ace_counts:
                        dict_by_face_card_rank[ace_count] = None
                    dict_by_num_of_cards[face_card_rank] = dict_by_face_card_rank
                dict_by_sum[num_of_cards] = dict_by_num_of_cards
            self.matrix[sum] = dict_by_sum
        
        # When we have no data on a certain situation, default to simple strategy of 
        # hitting until sum is 17
        self.defaut_strat = 17

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
        # Set iteration number, which will be overrided when the number of simulation reaches int trials (check max_trials)
        iter_num = round(trials * 0.67)
        # Initialize matrix to store win percentages
        percentage_matrix = {}
        for sum in self.desired_sum:
            dict_by_sum = {}
            for num_of_cards in self.nums_of_cards:
                dict_by_num_of_cards = {}
                for face_card_rank in RANKS:
                    dict_by_face_card_rank = {}
                    for ace_count in self.ace_counts:
                        dict_by_face_card_rank[ace_count] = None
                    dict_by_num_of_cards[face_card_rank] = dict_by_face_card_rank
                dict_by_sum[num_of_cards] = dict_by_num_of_cards
            percentage_matrix[sum] = dict_by_sum
        # Initialize matrix to store how many times the scenario has been simulated    
        sim_num_matrix = {}
        for sum in self.desired_sum:
            dict_by_sum = {}
            for num_of_cards in self.nums_of_cards:
                dict_by_num_of_cards = {}
                for face_card_rank in RANKS:
                    dict_by_face_card_rank = {}
                    for ace_count in self.ace_counts:
                        dict_by_face_card_rank[ace_count] = 0
                    dict_by_num_of_cards[face_card_rank] = dict_by_face_card_rank
                dict_by_sum[num_of_cards] = dict_by_num_of_cards
            sim_num_matrix[sum] = dict_by_sum

        num_of_cards_list = [6, 5, 4, 3, 2]
        # divide up the trials into num_of_cards_list
        max_trials = trials
        for num_of_cards in num_of_cards_list:
            # End the simulation if we've reached max_trials specified in the input to the function
            if max_trials <= 0:
                print("reached max_iter num for simulation")
                break
            for _ in range(iter_num): # while i < (round((trials/5) * (1/num_of_cards))): #(round(trials/6)): # * ((9-num_of_cards)/27))): #while i < (round((trials/num_of_cards) * 2)): #(round(trials * (num_of_cards/27))):
                # If we reach the max iteration, stop the simulation
                if max_trials <= 0:
                    print("reached max_iter num for simulation")
                    break
                dealerhand = Hand()
                playerhand = Hand()
                ace_count = 0
                deck = Deck()
                deck.shuffle()
            
                # Create playerhand 
                for _ in range(num_of_cards):
                    card = deck.deal_card()
                    if card.get_rank() == 'A':
                        # print("checkpoint, ace_count is", ace_count)
                        ace_count += 1
                    playerhand.add_card(card)    

                hand_sum = playerhand.get_value()
                if hand_sum in self.desired_sum:
                    max_trials -= 1
                    # print("Simulating ", playerhand)
                    # Deal card for dealer's facecard
                    face_card = deck.deal_card()
                    face_card_rank = face_card.get_rank()
                    dealerhand.add_card(face_card)

                    # Check if we've simulated checked the combination
                    current_percentage = percentage_matrix[hand_sum][num_of_cards][face_card_rank][ace_count]
                    
                    stand_win = 0
                    stand_loss = 0
                    hit_win = 0
                    hit_loss = 0
                    
                    # Simulate the dealer's hand
                    while dealerhand.get_value() < 17:
                        dealerhand.add_card(deck.deal_card())

                    stand_win, stand_loss = stand_win_percentage = self.do_stand(dealerhand, playerhand)
                    hit_win, hit_loss = self.do_hit(deck, dealerhand, playerhand, percentage_matrix, num_of_cards, face_card_rank, ace_count)
                    result = (stand_win/(stand_win + stand_loss), hit_win/(hit_win+hit_loss))

                    if current_percentage is None:
                        # Add the result to the percentage matrix
                        percentage_matrix[hand_sum][num_of_cards][face_card_rank][ace_count] = result
                        sim_num_matrix[hand_sum][num_of_cards][face_card_rank][ace_count] += 1
                    else:
                        # Update the value in the percentage matrix (take the average)
                        curr_percentage = percentage_matrix[hand_sum][num_of_cards][face_card_rank][ace_count] 
                        num = sim_num_matrix[hand_sum][num_of_cards][face_card_rank][ace_count]
                        updated_result = (((curr_percentage[0] * num) + result[0])/(num+1), ((curr_percentage[1] * num) + result[1])/(num+1))
                        percentage_matrix[hand_sum][num_of_cards][face_card_rank][ace_count] = updated_result
                        sim_num_matrix[hand_sum][num_of_cards][face_card_rank][ace_count] += 1
                    # i += 1
        # print("sim_num_matrix:", sim_num_matrix)
        
        # higher_ranks = ('A', '7', '8', '9', 'T', 'J', 'Q', 'K')
        # lower_ranks = ('2', '3', '4', '5', '6')
        # print("percentage_matrix:\n", percentage_matrix)
        # Create boolean matrix based on percentage matrix
        for sum in self.desired_sum:
            dict_by_sum = {}
            for num_of_cards in self.nums_of_cards:
                dict_by_num_of_cards = {}
                for face_card_rank in RANKS:
                    dict_by_face_card_rank = {}
                    for ace_count in self.ace_counts:
                        percentages = percentage_matrix[sum][num_of_cards][face_card_rank][ace_count]
                        # Set boolean randomly if not defined
                        if percentages is None:
                            dict_by_face_card_rank[ace_count] = False
                            # randnum = random.random()
                            # # hit more if it's 7-A
                            # if face_card_rank in higher_ranks:
                            #     if randnum > 0.8:
                            #         dict_by_face_card_rank[ace_count] = False
                            #     else:
                            #         dict_by_face_card_rank[ace_count] = True
                            # # stand more if it's 2-6
                            # if face_card_rank in lower_ranks:
                            #     if randnum > 0.8:
                            #         dict_by_face_card_rank[ace_count] = True
                            #     else:
                            #         dict_by_face_card_rank[ace_count] = False
                        else:
                            stand_win_percentage = percentages[0]
                            hit_win_percentage = percentages[1]
                            if stand_win_percentage >= hit_win_percentage:
                                dict_by_face_card_rank[ace_count] = False
                            else:
                                dict_by_face_card_rank[ace_count] = True
                    dict_by_num_of_cards[face_card_rank] = dict_by_face_card_rank
                dict_by_sum[num_of_cards] = dict_by_num_of_cards
            self.matrix[sum] = dict_by_sum
        # print("self.matrix:", self.matrix)

    def do_stand(self, dealerhand, playerhand):
        player_value = playerhand.get_value()
        if player_value > dealerhand.get_value() or dealerhand.get_value() > 21:
            return 1, 0
        else:
            return 0, 1

    def do_hit(self, deck, dealerhand, playerhand, percentage_matrix, num_of_cards, face_card_rank, ace_count):
        card = deck.deal_card()
        playerhand.add_card(card)
        if card.get_rank() == 'A':
            ace_count += 1
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
            if num_of_cards <= 5:
                current_strat = percentage_matrix[current_hand_sum][num_of_cards + 1][face_card_rank][ace_count]
                if current_strat is None:
                    # Fall back to default strat of hitting until sum reaches 17
                    while current_hand_sum < self.defaut_strat:
                        playerhand.add_card(deck.deal_card())
                        current_hand_sum = playerhand.get_value()
                    while dealerhand.get_value() < 17:
                        dealerhand.add_card(deck.deal_card())
                    if current_hand_sum <= 21 and (current_hand_sum > dealerhand.get_value() or dealerhand.get_value() > 21):
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
                while current_hand_sum < self.defaut_strat:
                    playerhand.add_card(deck.deal_card())
                    current_hand_sum = playerhand.get_value()
                while dealerhand.get_value() < 17:
                    dealerhand.add_card(deck.deal_card())
                if current_hand_sum <= 21 and (current_hand_sum > dealerhand.get_value() or dealerhand.get_value() > 21):
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
        # print("found_strings:", found_strings)
        ace_count = 0
        for string in found_strings:
            for char in string:
                if char == 'A':
                    ace_count += 1
        num_of_cards = len(found_strings)
        
        # If num of cards is 0 or 1, hit
        if num_of_cards <= 1:
            return True 
        
        # If there are 2 or more cards
        current_value = playerhand.get_value()

        # If num of cards is 8 or more, resort to default strategy
        if num_of_cards >= 7:
            if current_value < self.defaut_strat:
                return True
            else:
                return False

        # If the current value of the hand is 11 or less, always hit
        if current_value <= 11:
            return True
        # If the current value of the hand is 21 or more, stand
        elif current_value >= 21:
            return False
        # Else, lookup strategy in matrix and return
        else:
            face_card_rank = dealerfacecard.get_rank()
            return self.matrix[current_value][num_of_cards][face_card_rank][ace_count]

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
        return win/trials

def main():
    score = []
    sim_num = 100000
    play_num = 100000
    cpu_time = []
    for i in range (1):
        print("iteration", i)
        player = Player()

        # Record the starting CPU time
        start_cpu_time = time.process_time()
        player.sim(sim_num)
        # Record the ending CPU time
        end_cpu_time = time.process_time()
         # Calculate the CPU time used
        cpu_time_used = end_cpu_time - start_cpu_time
        cpu_time.append(cpu_time_used)

        score.append(player.play(play_num) * 100)
    print("result for default strat 17 and sim_num", sim_num, "and play_num", play_num)
    print("scores:", score)
    print("average:", sum(score)/len(score))
    print("average cputime:", sum(cpu_time)/len(cpu_time))

if __name__ == "__main__":
    main()

# TODO:
# - Can I increase the win percentage

        # # Set the parameters for a left-skewed distribution
        # left_bound = 1   # Lower bound
        # mode = 3        # Mode (peak)
        # right_bound = 8  # Upper bound

        # # Generate a random number from a left-skewed distribution
        # random_left_skewed = random.triangular(left_bound, mode, right_bound)

# size of 11_combs: 44
# fournum_count: 1
# tracker: 390
# valid_samples: 170
# odd_values [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21]
# size of 12_combs: 59
# fournum_count: 10
# tracker: 0
# valid_samples: 641
# odd_values []
# size of 13_combs: 74
# fournum_count: 12
# tracker: 0
# valid_samples: 811
# odd_values []
# size of 14_combs: 96
# fournum_count: 18
# tracker: 0
# valid_samples: 1023
# odd_values []
# size of 15_combs: 119
# fournum_count: 21
# tracker: 0
# valid_samples: 1284
# odd_values []
# size of 16_combs: 152
# fournum_count: 31
# tracker: 0
# valid_samples: 1590
# odd_values []
    

#archive
    
    # class Util:
#     @staticmethod
#     def find_combinations(self, deck, target, hand=Hand()):
#         current_sum = hand.get_value()

#         if current_sum == target:
#             print(hand)
#         if current_sum >= target:
#             return

#         for i in range(len(numbers)):
#             remaining_numbers = numbers[:i] + numbers[i+1:]
#             self.find_combinations(remaining_numbers, target, partial + [numbers[i]])

#     # Example usage:
#     for i in range(2, 12): 
#         # numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#         # number_of_numbers = {1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:16, 11:4}
#         deck = Deck()
#         target_sum = i
#         find_combinations(deck, target_sum)
#         print(f"Combinations of numbers that sum up to {target_sum} (using each number at most once, treating sorted combinations as the same):")

    # def combinations(self, cards, size, start=0, current=[]):
    #     if size == 0:
    #         yield current
    #         return
    #     for i in range(start, len(cards)):
    #         yield from self.combinations(cards, size - 1, i + 1, current + [cards[i]])

    # @staticmethod
    # def get_all_combinations(self, start_size=2, end_size=11):
    #     for size in range(start_size, end_size + 1):
    #         for combo in self.combinations(self.deck, size):
    #             yield combo

    # #face_card = Card('D', '3')
    
    # for i in range (11, 17):
    #     tracker = 0
    #     valid_samples = 0
    #     fournum_count = 0
    #     odd_values = []
    #     for comb in combs_list[i-11]:
    #         for face_card in dealer_face_cards:
    #             # Initialize dealer and player's hand
    #             dealer_hand = Hand()
    #             player_hand = Hand()
                
    #             # Create player_hand
    #             count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11: 0}
    #             for player_card in comb:
    #                 suit_idx = count[player_card]
    #                 card = Card(SUITS[suit_idx], values_flipped[player_card])
    #                 count[player_card] += 1
    #                 if card.get_value() == 1:
    #                     count[11] += 1
    #                 if card.get_value() == 11:
    #                     count[1] += 1
    #                 player_hand.add_card(card)
                
    #             # Do not go through the hands that are already 21 in value
    #             if player_hand.get_value() != i:
    #                 tracker += 13
    #                 odd_values.append(player_hand.get_value())
    #                 break

    #             # Set dealer_face card, but check if it is already used in player_cards
    #             if count[face_card.get_value()] < 4:
    #                 dealer_hand.add_card(face_card)
    #             else:
    #                 fournum_count += 1
    #                 break

    #             # Display the hands
    #             valid_samples += 1
    #             # print("Player's hand:", player_hand)
    #             # print("Player's hand value:", player_hand.get_value())
    #             # print("Dealer's hand:", dealer_hand)
    #     print(f"size of {i}_combs:", len(combs_list[i-11]))
    #     print("fournum_count:", fournum_count)
    #     print("tracker:", tracker)
    #     print("valid_samples:", valid_samples)
    #     print("odd_values", odd_values)

        # eleven_combs = [[1, 1, 1, 1, 2, 2, 3], [1, 1, 1, 1, 2, 5], [1, 1, 1, 1, 3, 4], [1, 1, 1, 1, 7], [1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 2, 2, 4], [1, 1, 1, 2, 3, 3], [1, 1, 1, 2, 6], [1, 1, 1, 3, 5], [1, 1, 1, 4, 4], [1, 1, 1, 8], [1, 1, 2, 2, 2, 3], [1, 1, 2, 2, 5], [1, 1, 2, 3, 4], [1, 1, 2, 7], [1, 1, 3, 3, 3], [1, 1, 3, 6], [1, 1, 4, 5], [1, 1, 9], [1, 2, 2, 2, 4], [1, 2, 2, 3, 3], [1, 2, 2, 6], [1, 2, 3, 5], [1, 2, 4, 4], [1, 2, 8], [1, 3, 3, 4], [1, 3, 7], [1, 4, 6], [1, 5, 5], [1, 10], [2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 2, 3, 4], [2, 2, 7], [2, 3, 3, 3], [2, 3, 6], [2, 4, 5], [2, 9], [3, 3, 5], [3, 4, 4], [3, 8], [4, 7], [5, 6], [11]]

        # twelve_combs = [[1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 1, 2, 2, 4], [1, 1, 1, 1, 2, 3, 3], [1, 1, 1, 1, 2, 6], [1, 1, 1, 1, 3, 5], [1, 1, 1, 1, 4, 4], [1, 1, 1, 1, 8], [1, 1, 1, 2, 2, 2, 3], [1, 1, 1, 2, 2, 5], [1, 1, 1, 2, 3, 4], [1, 1, 1, 2, 7], [1, 1, 1, 3, 3, 3], [1, 1, 1, 3, 6], [1, 1, 1, 4, 5], [1, 1, 1, 9], [1, 1, 2, 2, 2, 4], [1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 6], [1, 1, 2, 3, 5], [1, 1, 2, 4, 4], [1, 1, 2, 8], [1, 1, 3, 3, 4], [1, 1, 3, 7], [1, 1, 4, 6], [1, 1, 5, 5], [1, 1, 10], [1, 2, 2, 2, 2, 3], [1, 2, 2, 2, 5], [1, 2, 2, 3, 4], [1, 2, 2, 7], [1, 2, 3, 3, 3], [1, 2, 3, 6], [1, 2, 4, 5], [1, 2, 9], [1, 3, 3, 5], [1, 3, 4, 4], [1, 3, 8], [1, 4, 7], [1, 5, 6], [1, 11], [2, 2, 2, 2, 4], [2, 2, 2, 3, 3], [2, 2, 2, 6], [2, 2, 3, 5], [2, 2, 4, 4], [2, 2, 8], [2, 3, 3, 4], [2, 3, 7], [2, 4, 6], [2, 5, 5], [2, 10], [3, 3, 3, 3], [3, 3, 6], [3, 4, 5], [3, 9], [4, 4, 4], [4, 8], [5, 7], [6, 6]]

        # thirteen_combs = [[1, 1, 1, 1, 2, 2, 2, 3], [1, 1, 1, 1, 2, 2, 5], [1, 1, 1, 1, 2, 3, 4], [1, 1, 1, 1, 2, 7], [1, 1, 1, 1, 3, 3, 3], [1, 1, 1, 1, 3, 6], [1, 1, 1, 1, 4, 5], [1, 1, 1, 1, 9], [1, 1, 1, 2, 2, 2, 4], [1, 1, 1, 2, 2, 3, 3], [1, 1, 1, 2, 2, 6], [1, 1, 1, 2, 3, 5], [1, 1, 1, 2, 4, 4], [1, 1, 1, 2, 8], [1, 1, 1, 3, 3, 4], [1, 1, 1, 3, 7], [1, 1, 1, 4, 6], [1, 1, 1, 5, 5], [1, 1, 1, 10], [1, 1, 2, 2, 2, 2, 3], [1, 1, 2, 2, 2, 5], [1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 7], [1, 1, 2, 3, 3, 3], [1, 1, 2, 3, 6], [1, 1, 2, 4, 5], [1, 1, 2, 9], [1, 1, 3, 3, 5], [1, 1, 3, 4, 4], [1, 1, 3, 8], [1, 1, 4, 7], [1, 1, 5, 6], [1, 1, 11], [1, 2, 2, 2, 2, 4], [1, 2, 2, 2, 3, 3], [1, 2, 2, 2, 6], [1, 2, 2, 3, 5], [1, 2, 2, 4, 4], [1, 2, 2, 8], [1, 2, 3, 3, 4], [1, 2, 3, 7], [1, 2, 4, 6], [1, 2, 5, 5], [1, 2, 10], [1, 3, 3, 3, 3], [1, 3, 3, 6], [1, 3, 4, 5], [1, 3, 9], [1, 4, 4, 4], [1, 4, 8], [1, 5, 7], [1, 6, 6], [2, 2, 2, 2, 5], [2, 2, 2, 3, 4], [2, 2, 2, 7], [2, 2, 3, 3, 3], [2, 2, 3, 6], [2, 2, 4, 5], [2, 2, 9], [2, 3, 3, 5], [2, 3, 4, 4], [2, 3, 8], [2, 4, 7], [2, 5, 6], [2, 11], [3, 3, 3, 4], [3, 3, 7], [3, 4, 6], [3, 5, 5], [3, 10], [4, 4, 5], [4, 9], [5, 8], [6, 7]]

        # fourteen_combs = [[1, 1, 1, 1, 2, 2, 2, 4], [1, 1, 1, 1, 2, 2, 3, 3], [1, 1, 1, 1, 2, 2, 6], [1, 1, 1, 1, 2, 3, 5], [1, 1, 1, 1, 2, 4, 4], [1, 1, 1, 1, 2, 8], [1, 1, 1, 1, 3, 3, 4], [1, 1, 1, 1, 3, 7], [1, 1, 1, 1, 4, 6], [1, 1, 1, 1, 5, 5], [1, 1, 1, 1, 10], [1, 1, 1, 2, 2, 2, 2, 3], [1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 2, 2, 3, 4], [1, 1, 1, 2, 2, 7], [1, 1, 1, 2, 3, 3, 3], [1, 1, 1, 2, 3, 6], [1, 1, 1, 2, 4, 5], [1, 1, 1, 2, 9], [1, 1, 1, 3, 3, 5], [1, 1, 1, 3, 4, 4], [1, 1, 1, 3, 8], [1, 1, 1, 4, 7], [1, 1, 1, 5, 6], [1, 1, 1, 11], [1, 1, 2, 2, 2, 2, 4], [1, 1, 2, 2, 2, 3, 3], [1, 1, 2, 2, 2, 6], [1, 1, 2, 2, 3, 5], [1, 1, 2, 2, 4, 4], [1, 1, 2, 2, 8], [1, 1, 2, 3, 3, 4], [1, 1, 2, 3, 7], [1, 1, 2, 4, 6], [1, 1, 2, 5, 5], [1, 1, 2, 10], [1, 1, 3, 3, 3, 3], [1, 1, 3, 3, 6], [1, 1, 3, 4, 5], [1, 1, 3, 9], [1, 1, 4, 4, 4], [1, 1, 4, 8], [1, 1, 5, 7], [1, 1, 6, 6], [1, 2, 2, 2, 2, 5], [1, 2, 2, 2, 3, 4], [1, 2, 2, 2, 7], [1, 2, 2, 3, 3, 3], [1, 2, 2, 3, 6], [1, 2, 2, 4, 5], [1, 2, 2, 9], [1, 2, 3, 3, 5], [1, 2, 3, 4, 4], [1, 2, 3, 8], [1, 2, 4, 7], [1, 2, 5, 6], [1, 2, 11], [1, 3, 3, 3, 4], [1, 3, 3, 7], [1, 3, 4, 6], [1, 3, 5, 5], [1, 3, 10], [1, 4, 4, 5], [1, 4, 9], [1, 5, 8], [1, 6, 7], [2, 2, 2, 2, 3, 3], [2, 2, 2, 2, 6], [2, 2, 2, 3, 5], [2, 2, 2, 4, 4], [2, 2, 2, 8], [2, 2, 3, 3, 4], [2, 2, 3, 7], [2, 2, 4, 6], [2, 2, 5, 5], [2, 2, 10], [2, 3, 3, 3, 3], [2, 3, 3, 6], [2, 3, 4, 5], [2, 3, 9], [2, 4, 4, 4], [2, 4, 8], [2, 5, 7], [2, 6, 6], [3, 3, 3, 5], [3, 3, 4, 4], [3, 3, 8], [3, 4, 7], [3, 5, 6], [3, 11], [4, 4, 6], [4, 5, 5], [4, 10], [5, 9], [6, 8], [7, 7]]

        # fifteen_combs = [[1, 1, 1, 1, 2, 2, 2, 2, 3], [1, 1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 1, 2, 2, 3, 4], [1, 1, 1, 1, 2, 2, 7], [1, 1, 1, 1, 2, 3, 3, 3], [1, 1, 1, 1, 2, 3, 6], [1, 1, 1, 1, 2, 4, 5], [1, 1, 1, 1, 2, 9], [1, 1, 1, 1, 3, 3, 5], [1, 1, 1, 1, 3, 4, 4], [1, 1, 1, 1, 3, 8], [1, 1, 1, 1, 4, 7], [1, 1, 1, 1, 5, 6], [1, 1, 1, 2, 2, 2, 2, 4], [1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 1, 2, 2, 2, 6], [1, 1, 1, 2, 2, 3, 5], [1, 1, 1, 2, 2, 4, 4], [1, 1, 1, 2, 2, 8], [1, 1, 1, 2, 3, 3, 4], [1, 1, 1, 2, 3, 7], [1, 1, 1, 2, 4, 6], [1, 1, 1, 2, 5, 5], [1, 1, 1, 2, 10], [1, 1, 1, 3, 3, 3, 3], [1, 1, 1, 3, 3, 6], [1, 1, 1, 3, 4, 5], [1, 1, 1, 3, 9], [1, 1, 1, 4, 4, 4], [1, 1, 1, 4, 8], [1, 1, 1, 5, 7], [1, 1, 1, 6, 6], [1, 1, 2, 2, 2, 2, 5], [1, 1, 2, 2, 2, 3, 4], [1, 1, 2, 2, 2, 7], [1, 1, 2, 2, 3, 3, 3], [1, 1, 2, 2, 3, 6], [1, 1, 2, 2, 4, 5], [1, 1, 2, 2, 9], [1, 1, 2, 3, 3, 5], [1, 1, 2, 3, 4, 4], [1, 1, 2, 3, 8], [1, 1, 2, 4, 7], [1, 1, 2, 5, 6], [1, 1, 2, 11], [1, 1, 3, 3, 3, 4], [1, 1, 3, 3, 7], [1, 1, 3, 4, 6], [1, 1, 3, 5, 5], [1, 1, 3, 10], [1, 1, 4, 4, 5], [1, 1, 4, 9], [1, 1, 5, 8], [1, 1, 6, 7], [1, 2, 2, 2, 2, 3, 3], [1, 2, 2, 2, 2, 6], [1, 2, 2, 2, 3, 5], [1, 2, 2, 2, 4, 4], [1, 2, 2, 2, 8], [1, 2, 2, 3, 3, 4], [1, 2, 2, 3, 7], [1, 2, 2, 4, 6], [1, 2, 2, 5, 5], [1, 2, 2, 10], [1, 2, 3, 3, 3, 3], [1, 2, 3, 3, 6], [1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 4, 4, 4], [1, 2, 4, 8], [1, 2, 5, 7], [1, 2, 6, 6], [1, 3, 3, 3, 5], [1, 3, 3, 4, 4], [1, 3, 3, 8], [1, 3, 4, 7], [1, 3, 5, 6], [1, 3, 11], [1, 4, 4, 6], [1, 4, 5, 5], [1, 4, 10], [1, 5, 9], [1, 6, 8], [1, 7, 7], [2, 2, 2, 2, 3, 4], [2, 2, 2, 2, 7], [2, 2, 2, 3, 3, 3], [2, 2, 2, 3, 6], [2, 2, 2, 4, 5], [2, 2, 2, 9], [2, 2, 3, 3, 5], [2, 2, 3, 4, 4], [2, 2, 3, 8], [2, 2, 4, 7], [2, 2, 5, 6], [2, 2, 11], [2, 3, 3, 3, 4], [2, 3, 3, 7], [2, 3, 4, 6], [2, 3, 5, 5], [2, 3, 10], [2, 4, 4, 5], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 3, 3, 6], [3, 3, 4, 5], [3, 3, 9], [3, 4, 4, 4], [3, 4, 8], [3, 5, 7], [3, 6, 6], [4, 4, 7], [4, 5, 6], [4, 11], [5, 5, 5], [5, 10], [6, 9], [7, 8]]

        # sixteen_combs = [[1, 1, 1, 1, 2, 2, 2, 2, 4], [1, 1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 1, 1, 2, 2, 2, 6], [1, 1, 1, 1, 2, 2, 3, 5], [1, 1, 1, 1, 2, 2, 4, 4], [1, 1, 1, 1, 2, 2, 8], [1, 1, 1, 1, 2, 3, 3, 4], [1, 1, 1, 1, 2, 3, 7], [1, 1, 1, 1, 2, 4, 6], [1, 1, 1, 1, 2, 5, 5], [1, 1, 1, 1, 2, 10], [1, 1, 1, 1, 3, 3, 3, 3], [1, 1, 1, 1, 3, 3, 6], [1, 1, 1, 1, 3, 4, 5], [1, 1, 1, 1, 3, 9], [1, 1, 1, 1, 4, 4, 4], [1, 1, 1, 1, 4, 8], [1, 1, 1, 1, 5, 7], [1, 1, 1, 1, 6, 6], [1, 1, 1, 2, 2, 2, 2, 5], [1, 1, 1, 2, 2, 2, 3, 4], [1, 1, 1, 2, 2, 2, 7], [1, 1, 1, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 3, 6], [1, 1, 1, 2, 2, 4, 5], [1, 1, 1, 2, 2, 9], [1, 1, 1, 2, 3, 3, 5], [1, 1, 1, 2, 3, 4, 4], [1, 1, 1, 2, 3, 8], [1, 1, 1, 2, 4, 7], [1, 1, 1, 2, 5, 6], [1, 1, 1, 2, 11], [1, 1, 1, 3, 3, 3, 4], [1, 1, 1, 3, 3, 7], [1, 1, 1, 3, 4, 6], [1, 1, 1, 3, 5, 5], [1, 1, 1, 3, 10], [1, 1, 1, 4, 4, 5], [1, 1, 1, 4, 9], [1, 1, 1, 5, 8], [1, 1, 1, 6, 7], [1, 1, 2, 2, 2, 2, 3, 3], [1, 1, 2, 2, 2, 2, 6], [1, 1, 2, 2, 2, 3, 5], [1, 1, 2, 2, 2, 4, 4], [1, 1, 2, 2, 2, 8], [1, 1, 2, 2, 3, 3, 4], [1, 1, 2, 2, 3, 7], [1, 1, 2, 2, 4, 6], [1, 1, 2, 2, 5, 5], [1, 1, 2, 2, 10], [1, 1, 2, 3, 3, 3, 3], [1, 1, 2, 3, 3, 6], [1, 1, 2, 3, 4, 5], [1, 1, 2, 3, 9], [1, 1, 2, 4, 4, 4], [1, 1, 2, 4, 8], [1, 1, 2, 5, 7], [1, 1, 2, 6, 6], [1, 1, 3, 3, 3, 5], [1, 1, 3, 3, 4, 4], [1, 1, 3, 3, 8], [1, 1, 3, 4, 7], [1, 1, 3, 5, 6], [1, 1, 3, 11], [1, 1, 4, 4, 6], [1, 1, 4, 5, 5], [1, 1, 4, 10], [1, 1, 5, 9], [1, 1, 6, 8], [1, 1, 7, 7], [1, 2, 2, 2, 2, 3, 4], [1, 2, 2, 2, 2, 7], [1, 2, 2, 2, 3, 3, 3], [1, 2, 2, 2, 3, 6], [1, 2, 2, 2, 4, 5], [1, 2, 2, 2, 9], [1, 2, 2, 3, 3, 5], [1, 2, 2, 3, 4, 4], [1, 2, 2, 3, 8], [1, 2, 2, 4, 7], [1, 2, 2, 5, 6], [1, 2, 2, 11], [1, 2, 3, 3, 3, 4], [1, 2, 3, 3, 7], [1, 2, 3, 4, 6], [1, 2, 3, 5, 5], [1, 2, 3, 10], [1, 2, 4, 4, 5], [1, 2, 4, 9], [1, 2, 5, 8], [1, 2, 6, 7], [1, 3, 3, 3, 6], [1, 3, 3, 4, 5], [1, 3, 3, 9], [1, 3, 4, 4, 4], [1, 3, 4, 8], [1, 3, 5, 7], [1, 3, 6, 6], [1, 4, 4, 7], [1, 4, 5, 6], [1, 4, 11], [1, 5, 5, 5], [1, 5, 10], [1, 6, 9], [1, 7, 8], [2, 2, 2, 2, 3, 5], [2, 2, 2, 2, 4, 4], [2, 2, 2, 2, 8], [2, 2, 2, 3, 3, 4], [2, 2, 2, 3, 7], [2, 2, 2, 4, 6], [2, 2, 2, 5, 5], [2, 2, 2, 10], [2, 2, 3, 3, 3, 3], [2, 2, 3, 3, 6], [2, 2, 3, 4, 5], [2, 2, 3, 9], [2, 2, 4, 4, 4], [2, 2, 4, 8], [2, 2, 5, 7], [2, 2, 6, 6], [2, 3, 3, 3, 5], [2, 3, 3, 4, 4], [2, 3, 3, 8], [2, 3, 4, 7], [2, 3, 5, 6], [2, 3, 11], [2, 4, 4, 6], [2, 4, 5, 5], [2, 4, 10], [2, 5, 9], [2, 6, 8], [2, 7, 7], [3, 3, 3, 3, 4], [3, 3, 3, 7], [3, 3, 4, 6], [3, 3, 5, 5], [3, 3, 10], [3, 4, 4, 5], [3, 4, 9], [3, 5, 8], [3, 6, 7], [4, 4, 4, 4], [4, 4, 8], [4, 5, 7], [4, 6, 6], [5, 5, 6], [5, 11], [6, 10], [7, 9], [8, 8]]
        

    #     values_flipped = {1:'A', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'T', 11:'A'}

    # # Creating list of possible dealer's face cards
    # dealer_face_cards = []
    # for rank in RANKS:
    #     card = Card('D', rank)
    #     dealer_face_cards.append(card)
    
    # print(dealer_face_cards)

    # combs_list = [[[1, 1, 1, 1, 2, 2, 3], [1, 1, 1, 1, 2, 5], [1, 1, 1, 1, 3, 4], [1, 1, 1, 1, 7], [1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 2, 2, 4], [1, 1, 1, 2, 3, 3], [1, 1, 1, 2, 6], [1, 1, 1, 3, 5], [1, 1, 1, 4, 4], [1, 1, 1, 8], [1, 1, 2, 2, 2, 3], [1, 1, 2, 2, 5], [1, 1, 2, 3, 4], [1, 1, 2, 7], [1, 1, 3, 3, 3], [1, 1, 3, 6], [1, 1, 4, 5], [1, 1, 9], [1, 2, 2, 2, 4], [1, 2, 2, 3, 3], [1, 2, 2, 6], [1, 2, 3, 5], [1, 2, 4, 4], [1, 2, 8], [1, 3, 3, 4], [1, 3, 7], [1, 4, 6], [1, 5, 5], [1, 10], [2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 2, 3, 4], [2, 2, 7], [2, 3, 3, 3], [2, 3, 6], [2, 4, 5], [2, 9], [3, 3, 5], [3, 4, 4], [3, 8], [4, 7], [5, 6], [11]], 
    #             [[1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 1, 2, 2, 4], [1, 1, 1, 1, 2, 3, 3], [1, 1, 1, 1, 2, 6], [1, 1, 1, 1, 3, 5], [1, 1, 1, 1, 4, 4], [1, 1, 1, 1, 8], [1, 1, 1, 2, 2, 2, 3], [1, 1, 1, 2, 2, 5], [1, 1, 1, 2, 3, 4], [1, 1, 1, 2, 7], [1, 1, 1, 3, 3, 3], [1, 1, 1, 3, 6], [1, 1, 1, 4, 5], [1, 1, 1, 9], [1, 1, 2, 2, 2, 4], [1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 6], [1, 1, 2, 3, 5], [1, 1, 2, 4, 4], [1, 1, 2, 8], [1, 1, 3, 3, 4], [1, 1, 3, 7], [1, 1, 4, 6], [1, 1, 5, 5], [1, 1, 10], [1, 2, 2, 2, 2, 3], [1, 2, 2, 2, 5], [1, 2, 2, 3, 4], [1, 2, 2, 7], [1, 2, 3, 3, 3], [1, 2, 3, 6], [1, 2, 4, 5], [1, 2, 9], [1, 3, 3, 5], [1, 3, 4, 4], [1, 3, 8], [1, 4, 7], [1, 5, 6], [1, 11], [2, 2, 2, 2, 4], [2, 2, 2, 3, 3], [2, 2, 2, 6], [2, 2, 3, 5], [2, 2, 4, 4], [2, 2, 8], [2, 3, 3, 4], [2, 3, 7], [2, 4, 6], [2, 5, 5], [2, 10], [3, 3, 3, 3], [3, 3, 6], [3, 4, 5], [3, 9], [4, 4, 4], [4, 8], [5, 7], [6, 6]], 
    #             [[1, 1, 1, 1, 2, 2, 2, 3], [1, 1, 1, 1, 2, 2, 5], [1, 1, 1, 1, 2, 3, 4], [1, 1, 1, 1, 2, 7], [1, 1, 1, 1, 3, 3, 3], [1, 1, 1, 1, 3, 6], [1, 1, 1, 1, 4, 5], [1, 1, 1, 1, 9], [1, 1, 1, 2, 2, 2, 4], [1, 1, 1, 2, 2, 3, 3], [1, 1, 1, 2, 2, 6], [1, 1, 1, 2, 3, 5], [1, 1, 1, 2, 4, 4], [1, 1, 1, 2, 8], [1, 1, 1, 3, 3, 4], [1, 1, 1, 3, 7], [1, 1, 1, 4, 6], [1, 1, 1, 5, 5], [1, 1, 1, 10], [1, 1, 2, 2, 2, 2, 3], [1, 1, 2, 2, 2, 5], [1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 7], [1, 1, 2, 3, 3, 3], [1, 1, 2, 3, 6], [1, 1, 2, 4, 5], [1, 1, 2, 9], [1, 1, 3, 3, 5], [1, 1, 3, 4, 4], [1, 1, 3, 8], [1, 1, 4, 7], [1, 1, 5, 6], [1, 1, 11], [1, 2, 2, 2, 2, 4], [1, 2, 2, 2, 3, 3], [1, 2, 2, 2, 6], [1, 2, 2, 3, 5], [1, 2, 2, 4, 4], [1, 2, 2, 8], [1, 2, 3, 3, 4], [1, 2, 3, 7], [1, 2, 4, 6], [1, 2, 5, 5], [1, 2, 10], [1, 3, 3, 3, 3], [1, 3, 3, 6], [1, 3, 4, 5], [1, 3, 9], [1, 4, 4, 4], [1, 4, 8], [1, 5, 7], [1, 6, 6], [2, 2, 2, 2, 5], [2, 2, 2, 3, 4], [2, 2, 2, 7], [2, 2, 3, 3, 3], [2, 2, 3, 6], [2, 2, 4, 5], [2, 2, 9], [2, 3, 3, 5], [2, 3, 4, 4], [2, 3, 8], [2, 4, 7], [2, 5, 6], [2, 11], [3, 3, 3, 4], [3, 3, 7], [3, 4, 6], [3, 5, 5], [3, 10], [4, 4, 5], [4, 9], [5, 8], [6, 7]],
    #             [[1, 1, 1, 1, 2, 2, 2, 4], [1, 1, 1, 1, 2, 2, 3, 3], [1, 1, 1, 1, 2, 2, 6], [1, 1, 1, 1, 2, 3, 5], [1, 1, 1, 1, 2, 4, 4], [1, 1, 1, 1, 2, 8], [1, 1, 1, 1, 3, 3, 4], [1, 1, 1, 1, 3, 7], [1, 1, 1, 1, 4, 6], [1, 1, 1, 1, 5, 5], [1, 1, 1, 1, 10], [1, 1, 1, 2, 2, 2, 2, 3], [1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 2, 2, 3, 4], [1, 1, 1, 2, 2, 7], [1, 1, 1, 2, 3, 3, 3], [1, 1, 1, 2, 3, 6], [1, 1, 1, 2, 4, 5], [1, 1, 1, 2, 9], [1, 1, 1, 3, 3, 5], [1, 1, 1, 3, 4, 4], [1, 1, 1, 3, 8], [1, 1, 1, 4, 7], [1, 1, 1, 5, 6], [1, 1, 1, 11], [1, 1, 2, 2, 2, 2, 4], [1, 1, 2, 2, 2, 3, 3], [1, 1, 2, 2, 2, 6], [1, 1, 2, 2, 3, 5], [1, 1, 2, 2, 4, 4], [1, 1, 2, 2, 8], [1, 1, 2, 3, 3, 4], [1, 1, 2, 3, 7], [1, 1, 2, 4, 6], [1, 1, 2, 5, 5], [1, 1, 2, 10], [1, 1, 3, 3, 3, 3], [1, 1, 3, 3, 6], [1, 1, 3, 4, 5], [1, 1, 3, 9], [1, 1, 4, 4, 4], [1, 1, 4, 8], [1, 1, 5, 7], [1, 1, 6, 6], [1, 2, 2, 2, 2, 5], [1, 2, 2, 2, 3, 4], [1, 2, 2, 2, 7], [1, 2, 2, 3, 3, 3], [1, 2, 2, 3, 6], [1, 2, 2, 4, 5], [1, 2, 2, 9], [1, 2, 3, 3, 5], [1, 2, 3, 4, 4], [1, 2, 3, 8], [1, 2, 4, 7], [1, 2, 5, 6], [1, 2, 11], [1, 3, 3, 3, 4], [1, 3, 3, 7], [1, 3, 4, 6], [1, 3, 5, 5], [1, 3, 10], [1, 4, 4, 5], [1, 4, 9], [1, 5, 8], [1, 6, 7], [2, 2, 2, 2, 3, 3], [2, 2, 2, 2, 6], [2, 2, 2, 3, 5], [2, 2, 2, 4, 4], [2, 2, 2, 8], [2, 2, 3, 3, 4], [2, 2, 3, 7], [2, 2, 4, 6], [2, 2, 5, 5], [2, 2, 10], [2, 3, 3, 3, 3], [2, 3, 3, 6], [2, 3, 4, 5], [2, 3, 9], [2, 4, 4, 4], [2, 4, 8], [2, 5, 7], [2, 6, 6], [3, 3, 3, 5], [3, 3, 4, 4], [3, 3, 8], [3, 4, 7], [3, 5, 6], [3, 11], [4, 4, 6], [4, 5, 5], [4, 10], [5, 9], [6, 8], [7, 7]],
    #             [[1, 1, 1, 1, 2, 2, 2, 2, 3], [1, 1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 1, 2, 2, 3, 4], [1, 1, 1, 1, 2, 2, 7], [1, 1, 1, 1, 2, 3, 3, 3], [1, 1, 1, 1, 2, 3, 6], [1, 1, 1, 1, 2, 4, 5], [1, 1, 1, 1, 2, 9], [1, 1, 1, 1, 3, 3, 5], [1, 1, 1, 1, 3, 4, 4], [1, 1, 1, 1, 3, 8], [1, 1, 1, 1, 4, 7], [1, 1, 1, 1, 5, 6], [1, 1, 1, 2, 2, 2, 2, 4], [1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 1, 2, 2, 2, 6], [1, 1, 1, 2, 2, 3, 5], [1, 1, 1, 2, 2, 4, 4], [1, 1, 1, 2, 2, 8], [1, 1, 1, 2, 3, 3, 4], [1, 1, 1, 2, 3, 7], [1, 1, 1, 2, 4, 6], [1, 1, 1, 2, 5, 5], [1, 1, 1, 2, 10], [1, 1, 1, 3, 3, 3, 3], [1, 1, 1, 3, 3, 6], [1, 1, 1, 3, 4, 5], [1, 1, 1, 3, 9], [1, 1, 1, 4, 4, 4], [1, 1, 1, 4, 8], [1, 1, 1, 5, 7], [1, 1, 1, 6, 6], [1, 1, 2, 2, 2, 2, 5], [1, 1, 2, 2, 2, 3, 4], [1, 1, 2, 2, 2, 7], [1, 1, 2, 2, 3, 3, 3], [1, 1, 2, 2, 3, 6], [1, 1, 2, 2, 4, 5], [1, 1, 2, 2, 9], [1, 1, 2, 3, 3, 5], [1, 1, 2, 3, 4, 4], [1, 1, 2, 3, 8], [1, 1, 2, 4, 7], [1, 1, 2, 5, 6], [1, 1, 2, 11], [1, 1, 3, 3, 3, 4], [1, 1, 3, 3, 7], [1, 1, 3, 4, 6], [1, 1, 3, 5, 5], [1, 1, 3, 10], [1, 1, 4, 4, 5], [1, 1, 4, 9], [1, 1, 5, 8], [1, 1, 6, 7], [1, 2, 2, 2, 2, 3, 3], [1, 2, 2, 2, 2, 6], [1, 2, 2, 2, 3, 5], [1, 2, 2, 2, 4, 4], [1, 2, 2, 2, 8], [1, 2, 2, 3, 3, 4], [1, 2, 2, 3, 7], [1, 2, 2, 4, 6], [1, 2, 2, 5, 5], [1, 2, 2, 10], [1, 2, 3, 3, 3, 3], [1, 2, 3, 3, 6], [1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 4, 4, 4], [1, 2, 4, 8], [1, 2, 5, 7], [1, 2, 6, 6], [1, 3, 3, 3, 5], [1, 3, 3, 4, 4], [1, 3, 3, 8], [1, 3, 4, 7], [1, 3, 5, 6], [1, 3, 11], [1, 4, 4, 6], [1, 4, 5, 5], [1, 4, 10], [1, 5, 9], [1, 6, 8], [1, 7, 7], [2, 2, 2, 2, 3, 4], [2, 2, 2, 2, 7], [2, 2, 2, 3, 3, 3], [2, 2, 2, 3, 6], [2, 2, 2, 4, 5], [2, 2, 2, 9], [2, 2, 3, 3, 5], [2, 2, 3, 4, 4], [2, 2, 3, 8], [2, 2, 4, 7], [2, 2, 5, 6], [2, 2, 11], [2, 3, 3, 3, 4], [2, 3, 3, 7], [2, 3, 4, 6], [2, 3, 5, 5], [2, 3, 10], [2, 4, 4, 5], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 3, 3, 6], [3, 3, 4, 5], [3, 3, 9], [3, 4, 4, 4], [3, 4, 8], [3, 5, 7], [3, 6, 6], [4, 4, 7], [4, 5, 6], [4, 11], [5, 5, 5], [5, 10], [6, 9], [7, 8]],
    #             [[1, 1, 1, 1, 2, 2, 2, 2, 4], [1, 1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 1, 1, 2, 2, 2, 6], [1, 1, 1, 1, 2, 2, 3, 5], [1, 1, 1, 1, 2, 2, 4, 4], [1, 1, 1, 1, 2, 2, 8], [1, 1, 1, 1, 2, 3, 3, 4], [1, 1, 1, 1, 2, 3, 7], [1, 1, 1, 1, 2, 4, 6], [1, 1, 1, 1, 2, 5, 5], [1, 1, 1, 1, 2, 10], [1, 1, 1, 1, 3, 3, 3, 3], [1, 1, 1, 1, 3, 3, 6], [1, 1, 1, 1, 3, 4, 5], [1, 1, 1, 1, 3, 9], [1, 1, 1, 1, 4, 4, 4], [1, 1, 1, 1, 4, 8], [1, 1, 1, 1, 5, 7], [1, 1, 1, 1, 6, 6], [1, 1, 1, 2, 2, 2, 2, 5], [1, 1, 1, 2, 2, 2, 3, 4], [1, 1, 1, 2, 2, 2, 7], [1, 1, 1, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 3, 6], [1, 1, 1, 2, 2, 4, 5], [1, 1, 1, 2, 2, 9], [1, 1, 1, 2, 3, 3, 5], [1, 1, 1, 2, 3, 4, 4], [1, 1, 1, 2, 3, 8], [1, 1, 1, 2, 4, 7], [1, 1, 1, 2, 5, 6], [1, 1, 1, 2, 11], [1, 1, 1, 3, 3, 3, 4], [1, 1, 1, 3, 3, 7], [1, 1, 1, 3, 4, 6], [1, 1, 1, 3, 5, 5], [1, 1, 1, 3, 10], [1, 1, 1, 4, 4, 5], [1, 1, 1, 4, 9], [1, 1, 1, 5, 8], [1, 1, 1, 6, 7], [1, 1, 2, 2, 2, 2, 3, 3], [1, 1, 2, 2, 2, 2, 6], [1, 1, 2, 2, 2, 3, 5], [1, 1, 2, 2, 2, 4, 4], [1, 1, 2, 2, 2, 8], [1, 1, 2, 2, 3, 3, 4], [1, 1, 2, 2, 3, 7], [1, 1, 2, 2, 4, 6], [1, 1, 2, 2, 5, 5], [1, 1, 2, 2, 10], [1, 1, 2, 3, 3, 3, 3], [1, 1, 2, 3, 3, 6], [1, 1, 2, 3, 4, 5], [1, 1, 2, 3, 9], [1, 1, 2, 4, 4, 4], [1, 1, 2, 4, 8], [1, 1, 2, 5, 7], [1, 1, 2, 6, 6], [1, 1, 3, 3, 3, 5], [1, 1, 3, 3, 4, 4], [1, 1, 3, 3, 8], [1, 1, 3, 4, 7], [1, 1, 3, 5, 6], [1, 1, 3, 11], [1, 1, 4, 4, 6], [1, 1, 4, 5, 5], [1, 1, 4, 10], [1, 1, 5, 9], [1, 1, 6, 8], [1, 1, 7, 7], [1, 2, 2, 2, 2, 3, 4], [1, 2, 2, 2, 2, 7], [1, 2, 2, 2, 3, 3, 3], [1, 2, 2, 2, 3, 6], [1, 2, 2, 2, 4, 5], [1, 2, 2, 2, 9], [1, 2, 2, 3, 3, 5], [1, 2, 2, 3, 4, 4], [1, 2, 2, 3, 8], [1, 2, 2, 4, 7], [1, 2, 2, 5, 6], [1, 2, 2, 11], [1, 2, 3, 3, 3, 4], [1, 2, 3, 3, 7], [1, 2, 3, 4, 6], [1, 2, 3, 5, 5], [1, 2, 3, 10], [1, 2, 4, 4, 5], [1, 2, 4, 9], [1, 2, 5, 8], [1, 2, 6, 7], [1, 3, 3, 3, 6], [1, 3, 3, 4, 5], [1, 3, 3, 9], [1, 3, 4, 4, 4], [1, 3, 4, 8], [1, 3, 5, 7], [1, 3, 6, 6], [1, 4, 4, 7], [1, 4, 5, 6], [1, 4, 11], [1, 5, 5, 5], [1, 5, 10], [1, 6, 9], [1, 7, 8], [2, 2, 2, 2, 3, 5], [2, 2, 2, 2, 4, 4], [2, 2, 2, 2, 8], [2, 2, 2, 3, 3, 4], [2, 2, 2, 3, 7], [2, 2, 2, 4, 6], [2, 2, 2, 5, 5], [2, 2, 2, 10], [2, 2, 3, 3, 3, 3], [2, 2, 3, 3, 6], [2, 2, 3, 4, 5], [2, 2, 3, 9], [2, 2, 4, 4, 4], [2, 2, 4, 8], [2, 2, 5, 7], [2, 2, 6, 6], [2, 3, 3, 3, 5], [2, 3, 3, 4, 4], [2, 3, 3, 8], [2, 3, 4, 7], [2, 3, 5, 6], [2, 3, 11], [2, 4, 4, 6], [2, 4, 5, 5], [2, 4, 10], [2, 5, 9], [2, 6, 8], [2, 7, 7], [3, 3, 3, 3, 4], [3, 3, 3, 7], [3, 3, 4, 6], [3, 3, 5, 5], [3, 3, 10], [3, 4, 4, 5], [3, 4, 9], [3, 5, 8], [3, 6, 7], [4, 4, 4, 4], [4, 4, 8], [4, 5, 7], [4, 6, 6], [5, 5, 6], [5, 11], [6, 10], [7, 9], [8, 8]]]
    
    # for i in range (11, 17):
    #     for comb in combs_list[i-11]:
    #         for face_card in dealer_face_cards:
    #             # Initialize dealer and player's hand and deck
    #             dealer_hand = Hand()
    #             player_hand = Hand()
    #             deck = Deck() #self.make_deck()
                
    #             # Create player_hand
    #             count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11: 0}
    #             for player_card in comb:
    #                 suit_idx = count[player_card]
    #                 card = Card(SUITS[suit_idx], values_flipped[player_card])
    #                 count[player_card] += 1
    #                 if card.get_value() == 1:
    #                     count[11] += 1
    #                 if card.get_value() == 11:
    #                     count[1] += 1
    #                 player_hand.add_card(card)
    #                 # Pop the card from the deck
    #                 deck.remove(card)
                
    #             # Do not go through the hands that are already 21 in value
    #             if player_hand.get_value() != i:
    #                 break

    #             # Set dealer_face card, but check if it is already used in player_cards
    #             if count[face_card.get_value()] < 4:
    #                 dealer_hand.add_card(face_card)
    #                 deck.remove(card)
    #             else:
    #                 break
                
    #             # Run simulation to calculate the win percentage
                
    #             print(deck)
        # # Creating list of possible dealer's face cards
        # dealer_face_cards = []
        # for rank in RANKS:
        #     card = Card('D', rank)
        #     dealer_face_cards.append(card)
        
        # print(dealer_face_cards)

        # combs_list = [[[1, 1, 1, 1, 2, 2, 3], [1, 1, 1, 1, 2, 5], [1, 1, 1, 1, 3, 4], [1, 1, 1, 1, 7], [1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 2, 2, 4], [1, 1, 1, 2, 3, 3], [1, 1, 1, 2, 6], [1, 1, 1, 3, 5], [1, 1, 1, 4, 4], [1, 1, 1, 8], [1, 1, 2, 2, 2, 3], [1, 1, 2, 2, 5], [1, 1, 2, 3, 4], [1, 1, 2, 7], [1, 1, 3, 3, 3], [1, 1, 3, 6], [1, 1, 4, 5], [1, 1, 9], [1, 2, 2, 2, 4], [1, 2, 2, 3, 3], [1, 2, 2, 6], [1, 2, 3, 5], [1, 2, 4, 4], [1, 2, 8], [1, 3, 3, 4], [1, 3, 7], [1, 4, 6], [1, 5, 5], [1, 10], [2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 2, 3, 4], [2, 2, 7], [2, 3, 3, 3], [2, 3, 6], [2, 4, 5], [2, 9], [3, 3, 5], [3, 4, 4], [3, 8], [4, 7], [5, 6], [11]], 
        #             [[1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 1, 2, 2, 4], [1, 1, 1, 1, 2, 3, 3], [1, 1, 1, 1, 2, 6], [1, 1, 1, 1, 3, 5], [1, 1, 1, 1, 4, 4], [1, 1, 1, 1, 8], [1, 1, 1, 2, 2, 2, 3], [1, 1, 1, 2, 2, 5], [1, 1, 1, 2, 3, 4], [1, 1, 1, 2, 7], [1, 1, 1, 3, 3, 3], [1, 1, 1, 3, 6], [1, 1, 1, 4, 5], [1, 1, 1, 9], [1, 1, 2, 2, 2, 4], [1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 6], [1, 1, 2, 3, 5], [1, 1, 2, 4, 4], [1, 1, 2, 8], [1, 1, 3, 3, 4], [1, 1, 3, 7], [1, 1, 4, 6], [1, 1, 5, 5], [1, 1, 10], [1, 2, 2, 2, 2, 3], [1, 2, 2, 2, 5], [1, 2, 2, 3, 4], [1, 2, 2, 7], [1, 2, 3, 3, 3], [1, 2, 3, 6], [1, 2, 4, 5], [1, 2, 9], [1, 3, 3, 5], [1, 3, 4, 4], [1, 3, 8], [1, 4, 7], [1, 5, 6], [1, 11], [2, 2, 2, 2, 4], [2, 2, 2, 3, 3], [2, 2, 2, 6], [2, 2, 3, 5], [2, 2, 4, 4], [2, 2, 8], [2, 3, 3, 4], [2, 3, 7], [2, 4, 6], [2, 5, 5], [2, 10], [3, 3, 3, 3], [3, 3, 6], [3, 4, 5], [3, 9], [4, 4, 4], [4, 8], [5, 7], [6, 6]], 
        #             [[1, 1, 1, 1, 2, 2, 2, 3], [1, 1, 1, 1, 2, 2, 5], [1, 1, 1, 1, 2, 3, 4], [1, 1, 1, 1, 2, 7], [1, 1, 1, 1, 3, 3, 3], [1, 1, 1, 1, 3, 6], [1, 1, 1, 1, 4, 5], [1, 1, 1, 1, 9], [1, 1, 1, 2, 2, 2, 4], [1, 1, 1, 2, 2, 3, 3], [1, 1, 1, 2, 2, 6], [1, 1, 1, 2, 3, 5], [1, 1, 1, 2, 4, 4], [1, 1, 1, 2, 8], [1, 1, 1, 3, 3, 4], [1, 1, 1, 3, 7], [1, 1, 1, 4, 6], [1, 1, 1, 5, 5], [1, 1, 1, 10], [1, 1, 2, 2, 2, 2, 3], [1, 1, 2, 2, 2, 5], [1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 7], [1, 1, 2, 3, 3, 3], [1, 1, 2, 3, 6], [1, 1, 2, 4, 5], [1, 1, 2, 9], [1, 1, 3, 3, 5], [1, 1, 3, 4, 4], [1, 1, 3, 8], [1, 1, 4, 7], [1, 1, 5, 6], [1, 1, 11], [1, 2, 2, 2, 2, 4], [1, 2, 2, 2, 3, 3], [1, 2, 2, 2, 6], [1, 2, 2, 3, 5], [1, 2, 2, 4, 4], [1, 2, 2, 8], [1, 2, 3, 3, 4], [1, 2, 3, 7], [1, 2, 4, 6], [1, 2, 5, 5], [1, 2, 10], [1, 3, 3, 3, 3], [1, 3, 3, 6], [1, 3, 4, 5], [1, 3, 9], [1, 4, 4, 4], [1, 4, 8], [1, 5, 7], [1, 6, 6], [2, 2, 2, 2, 5], [2, 2, 2, 3, 4], [2, 2, 2, 7], [2, 2, 3, 3, 3], [2, 2, 3, 6], [2, 2, 4, 5], [2, 2, 9], [2, 3, 3, 5], [2, 3, 4, 4], [2, 3, 8], [2, 4, 7], [2, 5, 6], [2, 11], [3, 3, 3, 4], [3, 3, 7], [3, 4, 6], [3, 5, 5], [3, 10], [4, 4, 5], [4, 9], [5, 8], [6, 7]],
        #             [[1, 1, 1, 1, 2, 2, 2, 4], [1, 1, 1, 1, 2, 2, 3, 3], [1, 1, 1, 1, 2, 2, 6], [1, 1, 1, 1, 2, 3, 5], [1, 1, 1, 1, 2, 4, 4], [1, 1, 1, 1, 2, 8], [1, 1, 1, 1, 3, 3, 4], [1, 1, 1, 1, 3, 7], [1, 1, 1, 1, 4, 6], [1, 1, 1, 1, 5, 5], [1, 1, 1, 1, 10], [1, 1, 1, 2, 2, 2, 2, 3], [1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 2, 2, 3, 4], [1, 1, 1, 2, 2, 7], [1, 1, 1, 2, 3, 3, 3], [1, 1, 1, 2, 3, 6], [1, 1, 1, 2, 4, 5], [1, 1, 1, 2, 9], [1, 1, 1, 3, 3, 5], [1, 1, 1, 3, 4, 4], [1, 1, 1, 3, 8], [1, 1, 1, 4, 7], [1, 1, 1, 5, 6], [1, 1, 1, 11], [1, 1, 2, 2, 2, 2, 4], [1, 1, 2, 2, 2, 3, 3], [1, 1, 2, 2, 2, 6], [1, 1, 2, 2, 3, 5], [1, 1, 2, 2, 4, 4], [1, 1, 2, 2, 8], [1, 1, 2, 3, 3, 4], [1, 1, 2, 3, 7], [1, 1, 2, 4, 6], [1, 1, 2, 5, 5], [1, 1, 2, 10], [1, 1, 3, 3, 3, 3], [1, 1, 3, 3, 6], [1, 1, 3, 4, 5], [1, 1, 3, 9], [1, 1, 4, 4, 4], [1, 1, 4, 8], [1, 1, 5, 7], [1, 1, 6, 6], [1, 2, 2, 2, 2, 5], [1, 2, 2, 2, 3, 4], [1, 2, 2, 2, 7], [1, 2, 2, 3, 3, 3], [1, 2, 2, 3, 6], [1, 2, 2, 4, 5], [1, 2, 2, 9], [1, 2, 3, 3, 5], [1, 2, 3, 4, 4], [1, 2, 3, 8], [1, 2, 4, 7], [1, 2, 5, 6], [1, 2, 11], [1, 3, 3, 3, 4], [1, 3, 3, 7], [1, 3, 4, 6], [1, 3, 5, 5], [1, 3, 10], [1, 4, 4, 5], [1, 4, 9], [1, 5, 8], [1, 6, 7], [2, 2, 2, 2, 3, 3], [2, 2, 2, 2, 6], [2, 2, 2, 3, 5], [2, 2, 2, 4, 4], [2, 2, 2, 8], [2, 2, 3, 3, 4], [2, 2, 3, 7], [2, 2, 4, 6], [2, 2, 5, 5], [2, 2, 10], [2, 3, 3, 3, 3], [2, 3, 3, 6], [2, 3, 4, 5], [2, 3, 9], [2, 4, 4, 4], [2, 4, 8], [2, 5, 7], [2, 6, 6], [3, 3, 3, 5], [3, 3, 4, 4], [3, 3, 8], [3, 4, 7], [3, 5, 6], [3, 11], [4, 4, 6], [4, 5, 5], [4, 10], [5, 9], [6, 8], [7, 7]],
        #             [[1, 1, 1, 1, 2, 2, 2, 2, 3], [1, 1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 1, 2, 2, 3, 4], [1, 1, 1, 1, 2, 2, 7], [1, 1, 1, 1, 2, 3, 3, 3], [1, 1, 1, 1, 2, 3, 6], [1, 1, 1, 1, 2, 4, 5], [1, 1, 1, 1, 2, 9], [1, 1, 1, 1, 3, 3, 5], [1, 1, 1, 1, 3, 4, 4], [1, 1, 1, 1, 3, 8], [1, 1, 1, 1, 4, 7], [1, 1, 1, 1, 5, 6], [1, 1, 1, 2, 2, 2, 2, 4], [1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 1, 2, 2, 2, 6], [1, 1, 1, 2, 2, 3, 5], [1, 1, 1, 2, 2, 4, 4], [1, 1, 1, 2, 2, 8], [1, 1, 1, 2, 3, 3, 4], [1, 1, 1, 2, 3, 7], [1, 1, 1, 2, 4, 6], [1, 1, 1, 2, 5, 5], [1, 1, 1, 2, 10], [1, 1, 1, 3, 3, 3, 3], [1, 1, 1, 3, 3, 6], [1, 1, 1, 3, 4, 5], [1, 1, 1, 3, 9], [1, 1, 1, 4, 4, 4], [1, 1, 1, 4, 8], [1, 1, 1, 5, 7], [1, 1, 1, 6, 6], [1, 1, 2, 2, 2, 2, 5], [1, 1, 2, 2, 2, 3, 4], [1, 1, 2, 2, 2, 7], [1, 1, 2, 2, 3, 3, 3], [1, 1, 2, 2, 3, 6], [1, 1, 2, 2, 4, 5], [1, 1, 2, 2, 9], [1, 1, 2, 3, 3, 5], [1, 1, 2, 3, 4, 4], [1, 1, 2, 3, 8], [1, 1, 2, 4, 7], [1, 1, 2, 5, 6], [1, 1, 2, 11], [1, 1, 3, 3, 3, 4], [1, 1, 3, 3, 7], [1, 1, 3, 4, 6], [1, 1, 3, 5, 5], [1, 1, 3, 10], [1, 1, 4, 4, 5], [1, 1, 4, 9], [1, 1, 5, 8], [1, 1, 6, 7], [1, 2, 2, 2, 2, 3, 3], [1, 2, 2, 2, 2, 6], [1, 2, 2, 2, 3, 5], [1, 2, 2, 2, 4, 4], [1, 2, 2, 2, 8], [1, 2, 2, 3, 3, 4], [1, 2, 2, 3, 7], [1, 2, 2, 4, 6], [1, 2, 2, 5, 5], [1, 2, 2, 10], [1, 2, 3, 3, 3, 3], [1, 2, 3, 3, 6], [1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 4, 4, 4], [1, 2, 4, 8], [1, 2, 5, 7], [1, 2, 6, 6], [1, 3, 3, 3, 5], [1, 3, 3, 4, 4], [1, 3, 3, 8], [1, 3, 4, 7], [1, 3, 5, 6], [1, 3, 11], [1, 4, 4, 6], [1, 4, 5, 5], [1, 4, 10], [1, 5, 9], [1, 6, 8], [1, 7, 7], [2, 2, 2, 2, 3, 4], [2, 2, 2, 2, 7], [2, 2, 2, 3, 3, 3], [2, 2, 2, 3, 6], [2, 2, 2, 4, 5], [2, 2, 2, 9], [2, 2, 3, 3, 5], [2, 2, 3, 4, 4], [2, 2, 3, 8], [2, 2, 4, 7], [2, 2, 5, 6], [2, 2, 11], [2, 3, 3, 3, 4], [2, 3, 3, 7], [2, 3, 4, 6], [2, 3, 5, 5], [2, 3, 10], [2, 4, 4, 5], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 3, 3, 6], [3, 3, 4, 5], [3, 3, 9], [3, 4, 4, 4], [3, 4, 8], [3, 5, 7], [3, 6, 6], [4, 4, 7], [4, 5, 6], [4, 11], [5, 5, 5], [5, 10], [6, 9], [7, 8]],
        #             [[1, 1, 1, 1, 2, 2, 2, 2, 4], [1, 1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 1, 1, 2, 2, 2, 6], [1, 1, 1, 1, 2, 2, 3, 5], [1, 1, 1, 1, 2, 2, 4, 4], [1, 1, 1, 1, 2, 2, 8], [1, 1, 1, 1, 2, 3, 3, 4], [1, 1, 1, 1, 2, 3, 7], [1, 1, 1, 1, 2, 4, 6], [1, 1, 1, 1, 2, 5, 5], [1, 1, 1, 1, 2, 10], [1, 1, 1, 1, 3, 3, 3, 3], [1, 1, 1, 1, 3, 3, 6], [1, 1, 1, 1, 3, 4, 5], [1, 1, 1, 1, 3, 9], [1, 1, 1, 1, 4, 4, 4], [1, 1, 1, 1, 4, 8], [1, 1, 1, 1, 5, 7], [1, 1, 1, 1, 6, 6], [1, 1, 1, 2, 2, 2, 2, 5], [1, 1, 1, 2, 2, 2, 3, 4], [1, 1, 1, 2, 2, 2, 7], [1, 1, 1, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 3, 6], [1, 1, 1, 2, 2, 4, 5], [1, 1, 1, 2, 2, 9], [1, 1, 1, 2, 3, 3, 5], [1, 1, 1, 2, 3, 4, 4], [1, 1, 1, 2, 3, 8], [1, 1, 1, 2, 4, 7], [1, 1, 1, 2, 5, 6], [1, 1, 1, 2, 11], [1, 1, 1, 3, 3, 3, 4], [1, 1, 1, 3, 3, 7], [1, 1, 1, 3, 4, 6], [1, 1, 1, 3, 5, 5], [1, 1, 1, 3, 10], [1, 1, 1, 4, 4, 5], [1, 1, 1, 4, 9], [1, 1, 1, 5, 8], [1, 1, 1, 6, 7], [1, 1, 2, 2, 2, 2, 3, 3], [1, 1, 2, 2, 2, 2, 6], [1, 1, 2, 2, 2, 3, 5], [1, 1, 2, 2, 2, 4, 4], [1, 1, 2, 2, 2, 8], [1, 1, 2, 2, 3, 3, 4], [1, 1, 2, 2, 3, 7], [1, 1, 2, 2, 4, 6], [1, 1, 2, 2, 5, 5], [1, 1, 2, 2, 10], [1, 1, 2, 3, 3, 3, 3], [1, 1, 2, 3, 3, 6], [1, 1, 2, 3, 4, 5], [1, 1, 2, 3, 9], [1, 1, 2, 4, 4, 4], [1, 1, 2, 4, 8], [1, 1, 2, 5, 7], [1, 1, 2, 6, 6], [1, 1, 3, 3, 3, 5], [1, 1, 3, 3, 4, 4], [1, 1, 3, 3, 8], [1, 1, 3, 4, 7], [1, 1, 3, 5, 6], [1, 1, 3, 11], [1, 1, 4, 4, 6], [1, 1, 4, 5, 5], [1, 1, 4, 10], [1, 1, 5, 9], [1, 1, 6, 8], [1, 1, 7, 7], [1, 2, 2, 2, 2, 3, 4], [1, 2, 2, 2, 2, 7], [1, 2, 2, 2, 3, 3, 3], [1, 2, 2, 2, 3, 6], [1, 2, 2, 2, 4, 5], [1, 2, 2, 2, 9], [1, 2, 2, 3, 3, 5], [1, 2, 2, 3, 4, 4], [1, 2, 2, 3, 8], [1, 2, 2, 4, 7], [1, 2, 2, 5, 6], [1, 2, 2, 11], [1, 2, 3, 3, 3, 4], [1, 2, 3, 3, 7], [1, 2, 3, 4, 6], [1, 2, 3, 5, 5], [1, 2, 3, 10], [1, 2, 4, 4, 5], [1, 2, 4, 9], [1, 2, 5, 8], [1, 2, 6, 7], [1, 3, 3, 3, 6], [1, 3, 3, 4, 5], [1, 3, 3, 9], [1, 3, 4, 4, 4], [1, 3, 4, 8], [1, 3, 5, 7], [1, 3, 6, 6], [1, 4, 4, 7], [1, 4, 5, 6], [1, 4, 11], [1, 5, 5, 5], [1, 5, 10], [1, 6, 9], [1, 7, 8], [2, 2, 2, 2, 3, 5], [2, 2, 2, 2, 4, 4], [2, 2, 2, 2, 8], [2, 2, 2, 3, 3, 4], [2, 2, 2, 3, 7], [2, 2, 2, 4, 6], [2, 2, 2, 5, 5], [2, 2, 2, 10], [2, 2, 3, 3, 3, 3], [2, 2, 3, 3, 6], [2, 2, 3, 4, 5], [2, 2, 3, 9], [2, 2, 4, 4, 4], [2, 2, 4, 8], [2, 2, 5, 7], [2, 2, 6, 6], [2, 3, 3, 3, 5], [2, 3, 3, 4, 4], [2, 3, 3, 8], [2, 3, 4, 7], [2, 3, 5, 6], [2, 3, 11], [2, 4, 4, 6], [2, 4, 5, 5], [2, 4, 10], [2, 5, 9], [2, 6, 8], [2, 7, 7], [3, 3, 3, 3, 4], [3, 3, 3, 7], [3, 3, 4, 6], [3, 3, 5, 5], [3, 3, 10], [3, 4, 4, 5], [3, 4, 9], [3, 5, 8], [3, 6, 7], [4, 4, 4, 4], [4, 4, 8], [4, 5, 7], [4, 6, 6], [5, 5, 6], [5, 11], [6, 10], [7, 9], [8, 8]]]
        
        # for i in range (11, 17):
        #     for comb in combs_list[i-11]:
        #         for face_card in dealer_face_cards:
        #             # Initialize dealer and player's hand and deck
        #             dealer_hand = Hand()
        #             player_hand = Hand()
        #             deck = Deck() #self.make_deck()
                    
        #             # Create player_hand
        #             count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11: 0}
        #             for player_card in comb:
        #                 suit_idx = count[player_card]
        #                 card = Card(SUITS[suit_idx], values_flipped[player_card])
        #                 count[player_card] += 1
        #                 if card.get_value() == 1:
        #                     count[11] += 1
        #                 if card.get_value() == 11:
        #                     count[1] += 1
        #                 player_hand.add_card(card)
        #                 # Pop the card from the deck
        #                 deck.remove(card)
                    
        #             # Do not go through the hands that are already 21 in value
        #             if player_hand.get_value() != i:
        #                 break

        #             # Set dealer_face card, but check if it is already used in player_cards
        #             if count[face_card.get_value()] < 4:
        #                 dealer_hand.add_card(face_card)
        #                 deck.remove(card)
        #             else:
        #                 break
                    
        #             # Run simulation to calculate the win percentage
                    
        #             print(deck)
        # Create a deck and shuffle it
        # my_deck = Deck()
        # my_deck.shuffle()
        # Minimum cards that need to be calculated is 2, since we cannot bust with 2 cards
        # Maximum cards that need to be calculated is 11, since there is no combination of cards that will not result in a bust with 12 cards
        # for all the combinations of cards that we can get
        # if the sum is already a bust, set value to false
        # else, simulate the rest of the game for 

        # Need to abstract out the card combinations to sum of cards(and maybe the number of cards), since the combination is too much
        # Combinations of 2 cards: 1326
        # Combinations of 3 cards: 22100
        # Combinations of 4 cards: 270725
        # Combinations of 5 cards: 2598960
        # Combinations of 6 cards: 20358520
        # Combinations of 7 cards: 133784560
        # Combinations of 8 cards: 752538150
        # Combinations of 9 cards: 3679075400
        # Combinations of 10 cards: 15820024220
        # Combinations of 11 cards: 60403728840
        # Combinations of 12 cards: 206379406870 / 4

    # def make_deck(self):
    #     self.deck = []
    #     for s in SUITS:
    #         for r in RANKS:
    #             self.deck.append(Card(s, r))
    #     # create a Deck object

    # def shuffle(self, deck):
    #     random.shuffle(deck)
    #     # shuffle the deck

    # def pop_card(self, card, deck):
    #     deck.pop(card)
    #     # deal a card object from the deck

    # def __str__(self):
    #     ans = "The deck: "
    #     for c in self.deck:
    #         ans += str(c) + " "
    #     return ans
        # return a string representing the deck
    


    # For each combination of hands and face card, run simulation
    # For each combination of hands
    # Hand.cards()
    #     for _ in range(trials):

    #     return None
        # run random trials and update the matrix
    

        # Create matrix for percentages
        # self.matrix = {}
        # desired_sum = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        # nums_of_cards = [1, 2, 3, 4, 5, 6, 7, 8]
        # for sum in desired_sum:
        #     dict_by_sum = {}
        #     for num_of_cards in nums_of_cards:
        #         dict_by_num_of_cards = {}
        #         for face_card_rank in RANKS:
        #             dict_by_num_of_cards[face_card_rank] = None
        #         dict_by_sum[num_of_cards] = dict_by_num_of_cards
        #     self.matrix[sum] = dict_by_sum
                     


        # dict_by_sum = {1:{'A':None, '2':None, '3':None, '4':None, '5':None, '6':None, '7':None, 8:None, 9:None, 10:None}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
        # result_dict = {11:None, 12:None, 13:None, 14:None, 15:None, 16:None, 17:None, 18:None, 19:None, 20:None}
        # result_dict = {11:, 12:None, 13:None, 14:None, 15:None, 16:None, 17:None, 18:None, 19:None, 20:None}
                
            

        
    # for _ in range(trials):
    #     player_hand
            
    #         # Player's turn
    #         while player_hand.get_value() < 17:
        #         player_hand_simulation.append(random.choice(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']))

        #     # Dealer's turn
        #     while sum(dealer_hand_simulation) < 17:
        #         dealer_hand_simulation.append(random.choice(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']))

        #     # Determine the winner
        #     player_sum = sum(player_hand_simulation)
        #     dealer_sum = sum(dealer_hand_simulation)

        #     if player_sum > 21 or (dealer_sum <= 21 and dealer_sum >= player_sum):
        #         stand_wins += 1
        #     else:
        #         hit_wins += 1

        # # Calculate probabilities
        # prob_stand = stand_wins / num_simulations
        # prob_hit = hit_wins / num_simulations


        
        # # Deal two cards to each player
        # player_hand.add_card(card)
        # dealer_hand.add_card(my_deck.deal_card())
        # player_hand.add_card(my_deck.deal_card())
        # dealer_hand.add_card(my_deck.deal_card())

        # # Display the hands
        # print("Player's hand:", player_hand)
        # print("Dealer's hand:", dealer_hand)

        # Play the game (add more game logic as needed)
        # For example, you might ask the player if they want to hit or stand, and then deal additional cards accordingly.

        # Display the final hands and their values
        # print("Player's final hand:", player_hand, "Value:", player_hand.get_value())
        # print("Dealer's final hand:", dealer_hand, "Value:", dealer_hand.get_value())
                
                                
                    # sim_num_matrix[hand_sum][num_of_cards][face_card_rank] = 1
                # else:
                #     percentage_matrix[hand_sum][num_of_cards][face_card_rank] = (current_percentage * sim_num + result)/(sim_num + 1)
                    # sim_num_matrix[hand_sum][num_of_cards][face_card_rank] += 1
                # Check for convergence or check if all of the matrix is filled
                # if percentage_matrix[hand_sum][num_of_cards][face_card_rank] is not None and abs(result - result_dict[hand_sum]) < desired_precision:
                #     # the iteration num 
                #     print(f"Converged after {iteration + 1} iterations.")
                #     break

        # Check if the matrix is filled
        
        # dealer_hand.add_card(cards[-1])


        # # Initialize deck and remove cards that are already dealt
        # deck = Deck()
        # cards_to_remove = []
        # cards_to_remove.append(dealer_hand)
        # cards_to_remove.append(player_hand)
        # deck = [x for x in deck if x not in cards_to_remove]
        
        # # Simple approach: assume player and the dealer both follow the same strategy
        # for player_hand_num in range ()
        #     stand_wins = 0
        #     hit_wins = 0