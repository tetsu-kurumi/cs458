## Summary output of 100000 trials
Win rate over 100000 trials: 43.481%

## Code Explanation
* `__init__(self)`
    Initializes a matrix (in the form of a nested dictionary) which takes in as input 
    the player hand's value, player hand's number of cards, and number of aces in the player's hand,
    and sets a boolean value as the output (which is returned when the hitme function performs a matrix lookup)

* `sim(self, trials: int) -> None`
    This function performs a Monte Carlo Simulation, which calculates the win percentage of if we choose to hit or stand in a given state 
    (which is defined by the player hand's value, player hand's number of cards, and number of aces in the player's hand).
    - Initialization
        The function initializes two matrices, both which have the same dimensions as the matrix defined in self.matrix:
        - percentage_matrix: stores the win percentage of hit and stand for every state
        - sim_num_matrix: stores the number of times the function has simulated a given state
    - Simulation loop
        The function simulates states randonmly, but in a specific order, starting from player hand's number of cards = 7, down to 2.
        I choose to do so, since by doing this, the sim function can utilize information from previous simulations to calculate win probabilties for the strategy "hit" too. 
        In other words, when calculating the win probability when choosing to hit at a certain state (e.g. sum = 13, player hand's number of cards = 3, ace count = 0), the function deals a card, then looks up the percentage_matrix to see if the state it is in right now with an additional card has been simulated before,(e.g. if it a 4 is dealt, it looks up the matrix for state (sum = 17, player hand's number of cards = 4, ace count = 0)) and if it is, it propagates the percentage that has already been calculated for that as the win percentage for the original state that it is simulating in the moment.
        In theory, the matrix should get populated from the states with the most number of cards, thus maximizing the probability of the simulation to use that information in states with less number of cards, recursively.
        The win percentage for strategy "stand" is also calculated for each state the simulation encounters.
        These calculations are done by  `do_hit(self, deck, dealerhand, playerhand, percentage_matrix, num_of_cards, face_card_rank, ace_count, sim_num_matrix)` and `do_stand(self, dealerhand, playerhand)`.
    - Updating matrix
        Once the win probabilties for both strategy stand and hit have been calculated, the function updates the matrix's specific state cell, by calculating the average win rate.
    - Simulation number
        The simulation is done in 5 batches (player hand's number of cards = 7, down to 2), and thus the `trials` are divided into the batches. The function is made sure to stop its simulation if it reaches the number of simulations defined by `trials` with the `max_trials` variable.
    - Converting the win percentage matrix into a boolean matrix
        Once the max iteration number is reached, the probability_matrix is coverted into a boolean matrix, where each state has corresponding boolean, which is stored in `self.matrix`. The conversion is done by comparing the win probability of hit (True) and stand (False), and choosing the strategy that yields a higher win probability.
        The only exceptions are when there are less than 3 simulations done for a certain cell. In this case, due to the lack of data, the function follows the default strategy, which is the strategy of the dealer, and assigns a boolean depending on the value of the hand.
* `do_stand(self, dealerhand, playerhand)` 
    This function simply returns (win = 1, loss = 0) if the player would win and (win = 0, loss = 1) if the player would lose in the given state when chosing to stand. 
    
* `do_hit(self, deck, dealerhand, playerhand, percentage_matrix, num_of_cards, face_card_rank, ace_count, sim_num_matrix)`
    This function simulates the scenario where the player hits. As explained in the `sim` function section, deals a hand to simulate a hit.If this makes the player go bust, it returns (win = 0, loss = 1). If not, the function looksup if this updates state has been simulated before. If it has, it propagates the probability previously stored, and if not, it defaults to the default strategy, which is the dealer's strategy, and simulates whether the player wins or not, and returns the result.
    """

* `hitme(self, playerhand: Type[Hand], dealerfacecard: Type[Card]) -> bool` 
    This function first checks if the input playerhand has a value less that 12 or has less than 2 cards or more than 20.
    If the value is less than 12 or the number of cards is less than 2, the function automatically returns True (since it is mathematically impossible to bust with another card) and if the value 21 or more the function returns False (since mathematically, it is impossible to hit anymore).
    Then, if it does not meet these criteria (if there are 2 or more cards, and the value is between 12 and 20), the function looks up the given state in the lookup table defined in `self.matrix`, and returns the corresponding boolean value.

* `play(self, trials: int) -> float` 
    This function first checks if `self.matrix` has been defined or not, and if not, throws an error.
    Then, it simulates a black jack game play for the iteration number defined by `trials` and records the number of times that the player wins, and lastly returns the win proportion against the number of trials.


## Simulation Output 
### Decision Matrix (original appended at the end):
player hand value: 12
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 4
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
    num of cards: 5
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
    num of cards: 6
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
player hand value: 13
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 4
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 5
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 6
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
player hand value: 14
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 4
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 5
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 6
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
player hand value: 15
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 4
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
    num of cards: 5
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
    num of cards: 6
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
player hand value: 16
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 4
      face card rank: A
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
    num of cards: 5
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
    num of cards: 6
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 2
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 3
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 4
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 5
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 6
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: True
        ace count 4: True
player hand value: 17
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 4
      face card rank: A
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
    num of cards: 5
      face card rank: A
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 6
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
player hand value: 18
    num of cards: 2
      face card rank: A
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 4
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
    num of cards: 5
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 6
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
player hand value: 19
    num of cards: 2
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 4
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 5
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 6
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
player hand value: 20
    num of cards: 2
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 4
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 5
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 6
      face card rank: A
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
---
### Percentage Matrix (original appended at the end):
player hand value: 12
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13319672131147547, 0.18822229143584804), 1: None, 2: (0.07692307692307693, 0.4064560439560439), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3482352941176472, 0.3837334660767491), 1: None, 2: (0.4, 0.516185477998875), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3312368972746332, 0.3483988261179578), 1: None, 2: (0.45, 0.5143935910644835), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3890160183066363, 0.38835995342150886), 1: None, 2: (0.2592592592592593, 0.6081935300235954), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.41295546558704455, 0.3811616321252021), 1: None, 2: (0.34782608695652173, 0.4922077922077924), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4354066985645933, 0.40104002693604285), 1: None, 2: (0.5416666666666666, 0.6317114598364598), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2761506276150629, 0.3619787060956271), 1: None, 2: (0.21739130434782608, 0.6364747686675852), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2652173913043476, 0.31196001910311305), 1: None, 2: (0.23529411764705882, 0.4557350742355994), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24168514412416892, 0.2843532757096903), 1: None, 2: (0.36, 0.5599135792144839), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20682730923694773, 0.26810907173040677), 1: None, 2: (0.0967741935483871, 0.3645519391310865), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20292887029288706, 0.25514321643898635), 1: None, 2: (0.24, 0.509835503013733), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19915254237288132, 0.26422457528308424), 1: None, 2: (0.3333333333333333, 0.48983836969131084), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2106430155210643, 0.2367863279487198), 1: None, 2: (0.24, 0.3953128432414146), 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.072463768115942, 0.18706496258264318), 1: (0.11904761904761904, 0.21729301201523235), 2: (0.0, 0.21860119047619048), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4074074074074074, 0.4829553545315817), 1: (0.38333333333333336, 0.3609219441760427), 2: (0.36363636363636365, 0.42994732540187086), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3888888888888889, 0.3925756469929404), 1: (0.46, 0.35400337490505324), 2: (0.41379310344827586, 0.3594892598949394), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.32142857142857145, 0.4236509603841537), 1: (0.3333333333333333, 0.387707267344052), 2: (0.38461538461538464, 0.4231716404510522), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.49999999999999994, 0.4482547138210667), 1: (0.453125, 0.43282113263651134), 2: (0.3181818181818182, 0.351010101010101), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3787878787878788, 0.38629815438531645), 1: (0.4305555555555556, 0.4757822941124684), 2: (0.36666666666666664, 0.36414141414141415), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22222222222222218, 0.3568857272459449), 1: (0.22641509433962265, 0.310214761730689), 2: (0.4782608695652174, 0.30280299410734196), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2545454545454545, 0.358087436817094), 1: (0.25862068965517243, 0.3565200599989269), 2: (0.20833333333333334, 0.3975698491323491), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2923076923076924, 0.2839241592329802), 1: (0.26666666666666666, 0.30105554015548974), 2: (0.23076923076923078, 0.31899687793352965), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20289855072463772, 0.20900077241599982), 1: (0.10909090909090909, 0.26230775688206015), 2: (0.18181818181818182, 0.30951858783524727), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1594202898550725, 0.353910932146837), 1: (0.17910447761194032, 0.285255585084913), 2: (0.2631578947368421, 0.4009711779448621), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18309859154929578, 0.2147982592838829), 1: (0.21153846153846154, 0.3033376719250799), 2: (0.3, 0.2922181086886969), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19696969696969696, 0.3080598148096547), 1: (0.1499999999999999, 0.24278357062461936), 2: (0.15625, 0.2732288544788545), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.27649769585253453), 2: (0.16666666666666666, 0.16666666666666666), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.5714285714285714), 1: (0.23076923076923078, 0.1804029304029304), 2: (0.4, 0.45614035087719296), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.36363636363636365, 0.24830235124352773), 2: (0.5, 0.29166666666666663), 3: (1.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.2222222222222222), 1: (0.45454545454545453, 0.5443139469226425), 2: (0.2727272727272727, 0.43496503496503497), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.38461538461538464, 0.3143123543123543), 2: (0.5, 0.3333333333333333), 3: (1.0, 0.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5333333333333333, 0.4945484400656814), 2: (0.42857142857142855, 0.2285714285714286), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.4444444444444444), 1: (0.19047619047619047, 0.4140559732664995), 2: (0.75, 0.41666666666666663), 3: (0.0, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18181818181818182, 0.5757575757575758), 1: (0.23076923076923078, 0.35), 2: (0.16666666666666666, 0.6443602693602694), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.08333333333333333), 1: (0.18181818181818182, 0.20979020979020976), 2: (0.3333333333333333, 0.43333333333333335), 3: (0.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.07272727272727272), 1: (0.3157894736842105, 0.1710359463842436), 2: (0.0, 0.2547846889952153), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1111111111111111, 0.2469135802469136), 1: (0.09090909090909091, 0.24139724460870707), 2: (0.14285714285714285, 0.4277551020408163), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.45454545454545453, 0.4519936204146731), 2: (0.0, 0.15861471861471862), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.21710526315789475), 1: (0.2222222222222222, 0.25771604938271603), 2: (0.2727272727272727, 0.1811688311688312), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.25), 2: (0.0, 0.3333333333333333), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (1.0, 1.0), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.4444444444444444), 3: (0.0, 0.8333333333333333), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (1.0, 0.6666666666666666), 3: (0.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.6666666666666666), 3: (1.0, 1.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.5), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.5), 3: (0.0, 1.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 1.0), 2: (0.3333333333333333, 0.0), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.5), 3: (0.0, 1.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.16666666666666666, 0.20833333333333334), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.2), 2: (0.0, 0.0), 3: None, 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (1.0, 1.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 1.0), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}
player hand value: 13
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13677130044843056, 0.17778238136610902), 1: (0.05128205128205128, 0.25656576662927966), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34894613583138134, 0.33739975934750355), 1: (0.3333333333333334, 0.4310132415448555), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.35733333333333334, 0.3173419727052053), 1: (0.3888888888888889, 0.45703528384973385), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.41894736842105246, 0.3693968392902241), 1: (0.38461538461538464, 0.5089356002050505), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4158878504672896, 0.3347468184351956), 1: (0.3698630136986302, 0.5058207045376731), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4247191011235955, 0.35929411723481747), 1: (0.3448275862068966, 0.5223938807451941), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.27713625866050823, 0.3447052392360102), 1: (0.28125, 0.5488415393334367), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2549019607843138, 0.31467266290930296), 1: (0.2931034482758622, 0.5126527175154746), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23221757322175743, 0.2600839156247956), 1: (0.18181818181818182, 0.40048089104802254), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2191142191142192, 0.22176363964347612), 1: (0.18032786885245902, 0.3790497065644507), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2009237875288684, 0.23192446853397952), 1: (0.2424242424242425, 0.33097791228344525), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21158129175946544, 0.23686894332385827), 1: (0.1694915254237288, 0.3793053052142874), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21700223713646535, 0.22295407489947308), 1: (0.1515151515151515, 0.38255022839126357), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.12643678160919544, 0.20847398193695976), 1: (0.11538461538461539, 0.12213205539830449), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3875, 0.29175273894387244), 1: (0.36448598130841126, 0.36264351211493856), 2: None, 3: (1.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4375, 0.2394683104137406), 1: (0.36111111111111116, 0.38243761473923904), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.35323664000134586), 1: (0.423728813559322, 0.31618600723529383), 2: None, 3: (0.5, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.45121951219512196, 0.31274897448409245), 1: (0.4672897196261682, 0.3636000921894176), 2: None, 3: (0.25, 0.25), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.41333333333333333, 0.26405134394430907), 1: (0.4019607843137255, 0.377179630305386), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22972972972972974, 0.2657719208710158), 1: (0.21951219512195122, 0.3871853618176824), 2: None, 3: (0.0, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15942028985507245, 0.2800830629835613), 1: (0.21551724137931033, 0.3645668288548376), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2717391304347827, 0.29972404652130363), 1: (0.14678899082568808, 0.27289744813869754), 2: None, 3: (0.5, 1.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20253164556962025, 0.20111793996860636), 1: (0.2459016393442623, 0.2671259633727278), 2: None, 3: (1.0, 1.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1111111111111111, 0.31085854572606675), 1: (0.2636363636363638, 0.2538612819119989), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24468085106382984, 0.19499128320814732), 1: (0.19379844961240314, 0.28406289997656065), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.17948717948717952, 0.2539832004407869), 1: (0.16216216216216217, 0.2834538669278945), 2: None, 3: (0.5, 0.5), 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.14545454545454548), 1: (0.05555555555555555, 0.2838882864973946), 2: (0.0, 0.3), 3: (0.0, 0.0), 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.36734693877551017), 1: (0.4444444444444444, 0.282010582010582), 2: (0.3333333333333333, 0.19999999999999998), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.5384615384615384, 0.4079939668174963), 2: (0.5, 0.16666666666666666), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.6666666666666666), 1: (0.4444444444444444, 0.4444444444444444), 2: (0.6666666666666666, 0.3333333333333333), 3: (0.0, 1.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.36875), 1: (0.3684210526315789, 0.2391387559808612), 2: (0.5714285714285714, 0.3333333333333333), 3: (1.0, 0.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.6923076923076923), 1: (0.42857142857142855, 0.4439909297052155), 2: (0.4444444444444444, 0.20158730158730154), 3: (0.0, 0.5), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.45777777777777773), 1: (0.2916666666666667, 0.33575837742504405), 2: (0.3333333333333333, 0.3888888888888889), 3: (0.0, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.14285714285714285, 0.3321995464852608), 1: (0.45, 0.43710573476702497), 2: (0.14285714285714285, 0.1396103896103896), 3: (0.0, 1.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.05555555555555555), 1: (0.35714285714285715, 0.2591004233861377), 2: (0.42857142857142855, 0.4), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.045454545454545456), 1: (0.15, 0.17308775783040486), 2: (0.16666666666666666, 0.038461538461538464), 3: (0.0, 0.5), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2857142857142857, 0.15873015873015875), 1: (0.4444444444444444, 0.2639978110992603), 2: (0.5, 0.4365079365079365), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.45454545454545453, 0.22727272727272727), 1: (0.16, 0.2367213838792786), 2: (0.3333333333333333, 0.1828282828282828), 3: (1.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.10796221322537111), 1: (0.23529411764705882, 0.21586452762923347), 2: (0.15384615384615385, 0.22252747252747251), 3: (0.5, 0.5), 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.3333333333333333), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.25, 0.0), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: (0.3333333333333333, 0.1111111111111111), 3: (1.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.75, 0.25), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.3333333333333333, 0.3333333333333333), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.4, 0.4), 2: (1.0, 0.5), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.5), 2: (1.0, 0.0), 3: (0.5, 1.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.3333333333333333, 0.3333333333333333), 2: (0.25, 0.25), 3: (0.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6666666666666666, 0.5), 2: (0.0, 0.5), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 1.0), 1: (0.0, 0.5), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.25, 0.2375), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.3333333333333333, 0.13333333333333333), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.0), 2: (0.3333333333333333, 0.4777777777777778), 3: None, 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 14
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.11347517730496454, 0.1516710421109428), 1: (0.0851063829787234, 0.24207172171949123), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.36299765807962536, 0.32760933216574467), 1: (0.36923076923076925, 0.4880864676469823), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3520782396088017, 0.3100180640886652), 1: (0.3, 0.5327440726859873), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4591194968553459, 0.3045097626237968), 1: (0.373134328358209, 0.52053666501155), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.38235294117647045, 0.3213781789033251), 1: (0.4857142857142857, 0.5624026545834019), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4157608695652174, 0.34845380556821665), 1: (0.3783783783783784, 0.5082985711749148), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.27272727272727243, 0.3094019437969013), 1: (0.20833333333333334, 0.4657228668063705), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2317073170731706, 0.28140231112089326), 1: (0.32876712328767116, 0.45642480580943257), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2282051282051282, 0.25349982226500445), 1: (0.22535211267605634, 0.4618169235887434), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20320855614973266, 0.2285545689192187), 1: (0.14084507042253516, 0.356413455177432), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22332506203473945, 0.24941679148781842), 1: (0.2241379310344828, 0.37032123623184726), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20222222222222228, 0.22115929787857508), 1: (0.19672131147540986, 0.3827118111378637), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24285714285714305, 0.21566306223004653), 1: (0.3, 0.37800549025530256), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.11290322580645167, 0.21808115837071446), 1: (0.08247422680412367, 0.17970668018273842), 2: (0.3333333333333333, 0.3857142857142857), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3636363636363637, 0.24244679575898737), 1: (0.3629032258064517, 0.2922866564365771), 2: (1.0, 0.6371610845295056), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.485981308411215, 0.2880844418698081), 1: (0.4948453608247423, 0.2963670890449401), 2: (0.2857142857142857, 0.4095238095238095), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3805309734513274, 0.3340181663207461), 1: (0.45714285714285713, 0.29141199325184364), 2: (0.5, 0.5233134920634921), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.38333333333333325, 0.3223179844909864), 1: (0.4782608695652174, 0.30934624740776795), 2: (0.0, 0.30657596371882084), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4112903225806452, 0.29929564437647066), 1: (0.3921568627450982, 0.3717812627264049), 2: (0.4, 0.4646464646464647), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3220338983050847, 0.2410627899519784), 1: (0.2708333333333333, 0.3804176473741383), 2: (0.2, 0.445103785103785), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20769230769230773, 0.29438644837581945), 1: (0.25225225225225223, 0.3053958337354726), 2: (0.2857142857142857, 0.5373709623709624), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24193548387096775, 0.22124434897289313), 1: (0.23711340206185572, 0.22644383188991396), 2: (0.0, 0.7696969696969698), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20212765957446813, 0.22696928445000342), 1: (0.2032520325203252, 0.2545932381619158), 2: (0.25, 0.33452380952380956), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21641791044776118, 0.24644971189059456), 1: (0.21232876712328766, 0.22972319326292603), 2: (0.5, 0.33333333333333337), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.26785714285714307, 0.23253893164507472), 1: (0.26595744680851063, 0.2616864296786532), 2: (0.0, 0.5001274542451012), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.26, 0.23356372472354947), 1: (0.2127659574468085, 0.21789421062679967), 2: (0.125, 0.4230207292707293), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.125, 0.21130952380952378), 1: (0.19047619047619047, 0.1088112664420607), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.75, 0.25), 1: (0.36363636363636365, 0.4670995670995672), 2: (0.2857142857142857, 0.23809523809523808), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.10681818181818184), 1: (0.38461538461538464, 0.3067339115133233), 2: (0.3333333333333333, 0.2737891737891738), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6, 0.42749999999999994), 1: (0.3333333333333333, 0.27031055900621115), 2: (0.3125, 0.2423076923076923), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.38461538461538464, 0.38461538461538464), 1: (0.391304347826087, 0.41992094861660073), 2: (0.7333333333333333, 0.4339181286549707), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.2908424908424908), 1: (0.4642857142857143, 0.3248085141102918), 2: (0.5833333333333334, 0.3095238095238095), 3: None, 4: (1.0, 1.0)}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.09090909090909091, 0.1636363636363636), 1: (0.25925925925925924, 0.4462841775219943), 2: (0.42857142857142855, 0.19999999999999998), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3, 0.32), 1: (0.23809523809523808, 0.3633299197815326), 2: (0.08333333333333333, 0.3731060606060606), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4166666666666667, 0.3543192918192917), 1: (0.29411764705882354, 0.16053064582476348), 2: (0.25, 0.43333333333333335), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23529411764705882, 0.1770944741532977), 1: (0.13333333333333333, 0.22299473843591494), 2: (0.2727272727272727, 0.3509504849217768), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.08333333333333333, 0.24537037037037038), 1: (0.35294117647058826, 0.386651014160605), 2: (0.25, 0.318452380952381), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.125, 0.16346153846153844), 1: (0.1891891891891892, 0.26410853252958516), 2: (0.6, 0.2625), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.18558897243107766), 1: (0.12121212121212122, 0.25991735537190086), 2: (0.36363636363636365, 0.5130369630369631), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.0), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.25, 0.2), 2: (0.4, 0.4), 3: (1.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 1.0), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 1.0), 2: (0.5, 0.25), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6666666666666666, 0.28571428571428575), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.2, 0.5666666666666667), 2: (0.0, 0.8), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.42857142857142855, 0.14285714285714285), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.25), 2: (0.3333333333333333, 0.0), 3: (1.0, 0.5), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.25, 0.0), 2: (0.0, 0.47348484848484856), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.3333333333333333, 0.3333333333333333), 2: (0.2, 0.21333333333333332), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.5, 0.3125), 2: (0.0, 0.275), 3: (0.0, 0.0), 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (1.0, 0.5), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 1.0), 2: (1.0, 1.0), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 15
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.14657210401891257, 0.14893896207897972), 1: (0.043478260869565216, 0.24853654438574332), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4114583333333332, 0.27046523314403276), 1: (0.3018867924528302, 0.47937129790004523), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.373015873015873, 0.28116941944911333), 1: (0.3972602739726027, 0.520385372095045), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.42406876790830944, 0.2837302396514831), 1: (0.2608695652173913, 0.5408998503245145), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.42201834862385323, 0.3018254260579836), 1: (0.43661971830985913, 0.5254287299584811), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.455012853470437, 0.29035766385679546), 1: (0.47058823529411764, 0.5282750138347728), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2528409090909091, 0.2846800628463758), 1: (0.22807017543859648, 0.5462221986632688), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2664835164835167, 0.23542520552664242), 1: (0.2698412698412698, 0.43110095297118867), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20887728459530025, 0.2347382252880028), 1: (0.21874999999999997, 0.3543395293802357), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19170984455958548, 0.19581417097184708), 1: (0.24242424242424243, 0.3486360160763315), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19662921348314608, 0.19959002152305133), 1: (0.09677419354838708, 0.3127597786235842), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23469387755102045, 0.21994508597781057), 1: (0.12500000000000003, 0.42037415675057277), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23835616438356164, 0.22585832934293942), 1: (0.2597402597402597, 0.34076516760062997), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.10439560439560447, 0.16373676390398004), 1: (0.09375, 0.1660449725232492), 2: (0.0, 0.3818027210884353), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3443708609271523, 0.25195052991911143), 1: (0.3626373626373626, 0.3178496564985484), 2: (0.0, 0.8), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.40506329113924044, 0.2705096354722406), 1: (0.35514018691588783, 0.31523460521273233), 2: (0.0, 0.5213675213675214), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4588235294117648, 0.3152934768678711), 1: (0.4086956521739132, 0.2823114374126245), 2: (0.6, 0.6332539682539682), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4187500000000002, 0.28047009556646213), 1: (0.4672897196261682, 0.2466721882883953), 2: (0.6666666666666666, 0.5001984126984127), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.46111111111111114, 0.275333754807439), 1: (0.4485981308411215, 0.31766580671798605), 2: (0.5, 0.4329365079365079), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21951219512195122, 0.3003993926676418), 1: (0.255813953488372, 0.3572391301511659), 2: (0.16666666666666666, 0.45722934472934473), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22994652406417113, 0.30018916614026137), 1: (0.25000000000000006, 0.2543724480367947), 2: (0.5, 0.4217472342472343), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21556886227544914, 0.2275663345301274), 1: (0.2727272727272727, 0.2489946755557446), 2: (0.4444444444444444, 0.8038480038480038), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18124999999999997, 0.17491634411738424), 1: (0.2777777777777776, 0.22004945434774598), 2: (0.14285714285714285, 0.2528822055137845), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24309392265193375, 0.19730231192068504), 1: (0.21505376344086022, 0.25422381882005957), 2: (0.2727272727272727, 0.42854191263282176), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22527472527472522, 0.21434264650303947), 1: (0.216, 0.2376622810171732), 2: (0.125, 0.2748359973359973), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18120805369127516, 0.17469055672838835), 1: (0.19626168224299065, 0.21089320739011108), 2: (0.14285714285714285, 0.3232909947195662), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.045454545454545456, 0.18928571428571422), 1: (0.21739130434782608, 0.1085758286484299), 2: (0.5714285714285714, 0.17142857142857143), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5625, 0.2857142857142857), 1: (0.25, 0.39285714285714285), 2: (0.8, 0.09473684210526315), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2631578947368421, 0.22488038277511965), 1: (0.297872340425532, 0.2945907086238752), 2: (0.3076923076923077, 0.15384615384615385), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.42857142857142855, 0.1339285714285714), 1: (0.46511627906976744, 0.24713852376137513), 2: (0.3888888888888889, 0.281054131054131), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5789473684210527, 0.3394736842105263), 1: (0.325, 0.16623376623376623), 2: (0.3333333333333333, 0.3201754385964913), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4583333333333333, 0.3493589743589743), 1: (0.4146341463414634, 0.3255724054349132), 2: (0.3333333333333333, 0.17261904761904764), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.14444444444444443), 1: (0.17142857142857143, 0.3043660739149461), 2: (0.4375, 0.27179487179487183), 3: (0.0, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.3555555555555555), 1: (0.19444444444444445, 0.3821631251066734), 2: (0.07692307692307693, 0.2806915306915307), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3, 0.2106410256410257), 1: (0.25, 0.28220113220113235), 2: (0.29411764705882354, 0.3254901960784314), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2777777777777778, 0.1127946127946128), 1: (0.3, 0.21201980054921235), 2: (0.3684210526315789, 0.15751699823721985), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.5208333333333334), 1: (0.19148936170212766, 0.20216837330620865), 2: (0.2727272727272727, 0.2194805194805195), 3: (0.0, 1.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1111111111111111, 0.12759462759462759), 1: (0.26315789473684215, 0.2372679086841137), 2: (0.16666666666666666, 0.08686868686868687), 3: (0.0, 1.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2608695652173913, 0.24528713087065485), 1: (0.22727272727272727, 0.19228650137741043), 2: (0.1875, 0.14426510989010988), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.14285714285714285, 0.32142857142857145), 2: (1.0, 0.6666666666666666), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.25, 0.25), 2: (1.0, 0.6666666666666666), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.25, 0.25), 2: (0.6666666666666666, 0.3333333333333333), 3: (0.5, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 1.0), 1: (1.0, 0.0), 2: (0.0, 0.0), 3: (1.0, 1.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (1.0, 0.0), 3: (1.0, 1.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.5), 1: (0.5, 0.5714285714285715), 2: (0.5, 0.5), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6, 0.3333333333333333), 2: (0.5, 0.5), 3: (0.0, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.4, 0.6), 2: (0.3333333333333333, 0.0), 3: (0.0, 1.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.2857142857142857, 0.42857142857142855), 2: (0.3333333333333333, 0.3333333333333333), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.08333333333333333), 2: (0.5, 0.25), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.3333333333333333, 0.0), 2: (0.42857142857142855, 0.4857142857142857), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.25), 2: (0.0, 0.3333333333333333), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.0), 2: (0.2, 0.18666666666666668), 3: None, 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.6666666666666666, 0.0), 3: (0.0, 0.0), 4: (0.0, 0.0)}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.0), 3: None, 4: None}
player hand value: 16
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.12654320987654324, 0.17829929394914631), 1: (0.14634146341463414, 0.19608339528793475), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3742690058479532, 0.2608196289683232), 1: (0.44776119402985076, 0.505611423470759), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.33862433862433877, 0.23320108813493293), 1: (0.36619718309859156, 0.5237956099883471), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4360465116279071, 0.23639081110845642), 1: (0.30000000000000004, 0.5196926329181244), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34925373134328347, 0.2620162836818687), 1: (0.5, 0.5319313681071844), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4294871794871794, 0.30666650793159345), 1: (0.38333333333333336, 0.5547701693368539), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2385057471264369, 0.24487158355355992), 1: (0.3, 0.4385391738631073), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24633431085043989, 0.24041115519497508), 1: (0.2881355932203391, 0.42225106221794), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21725239616613418, 0.2199538316662492), 1: (0.18181818181818182, 0.3623564399473265), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20489296636085627, 0.1666306487448717), 1: (0.26666666666666666, 0.34675929169019276), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21554770318021202, 0.18895187485339693), 1: (0.17307692307692307, 0.32537153605183633), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20625, 0.1860455160159515), 1: (0.23728813559322035, 0.37298711313295924), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19417475728155345, 0.210089747157374), 1: (0.2424242424242425, 0.3626984972062741), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.10144927536231886, 0.10538768544410725), 1: (0.09333333333333334, 0.12526623119198785), 2: (0.0, 0.16666666666666666), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.39898989898989884, 0.231845435955927), 1: (0.3917525773195876, 0.28058207542743646), 2: (0.2, 0.5866666666666667), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3155339805825242, 0.25195546478486847), 1: (0.4615384615384617, 0.22016241121312743), 2: (0.6666666666666666, 0.6527065527065528), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4375, 0.22751963650957466), 1: (0.4727272727272728, 0.2869938091126787), 2: (0.8, 0.7214565826330532), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.46842105263157885, 0.2377129985289309), 1: (0.38202247191011246, 0.308723127744634), 2: (0.5, 0.4861111111111111), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.46634615384615397, 0.27311815864447464), 1: (0.44660194174757284, 0.2541983960473208), 2: (0.75, 0.547077922077922), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3103448275862068, 0.2518192327448073), 1: (0.2857142857142857, 0.315084230307149), 2: (0.25, 0.37637362637362637), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23280423280423287, 0.23335801779443158), 1: (0.24770642201834858, 0.2865628309127797), 2: (0.0, 0.42713635570778424), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24509803921568626, 0.2313759210789966), 1: (0.2857142857142857, 0.29651514480693086), 2: (0.25, 0.7291666666666667), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.158974358974359, 0.15270499405804563), 1: (0.3076923076923076, 0.19040166283907695), 2: (0.0, 0.23486684766589075), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20500000000000007, 0.20075299258280066), 1: (0.13559322033898305, 0.2070569193839295), 2: (0.0, 0.484375), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22279792746113988, 0.15644576967474114), 1: (0.23148148148148148, 0.2416591814838011), 2: (0.3333333333333333, 0.49296128707893416), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22926829268292684, 0.17246482609649985), 1: (0.1875, 0.21625411427595817), 2: (0.0, 0.3042438271604938), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.125, 0.12261904761904761), 1: (0.12962962962962962, 0.1302144513719466), 2: (0.0, 0.028571428571428574), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3076923076923077, 0.33516483516483514), 1: (0.4318181818181818, 0.2362012987012987), 2: (0.5, 0.1923076923076923), 3: (0.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.42857142857142855, 0.12221706864564007), 1: (0.391304347826087, 0.3744405370843989), 2: (0.5333333333333333, 0.2626780626780626), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.1898148148148148), 1: (0.4999999999999998, 0.26990983770787425), 2: (0.5882352941176471, 0.2882352941176471), 3: (0.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.43478260869565216, 0.10013175230566532), 1: (0.5254237288135594, 0.18920390344119162), 2: (0.08333333333333333, 0.27777777777777773), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25806451612903225, 0.2606537922105944), 1: (0.5333333333333333, 0.22099069512862618), 2: (0.5454545454545454, 0.3822510822510823), 3: (0.0, 0.0), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34375, 0.3204861111111111), 1: (0.3888888888888889, 0.21456557665134662), 2: (0.5384615384615384, 0.3230769230769231), 3: (1.0, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13043478260869565, 0.3417874396135265), 1: (0.20634920634920634, 0.2809414088215932), 2: (0.14285714285714285, 0.14285714285714285), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.38461538461538464, 0.14032121724429414), 1: (0.27419354838709675, 0.26962365591397863), 2: (0.25, 0.19444444444444445), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.17391304347826086, 0.13537549407114624), 1: (0.26666666666666666, 0.16503141797259438), 2: (0.1875, 0.22322414427677584), 3: (0.0, 1.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.28125, 0.16666666666666669), 1: (0.1896551724137931, 0.22678083036403868), 2: (0.4166666666666667, 0.3142857142857143), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21621621621621623, 0.2234630234630235), 1: (0.2127659574468085, 0.2711023578884721), 2: (0.23076923076923078, 0.1738927738927739), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0967741935483871, 0.19500363812757704), 1: (0.2653061224489796, 0.13756957328385894), 2: (0.2857142857142857, 0.17091836734693877), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.3333333333333333), 1: (0.25, 0.03125), 2: (0.0, 0.16666666666666666), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 1.0), 1: (0.3333333333333333, 0.17777777777777778), 2: (0.6, 0.0), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.4444444444444444, 0.0), 2: (0.5555555555555556, 0.2592592592592593), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.17142857142857143), 2: (0.5, 0.5), 3: (1.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.5), 1: (0.8, 0.2), 2: (0.2857142857142857, 0.14285714285714285), 3: (1.0, 0.5), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.8, 0.2), 2: (0.6666666666666666, 0.3333333333333333), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.125, 0.375), 2: (0.3333333333333333, 0.16666666666666666), 3: (0.0, 0.6666666666666666), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.6666666666666666, 0.3333333333333333), 2: (0.25, 0.0), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.0), 1: (0.0, 0.1), 2: (0.4, 0.2), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.0), 1: (0.25, 0.3125), 2: (0.0, 0.17532467532467533), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.6666666666666666), 1: (0.125, 0.40625), 2: (0.0, 0.13333333333333333), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.5), 1: (0.0, 0.0), 2: (0.125, 0.3125), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.26969696969696966), 2: (0.0, 0.6), 3: None, 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.0, 1.0), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
player hand value: 17
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.12166172106824924, 0.132643936260994), 1: (0.02127659574468085, 0.25585967718152), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3507246376811594, 0.22649277128934112), 1: (0.4098360655737705, 0.4361796210128611), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3485342019543974, 0.25834063809474456), 1: (0.3787878787878788, 0.4534869615611507), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4471299093655589, 0.2225350111378418), 1: (0.3571428571428572, 0.5499395354167085), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.42406876790830955, 0.2503375085465671), 1: (0.3508771929824562, 0.5290155341161787), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3908794788273615, 0.21542706387207589), 1: (0.3400000000000001, 0.5022980468956738), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3233082706766916, 0.28138435605405177), 1: (0.3230769230769231, 0.4456540481311874), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23666666666666666, 0.2271904788746508), 1: (0.2857142857142857, 0.4386799797413207), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22461538461538466, 0.18938570931331103), 1: (0.25, 0.42983312711295707), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19528619528619529, 0.16859497993739597), 1: (0.2033898305084746, 0.412409066961779), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21753246753246758, 0.14951461200782218), 1: (0.3026315789473684, 0.34382055925918004), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19999999999999996, 0.16998846321175545), 1: (0.19480519480519481, 0.35257419475132357), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21865889212827994, 0.1669781859666509), 1: (0.1891891891891892, 0.31925264142310317), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1245136186770428, 0.12053413512557482), 1: (0.13924050632911392, 0.16281310338317723), 2: (0.0, 0.7142857142857143), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3991935483870968, 0.23038216264022737), 1: (0.2735849056603773, 0.2207371377290956), 2: (0.45454545454545453, 0.5140640858344209), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.42035398230088494, 0.2657180209171364), 1: (0.31632653061224486, 0.21031130802337955), 2: (0.4, 0.43431372549019615), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.37558685446009404, 0.20905872516863216), 1: (0.48245614035087714, 0.3018089625680134), 2: (0.6666666666666666, 0.5048611111111111), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4951456310679609, 0.1690894004365329), 1: (0.41739130434782606, 0.2960651631243186), 2: (0.75, 0.6607142857142857), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3925233644859813, 0.21621605335328906), 1: (0.3969465648854962, 0.3481308622659101), 2: (0.75, 0.6875), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.311111111111111, 0.23507710599845436), 1: (0.2222222222222222, 0.2878383224421562), 2: (0.0, 0.29758241758241755), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2270742358078603, 0.20549636346037595), 1: (0.1834862385321101, 0.34412476269856523), 2: (0.0, 0.47602628852628853), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21929824561403508, 0.19403025031721635), 1: (0.3010752688172044, 0.17950164401698124), 2: (0.0, 0.5628342245989305), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2382978723404257, 0.15153764015643673), 1: (0.23300970873786409, 0.22248415023605506), 2: (0.125, 0.28240240620623397), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21459227467811165, 0.14317474590742887), 1: (0.14814814814814814, 0.2173330681521261), 2: (0.25, 0.2558441558441558), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2872340425531914, 0.196366213069144), 1: (0.24347826086956512, 0.23504973886809674), 2: (0.2857142857142857, 0.4694638694638695), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22413793103448276, 0.1451091970676499), 1: (0.23232323232323232, 0.18841925095169934), 2: (0.3333333333333333, 0.2567511192511192), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16279069767441862, 0.17973421926910296), 1: (0.11904761904761904, 0.1357820547573868), 2: (0.0, 0.14285714285714285), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1111111111111111, 0.1746031746031746), 1: (0.3606557377049181, 0.3077283372365339), 2: (0.5, 0.19266917293233082), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.53125, 0.10973011363636365), 1: (0.4807692307692308, 0.16077488687782804), 2: (0.2222222222222222, 0.26495726495726496), 3: (1.0, 1.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.47058823529411764, 0.23434873949579835), 1: (0.49122807017543857, 0.20693618103229086), 2: (0.35, 0.15673076923076926), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5609756097560976, 0.17012195121951218), 1: (0.45714285714285713, 0.22967099567099558), 2: (0.35714285714285715, 0.33458646616541354), 3: (0.0, 0.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6216216216216216, 0.29967329967329964), 1: (0.5185185185185185, 0.24144316730523632), 2: (0.25, 0.25), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3157894736842105, 0.23095238095238094), 1: (0.3088235294117647, 0.25317910790047016), 2: (0.15384615384615385, 0.21025641025641026), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15, 0.2375), 1: (0.2328767123287671, 0.18915051659196605), 2: (0.3076923076923077, 0.24145299145299146), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20454545454545456, 0.15943147761329582), 1: (0.27777777777777785, 0.1334656084656084), 2: (0.18181818181818182, 0.5393939393939394), 3: (0.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23076923076923078, 0.14836144247908953), 1: (0.20512820512820512, 0.16047199599831174), 2: (0.0, 0.3179093633639088), 3: (0.0, 1.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.225, 0.12676767676767678), 1: (0.22222222222222218, 0.13589010483420416), 2: (0.18181818181818182, 0.3753246753246753), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2857142857142857, 0.15129768190992682), 1: (0.2, 0.1745698380566802), 2: (0.07692307692307693, 0.17156177156177158), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23255813953488372, 0.07444085901858237), 1: (0.1276595744680851, 0.15053191489361697), 2: (0.21428571428571427, 0.2620115995115996), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.08333333333333333), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.0), 1: (0.5, 0.041666666666666664), 2: (0.375, 0.125), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.42857142857142855, 0.3333333333333333), 2: (0.3333333333333333, 0.2222222222222222), 3: (0.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.1875), 2: (0.16666666666666666, 0.5), 3: (0.5, 0.5), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.0), 1: (0.8181818181818182, 0.25757575757575757), 2: (0.3333333333333333, 0.3333333333333333), 3: (0.5, 0.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.5), 1: (0.5652173913043478, 0.32298136645962733), 2: (0.5, 0.2), 3: (0.0, 0.3333333333333333), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.5), 1: (0.5, 0.125), 2: (0.23076923076923078, 0.3076923076923077), 3: (0.0, 1.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.3333333333333333), 1: (0.375, 0.25), 2: (0.125, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.5), 1: (0.3076923076923077, 0.19230769230769232), 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.25, 0.125), 2: (0.5, 0.2916666666666667), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.2222222222222222, 0.10277777777777779), 2: (0.2, 0.27999999999999997), 3: (0.0, 0.5), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.2, 0.0), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.16666666666666666, 0.1597222222222222), 2: (0.3, 0.05), 3: None, 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.3333333333333333, 0.0), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (1.0, 1.0), 3: (0.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 1.0), 3: (0.5, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 1.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.5), 2: (0.0, 0.0), 3: None, 4: (1.0, 1.0)}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.4, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.3333333333333333, 0.6666666666666666), 3: None, 4: None}
player hand value: 18
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2491909385113269, 0.10346585117227325), 1: (0.17307692307692316, 0.28224050634730313), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.48366013071895425, 0.16041700225024036), 1: (0.6231884057971016, 0.5490380280726849), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.514754098360656, 0.14572134558186176), 1: (0.5, 0.5335214213384807), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5212355212355216, 0.17247283580277176), 1: (0.5873015873015872, 0.5338323273581601), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5212765957446807, 0.21944971299443505), 1: (0.5483870967741935, 0.5283281412235727), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5878378378378382, 0.1959575247470558), 1: (0.6666666666666666, 0.556077133861059), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6734693877551019, 0.2291246960232692), 1: (0.72, 0.6060530530622309), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3472222222222221, 0.2121251312040787), 1: (0.24193548387096775, 0.45725988037766835), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.36923076923076925, 0.18416759955221487), 1: (0.2686567164179105, 0.4419734762663878), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.31007751937984496, 0.14499184476960478), 1: (0.36486486486486486, 0.3436780483526215), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.31451612903225795, 0.1336957011789636), 1: (0.3157894736842105, 0.36695808309939143), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.12318431211045505), 1: (0.27868852459016397, 0.3879433740922689), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.37969924812030065, 0.15215183639505306), 1: (0.49180327868852447, 0.34158919984033714), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21481481481481482, 0.11181657848324508), 1: (0.24731182795698925, 0.20450349990252686), 2: (0.3333333333333333, 0.546031746031746), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5137254901960784, 0.15470803706097824), 1: (0.4770642201834863, 0.19607986822755963), 2: (0.6, 0.5174825174825175), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4898785425101216, 0.18650472334682858), 1: (0.5585585585585585, 0.24843108020060584), 2: (0.6666666666666666, 0.5612759063739456), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5138339920948621, 0.14977666065466813), 1: (0.46956521739130436, 0.317739316881203), 2: (0.4, 0.5674229691876749), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5636363636363644, 0.21775329706883736), 1: (0.5544554455445546, 0.28588697164388455), 2: (0.6, 0.40952380952380957), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6425531914893622, 0.20577796575884075), 1: (0.5378151260504204, 0.35620374148321904), 2: (1.0, 0.5793650793650793), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6491228070175439, 0.19298867736717693), 1: (0.7340425531914895, 0.26011892264996095), 2: (0.6666666666666666, 0.6666666666666666), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34509803921568627, 0.224478247381877), 1: (0.4239130434782609, 0.25933641877466757), 2: (0.5, 0.4932012432012432), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3566176470588234, 0.16564444778912796), 1: (0.3613445378151261, 0.3031238338242529), 2: (0.5, 0.6627450980392157), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3151750972762646, 0.12150268667778398), 1: (0.33620689655172414, 0.21552088300146638), 2: (0.4, 0.4064390155299247), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3720930232558139, 0.1362565495848038), 1: (0.2477064220183487, 0.2278685415034844), 2: (0.5714285714285714, 0.3484848484848485), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.31297709923664113, 0.1518668536116737), 1: (0.36111111111111116, 0.18808614548794295), 2: (0.0, 0.5490384615384616), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3245283018867925, 0.1664753448549232), 1: (0.3391304347826087, 0.1918623531354449), 2: (0.75, 0.259875695292362), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2592592592592593, 0.07799564270152505), 1: (0.22727272727272732, 0.1536656891495601), 2: (0.0, 0.06666666666666667), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4186046511627907, 0.1096345514950166), 1: (0.5555555555555556, 0.15491452991452992), 2: (0.38461538461538464, 0.2203103913630229), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6530612244897961, 0.16914038342609775), 1: (0.5151515151515151, 0.07538050185109009), 2: (0.7777777777777778, 0.2222222222222222), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5185185185185185, 0.064170692431562), 1: (0.4794520547945205, 0.17239199157007373), 2: (0.42857142857142855, 0.5523809523809524), 3: (1.0, 1.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6, 0.20585858585858585), 1: (0.5609756097560976, 0.1788617886178861), 2: (0.7777777777777778, 0.6120857699805068), 3: (1.0, 1.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666667, 0.2036693191865605), 1: (0.5925925925925926, 0.17783656672545564), 2: (0.7142857142857143, 0.14285714285714285), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6461538461538462, 0.19658119658119663), 1: (0.585714285714286, 0.2103276047261009), 2: (0.5, 0.2), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.39344262295081966, 0.2297684100962789), 1: (0.41025641025641024, 0.1648898443253282), 2: (0.45454545454545453, 0.2323232323232323), 3: (0.5, 0.5), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.07743589743589743), 1: (0.303370786516854, 0.2540919754402901), 2: (0.38461538461538464, 0.1282051282051282), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.39215686274509803, 0.10797046091163737), 1: (0.3552631578947369, 0.1572454631665158), 2: (0.35714285714285715, 0.12087912087912091), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.43137254901960786, 0.18243819266837172), 1: (0.38823529411764707, 0.2574789915966386), 2: (0.3333333333333333, 0.0), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18518518518518517, 0.14814814814814814), 1: (0.3763440860215054, 0.09806040026753099), 2: (0.4444444444444444, 0.25925925925925924), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2833333333333333, 0.10350877192982454), 1: (0.39080459770114945, 0.08424429976154114), 2: (0.16666666666666666, 0.2656305114638448), 3: (0.0, 0.0), 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.35714285714285715, 0.07142857142857142), 2: (0.0, 0.2), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.8571428571428571, 0.1142857142857143), 2: (0.6666666666666666, 0.4444444444444444), 3: (1.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.5), 1: (0.4375, 0.0625), 2: (0.5, 0.2333333333333333), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.3333333333333333), 1: (0.2857142857142857, 0.2653061224489796), 2: (0.4666666666666667, 0.2), 3: (0.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.16666666666666666), 1: (0.5, 0.109375), 2: (0.6666666666666666, 0.1111111111111111), 3: (1.0, 0.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.25), 1: (0.7142857142857143, 0.0), 2: (0.6, 0.2), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.6071428571428571, 0.13333333333333336), 2: (0.6, 0.2), 3: (0.5, 0.5), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.3333333333333333), 1: (0.2777777777777778, 0.2222222222222222), 2: (0.3333333333333333, 0.13333333333333333), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16666666666666666, 0.0), 1: (0.36363636363636365, 0.0), 2: (0.3, 0.1), 3: (1.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.4117647058823529, 0.0784313725490196), 2: (0.47368421052631576, 0.10526315789473684), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.25), 1: (0.22727272727272727, 0.18181818181818182), 2: (0.2857142857142857, 0.0), 3: (0.3333333333333333, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.42857142857142855, 0.32142857142857145), 1: (0.18181818181818182, 0.1515151515151515), 2: (0.0, 0.2), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2857142857142857, 0.14285714285714285), 1: (0.18181818181818182, 0.10909090909090909), 2: (0.375, 0.0), 3: (0.0, 0.0), 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 1.0), 2: None, 3: (1.0, 0.0), 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.3333333333333333, 0.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.5, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (1.0, 0.3333333333333333), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.0, 0.0), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: None, 3: (0.0, 0.0), 4: (0.0, 1.0)}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: (1.0, 0.0)}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: None, 2: (0.25, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.25, 0.5), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.3333333333333333, 0.0), 3: None, 4: None}
player hand value: 19
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.40942028985507256, 0.09239130434782614), 1: (0.32653061224489793, 0.2608676733374762), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6425992779783394, 0.10974729241877255), 1: (0.5588235294117647, 0.5623233796124388), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6450216450216453, 0.1649273345701917), 1: (0.7758620689655172, 0.5720712817113955), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6437768240343347, 0.12428088759017449), 1: (0.6933333333333331, 0.6043180801828965), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6819923371647514, 0.13300492610837447), 1: (0.5957446808510639, 0.6085154334913061), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7230769230769228, 0.1420118343195266), 1: (0.596153846153846, 0.505273762662575), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7620817843866169, 0.1594691310843206), 1: (0.8275862068965517, 0.6210208130827629), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6844106463878326, 0.1441187293020974), 1: (0.675, 0.6398783169937409), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4627659574468085, 0.11231884057971013), 1: (0.49230769230769234, 0.4362884582045937), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4152542372881356, 0.08215878679750216), 1: (0.5, 0.4524998041699519), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4380952380952381, 0.09679730299199325), 1: (0.4305555555555556, 0.4077537261660702), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.40234375, 0.10571808510638295), 1: (0.5131578947368419, 0.4339559743710507), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.36507936507936506, 0.0983881525118638), 1: (0.4153846153846154, 0.37849904302919124), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.38831615120274904, 0.09348962011015399), 1: (0.3645833333333334, 0.1711562542870294), 2: (0.6, 0.43690476190476185), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6401515151515149, 0.12643939393939396), 1: (0.6796116504854369, 0.2840971299908113), 2: (1.0, 0.6923076923076923), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6035087719298239, 0.16194056569996426), 1: (0.6792452830188679, 0.25609565837424486), 2: (0.75, 0.6319444444444444), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6262975778546713, 0.15505025539627612), 1: (0.7029702970297032, 0.2943012688247425), 2: (0.8181818181818182, 0.6833193321829687), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6872427983539094, 0.11790323225058925), 1: (0.7281553398058253, 0.23770303026367504), 2: (0.42857142857142855, 0.5578231292517007), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7246376811594201, 0.1277997364953884), 1: (0.693877551020408, 0.30245842576817883), 2: (0.5, 0.5565476190476191), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7918367346938775, 0.1617083946980855), 1: (0.7476635514018691, 0.30269465708796806), 2: (1.0, 0.7275), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7640449438202247, 0.13501687247376423), 1: (0.8210526315789474, 0.3777785710782697), 2: (0.6666666666666666, 0.510995485995486), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4269230769230769, 0.1340860973888496), 1: (0.40540540540540543, 0.18422003301968337), 2: (0.6, 0.6366666666666668), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3993288590604026, 0.09912933067295478), 1: (0.5315315315315318, 0.1479855691284127), 2: (0.25, 0.369388575937619), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.39655172413793116, 0.10445673389720235), 1: (0.4074074074074074, 0.23902640493109603), 2: (0.5, 0.533779761904762), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.39436619718309857, 0.12616122265507942), 1: (0.48979591836734687, 0.24735940334097795), 2: (0.5, 0.3178382401911814), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4659090909090909, 0.1163277511961723), 1: (0.5428571428571426, 0.18890854705773807), 2: (0.42857142857142855, 0.41258364651221796), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.26136363636363635, 0.06378299120234603), 1: (0.3492063492063492, 0.060757636387888496), 2: (0.625, 0.15), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6545454545454545, 0.12727272727272726), 1: (0.6043956043956041, 0.06419895893580102), 2: (0.5454545454545454, 0.21937645687645688), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7000000000000002, 0.06008403361344538), 1: (0.6444444444444446, 0.12268518518518516), 2: (0.75, 0.13846153846153847), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6705882352941176, 0.15388235294117644), 1: (0.6310679611650483, 0.09805825242718448), 2: (0.7333333333333333, 0.06666666666666667), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.609375, 0.11500000000000003), 1: (0.7524752475247525, 0.13307120185702773), 2: (0.6428571428571429, 0.3095238095238095), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6210526315789474, 0.15964912280701749), 1: (0.6853932584269664, 0.18607036770539284), 2: (0.5, 0.16666666666666666), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.797752808988764, 0.13571850975754), 1: (0.7872340425531915, 0.12702634245187433), 2: (0.8, 0.6466666666666667), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8024691358024689, 0.19474313022700127), 1: (0.7435897435897436, 0.15694953194953198), 2: (0.7333333333333333, 0.20252525252525252), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.46987951807228917, 0.09604130808950086), 1: (0.4943820224719101, 0.17354200107009102), 2: (0.8333333333333334, 0.19444444444444445), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.35365853658536583, 0.09854976928147662), 1: (0.4642857142857143, 0.08599337170765742), 2: (0.26666666666666666, 0.22804359383306752), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4250000000000001, 0.10297619047619047), 1: (0.4819277108433735, 0.1134779802439572), 2: (0.6, 0.3985714285714286), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.48936170212765956, 0.11198208286674129), 1: (0.45918367346938777, 0.10537022501308217), 2: (0.47058823529411764, 0.033155080213903745), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4823529411764706, 0.12764705882352936), 1: (0.5058823529411766, 0.12212885154061623), 2: (0.4, 0.2256980056980057), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5714285714285714, 0.0), 1: (0.47058823529411764, 0.058823529411764705), 2: (0.2, 0.2), 3: (1.0, 1.0), 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.6, 0.25), 2: (0.6923076923076923, 0.07692307692307693), 3: (1.0, 1.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.7083333333333334, 0.16666666666666666), 2: (0.38461538461538464, 0.07692307692307693), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.375, 0.0), 1: (0.5217391304347826, 0.17391304347826086), 2: (0.6923076923076923, 0.15384615384615385), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.625, 0.0), 1: (0.7727272727272727, 0.13636363636363635), 2: (0.6666666666666666, 0.0), 3: (1.0, 1.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6923076923076923, 0.13186813186813187), 1: (0.6896551724137929, 0.1724137931034483), 2: (0.35714285714285715, 0.14285714285714285), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8, 0.06666666666666667), 1: (0.8148148148148148, 0.1111111111111111), 2: (0.7333333333333333, 0.13333333333333333), 3: (0.5, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.18181818181818182), 1: (0.7142857142857143, 0.09523809523809523), 2: (0.7272727272727273, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5714285714285714, 0.2857142857142857), 1: (0.45, 0.2), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16666666666666666, 0.3333333333333333), 1: (0.42857142857142855, 0.2110389610389611), 2: (0.5454545454545454, 0.0), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2222222222222222, 0.1111111111111111), 1: (0.43478260869565216, 0.21739130434782608), 2: (0.7, 0.1), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.14285714285714285, 0.0), 1: (0.38461538461538464, 0.07692307692307693), 2: (0.36363636363636365, 0.2727272727272727), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.16666666666666666), 1: (0.5, 0.0823529411764706), 2: (0.3076923076923077, 0.07692307692307693), 3: (0.0, 0.0), 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.25, 0.0), 2: (0.3333333333333333, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.3333333333333333, 0.0), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 1.0), 1: (0.0, 0.0), 2: (1.0, 0.0), 3: (0.6666666666666666, 0.6666666666666666), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 1.0), 1: None, 2: (0.5, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: (0.8, 0.0), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 1.0), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.75, 0.25), 2: (0.3333333333333333, 0.3333333333333333), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.16666666666666666, 0.16666666666666666), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.0), 1: (0.25, 0.25), 2: (0.4, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.25, 0.0), 2: (0.3333333333333333, 0.3333333333333333), 3: (1.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.25, 0.0), 2: (0.5, 0.25), 3: None, 4: None}
player hand value: 20
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5184426229508189, 0.045081967213114756), 1: (0.5000000000000001, 0.2944727660534947), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7867203219315896, 0.058350100603621745), 1: (0.7246376811594203, 0.5127917388711748), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7447698744769872, 0.06066945606694561), 1: (0.7567567567567568, 0.5549023944232132), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7835497835497837, 0.0541125541125541), 1: (0.8, 0.5922963140394927), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7829457364341083, 0.09689922480620156), 1: (0.7500000000000001, 0.6084696961654891), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7785087719298246, 0.07894736842105267), 1: (0.855072463768116, 0.632457598067964), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8224101479915433, 0.06342494714587736), 1: (0.9047619047619048, 0.5918703201321374), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.87, 0.07200000000000009), 1: (0.8, 0.5702396249913996), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.790224032586558, 0.06517311608961299), 1: (0.8, 0.4969518809022332), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5995575221238946, 0.0641592920353982), 1: (0.6363636363636364, 0.4223573758060763), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.543181818181818, 0.10227272727272728), 1: (0.5606060606060606, 0.4200904349110166), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5154394299287404, 0.06888361045130634), 1: (0.6333333333333333, 0.4205722409245637), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5568445475638043, 0.0788863109048724), 1: (0.47368421052631576, 0.3772982144197636), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5045871559633031, 0.048929663608562705), 1: (0.5, 0.15396588042554105), 2: (1.0, 0.2857142857142857), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7653846153846153, 0.08076923076923076), 1: (0.7565217391304347, 0.24558228735705556), 2: (0.7692307692307693, 0.5716227092745311), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7642585551330798, 0.07984790874524718), 1: (0.7946428571428571, 0.3085597297611048), 2: (0.5, 0.5150620077090665), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8051470588235294, 0.07352941176470588), 1: (0.7978723404255319, 0.2586341941538615), 2: (0.8, 0.7458333333333333), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7727272727272725, 0.05303030303030303), 1: (0.7959183673469388, 0.27064388394333116), 2: (0.7142857142857143, 0.5526077097505668), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7862595419847326, 0.10305343511450382), 1: (0.8461538461538463, 0.2865900503777248), 2: (1.0, 0.7173971861471862), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8359374999999999, 0.09375000000000004), 1: (0.8037383177570093, 0.29778447564350374), 2: (0.6, 0.647008547008547), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8706293706293705, 0.06293706293706296), 1: (0.8951612903225806, 0.25077932207850595), 2: (1.0, 0.5324695366362033), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7692307692307693, 0.09890109890109891), 1: (0.855072463768116, 0.3475894325489754), 2: (0.8, 0.7187394957983193), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5392491467576791, 0.0716723549488055), 1: (0.49473684210526314, 0.19185524511681426), 2: (0.5, 0.4969038138894598), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5283018867924532, 0.07924528301886792), 1: (0.610619469026549, 0.24758309902027878), 2: (0.75, 0.5733630952380953), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5429553264604821, 0.06529209621993125), 1: (0.5744680851063829, 0.2602378935707468), 2: (0.625, 0.4719542712189771), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5098814229249017, 0.09090909090909097), 1: (0.5154639175257731, 0.20557747563112555), 2: (1.0, 0.36684565434565436), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.49999999999999994, 0.06249999999999999), 1: (0.4520547945205479, 0.1134367136160695), 2: (0.42857142857142855, 0.08571428571428573), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7857142857142854, 0.0476190476190476), 1: (0.7899999999999998, 0.07004761904761905), 2: (0.8181818181818182, 0.17224880382775115), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.775, 0.075), 1: (0.8061224489795918, 0.08331665999733225), 2: (0.5882352941176471, 0.0261437908496732), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.77, 0.09), 1: (0.7619047619047619, 0.06573498964803312), 2: (0.875, 0.3), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6956521739130432, 0.06521739130434782), 1: (0.7766990291262136, 0.13196822594880847), 2: (0.625, 0.28179824561403505), 3: (1.0, 1.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8461538461538461, 0.06730769230769232), 1: (0.8181818181818182, 0.14273958799820877), 2: (0.9090909090909091, 0.26666666666666666), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8952380952380953, 0.0761904761904762), 1: (0.8865979381443299, 0.07949125390796578), 2: (0.7692307692307693, 0.3076923076923077), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.925531914893617, 0.0851063829787234), 1: (0.8118811881188119, 0.11969361682712044), 2: (0.8333333333333334, 0.21759259259259256), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8415841584158416, 0.11881188118811879), 1: (0.8256880733944955, 0.06948861536017492), 2: (1.0, 0.14545454545454542), 3: (1.0, 1.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4761904761904763, 0.023809523809523808), 1: (0.5225225225225224, 0.08501237724210696), 2: (0.6428571428571429, 0.1043956043956044), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6516853932584268, 0.07865168539325844), 1: (0.5943396226415091, 0.06855065139263249), 2: (0.6875, 0.0874404761904762), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5809523809523807, 0.05714285714285714), 1: (0.5531914893617019, 0.05064856289660318), 2: (0.6923076923076923, 0.3589743589743589), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5378151260504204, 0.09243697478991594), 1: (0.5526315789473685, 0.10831339712918661), 2: (0.6, 0.23904761904761904), 3: (1.0, 1.0), 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6, 0.06666666666666667), 1: (0.5161290322580645, 0.0), 2: (1.0, 0.5), 3: (1.0, 1.0), 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5714285714285714, 0.14285714285714285), 1: (0.5714285714285714, 0.09523809523809523), 2: (0.9473684210526315, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8181818181818182, 0.09090909090909091), 1: (0.7352941176470589, 0.0), 2: (0.6666666666666666, 0.06349206349206349), 3: (1.0, 1.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.9, 0.0), 1: (0.84, 0.08), 2: (0.9, 0.1), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.85, 0.15), 1: (0.84, 0.08), 2: (0.8421052631578947, 0.0), 3: (1.0, 0.5), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6923076923076923, 0.15384615384615385), 1: (0.8333333333333334, 0.03333333333333333), 2: (0.7142857142857143, 0.14285714285714285), 3: (1.0, 0.0), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7777777777777778, 0.05555555555555555), 1: (0.868421052631579, 0.15789473684210525), 2: (0.8, 0.06666666666666667), 3: (1.0, 1.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8888888888888888, 0.0), 1: (0.967741935483871, 0.0967741935483871), 2: (0.9444444444444444, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8461538461538461, 0.15384615384615385), 1: (0.8285714285714286, 0.11428571428571428), 2: (0.9333333333333333, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.36363636363636365, 0.0), 1: (0.5135135135135135, 0.13513513513513514), 2: (0.23076923076923078, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.07142857142857142), 1: (0.5238095238095238, 0.023809523809523808), 2: (0.7142857142857143, 0.14285714285714285), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5384615384615384, 0.07692307692307693), 1: (0.5526315789473685, 0.10526315789473684), 2: (0.5333333333333333, 0.13333333333333333), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7368421052631579, 0.05263157894736842), 1: (0.55, 0.1), 2: (0.6428571428571429, 0.0), 3: (1.0, 0.0), 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6666666666666666, 0.3333333333333333), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.8, 0.4), 2: (1.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.5), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.7142857142857143, 0.14285714285714285), 2: (1.0, 0.0), 3: (1.0, 1.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.75, 0.0), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.7142857142857143, 0.2857142857142857), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6666666666666666, 0.3333333333333333), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.25), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (1.0, 0.0), 2: (1.0, 0.25), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.125), 2: (0.7272727272727273, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.8, 0.2), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: None, 3: (1.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.4, 0.0), 2: (0.6, 0.0), 3: None, 4: None}
---
### Decision Matrix (original):
`{12: {2: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: True, 2: True, 3: True, 4: True}, '3': {0: True, 1: True, 2: True, 3: True, 4: True}, '4': {0: False, 1: True, 2: True, 3: True, 4: True}, '5': {0: False, 1: True, 2: True, 3: True, 4: True}, '6': {0: False, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}, 3: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: False, 2: True, 3: True, 4: True}, '3': {0: True, 1: False, 2: False, 3: True, 4: True}, '4': {0: True, 1: True, 2: True, 3: True, 4: True}, '5': {0: False, 1: False, 2: True, 3: True, 4: True}, '6': {0: True, 1: True, 2: False, 3: True, 4: True}, '7': {0: True, 1: True, 2: False, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: False, 1: True, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: False, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}, 4: {'A': {0: True, 1: True, 2: False, 3: True, 4: True}, '2': {0: True, 1: False, 2: True, 3: True, 4: True}, '3': {0: False, 1: False, 2: False, 3: True, 4: True}, '4': {0: False, 1: True, 2: True, 3: True, 4: True}, '5': {0: True, 1: False, 2: True, 3: True, 4: True}, '6': {0: True, 1: False, 2: False, 3: True, 4: True}, '7': {0: True, 1: True, 2: False, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: False, 1: False, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: False, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: False, 3: True, 4: True}}, 5: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: True, 2: True, 3: True, 4: True}, '3': {0: True, 1: True, 2: True, 3: True, 4: True}, '4': {0: True, 1: True, 2: False, 3: True, 4: True}, '5': {0: True, 1: True, 2: True, 3: True, 4: True}, '6': {0: True, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: False, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: False, 3: True, 4: True}}, 6: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: True, 2: True, 3: True, 4: True}, '3': {0: True, 1: True, 2: True, 3: True, 4: True}, '4': {0: True, 1: True, 2: True, 3: True, 4: True}, '5': {0: True, 1: True, 2: True, 3: True, 4: True}, '6': {0: True, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}}, 13: {2: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: False, 1: True, 2: True, 3: True, 4: True}, '3': {0: False, 1: True, 2: True, 3: True, 4: True}, '4': {0: False, 1: True, 2: True, 3: True, 4: True}, '5': {0: False, 1: True, 2: True, 3: True, 4: True}, '6': {0: False, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}, 3: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: False, 1: False, 2: True, 3: True, 4: True}, '3': {0: False, 1: True, 2: True, 3: True, 4: True}, '4': {0: False, 1: False, 2: True, 3: True, 4: True}, '5': {0: False, 1: False, 2: True, 3: False, 4: True}, '6': {0: False, 1: False, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: False, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: False, 2: True, 3: True, 4: True}, 'Q': {0: False, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}, 4: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: False, 2: False, 3: True, 4: True}, '3': {0: True, 1: False, 2: False, 3: True, 4: True}, '4': {0: True, 1: False, 2: False, 3: True, 4: True}, '5': {0: True, 1: False, 2: False, 3: True, 4: True}, '6': {0: True, 1: True, 2: False, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: False, 2: False, 3: True, 4: True}, '9': {0: False, 1: False, 2: False, 3: True, 4: True}, 'T': {0: False, 1: True, 2: False, 3: True, 4: True}, 'J': {0: False, 1: False, 2: False, 3: True, 4: True}, 'Q': {0: False, 1: True, 2: False, 3: True, 4: True}, 'K': {0: True, 1: False, 2: True, 3: True, 4: True}}, 5: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: True, 2: False, 3: True, 4: True}, '3': {0: True, 1: True, 2: False, 3: True, 4: True}, '4': {0: True, 1: True, 2: False, 3: True, 4: True}, '5': {0: True, 1: True, 2: False, 3: True, 4: True}, '6': {0: True, 1: False, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: False, 2: False, 3: True, 4: True}, '9': {0: True, 1: False, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: False, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: False, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}, 6: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: True, 2: True, 3: True, 4: True}, '3': {0: True, 1: True, 2: True, 3: True, 4: True}, '4': {0: True, 1: True, 2: True, 3: True, 4: True}, '5': {0: True, 1: True, 2: True, 3: True, 4: True}, '6': {0: True, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}}, 14: {2: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: False, 1: True, 2: True, 3: True, 4: True}, '3': {0: False, 1: True, 2: True, 3: True, 4: True}, '4': {0: False, 1: True, 2: True, 3: True, 4: True}, '5': {0: False, 1: True, 2: True, 3: True, 4: True}, '6': {0: False, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: True, 3: True, 4: True}, 'K': {0: False, 1: True, 2: True, 3: True, 4: True}}, 3: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: False, 1: False, 2: True, 3: True, 4: True}, '3': {0: False, 1: False, 2: True, 3: True, 4: True}, '4': {0: False, 1: False, 2: True, 3: True, 4: True}, '5': {0: False, 1: False, 2: True, 3: True, 4: True}, '6': {0: False, 1: False, 2: True, 3: True, 4: True}, '7': {0: False, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: False, 1: False, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: False, 3: True, 4: True}, 'Q': {0: False, 1: False, 2: True, 3: True, 4: True}, 'K': {0: False, 1: True, 2: True, 3: True, 4: True}}, 4: {'A': {0: True, 1: False, 2: False, 3: True, 4: True}, '2': {0: False, 1: True, 2: False, 3: True, 4: True}, '3': {0: False, 1: False, 2: False, 3: True, 4: True}, '4': {0: False, 1: False, 2: False, 3: True, 4: True}, '5': {0: False, 1: True, 2: False, 3: True, 4: True}, '6': {0: False, 1: False, 2: False, 3: True, 4: True}, '7': {0: True, 1: True, 2: False, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: False, 1: False, 2: True, 3: True, 4: True}, 'T': {0: False, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: False, 3: True, 4: True}, 'K': {0: False, 1: True, 2: True, 3: True, 4: True}}, 5: {'A': {0: True, 1: False, 2: True, 3: True, 4: True}, '2': {0: True, 1: False, 2: False, 3: True, 4: True}, '3': {0: True, 1: True, 2: True, 3: True, 4: True}, '4': {0: True, 1: True, 2: False, 3: True, 4: True}, '5': {0: True, 1: True, 2: True, 3: True, 4: True}, '6': {0: True, 1: False, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: False, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: False, 3: True, 4: True}, 'T': {0: True, 1: False, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: False, 3: True, 4: True}, 'Q': {0: True, 1: False, 2: True, 3: True, 4: True}, 'K': {0: True, 1: False, 2: True, 3: True, 4: True}}, 6: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: True, 2: True, 3: True, 4: True}, '3': {0: True, 1: True, 2: True, 3: True, 4: True}, '4': {0: True, 1: True, 2: True, 3: True, 4: True}, '5': {0: True, 1: True, 2: True, 3: True, 4: True}, '6': {0: True, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}}, 15: {2: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: False, 1: True, 2: True, 3: True, 4: True}, '3': {0: False, 1: True, 2: True, 3: True, 4: True}, '4': {0: False, 1: True, 2: True, 3: True, 4: True}, '5': {0: False, 1: True, 2: True, 3: True, 4: True}, '6': {0: False, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: False, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: False, 1: True, 2: True, 3: True, 4: True}, 'K': {0: False, 1: True, 2: True, 3: True, 4: True}}, 3: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: False, 1: False, 2: True, 3: True, 4: True}, '3': {0: False, 1: False, 2: True, 3: True, 4: True}, '4': {0: False, 1: False, 2: True, 3: True, 4: True}, '5': {0: False, 1: False, 2: False, 3: True, 4: True}, '6': {0: False, 1: False, 2: False, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: False, 3: True, 4: True}, '9': {0: True, 1: False, 2: True, 3: True, 4: True}, 'T': {0: False, 1: False, 2: True, 3: True, 4: True}, 'J': {0: False, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: False, 1: True, 2: True, 3: True, 4: True}, 'K': {0: False, 1: True, 2: True, 3: True, 4: True}}, 4: {'A': {0: True, 1: False, 2: False, 3: True, 4: True}, '2': {0: False, 1: True, 2: False, 3: True, 4: True}, '3': {0: False, 1: False, 2: False, 3: True, 4: True}, '4': {0: False, 1: False, 2: False, 3: True, 4: True}, '5': {0: False, 1: False, 2: False, 3: True, 4: True}, '6': {0: False, 1: False, 2: False, 3: True, 4: True}, '7': {0: False, 1: True, 2: False, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: False, 1: True, 2: True, 3: True, 4: True}, 'T': {0: False, 1: False, 2: False, 3: True, 4: True}, 'J': {0: True, 1: True, 2: False, 3: True, 4: True}, 'Q': {0: True, 1: False, 2: False, 3: True, 4: True}, 'K': {0: False, 1: False, 2: False, 3: True, 4: True}}, 5: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: False, 2: False, 3: True, 4: True}, '3': {0: True, 1: False, 2: False, 3: True, 4: True}, '4': {0: True, 1: True, 2: True, 3: True, 4: True}, '5': {0: True, 1: True, 2: False, 3: True, 4: True}, '6': {0: True, 1: True, 2: False, 3: True, 4: True}, '7': {0: True, 1: False, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: False, 3: True, 4: True}, '9': {0: True, 1: True, 2: False, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: False, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: False, 2: False, 3: True, 4: True}}, 6: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: True, 2: True, 3: True, 4: True}, '3': {0: True, 1: True, 2: True, 3: True, 4: True}, '4': {0: True, 1: True, 2: True, 3: True, 4: True}, '5': {0: True, 1: True, 2: False, 3: True, 4: True}, '6': {0: True, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: False, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}}, 16: {2: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: False, 1: True, 2: True, 3: True, 4: True}, '3': {0: False, 1: True, 2: True, 3: True, 4: True}, '4': {0: False, 1: True, 2: True, 3: True, 4: True}, '5': {0: False, 1: True, 2: True, 3: True, 4: True}, '6': {0: False, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: False, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: False, 1: True, 2: True, 3: True, 4: True}, 'J': {0: False, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: False, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}, 3: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: False, 1: False, 2: True, 3: True, 4: True}, '3': {0: False, 1: False, 2: False, 3: True, 4: True}, '4': {0: False, 1: False, 2: False, 3: True, 4: True}, '5': {0: False, 1: False, 2: False, 3: True, 4: True}, '6': {0: False, 1: False, 2: False, 3: True, 4: True}, '7': {0: False, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: False, 1: True, 2: True, 3: True, 4: True}, 'T': {0: False, 1: False, 2: True, 3: True, 4: True}, 'J': {0: False, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: False, 1: True, 2: True, 3: True, 4: True}, 'K': {0: False, 1: True, 2: True, 3: True, 4: True}}, 4: {'A': {0: False, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: False, 2: False, 3: True, 4: True}, '3': {0: False, 1: False, 2: False, 3: True, 4: True}, '4': {0: False, 1: False, 2: False, 3: True, 4: True}, '5': {0: False, 1: False, 2: True, 3: True, 4: True}, '6': {0: True, 1: False, 2: False, 3: True, 4: True}, '7': {0: False, 1: False, 2: False, 3: True, 4: True}, '8': {0: True, 1: True, 2: False, 3: True, 4: True}, '9': {0: False, 1: False, 2: False, 3: True, 4: True}, 'T': {0: False, 1: False, 2: True, 3: True, 4: True}, 'J': {0: False, 1: True, 2: False, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: False, 3: True, 4: True}, 'K': {0: True, 1: False, 2: False, 3: True, 4: True}}, 5: {'A': {0: False, 1: False, 2: True, 3: True, 4: True}, '2': {0: True, 1: False, 2: False, 3: True, 4: True}, '3': {0: True, 1: False, 2: False, 3: True, 4: True}, '4': {0: True, 1: False, 2: False, 3: True, 4: True}, '5': {0: True, 1: False, 2: False, 3: True, 4: True}, '6': {0: True, 1: False, 2: False, 3: True, 4: True}, '7': {0: True, 1: True, 2: False, 3: True, 4: True}, '8': {0: True, 1: False, 2: False, 3: True, 4: True}, '9': {0: False, 1: True, 2: False, 3: True, 4: True}, 'T': {0: False, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: False, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}, 6: {'A': {0: True, 1: True, 2: True, 3: True, 4: True}, '2': {0: True, 1: True, 2: True, 3: True, 4: True}, '3': {0: True, 1: True, 2: True, 3: True, 4: True}, '4': {0: True, 1: True, 2: True, 3: True, 4: True}, '5': {0: True, 1: True, 2: True, 3: True, 4: True}, '6': {0: True, 1: True, 2: True, 3: True, 4: True}, '7': {0: True, 1: True, 2: True, 3: True, 4: True}, '8': {0: True, 1: True, 2: True, 3: True, 4: True}, '9': {0: True, 1: True, 2: True, 3: True, 4: True}, 'T': {0: True, 1: True, 2: True, 3: True, 4: True}, 'J': {0: True, 1: True, 2: True, 3: True, 4: True}, 'Q': {0: True, 1: True, 2: True, 3: True, 4: True}, 'K': {0: True, 1: True, 2: True, 3: True, 4: True}}}, 17: {2: {'A': {0: True, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: True, 2: False, 3: False, 4: False}, '3': {0: False, 1: True, 2: False, 3: False, 4: False}, '4': {0: False, 1: True, 2: False, 3: False, 4: False}, '5': {0: False, 1: True, 2: False, 3: False, 4: False}, '6': {0: False, 1: True, 2: False, 3: False, 4: False}, '7': {0: False, 1: True, 2: False, 3: False, 4: False}, '8': {0: False, 1: True, 2: False, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: True, 2: False, 3: False, 4: False}, 'J': {0: False, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: True, 2: False, 3: False, 4: False}, 'K': {0: False, 1: True, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: True, 3: False, 4: False}, '3': {0: False, 1: False, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: True, 2: True, 3: False, 4: False}, '8': {0: False, 1: True, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: True, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: False, 4: False}, 'J': {0: False, 1: True, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: True, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: True, 1: True, 2: True, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: True, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: True, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: True, 3: False, 4: False}, 'K': {0: False, 1: True, 2: True, 3: False, 4: False}}, 5: {'A': {0: False, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: True, 4: False}, '7': {0: False, 1: False, 2: True, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: True, 3: False, 4: False}}}, 18: {2: {'A': {0: False, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: True, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: True, 2: False, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: True, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: True, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: True, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: True, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: True, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 19: {2: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: True, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: True, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: True, 3: False, 4: False}, '6': {0: False, 1: False, 2: True, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: True, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 20: {2: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: True, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}}`

### Percentage Matrix (original):
`{12: {2: {'A': {0: (0.13319672131147547, 0.18822229143584804), 1: None, 2: (0.07692307692307693, 0.4064560439560439), 3: None, 4: None}, '2': {0: (0.3482352941176472, 0.3837334660767491), 1: None, 2: (0.4, 0.516185477998875), 3: None, 4: None}, '3': {0: (0.3312368972746332, 0.3483988261179578), 1: None, 2: (0.45, 0.5143935910644835), 3: None, 4: None}, '4': {0: (0.3890160183066363, 0.38835995342150886), 1: None, 2: (0.2592592592592593, 0.6081935300235954), 3: None, 4: None}, '5': {0: (0.41295546558704455, 0.3811616321252021), 1: None, 2: (0.34782608695652173, 0.4922077922077924), 3: None, 4: None}, '6': {0: (0.4354066985645933, 0.40104002693604285), 1: None, 2: (0.5416666666666666, 0.6317114598364598), 3: None, 4: None}, '7': {0: (0.2761506276150629, 0.3619787060956271), 1: None, 2: (0.21739130434782608, 0.6364747686675852), 3: None, 4: None}, '8': {0: (0.2652173913043476, 0.31196001910311305), 1: None, 2: (0.23529411764705882, 0.4557350742355994), 3: None, 4: None}, '9': {0: (0.24168514412416892, 0.2843532757096903), 1: None, 2: (0.36, 0.5599135792144839), 3: None, 4: None}, 'T': {0: (0.20682730923694773, 0.26810907173040677), 1: None, 2: (0.0967741935483871, 0.3645519391310865), 3: None, 4: None}, 'J': {0: (0.20292887029288706, 0.25514321643898635), 1: None, 2: (0.24, 0.509835503013733), 3: None, 4: None}, 'Q': {0: (0.19915254237288132, 0.26422457528308424), 1: None, 2: (0.3333333333333333, 0.48983836969131084), 3: None, 4: None}, 'K': {0: (0.2106430155210643, 0.2367863279487198), 1: None, 2: (0.24, 0.3953128432414146), 3: None, 4: None}}, 3: {'A': {0: (0.072463768115942, 0.18706496258264318), 1: (0.11904761904761904, 0.21729301201523235), 2: (0.0, 0.21860119047619048), 3: None, 4: None}, '2': {0: (0.4074074074074074, 0.4829553545315817), 1: (0.38333333333333336, 0.3609219441760427), 2: (0.36363636363636365, 0.42994732540187086), 3: None, 4: None}, '3': {0: (0.3888888888888889, 0.3925756469929404), 1: (0.46, 0.35400337490505324), 2: (0.41379310344827586, 0.3594892598949394), 3: None, 4: None}, '4': {0: (0.32142857142857145, 0.4236509603841537), 1: (0.3333333333333333, 0.387707267344052), 2: (0.38461538461538464, 0.4231716404510522), 3: None, 4: None}, '5': {0: (0.49999999999999994, 0.4482547138210667), 1: (0.453125, 0.43282113263651134), 2: (0.3181818181818182, 0.351010101010101), 3: None, 4: None}, '6': {0: (0.3787878787878788, 0.38629815438531645), 1: (0.4305555555555556, 0.4757822941124684), 2: (0.36666666666666664, 0.36414141414141415), 3: None, 4: None}, '7': {0: (0.22222222222222218, 0.3568857272459449), 1: (0.22641509433962265, 0.310214761730689), 2: (0.4782608695652174, 0.30280299410734196), 3: None, 4: None}, '8': {0: (0.2545454545454545, 0.358087436817094), 1: (0.25862068965517243, 0.3565200599989269), 2: (0.20833333333333334, 0.3975698491323491), 3: None, 4: None}, '9': {0: (0.2923076923076924, 0.2839241592329802), 1: (0.26666666666666666, 0.30105554015548974), 2: (0.23076923076923078, 0.31899687793352965), 3: None, 4: None}, 'T': {0: (0.20289855072463772, 0.20900077241599982), 1: (0.10909090909090909, 0.26230775688206015), 2: (0.18181818181818182, 0.30951858783524727), 3: None, 4: None}, 'J': {0: (0.1594202898550725, 0.353910932146837), 1: (0.17910447761194032, 0.285255585084913), 2: (0.2631578947368421, 0.4009711779448621), 3: None, 4: None}, 'Q': {0: (0.18309859154929578, 0.2147982592838829), 1: (0.21153846153846154, 0.3033376719250799), 2: (0.3, 0.2922181086886969), 3: None, 4: None}, 'K': {0: (0.19696969696969696, 0.3080598148096547), 1: (0.1499999999999999, 0.24278357062461936), 2: (0.15625, 0.2732288544788545), 3: None, 4: None}}, 4: {'A': {0: (0.0, 0.0), 1: (0.0, 0.27649769585253453), 2: (0.16666666666666666, 0.16666666666666666), 3: None, 4: None}, '2': {0: (1.0, 0.5714285714285714), 1: (0.23076923076923078, 0.1804029304029304), 2: (0.4, 0.45614035087719296), 3: None, 4: None}, '3': {0: (0.0, 0.0), 1: (0.36363636363636365, 0.24830235124352773), 2: (0.5, 0.29166666666666663), 3: (1.0, 0.0), 4: None}, '4': {0: (0.6666666666666666, 0.2222222222222222), 1: (0.45454545454545453, 0.5443139469226425), 2: (0.2727272727272727, 0.43496503496503497), 3: None, 4: None}, '5': {0: (0.0, 0.0), 1: (0.38461538461538464, 0.3143123543123543), 2: (0.5, 0.3333333333333333), 3: (1.0, 0.0), 4: None}, '6': {0: None, 1: (0.5333333333333333, 0.4945484400656814), 2: (0.42857142857142855, 0.2285714285714286), 3: None, 4: None}, '7': {0: (0.25, 0.4444444444444444), 1: (0.19047619047619047, 0.4140559732664995), 2: (0.75, 0.41666666666666663), 3: (0.0, 0.0), 4: None}, '8': {0: (0.18181818181818182, 0.5757575757575758), 1: (0.23076923076923078, 0.35), 2: (0.16666666666666666, 0.6443602693602694), 3: None, 4: None}, '9': {0: (0.0, 0.08333333333333333), 1: (0.18181818181818182, 0.20979020979020976), 2: (0.3333333333333333, 0.43333333333333335), 3: (0.0, 0.0), 4: None}, 'T': {0: (0.4, 0.07272727272727272), 1: (0.3157894736842105, 0.1710359463842436), 2: (0.0, 0.2547846889952153), 3: None, 4: None}, 'J': {0: (0.1111111111111111, 0.2469135802469136), 1: (0.09090909090909091, 0.24139724460870707), 2: (0.14285714285714285, 0.4277551020408163), 3: None, 4: None}, 'Q': {0: (0.0, 0.0), 1: (0.45454545454545453, 0.4519936204146731), 2: (0.0, 0.15861471861471862), 3: None, 4: None}, 'K': {0: (0.0, 0.21710526315789475), 1: (0.2222222222222222, 0.25771604938271603), 2: (0.2727272727272727, 0.1811688311688312), 3: None, 4: None}}, 5: {'A': {0: None, 1: (0.0, 0.25), 2: (0.0, 0.3333333333333333), 3: None, 4: None}, '2': {0: None, 1: (1.0, 0.0), 2: (1.0, 1.0), 3: None, 4: None}, '3': {0: None, 1: None, 2: (0.0, 0.4444444444444444), 3: (0.0, 0.8333333333333333), 4: None}, '4': {0: None, 1: (1.0, 0.0), 2: (1.0, 0.6666666666666666), 3: (0.0, 0.0), 4: None}, '5': {0: None, 1: None, 2: (1.0, 0.6666666666666666), 3: (1.0, 1.0), 4: None}, '6': {0: None, 1: None, 2: (1.0, 0.5), 3: None, 4: None}, '7': {0: None, 1: None, 2: (0.0, 0.5), 3: (0.0, 1.0), 4: None}, '8': {0: None, 1: (0.5, 1.0), 2: (0.3333333333333333, 0.0), 3: None, 4: None}, '9': {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}, 'T': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, 'J': {0: None, 1: None, 2: (0.0, 0.5), 3: (0.0, 1.0), 4: None}, 'Q': {0: None, 1: (0.16666666666666666, 0.20833333333333334), 2: (0.0, 0.0), 3: None, 4: None}, 'K': {0: None, 1: (0.5, 0.2), 2: (0.0, 0.0), 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: (1.0, 1.0), 4: None}, '8': {0: None, 1: (1.0, 1.0), 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}}}, 13: {2: {'A': {0: (0.13677130044843056, 0.17778238136610902), 1: (0.05128205128205128, 0.25656576662927966), 2: None, 3: None, 4: None}, '2': {0: (0.34894613583138134, 0.33739975934750355), 1: (0.3333333333333334, 0.4310132415448555), 2: None, 3: None, 4: None}, '3': {0: (0.35733333333333334, 0.3173419727052053), 1: (0.3888888888888889, 0.45703528384973385), 2: None, 3: None, 4: None}, '4': {0: (0.41894736842105246, 0.3693968392902241), 1: (0.38461538461538464, 0.5089356002050505), 2: None, 3: None, 4: None}, '5': {0: (0.4158878504672896, 0.3347468184351956), 1: (0.3698630136986302, 0.5058207045376731), 2: None, 3: None, 4: None}, '6': {0: (0.4247191011235955, 0.35929411723481747), 1: (0.3448275862068966, 0.5223938807451941), 2: None, 3: None, 4: None}, '7': {0: (0.27713625866050823, 0.3447052392360102), 1: (0.28125, 0.5488415393334367), 2: None, 3: None, 4: None}, '8': {0: (0.2549019607843138, 0.31467266290930296), 1: (0.2931034482758622, 0.5126527175154746), 2: None, 3: None, 4: None}, '9': {0: (0.23221757322175743, 0.2600839156247956), 1: (0.18181818181818182, 0.40048089104802254), 2: None, 3: None, 4: None}, 'T': {0: (0.2191142191142192, 0.22176363964347612), 1: (0.18032786885245902, 0.3790497065644507), 2: None, 3: None, 4: None}, 'J': {0: (0.2009237875288684, 0.23192446853397952), 1: (0.2424242424242425, 0.33097791228344525), 2: None, 3: None, 4: None}, 'Q': {0: (0.21158129175946544, 0.23686894332385827), 1: (0.1694915254237288, 0.3793053052142874), 2: None, 3: None, 4: None}, 'K': {0: (0.21700223713646535, 0.22295407489947308), 1: (0.1515151515151515, 0.38255022839126357), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.12643678160919544, 0.20847398193695976), 1: (0.11538461538461539, 0.12213205539830449), 2: None, 3: None, 4: None}, '2': {0: (0.3875, 0.29175273894387244), 1: (0.36448598130841126, 0.36264351211493856), 2: None, 3: (1.0, 0.0), 4: None}, '3': {0: (0.4375, 0.2394683104137406), 1: (0.36111111111111116, 0.38243761473923904), 2: None, 3: None, 4: None}, '4': {0: (0.5, 0.35323664000134586), 1: (0.423728813559322, 0.31618600723529383), 2: None, 3: (0.5, 0.0), 4: None}, '5': {0: (0.45121951219512196, 0.31274897448409245), 1: (0.4672897196261682, 0.3636000921894176), 2: None, 3: (0.25, 0.25), 4: None}, '6': {0: (0.41333333333333333, 0.26405134394430907), 1: (0.4019607843137255, 0.377179630305386), 2: None, 3: None, 4: None}, '7': {0: (0.22972972972972974, 0.2657719208710158), 1: (0.21951219512195122, 0.3871853618176824), 2: None, 3: (0.0, 0.0), 4: None}, '8': {0: (0.15942028985507245, 0.2800830629835613), 1: (0.21551724137931033, 0.3645668288548376), 2: None, 3: None, 4: None}, '9': {0: (0.2717391304347827, 0.29972404652130363), 1: (0.14678899082568808, 0.27289744813869754), 2: None, 3: (0.5, 1.0), 4: None}, 'T': {0: (0.20253164556962025, 0.20111793996860636), 1: (0.2459016393442623, 0.2671259633727278), 2: None, 3: (1.0, 1.0), 4: None}, 'J': {0: (0.1111111111111111, 0.31085854572606675), 1: (0.2636363636363638, 0.2538612819119989), 2: None, 3: None, 4: None}, 'Q': {0: (0.24468085106382984, 0.19499128320814732), 1: (0.19379844961240314, 0.28406289997656065), 2: None, 3: None, 4: None}, 'K': {0: (0.17948717948717952, 0.2539832004407869), 1: (0.16216216216216217, 0.2834538669278945), 2: None, 3: (0.5, 0.5), 4: None}}, 4: {'A': {0: (0.0, 0.14545454545454548), 1: (0.05555555555555555, 0.2838882864973946), 2: (0.0, 0.3), 3: (0.0, 0.0), 4: None}, '2': {0: (0.0, 0.36734693877551017), 1: (0.4444444444444444, 0.282010582010582), 2: (0.3333333333333333, 0.19999999999999998), 3: None, 4: None}, '3': {0: (0.5, 0.0), 1: (0.5384615384615384, 0.4079939668174963), 2: (0.5, 0.16666666666666666), 3: None, 4: None}, '4': {0: (0.3333333333333333, 0.6666666666666666), 1: (0.4444444444444444, 0.4444444444444444), 2: (0.6666666666666666, 0.3333333333333333), 3: (0.0, 1.0), 4: None}, '5': {0: (0.25, 0.36875), 1: (0.3684210526315789, 0.2391387559808612), 2: (0.5714285714285714, 0.3333333333333333), 3: (1.0, 0.0), 4: None}, '6': {0: (0.5, 0.6923076923076923), 1: (0.42857142857142855, 0.4439909297052155), 2: (0.4444444444444444, 0.20158730158730154), 3: (0.0, 0.5), 4: None}, '7': {0: (0.2, 0.45777777777777773), 1: (0.2916666666666667, 0.33575837742504405), 2: (0.3333333333333333, 0.3888888888888889), 3: (0.0, 0.0), 4: None}, '8': {0: (0.14285714285714285, 0.3321995464852608), 1: (0.45, 0.43710573476702497), 2: (0.14285714285714285, 0.1396103896103896), 3: (0.0, 1.0), 4: None}, '9': {0: (0.3333333333333333, 0.05555555555555555), 1: (0.35714285714285715, 0.2591004233861377), 2: (0.42857142857142855, 0.4), 3: None, 4: None}, 'T': {0: (0.25, 0.045454545454545456), 1: (0.15, 0.17308775783040486), 2: (0.16666666666666666, 0.038461538461538464), 3: (0.0, 0.5), 4: None}, 'J': {0: (0.2857142857142857, 0.15873015873015875), 1: (0.4444444444444444, 0.2639978110992603), 2: (0.5, 0.4365079365079365), 3: (0.0, 0.0), 4: None}, 'Q': {0: (0.45454545454545453, 0.22727272727272727), 1: (0.16, 0.2367213838792786), 2: (0.3333333333333333, 0.1828282828282828), 3: (1.0, 0.0), 4: None}, 'K': {0: (0.0, 0.10796221322537111), 1: (0.23529411764705882, 0.21586452762923347), 2: (0.15384615384615385, 0.22252747252747251), 3: (0.5, 0.5), 4: None}}, 5: {'A': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.3333333333333333), 3: None, 4: None}, '2': {0: None, 1: (0.0, 0.0), 2: (0.25, 0.0), 3: None, 4: None}, '3': {0: None, 1: (0.5, 0.0), 2: (0.3333333333333333, 0.1111111111111111), 3: (1.0, 0.0), 4: None}, '4': {0: None, 1: None, 2: (0.75, 0.25), 3: None, 4: None}, '5': {0: None, 1: (1.0, 0.0), 2: (0.3333333333333333, 0.3333333333333333), 3: None, 4: None}, '6': {0: None, 1: (0.4, 0.4), 2: (1.0, 0.5), 3: None, 4: None}, '7': {0: None, 1: (0.0, 0.5), 2: (1.0, 0.0), 3: (0.5, 1.0), 4: None}, '8': {0: None, 1: (0.3333333333333333, 0.3333333333333333), 2: (0.25, 0.25), 3: (0.0, 0.0), 4: None}, '9': {0: None, 1: (0.6666666666666666, 0.5), 2: (0.0, 0.5), 3: None, 4: None}, 'T': {0: (0.0, 1.0), 1: (0.0, 0.5), 2: (0.0, 0.0), 3: None, 4: None}, 'J': {0: None, 1: None, 2: (0.25, 0.2375), 3: None, 4: None}, 'Q': {0: None, 1: (0.0, 0.0), 2: (0.3333333333333333, 0.13333333333333333), 3: None, 4: None}, 'K': {0: (0.0, 0.0), 1: (0.0, 0.0), 2: (0.3333333333333333, 0.4777777777777778), 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: (1.0, 0.0), 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 14: {2: {'A': {0: (0.11347517730496454, 0.1516710421109428), 1: (0.0851063829787234, 0.24207172171949123), 2: None, 3: None, 4: None}, '2': {0: (0.36299765807962536, 0.32760933216574467), 1: (0.36923076923076925, 0.4880864676469823), 2: None, 3: None, 4: None}, '3': {0: (0.3520782396088017, 0.3100180640886652), 1: (0.3, 0.5327440726859873), 2: None, 3: None, 4: None}, '4': {0: (0.4591194968553459, 0.3045097626237968), 1: (0.373134328358209, 0.52053666501155), 2: None, 3: None, 4: None}, '5': {0: (0.38235294117647045, 0.3213781789033251), 1: (0.4857142857142857, 0.5624026545834019), 2: None, 3: None, 4: None}, '6': {0: (0.4157608695652174, 0.34845380556821665), 1: (0.3783783783783784, 0.5082985711749148), 2: None, 3: None, 4: None}, '7': {0: (0.27272727272727243, 0.3094019437969013), 1: (0.20833333333333334, 0.4657228668063705), 2: None, 3: None, 4: None}, '8': {0: (0.2317073170731706, 0.28140231112089326), 1: (0.32876712328767116, 0.45642480580943257), 2: None, 3: None, 4: None}, '9': {0: (0.2282051282051282, 0.25349982226500445), 1: (0.22535211267605634, 0.4618169235887434), 2: None, 3: None, 4: None}, 'T': {0: (0.20320855614973266, 0.2285545689192187), 1: (0.14084507042253516, 0.356413455177432), 2: None, 3: None, 4: None}, 'J': {0: (0.22332506203473945, 0.24941679148781842), 1: (0.2241379310344828, 0.37032123623184726), 2: None, 3: None, 4: None}, 'Q': {0: (0.20222222222222228, 0.22115929787857508), 1: (0.19672131147540986, 0.3827118111378637), 2: None, 3: None, 4: None}, 'K': {0: (0.24285714285714305, 0.21566306223004653), 1: (0.3, 0.37800549025530256), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.11290322580645167, 0.21808115837071446), 1: (0.08247422680412367, 0.17970668018273842), 2: (0.3333333333333333, 0.3857142857142857), 3: None, 4: None}, '2': {0: (0.3636363636363637, 0.24244679575898737), 1: (0.3629032258064517, 0.2922866564365771), 2: (1.0, 0.6371610845295056), 3: None, 4: None}, '3': {0: (0.485981308411215, 0.2880844418698081), 1: (0.4948453608247423, 0.2963670890449401), 2: (0.2857142857142857, 0.4095238095238095), 3: None, 4: None}, '4': {0: (0.3805309734513274, 0.3340181663207461), 1: (0.45714285714285713, 0.29141199325184364), 2: (0.5, 0.5233134920634921), 3: None, 4: None}, '5': {0: (0.38333333333333325, 0.3223179844909864), 1: (0.4782608695652174, 0.30934624740776795), 2: (0.0, 0.30657596371882084), 3: None, 4: None}, '6': {0: (0.4112903225806452, 0.29929564437647066), 1: (0.3921568627450982, 0.3717812627264049), 2: (0.4, 0.4646464646464647), 3: None, 4: None}, '7': {0: (0.3220338983050847, 0.2410627899519784), 1: (0.2708333333333333, 0.3804176473741383), 2: (0.2, 0.445103785103785), 3: None, 4: None}, '8': {0: (0.20769230769230773, 0.29438644837581945), 1: (0.25225225225225223, 0.3053958337354726), 2: (0.2857142857142857, 0.5373709623709624), 3: None, 4: None}, '9': {0: (0.24193548387096775, 0.22124434897289313), 1: (0.23711340206185572, 0.22644383188991396), 2: (0.0, 0.7696969696969698), 3: None, 4: None}, 'T': {0: (0.20212765957446813, 0.22696928445000342), 1: (0.2032520325203252, 0.2545932381619158), 2: (0.25, 0.33452380952380956), 3: None, 4: None}, 'J': {0: (0.21641791044776118, 0.24644971189059456), 1: (0.21232876712328766, 0.22972319326292603), 2: (0.5, 0.33333333333333337), 3: None, 4: None}, 'Q': {0: (0.26785714285714307, 0.23253893164507472), 1: (0.26595744680851063, 0.2616864296786532), 2: (0.0, 0.5001274542451012), 3: None, 4: None}, 'K': {0: (0.26, 0.23356372472354947), 1: (0.2127659574468085, 0.21789421062679967), 2: (0.125, 0.4230207292707293), 3: None, 4: None}}, 4: {'A': {0: (0.125, 0.21130952380952378), 1: (0.19047619047619047, 0.1088112664420607), 2: (0.0, 0.0), 3: None, 4: None}, '2': {0: (0.75, 0.25), 1: (0.36363636363636365, 0.4670995670995672), 2: (0.2857142857142857, 0.23809523809523808), 3: None, 4: None}, '3': {0: (0.2, 0.10681818181818184), 1: (0.38461538461538464, 0.3067339115133233), 2: (0.3333333333333333, 0.2737891737891738), 3: None, 4: None}, '4': {0: (0.6, 0.42749999999999994), 1: (0.3333333333333333, 0.27031055900621115), 2: (0.3125, 0.2423076923076923), 3: None, 4: None}, '5': {0: (0.38461538461538464, 0.38461538461538464), 1: (0.391304347826087, 0.41992094861660073), 2: (0.7333333333333333, 0.4339181286549707), 3: None, 4: None}, '6': {0: (0.4, 0.2908424908424908), 1: (0.4642857142857143, 0.3248085141102918), 2: (0.5833333333333334, 0.3095238095238095), 3: None, 4: (1.0, 1.0)}, '7': {0: (0.09090909090909091, 0.1636363636363636), 1: (0.25925925925925924, 0.4462841775219943), 2: (0.42857142857142855, 0.19999999999999998), 3: None, 4: None}, '8': {0: (0.3, 0.32), 1: (0.23809523809523808, 0.3633299197815326), 2: (0.08333333333333333, 0.3731060606060606), 3: None, 4: None}, '9': {0: (0.4166666666666667, 0.3543192918192917), 1: (0.29411764705882354, 0.16053064582476348), 2: (0.25, 0.43333333333333335), 3: None, 4: None}, 'T': {0: (0.23529411764705882, 0.1770944741532977), 1: (0.13333333333333333, 0.22299473843591494), 2: (0.2727272727272727, 0.3509504849217768), 3: None, 4: None}, 'J': {0: (0.08333333333333333, 0.24537037037037038), 1: (0.35294117647058826, 0.386651014160605), 2: (0.25, 0.318452380952381), 3: None, 4: None}, 'Q': {0: (0.125, 0.16346153846153844), 1: (0.1891891891891892, 0.26410853252958516), 2: (0.6, 0.2625), 3: None, 4: None}, 'K': {0: (0.25, 0.18558897243107766), 1: (0.12121212121212122, 0.25991735537190086), 2: (0.36363636363636365, 0.5130369630369631), 3: None, 4: None}}, 5: {'A': {0: (0.0, 0.0), 1: (0.0, 0.0), 2: None, 3: None, 4: None}, '2': {0: None, 1: (0.25, 0.2), 2: (0.4, 0.4), 3: (1.0, 0.0), 4: None}, '3': {0: None, 1: (0.0, 0.0), 2: (0.0, 1.0), 3: None, 4: None}, '4': {0: None, 1: (1.0, 1.0), 2: (0.5, 0.25), 3: None, 4: None}, '5': {0: None, 1: (1.0, 0.0), 2: None, 3: None, 4: None}, '6': {0: None, 1: (0.6666666666666666, 0.28571428571428575), 2: (0.5, 0.0), 3: None, 4: None}, '7': {0: (1.0, 0.0), 1: (0.2, 0.5666666666666667), 2: (0.0, 0.8), 3: None, 4: None}, '8': {0: (0.0, 0.0), 1: (0.42857142857142855, 0.14285714285714285), 2: (0.0, 0.0), 3: None, 4: None}, '9': {0: None, 1: (0.0, 0.25), 2: (0.3333333333333333, 0.0), 3: (1.0, 0.5), 4: None}, 'T': {0: None, 1: (0.25, 0.0), 2: (0.0, 0.47348484848484856), 3: (0.0, 0.0), 4: None}, 'J': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, 'Q': {0: None, 1: (0.3333333333333333, 0.3333333333333333), 2: (0.2, 0.21333333333333332), 3: None, 4: None}, 'K': {0: (0.0, 0.0), 1: (0.5, 0.3125), 2: (0.0, 0.275), 3: (0.0, 0.0), 4: None}}, 6: {'A': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: (1.0, 0.5), 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, '7': {0: None, 1: (0.0, 1.0), 2: (1.0, 1.0), 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 15: {2: {'A': {0: (0.14657210401891257, 0.14893896207897972), 1: (0.043478260869565216, 0.24853654438574332), 2: None, 3: None, 4: None}, '2': {0: (0.4114583333333332, 0.27046523314403276), 1: (0.3018867924528302, 0.47937129790004523), 2: None, 3: None, 4: None}, '3': {0: (0.373015873015873, 0.28116941944911333), 1: (0.3972602739726027, 0.520385372095045), 2: None, 3: None, 4: None}, '4': {0: (0.42406876790830944, 0.2837302396514831), 1: (0.2608695652173913, 0.5408998503245145), 2: None, 3: None, 4: None}, '5': {0: (0.42201834862385323, 0.3018254260579836), 1: (0.43661971830985913, 0.5254287299584811), 2: None, 3: None, 4: None}, '6': {0: (0.455012853470437, 0.29035766385679546), 1: (0.47058823529411764, 0.5282750138347728), 2: None, 3: None, 4: None}, '7': {0: (0.2528409090909091, 0.2846800628463758), 1: (0.22807017543859648, 0.5462221986632688), 2: None, 3: None, 4: None}, '8': {0: (0.2664835164835167, 0.23542520552664242), 1: (0.2698412698412698, 0.43110095297118867), 2: None, 3: None, 4: None}, '9': {0: (0.20887728459530025, 0.2347382252880028), 1: (0.21874999999999997, 0.3543395293802357), 2: None, 3: None, 4: None}, 'T': {0: (0.19170984455958548, 0.19581417097184708), 1: (0.24242424242424243, 0.3486360160763315), 2: None, 3: None, 4: None}, 'J': {0: (0.19662921348314608, 0.19959002152305133), 1: (0.09677419354838708, 0.3127597786235842), 2: None, 3: None, 4: None}, 'Q': {0: (0.23469387755102045, 0.21994508597781057), 1: (0.12500000000000003, 0.42037415675057277), 2: None, 3: None, 4: None}, 'K': {0: (0.23835616438356164, 0.22585832934293942), 1: (0.2597402597402597, 0.34076516760062997), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.10439560439560447, 0.16373676390398004), 1: (0.09375, 0.1660449725232492), 2: (0.0, 0.3818027210884353), 3: None, 4: None}, '2': {0: (0.3443708609271523, 0.25195052991911143), 1: (0.3626373626373626, 0.3178496564985484), 2: (0.0, 0.8), 3: None, 4: None}, '3': {0: (0.40506329113924044, 0.2705096354722406), 1: (0.35514018691588783, 0.31523460521273233), 2: (0.0, 0.5213675213675214), 3: None, 4: None}, '4': {0: (0.4588235294117648, 0.3152934768678711), 1: (0.4086956521739132, 0.2823114374126245), 2: (0.6, 0.6332539682539682), 3: None, 4: None}, '5': {0: (0.4187500000000002, 0.28047009556646213), 1: (0.4672897196261682, 0.2466721882883953), 2: (0.6666666666666666, 0.5001984126984127), 3: None, 4: None}, '6': {0: (0.46111111111111114, 0.275333754807439), 1: (0.4485981308411215, 0.31766580671798605), 2: (0.5, 0.4329365079365079), 3: None, 4: None}, '7': {0: (0.21951219512195122, 0.3003993926676418), 1: (0.255813953488372, 0.3572391301511659), 2: (0.16666666666666666, 0.45722934472934473), 3: None, 4: None}, '8': {0: (0.22994652406417113, 0.30018916614026137), 1: (0.25000000000000006, 0.2543724480367947), 2: (0.5, 0.4217472342472343), 3: None, 4: None}, '9': {0: (0.21556886227544914, 0.2275663345301274), 1: (0.2727272727272727, 0.2489946755557446), 2: (0.4444444444444444, 0.8038480038480038), 3: None, 4: None}, 'T': {0: (0.18124999999999997, 0.17491634411738424), 1: (0.2777777777777776, 0.22004945434774598), 2: (0.14285714285714285, 0.2528822055137845), 3: None, 4: None}, 'J': {0: (0.24309392265193375, 0.19730231192068504), 1: (0.21505376344086022, 0.25422381882005957), 2: (0.2727272727272727, 0.42854191263282176), 3: None, 4: None}, 'Q': {0: (0.22527472527472522, 0.21434264650303947), 1: (0.216, 0.2376622810171732), 2: (0.125, 0.2748359973359973), 3: None, 4: None}, 'K': {0: (0.18120805369127516, 0.17469055672838835), 1: (0.19626168224299065, 0.21089320739011108), 2: (0.14285714285714285, 0.3232909947195662), 3: None, 4: None}}, 4: {'A': {0: (0.045454545454545456, 0.18928571428571422), 1: (0.21739130434782608, 0.1085758286484299), 2: (0.5714285714285714, 0.17142857142857143), 3: None, 4: None}, '2': {0: (0.5625, 0.2857142857142857), 1: (0.25, 0.39285714285714285), 2: (0.8, 0.09473684210526315), 3: None, 4: None}, '3': {0: (0.2631578947368421, 0.22488038277511965), 1: (0.297872340425532, 0.2945907086238752), 2: (0.3076923076923077, 0.15384615384615385), 3: None, 4: None}, '4': {0: (0.42857142857142855, 0.1339285714285714), 1: (0.46511627906976744, 0.24713852376137513), 2: (0.3888888888888889, 0.281054131054131), 3: None, 4: None}, '5': {0: (0.5789473684210527, 0.3394736842105263), 1: (0.325, 0.16623376623376623), 2: (0.3333333333333333, 0.3201754385964913), 3: None, 4: None}, '6': {0: (0.4583333333333333, 0.3493589743589743), 1: (0.4146341463414634, 0.3255724054349132), 2: (0.3333333333333333, 0.17261904761904764), 3: None, 4: None}, '7': {0: (0.3333333333333333, 0.14444444444444443), 1: (0.17142857142857143, 0.3043660739149461), 2: (0.4375, 0.27179487179487183), 3: (0.0, 0.0), 4: None}, '8': {0: (0.2, 0.3555555555555555), 1: (0.19444444444444445, 0.3821631251066734), 2: (0.07692307692307693, 0.2806915306915307), 3: None, 4: None}, '9': {0: (0.3, 0.2106410256410257), 1: (0.25, 0.28220113220113235), 2: (0.29411764705882354, 0.3254901960784314), 3: None, 4: None}, 'T': {0: (0.2777777777777778, 0.1127946127946128), 1: (0.3, 0.21201980054921235), 2: (0.3684210526315789, 0.15751699823721985), 3: None, 4: None}, 'J': {0: (0.2, 0.5208333333333334), 1: (0.19148936170212766, 0.20216837330620865), 2: (0.2727272727272727, 0.2194805194805195), 3: (0.0, 1.0), 4: None}, 'Q': {0: (0.1111111111111111, 0.12759462759462759), 1: (0.26315789473684215, 0.2372679086841137), 2: (0.16666666666666666, 0.08686868686868687), 3: (0.0, 1.0), 4: None}, 'K': {0: (0.2608695652173913, 0.24528713087065485), 1: (0.22727272727272727, 0.19228650137741043), 2: (0.1875, 0.14426510989010988), 3: None, 4: None}}, 5: {'A': {0: (0.0, 0.0), 1: (0.14285714285714285, 0.32142857142857145), 2: (1.0, 0.6666666666666666), 3: None, 4: None}, '2': {0: (0.5, 0.0), 1: (0.25, 0.25), 2: (1.0, 0.6666666666666666), 3: None, 4: None}, '3': {0: (1.0, 0.0), 1: (0.25, 0.25), 2: (0.6666666666666666, 0.3333333333333333), 3: (0.5, 0.0), 4: None}, '4': {0: (0.0, 1.0), 1: (1.0, 0.0), 2: (0.0, 0.0), 3: (1.0, 1.0), 4: None}, '5': {0: None, 1: (1.0, 0.0), 2: (1.0, 0.0), 3: (1.0, 1.0), 4: None}, '6': {0: (0.5, 0.5), 1: (0.5, 0.5714285714285715), 2: (0.5, 0.5), 3: None, 4: None}, '7': {0: None, 1: (0.6, 0.3333333333333333), 2: (0.5, 0.5), 3: (0.0, 0.0), 4: None}, '8': {0: (0.5, 0.0), 1: (0.4, 0.6), 2: (0.3333333333333333, 0.0), 3: (0.0, 1.0), 4: None}, '9': {0: (0.0, 0.0), 1: (0.2857142857142857, 0.42857142857142855), 2: (0.3333333333333333, 0.3333333333333333), 3: None, 4: None}, 'T': {0: (0.0, 0.0), 1: (0.0, 0.08333333333333333), 2: (0.5, 0.25), 3: (0.0, 0.0), 4: None}, 'J': {0: (0.0, 0.0), 1: (0.3333333333333333, 0.0), 2: (0.42857142857142855, 0.4857142857142857), 3: None, 4: None}, 'Q': {0: (0.0, 0.0), 1: (0.0, 0.25), 2: (0.0, 0.3333333333333333), 3: None, 4: None}, 'K': {0: (0.0, 0.0), 1: (0.0, 0.0), 2: (0.2, 0.18666666666666668), 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, '5': {0: None, 1: None, 2: (0.6666666666666666, 0.0), 3: (0.0, 0.0), 4: (0.0, 0.0)}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}, '9': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, 'T': {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}, 'J': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: (1.0, 0.0), 3: None, 4: None}}}, 16: {2: {'A': {0: (0.12654320987654324, 0.17829929394914631), 1: (0.14634146341463414, 0.19608339528793475), 2: None, 3: None, 4: None}, '2': {0: (0.3742690058479532, 0.2608196289683232), 1: (0.44776119402985076, 0.505611423470759), 2: None, 3: None, 4: None}, '3': {0: (0.33862433862433877, 0.23320108813493293), 1: (0.36619718309859156, 0.5237956099883471), 2: None, 3: None, 4: None}, '4': {0: (0.4360465116279071, 0.23639081110845642), 1: (0.30000000000000004, 0.5196926329181244), 2: None, 3: None, 4: None}, '5': {0: (0.34925373134328347, 0.2620162836818687), 1: (0.5, 0.5319313681071844), 2: None, 3: None, 4: None}, '6': {0: (0.4294871794871794, 0.30666650793159345), 1: (0.38333333333333336, 0.5547701693368539), 2: None, 3: None, 4: None}, '7': {0: (0.2385057471264369, 0.24487158355355992), 1: (0.3, 0.4385391738631073), 2: None, 3: None, 4: None}, '8': {0: (0.24633431085043989, 0.24041115519497508), 1: (0.2881355932203391, 0.42225106221794), 2: None, 3: None, 4: None}, '9': {0: (0.21725239616613418, 0.2199538316662492), 1: (0.18181818181818182, 0.3623564399473265), 2: None, 3: None, 4: None}, 'T': {0: (0.20489296636085627, 0.1666306487448717), 1: (0.26666666666666666, 0.34675929169019276), 2: None, 3: None, 4: None}, 'J': {0: (0.21554770318021202, 0.18895187485339693), 1: (0.17307692307692307, 0.32537153605183633), 2: None, 3: None, 4: None}, 'Q': {0: (0.20625, 0.1860455160159515), 1: (0.23728813559322035, 0.37298711313295924), 2: None, 3: None, 4: None}, 'K': {0: (0.19417475728155345, 0.210089747157374), 1: (0.2424242424242425, 0.3626984972062741), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.10144927536231886, 0.10538768544410725), 1: (0.09333333333333334, 0.12526623119198785), 2: (0.0, 0.16666666666666666), 3: None, 4: None}, '2': {0: (0.39898989898989884, 0.231845435955927), 1: (0.3917525773195876, 0.28058207542743646), 2: (0.2, 0.5866666666666667), 3: None, 4: None}, '3': {0: (0.3155339805825242, 0.25195546478486847), 1: (0.4615384615384617, 0.22016241121312743), 2: (0.6666666666666666, 0.6527065527065528), 3: None, 4: None}, '4': {0: (0.4375, 0.22751963650957466), 1: (0.4727272727272728, 0.2869938091126787), 2: (0.8, 0.7214565826330532), 3: None, 4: None}, '5': {0: (0.46842105263157885, 0.2377129985289309), 1: (0.38202247191011246, 0.308723127744634), 2: (0.5, 0.4861111111111111), 3: None, 4: None}, '6': {0: (0.46634615384615397, 0.27311815864447464), 1: (0.44660194174757284, 0.2541983960473208), 2: (0.75, 0.547077922077922), 3: None, 4: None}, '7': {0: (0.3103448275862068, 0.2518192327448073), 1: (0.2857142857142857, 0.315084230307149), 2: (0.25, 0.37637362637362637), 3: None, 4: None}, '8': {0: (0.23280423280423287, 0.23335801779443158), 1: (0.24770642201834858, 0.2865628309127797), 2: (0.0, 0.42713635570778424), 3: None, 4: None}, '9': {0: (0.24509803921568626, 0.2313759210789966), 1: (0.2857142857142857, 0.29651514480693086), 2: (0.25, 0.7291666666666667), 3: None, 4: None}, 'T': {0: (0.158974358974359, 0.15270499405804563), 1: (0.3076923076923076, 0.19040166283907695), 2: (0.0, 0.23486684766589075), 3: None, 4: None}, 'J': {0: (0.20500000000000007, 0.20075299258280066), 1: (0.13559322033898305, 0.2070569193839295), 2: (0.0, 0.484375), 3: None, 4: None}, 'Q': {0: (0.22279792746113988, 0.15644576967474114), 1: (0.23148148148148148, 0.2416591814838011), 2: (0.3333333333333333, 0.49296128707893416), 3: None, 4: None}, 'K': {0: (0.22926829268292684, 0.17246482609649985), 1: (0.1875, 0.21625411427595817), 2: (0.0, 0.3042438271604938), 3: None, 4: None}}, 4: {'A': {0: (0.125, 0.12261904761904761), 1: (0.12962962962962962, 0.1302144513719466), 2: (0.0, 0.028571428571428574), 3: None, 4: None}, '2': {0: (0.3076923076923077, 0.33516483516483514), 1: (0.4318181818181818, 0.2362012987012987), 2: (0.5, 0.1923076923076923), 3: (0.0, 0.0), 4: None}, '3': {0: (0.42857142857142855, 0.12221706864564007), 1: (0.391304347826087, 0.3744405370843989), 2: (0.5333333333333333, 0.2626780626780626), 3: None, 4: None}, '4': {0: (0.3333333333333333, 0.1898148148148148), 1: (0.4999999999999998, 0.26990983770787425), 2: (0.5882352941176471, 0.2882352941176471), 3: (0.0, 0.0), 4: None}, '5': {0: (0.43478260869565216, 0.10013175230566532), 1: (0.5254237288135594, 0.18920390344119162), 2: (0.08333333333333333, 0.27777777777777773), 3: None, 4: None}, '6': {0: (0.25806451612903225, 0.2606537922105944), 1: (0.5333333333333333, 0.22099069512862618), 2: (0.5454545454545454, 0.3822510822510823), 3: (0.0, 0.0), 4: None}, '7': {0: (0.34375, 0.3204861111111111), 1: (0.3888888888888889, 0.21456557665134662), 2: (0.5384615384615384, 0.3230769230769231), 3: (1.0, 0.0), 4: None}, '8': {0: (0.13043478260869565, 0.3417874396135265), 1: (0.20634920634920634, 0.2809414088215932), 2: (0.14285714285714285, 0.14285714285714285), 3: None, 4: None}, '9': {0: (0.38461538461538464, 0.14032121724429414), 1: (0.27419354838709675, 0.26962365591397863), 2: (0.25, 0.19444444444444445), 3: None, 4: None}, 'T': {0: (0.17391304347826086, 0.13537549407114624), 1: (0.26666666666666666, 0.16503141797259438), 2: (0.1875, 0.22322414427677584), 3: (0.0, 1.0), 4: None}, 'J': {0: (0.28125, 0.16666666666666669), 1: (0.1896551724137931, 0.22678083036403868), 2: (0.4166666666666667, 0.3142857142857143), 3: None, 4: None}, 'Q': {0: (0.21621621621621623, 0.2234630234630235), 1: (0.2127659574468085, 0.2711023578884721), 2: (0.23076923076923078, 0.1738927738927739), 3: None, 4: None}, 'K': {0: (0.0967741935483871, 0.19500363812757704), 1: (0.2653061224489796, 0.13756957328385894), 2: (0.2857142857142857, 0.17091836734693877), 3: None, 4: None}}, 5: {'A': {0: (0.6666666666666666, 0.3333333333333333), 1: (0.25, 0.03125), 2: (0.0, 0.16666666666666666), 3: None, 4: None}, '2': {0: (0.5, 1.0), 1: (0.3333333333333333, 0.17777777777777778), 2: (0.6, 0.0), 3: None, 4: None}, '3': {0: (0.0, 0.0), 1: (0.4444444444444444, 0.0), 2: (0.5555555555555556, 0.2592592592592593), 3: None, 4: None}, '4': {0: None, 1: (0.5, 0.17142857142857143), 2: (0.5, 0.5), 3: (1.0, 0.0), 4: None}, '5': {0: (0.5, 0.5), 1: (0.8, 0.2), 2: (0.2857142857142857, 0.14285714285714285), 3: (1.0, 0.5), 4: None}, '6': {0: (0.0, 0.0), 1: (0.8, 0.2), 2: (0.6666666666666666, 0.3333333333333333), 3: None, 4: None}, '7': {0: None, 1: (0.125, 0.375), 2: (0.3333333333333333, 0.16666666666666666), 3: (0.0, 0.6666666666666666), 4: None}, '8': {0: (0.0, 0.0), 1: (0.6666666666666666, 0.3333333333333333), 2: (0.25, 0.0), 3: None, 4: None}, '9': {0: (0.25, 0.0), 1: (0.0, 0.1), 2: (0.4, 0.2), 3: None, 4: None}, 'T': {0: (0.2, 0.0), 1: (0.25, 0.3125), 2: (0.0, 0.17532467532467533), 3: (0.0, 0.0), 4: None}, 'J': {0: (1.0, 0.6666666666666666), 1: (0.125, 0.40625), 2: (0.0, 0.13333333333333333), 3: None, 4: None}, 'Q': {0: (0.25, 0.5), 1: (0.0, 0.0), 2: (0.125, 0.3125), 3: (0.0, 0.0), 4: None}, 'K': {0: (0.0, 0.0), 1: (0.0, 0.26969696969696966), 2: (0.0, 0.6), 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, '4': {0: None, 1: (1.0, 0.0), 2: (1.0, 0.0), 3: None, 4: None}, '5': {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}, '6': {0: None, 1: (1.0, 0.0), 2: (0.0, 1.0), 3: None, 4: None}, '7': {0: None, 1: (0.0, 0.0), 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}, '9': {0: None, 1: (1.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, 'T': {0: None, 1: None, 2: (1.0, 0.0), 3: (0.0, 0.0), 4: None}, 'J': {0: None, 1: (0.0, 0.0), 2: (0.5, 0.0), 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}}}, 17: {2: {'A': {0: (0.12166172106824924, 0.132643936260994), 1: (0.02127659574468085, 0.25585967718152), 2: None, 3: None, 4: None}, '2': {0: (0.3507246376811594, 0.22649277128934112), 1: (0.4098360655737705, 0.4361796210128611), 2: None, 3: None, 4: None}, '3': {0: (0.3485342019543974, 0.25834063809474456), 1: (0.3787878787878788, 0.4534869615611507), 2: None, 3: None, 4: None}, '4': {0: (0.4471299093655589, 0.2225350111378418), 1: (0.3571428571428572, 0.5499395354167085), 2: None, 3: None, 4: None}, '5': {0: (0.42406876790830955, 0.2503375085465671), 1: (0.3508771929824562, 0.5290155341161787), 2: None, 3: None, 4: None}, '6': {0: (0.3908794788273615, 0.21542706387207589), 1: (0.3400000000000001, 0.5022980468956738), 2: None, 3: None, 4: None}, '7': {0: (0.3233082706766916, 0.28138435605405177), 1: (0.3230769230769231, 0.4456540481311874), 2: None, 3: None, 4: None}, '8': {0: (0.23666666666666666, 0.2271904788746508), 1: (0.2857142857142857, 0.4386799797413207), 2: None, 3: None, 4: None}, '9': {0: (0.22461538461538466, 0.18938570931331103), 1: (0.25, 0.42983312711295707), 2: None, 3: None, 4: None}, 'T': {0: (0.19528619528619529, 0.16859497993739597), 1: (0.2033898305084746, 0.412409066961779), 2: None, 3: None, 4: None}, 'J': {0: (0.21753246753246758, 0.14951461200782218), 1: (0.3026315789473684, 0.34382055925918004), 2: None, 3: None, 4: None}, 'Q': {0: (0.19999999999999996, 0.16998846321175545), 1: (0.19480519480519481, 0.35257419475132357), 2: None, 3: None, 4: None}, 'K': {0: (0.21865889212827994, 0.1669781859666509), 1: (0.1891891891891892, 0.31925264142310317), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.1245136186770428, 0.12053413512557482), 1: (0.13924050632911392, 0.16281310338317723), 2: (0.0, 0.7142857142857143), 3: None, 4: None}, '2': {0: (0.3991935483870968, 0.23038216264022737), 1: (0.2735849056603773, 0.2207371377290956), 2: (0.45454545454545453, 0.5140640858344209), 3: None, 4: None}, '3': {0: (0.42035398230088494, 0.2657180209171364), 1: (0.31632653061224486, 0.21031130802337955), 2: (0.4, 0.43431372549019615), 3: None, 4: None}, '4': {0: (0.37558685446009404, 0.20905872516863216), 1: (0.48245614035087714, 0.3018089625680134), 2: (0.6666666666666666, 0.5048611111111111), 3: None, 4: None}, '5': {0: (0.4951456310679609, 0.1690894004365329), 1: (0.41739130434782606, 0.2960651631243186), 2: (0.75, 0.6607142857142857), 3: None, 4: None}, '6': {0: (0.3925233644859813, 0.21621605335328906), 1: (0.3969465648854962, 0.3481308622659101), 2: (0.75, 0.6875), 3: None, 4: None}, '7': {0: (0.311111111111111, 0.23507710599845436), 1: (0.2222222222222222, 0.2878383224421562), 2: (0.0, 0.29758241758241755), 3: None, 4: None}, '8': {0: (0.2270742358078603, 0.20549636346037595), 1: (0.1834862385321101, 0.34412476269856523), 2: (0.0, 0.47602628852628853), 3: None, 4: None}, '9': {0: (0.21929824561403508, 0.19403025031721635), 1: (0.3010752688172044, 0.17950164401698124), 2: (0.0, 0.5628342245989305), 3: None, 4: None}, 'T': {0: (0.2382978723404257, 0.15153764015643673), 1: (0.23300970873786409, 0.22248415023605506), 2: (0.125, 0.28240240620623397), 3: None, 4: None}, 'J': {0: (0.21459227467811165, 0.14317474590742887), 1: (0.14814814814814814, 0.2173330681521261), 2: (0.25, 0.2558441558441558), 3: None, 4: None}, 'Q': {0: (0.2872340425531914, 0.196366213069144), 1: (0.24347826086956512, 0.23504973886809674), 2: (0.2857142857142857, 0.4694638694638695), 3: None, 4: None}, 'K': {0: (0.22413793103448276, 0.1451091970676499), 1: (0.23232323232323232, 0.18841925095169934), 2: (0.3333333333333333, 0.2567511192511192), 3: None, 4: None}}, 4: {'A': {0: (0.16279069767441862, 0.17973421926910296), 1: (0.11904761904761904, 0.1357820547573868), 2: (0.0, 0.14285714285714285), 3: None, 4: None}, '2': {0: (0.1111111111111111, 0.1746031746031746), 1: (0.3606557377049181, 0.3077283372365339), 2: (0.5, 0.19266917293233082), 3: None, 4: None}, '3': {0: (0.53125, 0.10973011363636365), 1: (0.4807692307692308, 0.16077488687782804), 2: (0.2222222222222222, 0.26495726495726496), 3: (1.0, 1.0), 4: None}, '4': {0: (0.47058823529411764, 0.23434873949579835), 1: (0.49122807017543857, 0.20693618103229086), 2: (0.35, 0.15673076923076926), 3: None, 4: None}, '5': {0: (0.5609756097560976, 0.17012195121951218), 1: (0.45714285714285713, 0.22967099567099558), 2: (0.35714285714285715, 0.33458646616541354), 3: (0.0, 0.0), 4: None}, '6': {0: (0.6216216216216216, 0.29967329967329964), 1: (0.5185185185185185, 0.24144316730523632), 2: (0.25, 0.25), 3: None, 4: None}, '7': {0: (0.3157894736842105, 0.23095238095238094), 1: (0.3088235294117647, 0.25317910790047016), 2: (0.15384615384615385, 0.21025641025641026), 3: None, 4: None}, '8': {0: (0.15, 0.2375), 1: (0.2328767123287671, 0.18915051659196605), 2: (0.3076923076923077, 0.24145299145299146), 3: None, 4: None}, '9': {0: (0.20454545454545456, 0.15943147761329582), 1: (0.27777777777777785, 0.1334656084656084), 2: (0.18181818181818182, 0.5393939393939394), 3: (0.0, 0.0), 4: None}, 'T': {0: (0.23076923076923078, 0.14836144247908953), 1: (0.20512820512820512, 0.16047199599831174), 2: (0.0, 0.3179093633639088), 3: (0.0, 1.0), 4: None}, 'J': {0: (0.225, 0.12676767676767678), 1: (0.22222222222222218, 0.13589010483420416), 2: (0.18181818181818182, 0.3753246753246753), 3: None, 4: None}, 'Q': {0: (0.2857142857142857, 0.15129768190992682), 1: (0.2, 0.1745698380566802), 2: (0.07692307692307693, 0.17156177156177158), 3: (0.0, 0.0), 4: None}, 'K': {0: (0.23255813953488372, 0.07444085901858237), 1: (0.1276595744680851, 0.15053191489361697), 2: (0.21428571428571427, 0.2620115995115996), 3: None, 4: None}}, 5: {'A': {0: (0.0, 0.0), 1: (0.0, 0.08333333333333333), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}, '2': {0: (0.6666666666666666, 0.0), 1: (0.5, 0.041666666666666664), 2: (0.375, 0.125), 3: None, 4: None}, '3': {0: (1.0, 0.0), 1: (0.42857142857142855, 0.3333333333333333), 2: (0.3333333333333333, 0.2222222222222222), 3: (0.0, 0.0), 4: None}, '4': {0: None, 1: (0.5, 0.1875), 2: (0.16666666666666666, 0.5), 3: (0.5, 0.5), 4: None}, '5': {0: (0.6666666666666666, 0.0), 1: (0.8181818181818182, 0.25757575757575757), 2: (0.3333333333333333, 0.3333333333333333), 3: (0.5, 0.0), 4: None}, '6': {0: (0.5, 0.5), 1: (0.5652173913043478, 0.32298136645962733), 2: (0.5, 0.2), 3: (0.0, 0.3333333333333333), 4: None}, '7': {0: (0.5, 0.5), 1: (0.5, 0.125), 2: (0.23076923076923078, 0.3076923076923077), 3: (0.0, 1.0), 4: None}, '8': {0: (0.3333333333333333, 0.3333333333333333), 1: (0.375, 0.25), 2: (0.125, 0.0), 3: (0.0, 0.0), 4: None}, '9': {0: (0.0, 0.5), 1: (0.3076923076923077, 0.19230769230769232), 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: None}, 'T': {0: (0.0, 0.0), 1: (0.25, 0.125), 2: (0.5, 0.2916666666666667), 3: (0.0, 0.0), 4: None}, 'J': {0: (0.0, 0.0), 1: (0.2222222222222222, 0.10277777777777779), 2: (0.2, 0.27999999999999997), 3: (0.0, 0.5), 4: None}, 'Q': {0: (1.0, 0.0), 1: (0.2, 0.0), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}, 'K': {0: (0.0, 0.0), 1: (0.16666666666666666, 0.1597222222222222), 2: (0.3, 0.05), 3: None, 4: None}}, 6: {'A': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, '2': {0: None, 1: (0.0, 0.0), 2: (1.0, 0.0), 3: None, 4: None}, '3': {0: None, 1: None, 2: (0.3333333333333333, 0.0), 3: None, 4: None}, '4': {0: None, 1: (0.0, 0.0), 2: (1.0, 1.0), 3: (0.0, 0.0), 4: None}, '5': {0: None, 1: None, 2: (1.0, 0.0), 3: None, 4: None}, '6': {0: None, 1: (1.0, 0.0), 2: None, 3: None, 4: None}, '7': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, '8': {0: None, 1: None, 2: (0.0, 1.0), 3: (0.5, 0.0), 4: None}, '9': {0: None, 1: (0.5, 1.0), 2: (0.0, 0.0), 3: None, 4: None}, 'T': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, 'J': {0: (0.0, 0.0), 1: (0.0, 0.5), 2: (0.0, 0.0), 3: None, 4: (1.0, 1.0)}, 'Q': {0: None, 1: (0.0, 0.0), 2: (0.4, 0.0), 3: (0.0, 0.0), 4: None}, 'K': {0: None, 1: (0.0, 0.0), 2: (0.3333333333333333, 0.6666666666666666), 3: None, 4: None}}}, 18: {2: {'A': {0: (0.2491909385113269, 0.10346585117227325), 1: (0.17307692307692316, 0.28224050634730313), 2: None, 3: None, 4: None}, '2': {0: (0.48366013071895425, 0.16041700225024036), 1: (0.6231884057971016, 0.5490380280726849), 2: None, 3: None, 4: None}, '3': {0: (0.514754098360656, 0.14572134558186176), 1: (0.5, 0.5335214213384807), 2: None, 3: None, 4: None}, '4': {0: (0.5212355212355216, 0.17247283580277176), 1: (0.5873015873015872, 0.5338323273581601), 2: None, 3: None, 4: None}, '5': {0: (0.5212765957446807, 0.21944971299443505), 1: (0.5483870967741935, 0.5283281412235727), 2: None, 3: None, 4: None}, '6': {0: (0.5878378378378382, 0.1959575247470558), 1: (0.6666666666666666, 0.556077133861059), 2: None, 3: None, 4: None}, '7': {0: (0.6734693877551019, 0.2291246960232692), 1: (0.72, 0.6060530530622309), 2: None, 3: None, 4: None}, '8': {0: (0.3472222222222221, 0.2121251312040787), 1: (0.24193548387096775, 0.45725988037766835), 2: None, 3: None, 4: None}, '9': {0: (0.36923076923076925, 0.18416759955221487), 1: (0.2686567164179105, 0.4419734762663878), 2: None, 3: None, 4: None}, 'T': {0: (0.31007751937984496, 0.14499184476960478), 1: (0.36486486486486486, 0.3436780483526215), 2: None, 3: None, 4: None}, 'J': {0: (0.31451612903225795, 0.1336957011789636), 1: (0.3157894736842105, 0.36695808309939143), 2: None, 3: None, 4: None}, 'Q': {0: (0.4, 0.12318431211045505), 1: (0.27868852459016397, 0.3879433740922689), 2: None, 3: None, 4: None}, 'K': {0: (0.37969924812030065, 0.15215183639505306), 1: (0.49180327868852447, 0.34158919984033714), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.21481481481481482, 0.11181657848324508), 1: (0.24731182795698925, 0.20450349990252686), 2: (0.3333333333333333, 0.546031746031746), 3: None, 4: None}, '2': {0: (0.5137254901960784, 0.15470803706097824), 1: (0.4770642201834863, 0.19607986822755963), 2: (0.6, 0.5174825174825175), 3: None, 4: None}, '3': {0: (0.4898785425101216, 0.18650472334682858), 1: (0.5585585585585585, 0.24843108020060584), 2: (0.6666666666666666, 0.5612759063739456), 3: None, 4: None}, '4': {0: (0.5138339920948621, 0.14977666065466813), 1: (0.46956521739130436, 0.317739316881203), 2: (0.4, 0.5674229691876749), 3: None, 4: None}, '5': {0: (0.5636363636363644, 0.21775329706883736), 1: (0.5544554455445546, 0.28588697164388455), 2: (0.6, 0.40952380952380957), 3: None, 4: None}, '6': {0: (0.6425531914893622, 0.20577796575884075), 1: (0.5378151260504204, 0.35620374148321904), 2: (1.0, 0.5793650793650793), 3: None, 4: None}, '7': {0: (0.6491228070175439, 0.19298867736717693), 1: (0.7340425531914895, 0.26011892264996095), 2: (0.6666666666666666, 0.6666666666666666), 3: None, 4: None}, '8': {0: (0.34509803921568627, 0.224478247381877), 1: (0.4239130434782609, 0.25933641877466757), 2: (0.5, 0.4932012432012432), 3: None, 4: None}, '9': {0: (0.3566176470588234, 0.16564444778912796), 1: (0.3613445378151261, 0.3031238338242529), 2: (0.5, 0.6627450980392157), 3: None, 4: None}, 'T': {0: (0.3151750972762646, 0.12150268667778398), 1: (0.33620689655172414, 0.21552088300146638), 2: (0.4, 0.4064390155299247), 3: None, 4: None}, 'J': {0: (0.3720930232558139, 0.1362565495848038), 1: (0.2477064220183487, 0.2278685415034844), 2: (0.5714285714285714, 0.3484848484848485), 3: None, 4: None}, 'Q': {0: (0.31297709923664113, 0.1518668536116737), 1: (0.36111111111111116, 0.18808614548794295), 2: (0.0, 0.5490384615384616), 3: None, 4: None}, 'K': {0: (0.3245283018867925, 0.1664753448549232), 1: (0.3391304347826087, 0.1918623531354449), 2: (0.75, 0.259875695292362), 3: None, 4: None}}, 4: {'A': {0: (0.2592592592592593, 0.07799564270152505), 1: (0.22727272727272732, 0.1536656891495601), 2: (0.0, 0.06666666666666667), 3: None, 4: None}, '2': {0: (0.4186046511627907, 0.1096345514950166), 1: (0.5555555555555556, 0.15491452991452992), 2: (0.38461538461538464, 0.2203103913630229), 3: None, 4: None}, '3': {0: (0.6530612244897961, 0.16914038342609775), 1: (0.5151515151515151, 0.07538050185109009), 2: (0.7777777777777778, 0.2222222222222222), 3: None, 4: None}, '4': {0: (0.5185185185185185, 0.064170692431562), 1: (0.4794520547945205, 0.17239199157007373), 2: (0.42857142857142855, 0.5523809523809524), 3: (1.0, 1.0), 4: None}, '5': {0: (0.6, 0.20585858585858585), 1: (0.5609756097560976, 0.1788617886178861), 2: (0.7777777777777778, 0.6120857699805068), 3: (1.0, 1.0), 4: None}, '6': {0: (0.6666666666666667, 0.2036693191865605), 1: (0.5925925925925926, 0.17783656672545564), 2: (0.7142857142857143, 0.14285714285714285), 3: None, 4: None}, '7': {0: (0.6461538461538462, 0.19658119658119663), 1: (0.585714285714286, 0.2103276047261009), 2: (0.5, 0.2), 3: None, 4: None}, '8': {0: (0.39344262295081966, 0.2297684100962789), 1: (0.41025641025641024, 0.1648898443253282), 2: (0.45454545454545453, 0.2323232323232323), 3: (0.5, 0.5), 4: None}, '9': {0: (0.4, 0.07743589743589743), 1: (0.303370786516854, 0.2540919754402901), 2: (0.38461538461538464, 0.1282051282051282), 3: None, 4: None}, 'T': {0: (0.39215686274509803, 0.10797046091163737), 1: (0.3552631578947369, 0.1572454631665158), 2: (0.35714285714285715, 0.12087912087912091), 3: None, 4: None}, 'J': {0: (0.43137254901960786, 0.18243819266837172), 1: (0.38823529411764707, 0.2574789915966386), 2: (0.3333333333333333, 0.0), 3: None, 4: None}, 'Q': {0: (0.18518518518518517, 0.14814814814814814), 1: (0.3763440860215054, 0.09806040026753099), 2: (0.4444444444444444, 0.25925925925925924), 3: (0.0, 0.0), 4: None}, 'K': {0: (0.2833333333333333, 0.10350877192982454), 1: (0.39080459770114945, 0.08424429976154114), 2: (0.16666666666666666, 0.2656305114638448), 3: (0.0, 0.0), 4: None}}, 5: {'A': {0: (0.0, 0.0), 1: (0.35714285714285715, 0.07142857142857142), 2: (0.0, 0.2), 3: None, 4: None}, '2': {0: (0.0, 0.0), 1: (0.8571428571428571, 0.1142857142857143), 2: (0.6666666666666666, 0.4444444444444444), 3: (1.0, 0.0), 4: None}, '3': {0: (0.5, 0.5), 1: (0.4375, 0.0625), 2: (0.5, 0.2333333333333333), 3: None, 4: None}, '4': {0: (0.6666666666666666, 0.3333333333333333), 1: (0.2857142857142857, 0.2653061224489796), 2: (0.4666666666666667, 0.2), 3: (0.0, 0.0), 4: None}, '5': {0: (0.3333333333333333, 0.16666666666666666), 1: (0.5, 0.109375), 2: (0.6666666666666666, 0.1111111111111111), 3: (1.0, 0.0), 4: None}, '6': {0: (1.0, 0.25), 1: (0.7142857142857143, 0.0), 2: (0.6, 0.2), 3: None, 4: None}, '7': {0: (0.0, 0.0), 1: (0.6071428571428571, 0.13333333333333336), 2: (0.6, 0.2), 3: (0.5, 0.5), 4: None}, '8': {0: (0.3333333333333333, 0.3333333333333333), 1: (0.2777777777777778, 0.2222222222222222), 2: (0.3333333333333333, 0.13333333333333333), 3: None, 4: None}, '9': {0: (0.16666666666666666, 0.0), 1: (0.36363636363636365, 0.0), 2: (0.3, 0.1), 3: (1.0, 0.0), 4: None}, 'T': {0: (0.0, 0.0), 1: (0.4117647058823529, 0.0784313725490196), 2: (0.47368421052631576, 0.10526315789473684), 3: (0.0, 0.0), 4: None}, 'J': {0: (0.5, 0.25), 1: (0.22727272727272727, 0.18181818181818182), 2: (0.2857142857142857, 0.0), 3: (0.3333333333333333, 0.0), 4: None}, 'Q': {0: (0.42857142857142855, 0.32142857142857145), 1: (0.18181818181818182, 0.1515151515151515), 2: (0.0, 0.2), 3: None, 4: None}, 'K': {0: (0.2857142857142857, 0.14285714285714285), 1: (0.18181818181818182, 0.10909090909090909), 2: (0.375, 0.0), 3: (0.0, 0.0), 4: None}}, 6: {'A': {0: None, 1: (0.0, 1.0), 2: None, 3: (1.0, 0.0), 4: None}, '2': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, '3': {0: None, 1: (0.0, 0.0), 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: None}, '4': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}, '5': {0: None, 1: None, 2: (0.3333333333333333, 0.0), 3: None, 4: None}, '6': {0: None, 1: (0.0, 0.0), 2: (0.5, 0.0), 3: (1.0, 0.0), 4: None}, '7': {0: (0.0, 0.0), 1: (1.0, 0.3333333333333333), 2: (0.5, 0.0), 3: None, 4: None}, '8': {0: (1.0, 0.0), 1: (0.0, 0.0), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}, '9': {0: None, 1: (0.5, 0.0), 2: None, 3: (0.0, 0.0), 4: (0.0, 1.0)}, 'T': {0: None, 1: (0.5, 0.0), 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: (1.0, 0.0)}, 'J': {0: (1.0, 0.0), 1: None, 2: (0.25, 0.0), 3: (0.0, 0.0), 4: None}, 'Q': {0: None, 1: (1.0, 0.0), 2: (0.25, 0.5), 3: None, 4: None}, 'K': {0: None, 1: (1.0, 0.0), 2: (0.3333333333333333, 0.0), 3: None, 4: None}}}, 19: {2: {'A': {0: (0.40942028985507256, 0.09239130434782614), 1: (0.32653061224489793, 0.2608676733374762), 2: None, 3: None, 4: None}, '2': {0: (0.6425992779783394, 0.10974729241877255), 1: (0.5588235294117647, 0.5623233796124388), 2: None, 3: None, 4: None}, '3': {0: (0.6450216450216453, 0.1649273345701917), 1: (0.7758620689655172, 0.5720712817113955), 2: None, 3: None, 4: None}, '4': {0: (0.6437768240343347, 0.12428088759017449), 1: (0.6933333333333331, 0.6043180801828965), 2: None, 3: None, 4: None}, '5': {0: (0.6819923371647514, 0.13300492610837447), 1: (0.5957446808510639, 0.6085154334913061), 2: None, 3: None, 4: None}, '6': {0: (0.7230769230769228, 0.1420118343195266), 1: (0.596153846153846, 0.505273762662575), 2: None, 3: None, 4: None}, '7': {0: (0.7620817843866169, 0.1594691310843206), 1: (0.8275862068965517, 0.6210208130827629), 2: None, 3: None, 4: None}, '8': {0: (0.6844106463878326, 0.1441187293020974), 1: (0.675, 0.6398783169937409), 2: None, 3: None, 4: None}, '9': {0: (0.4627659574468085, 0.11231884057971013), 1: (0.49230769230769234, 0.4362884582045937), 2: None, 3: None, 4: None}, 'T': {0: (0.4152542372881356, 0.08215878679750216), 1: (0.5, 0.4524998041699519), 2: None, 3: None, 4: None}, 'J': {0: (0.4380952380952381, 0.09679730299199325), 1: (0.4305555555555556, 0.4077537261660702), 2: None, 3: None, 4: None}, 'Q': {0: (0.40234375, 0.10571808510638295), 1: (0.5131578947368419, 0.4339559743710507), 2: None, 3: None, 4: None}, 'K': {0: (0.36507936507936506, 0.0983881525118638), 1: (0.4153846153846154, 0.37849904302919124), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.38831615120274904, 0.09348962011015399), 1: (0.3645833333333334, 0.1711562542870294), 2: (0.6, 0.43690476190476185), 3: None, 4: None}, '2': {0: (0.6401515151515149, 0.12643939393939396), 1: (0.6796116504854369, 0.2840971299908113), 2: (1.0, 0.6923076923076923), 3: None, 4: None}, '3': {0: (0.6035087719298239, 0.16194056569996426), 1: (0.6792452830188679, 0.25609565837424486), 2: (0.75, 0.6319444444444444), 3: None, 4: None}, '4': {0: (0.6262975778546713, 0.15505025539627612), 1: (0.7029702970297032, 0.2943012688247425), 2: (0.8181818181818182, 0.6833193321829687), 3: None, 4: None}, '5': {0: (0.6872427983539094, 0.11790323225058925), 1: (0.7281553398058253, 0.23770303026367504), 2: (0.42857142857142855, 0.5578231292517007), 3: None, 4: None}, '6': {0: (0.7246376811594201, 0.1277997364953884), 1: (0.693877551020408, 0.30245842576817883), 2: (0.5, 0.5565476190476191), 3: None, 4: None}, '7': {0: (0.7918367346938775, 0.1617083946980855), 1: (0.7476635514018691, 0.30269465708796806), 2: (1.0, 0.7275), 3: None, 4: None}, '8': {0: (0.7640449438202247, 0.13501687247376423), 1: (0.8210526315789474, 0.3777785710782697), 2: (0.6666666666666666, 0.510995485995486), 3: None, 4: None}, '9': {0: (0.4269230769230769, 0.1340860973888496), 1: (0.40540540540540543, 0.18422003301968337), 2: (0.6, 0.6366666666666668), 3: None, 4: None}, 'T': {0: (0.3993288590604026, 0.09912933067295478), 1: (0.5315315315315318, 0.1479855691284127), 2: (0.25, 0.369388575937619), 3: None, 4: None}, 'J': {0: (0.39655172413793116, 0.10445673389720235), 1: (0.4074074074074074, 0.23902640493109603), 2: (0.5, 0.533779761904762), 3: None, 4: None}, 'Q': {0: (0.39436619718309857, 0.12616122265507942), 1: (0.48979591836734687, 0.24735940334097795), 2: (0.5, 0.3178382401911814), 3: None, 4: None}, 'K': {0: (0.4659090909090909, 0.1163277511961723), 1: (0.5428571428571426, 0.18890854705773807), 2: (0.42857142857142855, 0.41258364651221796), 3: None, 4: None}}, 4: {'A': {0: (0.26136363636363635, 0.06378299120234603), 1: (0.3492063492063492, 0.060757636387888496), 2: (0.625, 0.15), 3: None, 4: None}, '2': {0: (0.6545454545454545, 0.12727272727272726), 1: (0.6043956043956041, 0.06419895893580102), 2: (0.5454545454545454, 0.21937645687645688), 3: None, 4: None}, '3': {0: (0.7000000000000002, 0.06008403361344538), 1: (0.6444444444444446, 0.12268518518518516), 2: (0.75, 0.13846153846153847), 3: None, 4: None}, '4': {0: (0.6705882352941176, 0.15388235294117644), 1: (0.6310679611650483, 0.09805825242718448), 2: (0.7333333333333333, 0.06666666666666667), 3: None, 4: None}, '5': {0: (0.609375, 0.11500000000000003), 1: (0.7524752475247525, 0.13307120185702773), 2: (0.6428571428571429, 0.3095238095238095), 3: None, 4: None}, '6': {0: (0.6210526315789474, 0.15964912280701749), 1: (0.6853932584269664, 0.18607036770539284), 2: (0.5, 0.16666666666666666), 3: None, 4: None}, '7': {0: (0.797752808988764, 0.13571850975754), 1: (0.7872340425531915, 0.12702634245187433), 2: (0.8, 0.6466666666666667), 3: None, 4: None}, '8': {0: (0.8024691358024689, 0.19474313022700127), 1: (0.7435897435897436, 0.15694953194953198), 2: (0.7333333333333333, 0.20252525252525252), 3: None, 4: None}, '9': {0: (0.46987951807228917, 0.09604130808950086), 1: (0.4943820224719101, 0.17354200107009102), 2: (0.8333333333333334, 0.19444444444444445), 3: None, 4: None}, 'T': {0: (0.35365853658536583, 0.09854976928147662), 1: (0.4642857142857143, 0.08599337170765742), 2: (0.26666666666666666, 0.22804359383306752), 3: None, 4: None}, 'J': {0: (0.4250000000000001, 0.10297619047619047), 1: (0.4819277108433735, 0.1134779802439572), 2: (0.6, 0.3985714285714286), 3: None, 4: None}, 'Q': {0: (0.48936170212765956, 0.11198208286674129), 1: (0.45918367346938777, 0.10537022501308217), 2: (0.47058823529411764, 0.033155080213903745), 3: None, 4: None}, 'K': {0: (0.4823529411764706, 0.12764705882352936), 1: (0.5058823529411766, 0.12212885154061623), 2: (0.4, 0.2256980056980057), 3: None, 4: None}}, 5: {'A': {0: (0.5714285714285714, 0.0), 1: (0.47058823529411764, 0.058823529411764705), 2: (0.2, 0.2), 3: (1.0, 1.0), 4: None}, '2': {0: (1.0, 0.0), 1: (0.6, 0.25), 2: (0.6923076923076923, 0.07692307692307693), 3: (1.0, 1.0), 4: None}, '3': {0: (0.5, 0.0), 1: (0.7083333333333334, 0.16666666666666666), 2: (0.38461538461538464, 0.07692307692307693), 3: None, 4: None}, '4': {0: (0.375, 0.0), 1: (0.5217391304347826, 0.17391304347826086), 2: (0.6923076923076923, 0.15384615384615385), 3: None, 4: None}, '5': {0: (0.625, 0.0), 1: (0.7727272727272727, 0.13636363636363635), 2: (0.6666666666666666, 0.0), 3: (1.0, 1.0), 4: None}, '6': {0: (0.6923076923076923, 0.13186813186813187), 1: (0.6896551724137929, 0.1724137931034483), 2: (0.35714285714285715, 0.14285714285714285), 3: None, 4: None}, '7': {0: (0.8, 0.06666666666666667), 1: (0.8148148148148148, 0.1111111111111111), 2: (0.7333333333333333, 0.13333333333333333), 3: (0.5, 0.0), 4: None}, '8': {0: (1.0, 0.18181818181818182), 1: (0.7142857142857143, 0.09523809523809523), 2: (0.7272727272727273, 0.0), 3: (1.0, 0.0), 4: None}, '9': {0: (0.5714285714285714, 0.2857142857142857), 1: (0.45, 0.2), 2: (0.5, 0.0), 3: None, 4: None}, 'T': {0: (0.16666666666666666, 0.3333333333333333), 1: (0.42857142857142855, 0.2110389610389611), 2: (0.5454545454545454, 0.0), 3: None, 4: None}, 'J': {0: (0.2222222222222222, 0.1111111111111111), 1: (0.43478260869565216, 0.21739130434782608), 2: (0.7, 0.1), 3: None, 4: None}, 'Q': {0: (0.14285714285714285, 0.0), 1: (0.38461538461538464, 0.07692307692307693), 2: (0.36363636363636365, 0.2727272727272727), 3: None, 4: None}, 'K': {0: (0.6666666666666666, 0.16666666666666666), 1: (0.5, 0.0823529411764706), 2: (0.3076923076923077, 0.07692307692307693), 3: (0.0, 0.0), 4: None}}, 6: {'A': {0: None, 1: (0.25, 0.0), 2: (0.3333333333333333, 0.0), 3: None, 4: None}, '2': {0: (0.0, 0.0), 1: (0.3333333333333333, 0.0), 2: (1.0, 0.0), 3: None, 4: None}, '3': {0: (1.0, 1.0), 1: (0.0, 0.0), 2: (1.0, 0.0), 3: (0.6666666666666666, 0.6666666666666666), 4: None}, '4': {0: (1.0, 1.0), 1: None, 2: (0.5, 0.0), 3: (1.0, 0.0), 4: None}, '5': {0: None, 1: (1.0, 0.0), 2: (1.0, 0.0), 3: None, 4: None}, '6': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, '7': {0: None, 1: (0.5, 0.0), 2: (0.8, 0.0), 3: None, 4: None}, '8': {0: None, 1: (1.0, 1.0), 2: (0.5, 0.0), 3: None, 4: None}, '9': {0: None, 1: (0.75, 0.25), 2: (0.3333333333333333, 0.3333333333333333), 3: None, 4: None}, 'T': {0: None, 1: (1.0, 0.0), 2: (0.16666666666666666, 0.16666666666666666), 3: (0.0, 0.0), 4: None}, 'J': {0: (0.6666666666666666, 0.0), 1: (0.25, 0.25), 2: (0.4, 0.0), 3: (0.0, 0.0), 4: None}, 'Q': {0: (0.0, 0.0), 1: (0.25, 0.0), 2: (0.3333333333333333, 0.3333333333333333), 3: (1.0, 0.0), 4: None}, 'K': {0: None, 1: (0.25, 0.0), 2: (0.5, 0.25), 3: None, 4: None}}}, 20: {2: {'A': {0: (0.5184426229508189, 0.045081967213114756), 1: (0.5000000000000001, 0.2944727660534947), 2: None, 3: None, 4: None}, '2': {0: (0.7867203219315896, 0.058350100603621745), 1: (0.7246376811594203, 0.5127917388711748), 2: None, 3: None, 4: None}, '3': {0: (0.7447698744769872, 0.06066945606694561), 1: (0.7567567567567568, 0.5549023944232132), 2: None, 3: None, 4: None}, '4': {0: (0.7835497835497837, 0.0541125541125541), 1: (0.8, 0.5922963140394927), 2: None, 3: None, 4: None}, '5': {0: (0.7829457364341083, 0.09689922480620156), 1: (0.7500000000000001, 0.6084696961654891), 2: None, 3: None, 4: None}, '6': {0: (0.7785087719298246, 0.07894736842105267), 1: (0.855072463768116, 0.632457598067964), 2: None, 3: None, 4: None}, '7': {0: (0.8224101479915433, 0.06342494714587736), 1: (0.9047619047619048, 0.5918703201321374), 2: None, 3: None, 4: None}, '8': {0: (0.87, 0.07200000000000009), 1: (0.8, 0.5702396249913996), 2: None, 3: None, 4: None}, '9': {0: (0.790224032586558, 0.06517311608961299), 1: (0.8, 0.4969518809022332), 2: None, 3: None, 4: None}, 'T': {0: (0.5995575221238946, 0.0641592920353982), 1: (0.6363636363636364, 0.4223573758060763), 2: None, 3: None, 4: None}, 'J': {0: (0.543181818181818, 0.10227272727272728), 1: (0.5606060606060606, 0.4200904349110166), 2: None, 3: None, 4: None}, 'Q': {0: (0.5154394299287404, 0.06888361045130634), 1: (0.6333333333333333, 0.4205722409245637), 2: None, 3: None, 4: None}, 'K': {0: (0.5568445475638043, 0.0788863109048724), 1: (0.47368421052631576, 0.3772982144197636), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.5045871559633031, 0.048929663608562705), 1: (0.5, 0.15396588042554105), 2: (1.0, 0.2857142857142857), 3: None, 4: None}, '2': {0: (0.7653846153846153, 0.08076923076923076), 1: (0.7565217391304347, 0.24558228735705556), 2: (0.7692307692307693, 0.5716227092745311), 3: None, 4: None}, '3': {0: (0.7642585551330798, 0.07984790874524718), 1: (0.7946428571428571, 0.3085597297611048), 2: (0.5, 0.5150620077090665), 3: None, 4: None}, '4': {0: (0.8051470588235294, 0.07352941176470588), 1: (0.7978723404255319, 0.2586341941538615), 2: (0.8, 0.7458333333333333), 3: None, 4: None}, '5': {0: (0.7727272727272725, 0.05303030303030303), 1: (0.7959183673469388, 0.27064388394333116), 2: (0.7142857142857143, 0.5526077097505668), 3: None, 4: None}, '6': {0: (0.7862595419847326, 0.10305343511450382), 1: (0.8461538461538463, 0.2865900503777248), 2: (1.0, 0.7173971861471862), 3: None, 4: None}, '7': {0: (0.8359374999999999, 0.09375000000000004), 1: (0.8037383177570093, 0.29778447564350374), 2: (0.6, 0.647008547008547), 3: None, 4: None}, '8': {0: (0.8706293706293705, 0.06293706293706296), 1: (0.8951612903225806, 0.25077932207850595), 2: (1.0, 0.5324695366362033), 3: None, 4: None}, '9': {0: (0.7692307692307693, 0.09890109890109891), 1: (0.855072463768116, 0.3475894325489754), 2: (0.8, 0.7187394957983193), 3: None, 4: None}, 'T': {0: (0.5392491467576791, 0.0716723549488055), 1: (0.49473684210526314, 0.19185524511681426), 2: (0.5, 0.4969038138894598), 3: None, 4: None}, 'J': {0: (0.5283018867924532, 0.07924528301886792), 1: (0.610619469026549, 0.24758309902027878), 2: (0.75, 0.5733630952380953), 3: None, 4: None}, 'Q': {0: (0.5429553264604821, 0.06529209621993125), 1: (0.5744680851063829, 0.2602378935707468), 2: (0.625, 0.4719542712189771), 3: None, 4: None}, 'K': {0: (0.5098814229249017, 0.09090909090909097), 1: (0.5154639175257731, 0.20557747563112555), 2: (1.0, 0.36684565434565436), 3: None, 4: None}}, 4: {'A': {0: (0.49999999999999994, 0.06249999999999999), 1: (0.4520547945205479, 0.1134367136160695), 2: (0.42857142857142855, 0.08571428571428573), 3: None, 4: None}, '2': {0: (0.7857142857142854, 0.0476190476190476), 1: (0.7899999999999998, 0.07004761904761905), 2: (0.8181818181818182, 0.17224880382775115), 3: None, 4: None}, '3': {0: (0.775, 0.075), 1: (0.8061224489795918, 0.08331665999733225), 2: (0.5882352941176471, 0.0261437908496732), 3: None, 4: None}, '4': {0: (0.77, 0.09), 1: (0.7619047619047619, 0.06573498964803312), 2: (0.875, 0.3), 3: None, 4: None}, '5': {0: (0.6956521739130432, 0.06521739130434782), 1: (0.7766990291262136, 0.13196822594880847), 2: (0.625, 0.28179824561403505), 3: (1.0, 1.0), 4: None}, '6': {0: (0.8461538461538461, 0.06730769230769232), 1: (0.8181818181818182, 0.14273958799820877), 2: (0.9090909090909091, 0.26666666666666666), 3: None, 4: None}, '7': {0: (0.8952380952380953, 0.0761904761904762), 1: (0.8865979381443299, 0.07949125390796578), 2: (0.7692307692307693, 0.3076923076923077), 3: None, 4: None}, '8': {0: (0.925531914893617, 0.0851063829787234), 1: (0.8118811881188119, 0.11969361682712044), 2: (0.8333333333333334, 0.21759259259259256), 3: None, 4: None}, '9': {0: (0.8415841584158416, 0.11881188118811879), 1: (0.8256880733944955, 0.06948861536017492), 2: (1.0, 0.14545454545454542), 3: (1.0, 1.0), 4: None}, 'T': {0: (0.4761904761904763, 0.023809523809523808), 1: (0.5225225225225224, 0.08501237724210696), 2: (0.6428571428571429, 0.1043956043956044), 3: None, 4: None}, 'J': {0: (0.6516853932584268, 0.07865168539325844), 1: (0.5943396226415091, 0.06855065139263249), 2: (0.6875, 0.0874404761904762), 3: None, 4: None}, 'Q': {0: (0.5809523809523807, 0.05714285714285714), 1: (0.5531914893617019, 0.05064856289660318), 2: (0.6923076923076923, 0.3589743589743589), 3: None, 4: None}, 'K': {0: (0.5378151260504204, 0.09243697478991594), 1: (0.5526315789473685, 0.10831339712918661), 2: (0.6, 0.23904761904761904), 3: (1.0, 1.0), 4: None}}, 5: {'A': {0: (0.6, 0.06666666666666667), 1: (0.5161290322580645, 0.0), 2: (1.0, 0.5), 3: (1.0, 1.0), 4: None}, '2': {0: (0.5714285714285714, 0.14285714285714285), 1: (0.5714285714285714, 0.09523809523809523), 2: (0.9473684210526315, 0.0), 3: (0.0, 0.0), 4: None}, '3': {0: (0.8181818181818182, 0.09090909090909091), 1: (0.7352941176470589, 0.0), 2: (0.6666666666666666, 0.06349206349206349), 3: (1.0, 1.0), 4: None}, '4': {0: (0.9, 0.0), 1: (0.84, 0.08), 2: (0.9, 0.1), 3: None, 4: None}, '5': {0: (0.85, 0.15), 1: (0.84, 0.08), 2: (0.8421052631578947, 0.0), 3: (1.0, 0.5), 4: None}, '6': {0: (0.6923076923076923, 0.15384615384615385), 1: (0.8333333333333334, 0.03333333333333333), 2: (0.7142857142857143, 0.14285714285714285), 3: (1.0, 0.0), 4: None}, '7': {0: (0.7777777777777778, 0.05555555555555555), 1: (0.868421052631579, 0.15789473684210525), 2: (0.8, 0.06666666666666667), 3: (1.0, 1.0), 4: None}, '8': {0: (0.8888888888888888, 0.0), 1: (0.967741935483871, 0.0967741935483871), 2: (0.9444444444444444, 0.0), 3: (1.0, 0.0), 4: None}, '9': {0: (0.8461538461538461, 0.15384615384615385), 1: (0.8285714285714286, 0.11428571428571428), 2: (0.9333333333333333, 0.0), 3: (1.0, 0.0), 4: None}, 'T': {0: (0.36363636363636365, 0.0), 1: (0.5135135135135135, 0.13513513513513514), 2: (0.23076923076923078, 0.0), 3: (1.0, 0.0), 4: None}, 'J': {0: (0.5, 0.07142857142857142), 1: (0.5238095238095238, 0.023809523809523808), 2: (0.7142857142857143, 0.14285714285714285), 3: None, 4: None}, 'Q': {0: (0.5384615384615384, 0.07692307692307693), 1: (0.5526315789473685, 0.10526315789473684), 2: (0.5333333333333333, 0.13333333333333333), 3: (0.0, 0.0), 4: None}, 'K': {0: (0.7368421052631579, 0.05263157894736842), 1: (0.55, 0.1), 2: (0.6428571428571429, 0.0), 3: (1.0, 0.0), 4: None}}, 6: {'A': {0: None, 1: (0.6666666666666666, 0.3333333333333333), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}, '2': {0: None, 1: (0.8, 0.4), 2: (1.0, 0.0), 3: (0.0, 0.0), 4: None}, '3': {0: None, 1: (0.5, 0.5), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}, '4': {0: None, 1: (0.7142857142857143, 0.14285714285714285), 2: (1.0, 0.0), 3: (1.0, 1.0), 4: None}, '5': {0: (1.0, 0.0), 1: (0.75, 0.0), 2: (0.5, 0.0), 3: None, 4: None}, '6': {0: (1.0, 0.0), 1: (0.7142857142857143, 0.2857142857142857), 2: (0.5, 0.0), 3: None, 4: None}, '7': {0: None, 1: (0.6666666666666666, 0.3333333333333333), 2: (1.0, 0.0), 3: None, 4: None}, '8': {0: None, 1: (1.0, 0.25), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}, '9': {0: (1.0, 0.0), 1: (1.0, 0.0), 2: (1.0, 0.25), 3: None, 4: None}, 'T': {0: None, 1: (0.5, 0.125), 2: (0.7272727272727273, 0.0), 3: (1.0, 0.0), 4: None}, 'J': {0: (0.5, 0.0), 1: (0.8, 0.2), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}, 'Q': {0: None, 1: (0.0, 0.0), 2: None, 3: (1.0, 0.0), 4: None}, 'K': {0: (1.0, 0.0), 1: (0.4, 0.0), 2: (0.6, 0.0), 3: None, 4: None}}}}`
