from typing import Type
import random

# Define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# Define card class
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

# Define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        ans = "Hand contains "
        for i in range(len(self.cards)):
            ans += str(self.cards[i]) + " "
        return ans

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = False
        for c in self.cards:
            rank = c.get_rank()
            v = VALUES[rank]
            if rank == 'A':
                aces = True
            value += v
        if aces and value < 12:
            value += 10
        return value

# Define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    def __str__(self):
        ans = "The deck: "
        for c in self.deck:
            ans += str(c) + " "
        return ans

# Define player class
class Player:
    def __init__(self):
        self.matrix = None

    def sim(self, trials: int) -> None:
        matrix = [[[0, 0] for _ in range(10)] for _ in range(22)]  # Initialize matrix with zeros
        for _ in range(trials):
            deck = Deck()
            deck.shuffle()
            player_hand = Hand()
            dealer_hand = Hand()
            player_hand.add_card(deck.deal_card())
            player_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card())
            while player_hand.get_value() < 12:  # Hit if hand value is less than 12
                player_hand.add_card(deck.deal_card())
            while dealer_hand.get_value() < 17:  # Dealer must hit until hand value is 17 or higher
                dealer_hand.add_card(deck.deal_card())
            player_value = player_hand.get_value()
            dealer_value = dealer_hand.get_value()

            # If stand
            if player_value <= 21 and (dealer_value > 21 or player_value > dealer_value):
                matrix[player_value][VALUES[dealer_hand.cards[0].get_rank()] - 1][0] += 1
            # If we lose due to having something smaller than the dealer, simulate if hitting would've made us win
            elif player_value <= 21 and player_value <= dealer_value:
                # Hit one card
                player_hand.add_card(deck.deal_card())
                player_value = player_hand.get_value()
                # if player_value <= 21 and (dealer_value > 21 or player_value > dealer_value):
                #     matrix[player_value][VALUES[dealer_hand.cards[0].get_rank()] - 1][1] += 1
                if player_value <= 21:
                    matrix[player_value][VALUES[dealer_hand.cards[0].get_rank()] - 1][1] += 1
            
            # # Create list
            
            # # Update matrix
            # matrix[player_value][VALUES[dealer_hand.cards[0].get_rank()] - 1][0] = 
            # # Matrix should tell whether we will bust if we hit (if not, we should hit)
            # if player_value <= 21 and :
            #     matrix[player_value][VALUES[dealer_hand.cards[0].get_rank()] - 1] += 1
        self.matrix = matrix

        print(self.matrix)

        # boolean_matrix = [[0 for _ in range(10)] for _ in range(22)]
        # for row in matrix:
        #     row_sum = sum(row)
        #     for win_num in row:
        #         if 



        # for row_idx, row in enumerate(matrix):
        #     # print(row)
        #     row_sum = sum(row)
        #     for idx, face_card in enumerate(row):
        #         # print(face_card)
        #         if row_sum == 0:
        #             self.matrix[row_idx][idx] = False  # No data available for this hand value, hence False
        #         elif face_card / row_sum >= 0.5:
        #             self.matrix[row_idx][idx] = True
        #         else:
        #             self.matrix[row_idx][idx] = False
        #     else:
        #         self.matrix[row_idx][idx] = True
        # print(self.matrix)

    def hitme(self, playerhand: Type[Hand], dealerfacecard: Type[Card]) -> bool:
        if self.matrix is None:
            raise ValueError("Simulation not run yet. Call 'sim' method first.")
        player_value = playerhand.get_value()
        dealer_rank = dealerfacecard.get_rank()
        if player_value > 21:
            return False  # Player busts
        # row_sum = sum(self.matrix[player_value])
        # if row_sum == 0:
        #     return False  # No data available for this hand value
        # print(self.matrix[player_value][VALUES[dealer_rank] - 1] )
        # print("row_sum:", row_sum)
        print("decision:", self.matrix[player_value][VALUES[dealer_rank] - 1][1] >=  self.matrix[player_value][VALUES[dealer_rank] - 1][0])
        return self.matrix[player_value][VALUES[dealer_rank] - 1][1] >=  self.matrix[player_value][VALUES[dealer_rank] - 1][0]
        # return self.matrix[player_value][VALUES[dealer_rank]-1]


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

# Run simulation and play 100,000 hands
if __name__ == "__main__":
    player = Player()
    player.sim(100000)
    win_percentage = player.play(100000)
    print("Win percentage after playing 100,000 hands:", win_percentage * 100)
