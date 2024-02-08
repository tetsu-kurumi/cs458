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
        
        # print(percentage_matrix)
        # for sum in self.desired_sum:
        #     print("sum:", sum)
        #     for num_of_cards in self.nums_of_cards: 
        #         print("    num_of_cards:", num_of_cards)
        #         for face_card_rank in RANKS:
        #             print("      face_card_rank:", face_card_rank)
        #             print("        win percentage of stand:",percentage_matrix[sum][num_of_cards][face_card_rank][0])
        #             print("        win percentage of hit:",percentage_matrix[sum][num_of_cards][face_card_rank][1])
                        
        higher_ranks = ('A', '7', '8', '9', 'T', 'J', 'Q', 'K')
        lower_ranks = ('2', '3', '4', '5', '6')
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
                        # Default to default strategy (hit until sum is 17 if there is no percentage)
                        if percentages is None or sim_num_matrix[sum][num_of_cards][face_card_rank][ace_count] < 3:
                            if sum >= 17:
                                dict_by_face_card_rank[ace_count] = False
                            else:
                                randnum = random.random()
                                # hit more if it's 7-A
                                if face_card_rank in higher_ranks:
                                    if randnum > 0.8:
                                        dict_by_face_card_rank[ace_count] = False
                                    else:
                                        dict_by_face_card_rank[ace_count] = True
                                # stand more if it's 2-6
                                if face_card_rank in lower_ranks:
                                    if randnum > 0.8:
                                        dict_by_face_card_rank[ace_count] = True
                                    else:
                                        dict_by_face_card_rank[ace_count] = False
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
        
        # print("self.matrix:\n")
        # for sum in self.desired_sum:
        #     print("sum:", sum)
        #     for num_of_cards in self.nums_of_cards: 
        #         print("    num_of_cards:", num_of_cards)
        #         for face_card_rank in RANKS:
        #             print("        face_card_rank:", face_card_rank)
        #             print("        ",self.matrix[sum][num_of_cards][face_card_rank])
        

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
    print("archive.py")
    for i in range (100):
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
