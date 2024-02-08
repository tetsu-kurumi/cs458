## Summary output of 100000 trials
Win rate over 100000 trials: 43.389%

## Code Explanation
* `__init__(self)`
    Initializes a matrix (in the form of a nested dictionary) which takes in as input 
    the player hand's value, player hand's number of cards, and number of aces in the player's hand,
    and sets a boolean value as the output (which is returned when the hitme function performs a matrix lookup).
    Additionally, in this program, the initial strategy when there is no data point available is to Stand.

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
        The only exceptions are when there have been no simulations done for a certain cell. In this case, due to the lack of data, the function falls back to the default strategy, which is to Stand, and assigns False.
* `do_stand(self, dealerhand, playerhand)` 
    This function simply returns (win = 1, loss = 0) if the player would win and (win = 0, loss = 1) if the player would lose in the given state when chosing to stand. 
    
* `do_hit(self, deck, dealerhand, playerhand, percentage_matrix, num_of_cards, face_card_rank, ace_count, sim_num_matrix)`
    This function simulates the scenario where the player hits. As explained in the `sim` function section, deals a hand to simulate a hit.If this makes the player go bust, it returns (win = 0, loss = 1). If not, the function looksup if this updates state has been simulated before. If it has, it propagates the probability previously stored, and if not, it defaults falls back to the initial strategy, which is to Stand and returns the simulated result.
    """

* `hitme(self, playerhand: Type[Hand], dealerfacecard: Type[Card]) -> bool` 
    This function first checks if the input playerhand has a value of 21 or larger or 7 or more cards (since this does not exist in the lookup table). If this is the case, the function returns False, which is the initial strategy. Otherwise, the function looks up the given state in the lookup table defined in `self.matrix`, and returns the corresponding boolean value.

* `play(self, trials: int) -> float` 
    This function first checks if `self.matrix` has been defined or not, and if not, throws an error.
    Then, it simulates a black jack game play for the iteration number defined by `trials` and records the number of times that the player wins, and lastly returns the win proportion against the number of trials.


## Simulation Output 
### Decision Matrix (original appended at the end):
<pre>

player hand value: 2
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
player hand value: 3
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
player hand value: 4
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
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
player hand value: 5
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
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
player hand value: 6
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
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
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
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
        ace count 0: True
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
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
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
player hand value: 7
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
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
player hand value: 8
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: True
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
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
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
player hand value: 9
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 4
      face card rank: A
        ace count 0: True
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
        ace count 0: True
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
        ace count 0: True
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
player hand value: 10
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
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
        ace count 0: True
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
        ace count 0: True
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
player hand value: 11
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
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
player hand value: 12
    num of cards: 2
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: True
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
        ace count 2: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: True
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
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
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
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
    num of cards: 4
      face card rank: A
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: True
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
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
        ace count 1: True
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
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
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
        ace count 3: True
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
player hand value: 13
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
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: True
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
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: False
      face card rank: J
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 4
      face card rank: A
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 4
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 5
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: True
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
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
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: True
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
        ace count 3: True
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
        ace count 2: True
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
player hand value: 14
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
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
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
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: True
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
        ace count 2: True
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
        ace count 2: True
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
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: True
        ace count 2: True
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
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 3
        ace count 0: True
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
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 6
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: True
        ace count 1: True
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
        ace count 0: True
        ace count 1: True
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
        ace count 3: True
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
        ace count 2: True
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
        ace count 1: False
        ace count 2: True
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
        ace count 3: True
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: True
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
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 6
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
        ace count 3: True
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
        ace count 3: True
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
        ace count 3: True
        ace count 4: False
player hand value: 15
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
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
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
        ace count 0: True
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
        ace count 0: True
        ace count 1: True
        ace count 2: True
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
        ace count 1: True
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
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 7
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: True
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
        ace count 0: True
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
    num of cards: 4
      face card rank: A
        ace count 0: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
        ace count 1: True
        ace count 2: True
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
        ace count 2: True
        ace count 3: True
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
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
    num of cards: 5
      face card rank: A
        ace count 0: False
        ace count 1: True
        ace count 2: False
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
        ace count 3: True
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
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: True
        ace count 2: True
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
player hand value: 16
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
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
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
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 3
      face card rank: A
        ace count 0: True
        ace count 1: False
        ace count 2: True
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
        ace count 2: True
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
        ace count 0: True
        ace count 1: True
        ace count 2: True
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
        ace count 2: True
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
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
    num of cards: 4
      face card rank: A
        ace count 0: False
        ace count 1: True
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 2
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
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
        ace count 0: True
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
        ace count 3: True
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: Q
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: True
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
        ace count 1: True
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
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: T
        ace count 0: False
        ace count 1: True
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
        ace count 1: True
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
player hand value: 17
    num of cards: 2
      face card rank: A
        ace count 0: False
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
        ace count 0: True
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: True
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
        ace count 0: True
        ace count 1: True
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
        ace count 1: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: True
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
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
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: J
        ace count 0: False
        ace count 1: False
        ace count 2: False
        ace count 3: True
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
        ace count 0: True
        ace count 1: True
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
        ace count 1: True
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
        ace count 0: True
        ace count 1: False
        ace count 2: True
        ace count 3: False
        ace count 4: False
      face card rank: 9
        ace count 0: False
        ace count 1: False
        ace count 2: True
        ace count 3: True
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
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: K
        ace count 0: False
        ace count 1: True
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
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
      face card rank: 8
        ace count 0: False
        ace count 1: False
        ace count 2: True
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
        ace count 1: True
        ace count 2: False
        ace count 3: False
        ace count 4: False
player hand value: 18
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
        ace count 1: True
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
        ace count 2: True
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
        ace count 2: True
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
        ace count 0: True
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
        ace count 2: True
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
        ace count 2: True
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
        ace count 3: True
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
        ace count 2: True
        ace count 3: True
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
        ace count 1: True
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
        ace count 0: True
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
</pre>

### Percentage Matrix (original appended at the end):
<pre>
player hand value: 2
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 3
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 4
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13333333333333333, 0.23903833913017072), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.38461538461538464, 0.4541194819403468), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.44, 0.49523368674158846), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6842105263157895, 0.47539332325286027), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.5232636075296768), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.47058823529411764, 0.5072070514602947), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24, 0.39606311137093114), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.3767314925592427), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15384615384615385, 0.42031313603836473), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.041666666666666664, 0.22589992783647814), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13043478260869565, 0.34840586269670165), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19047619047619047, 0.29481670154808404), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.10344827586206896, 0.29820765133592286), 1: None, 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 5
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.11864406779661016, 0.177804272969106), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.35714285714285715, 0.39637155707300015), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34782608695652173, 0.5099049340066099), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4583333333333333, 0.47089127726032715), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.38181818181818183, 0.5250717482487127), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3888888888888889, 0.457423806873279), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.28378378378378377, 0.40899453622905474), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20634920634920634, 0.39392388745601925), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15384615384615385, 0.38575228321695815), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18840579710144928, 0.27691582219885724), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2459016393442623, 0.31643899544988907), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.35294117647058826, 0.29384537780770953), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.29545454545454547, 0.29479553757714005), 1: None, 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 6
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.06944444444444445, 0.17290503720707878), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3090909090909091, 0.4161162603841784), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3142857142857143, 0.4581228079006277), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.375, 0.45112891398170646), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4444444444444444, 0.5120771228285294), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.38095238095238093, 0.46388903579569324), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.31645569620253156, 0.40197799335172046), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25423728813559326, 0.37897749174603035), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.31578947368421045, 0.32842290469127744), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19480519480519481, 0.27150260103649065), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16883116883116883, 0.30760699379302164), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.29460455582025186), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2875, 0.3040119497570522), 1: None, 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.5), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.175), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.4444444444444444), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.5185185185185185), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.18162393162393164), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.4666666666666666), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.3046875), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 7
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.11851851851851856, 0.18446525130040756), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3557692307692308, 0.42175996517675507), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.41414141414141414, 0.4174858326281017), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4787234042553193, 0.4669902098482544), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.44, 0.5188893837771856), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3947368421052632, 0.5034383839941022), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.28057553956834536, 0.40230076758688155), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.256637168141593, 0.3920450139880368), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19327731092436976, 0.35467654496280027), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22900763358778628, 0.2759134901579947), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16666666666666666, 0.28177875457491464), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15315315315315314, 0.2868883905743196), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.30188679245283034, 0.286222999615228), 1: None, 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1111111111111111, 0.18375074871336017), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.5733333333333334), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.3833333333333333), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.13793103448275862), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.5481268799562483), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.4284089854265292), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.47619064143876183), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.30238095238095236), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.22580645161290322), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.21819580491307247), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.4946581196581197), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.24007936507936506), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.2276107317927171), 1: None, 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 8
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1260504201680674, 0.20384742971049094), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.32786885245901654, 0.45138048376766143), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3650793650793651, 0.4735977184148374), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3787878787878788, 0.5142752697073047), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4833333333333332, 0.5382681930168046), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3983739837398374, 0.5274596073999488), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.4990934155985208), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2753623188405798, 0.4309503473474027), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.26356589147286813, 0.391941695434892), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1875, 0.2975842421863591), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1736111111111111, 0.33653719230178053), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15107913669064757, 0.2936893103346056), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21604938271604937, 0.3240295146489123), 1: None, 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.20408163265306123), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.46593468468468463), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.6635869565217392), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5454545454545454, 0.5357110405836044), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7619047619047619, 0.5538022494544232), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.36363636363636365, 0.582468568114501), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23076923076923078, 0.48030384498863393), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.3717861926391801), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.3514531698201111), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.14285714285714285, 0.21442670232992816), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15384615384615385, 0.4149241938166869), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18181818181818182, 0.28333803877282143), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.14285714285714285, 0.3149638802889577), 1: None, 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 9
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13020833333333334, 0.277177373843008), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.27397260273972596, 0.515073138143368), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3959731543624161, 0.5314525277247333), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.46206896551724136, 0.5577719162323224), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4046242774566474, 0.5873802022266021), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4318181818181818, 0.5610867204436993), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2635135135135135, 0.5870788167083062), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2650602409638554, 0.5467881736517427), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2122905027932961, 0.4047450515795757), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.17751479289940833, 0.3575410065395132), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.192090395480226, 0.35718073892112817), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20430107526881724, 0.3566117603025422), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2275449101796408, 0.36448772575819277), 1: None, 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15789473684210525, 0.2810322372669029), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.10526315789473684, 0.5426031976723941), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.5694763205828777), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.4191206705449585), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5882352941176471, 0.6501863354037266), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.6119417061171447), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16666666666666666, 0.5548557148106689), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.17391304347826086, 0.5517249550805906), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.09090909090909091, 0.484011579516098), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.34351067657519263), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2777777777777778, 0.35405419115573666), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3157894736842105, 0.380679682289439), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18518518518518517, 0.33624979763872215), 1: None, 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.5555555555555556), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.9166666666666667), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 1.0), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 10
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13513513513513514, 0.30310193379474093), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3485714285714287, 0.5805226295342225), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.40340909090909083, 0.6195861678046782), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.47398843930635837, 0.6015351152428632), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4072164948453608, 0.6171468726311236), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4606741573033707, 0.6137139585273333), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2662337662337662, 0.6355415885245231), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16574585635359126, 0.5681217208728527), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18041237113402064, 0.5507762031252192), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.26285714285714296, 0.43237904762547663), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19642857142857142, 0.42709339439783245), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19895287958115182, 0.41010013311620896), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25252525252525254, 0.42538591900868866), 1: None, 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.04, 0.2633740639755678), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2857142857142857, 0.6885859169145971), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.625, 0.665144025686202), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4074074074074074, 0.6223380671841926), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5294117647058824, 0.7258053221288514), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.42857142857142855, 0.635404072638463), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.6784583802722935), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15384615384615385, 0.6225982793954781), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24, 0.6979299938479723), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20689655172413793, 0.3793485147412033), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.11538461538461539, 0.4074810664632429), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2647058823529412, 0.4308299984804612), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.48580855428477565), 1: None, 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.07692307692307693), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.8571428571428571), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.3333333333333333), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.8333333333333334), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 1.0), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.4), 1: None, 2: None, 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 11
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13397129186602877, 0.3691705061214646), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.33170731707317075, 0.6104069233843824), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.32701421800947855, 0.5835459610539956), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.39252336448598124, 0.6564006157179855), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4343891402714932, 0.6706510221858538), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4263959390862944, 0.6168171174212859), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23076923076923078, 0.6108307849958705), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.27000000000000013, 0.6208349178890251), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23981900452488686, 0.5564170795731257), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.17727272727272728, 0.4717446798120193), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2318840579710145, 0.45568287488509496), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22869955156950691, 0.4984154213078719), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1863636363636364, 0.47698855438464255), 1: None, 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13953488372093023, 0.29026947533242337), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2857142857142857, 0.6093853002490438), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3448275862068966, 0.5866760957701017), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.44680851063829785, 0.5909631560911607), 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5714285714285714, 0.6591659272404614), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.43478260869565216, 0.7267614407108869), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16666666666666674, 0.6303758869365754), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.7056973200774846), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.33962264150943405, 0.6746835593000425), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.27272727272727276, 0.4619982467189612), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18421052631578946, 0.5924626685538109), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.5225566349148052), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3, 0.4354760919966702), 1: None, 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.41666666666666663), 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 1.0), 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 1.0), 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.5), 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.7), 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.7), 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.5416666666666666), 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.6875), 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 1.0), 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.375), 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: None, 2: None, 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 12
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13493975903614455, 0.1624061318298178), 1: None, 2: (0.0, 0.2861190025252526), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.36781609195402293, 0.349454463066593), 1: None, 2: (0.5238095238095238, 0.7062794348508635), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3900709219858156, 0.34899316438820377), 1: None, 2: (0.4, 0.6026038386564703), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4070080862533694, 0.3755361224626114), 1: None, 2: (0.47058823529411764, 0.5509612269816353), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4593967517401392, 0.4159446846696459), 1: None, 2: (0.375, 0.6084110122681551), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4117647058823528, 0.38480040454037095), 1: None, 2: (0.5, 0.5820887445887446), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22015915119363394, 0.36138111858720345), 1: None, 2: (0.3333333333333333, 0.5732690445743515), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20947630922693275, 0.32250654659585926), 1: None, 2: (0.34782608695652173, 0.5012884292935444), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1926121372031661, 0.27167362099957426), 1: None, 2: (0.0, 0.3917821450141018), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20518867924528306, 0.2735660089794683), 1: None, 2: (0.2, 0.5020792915931804), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2026315789473684, 0.2778691701275279), 1: None, 2: (0.22727272727272727, 0.49391905685611975), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20243902439024397, 0.23505269262078513), 1: None, 2: (0.2916666666666667, 0.38743059092323806), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20460358056265987, 0.29379192857730296), 1: None, 2: (0.3333333333333333, 0.5292749134095802), 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1320754716981132, 0.23407870298918673), 1: (0.11363636363636363, 0.21373546394599438), 2: (0.09090909090909091, 0.12954545454545457), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.3441944429821925), 1: (0.37735849056603776, 0.30044561102419526), 2: (0.46153846153846156, 0.2807692307692308), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.45454545454545453, 0.3832404222179891), 1: (0.37254901960784315, 0.2740223749986086), 2: (0.21052631578947367, 0.4532485058800849), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.41153915681541703), 1: (0.38596491228070173, 0.3488886289989283), 2: (0.2727272727272727, 0.41025641025641024), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3695652173913043, 0.45497454293643746), 1: (0.5399999999999999, 0.3441212492594758), 2: (0.47619047619047616, 0.32668178382464097), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.41071428571428575, 0.4208048913692097), 1: (0.4444444444444444, 0.44141689754199415), 2: (0.42857142857142855, 0.39360639360639355), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34545454545454546, 0.33485490688137093), 1: (0.33962264150943394, 0.3122948840008997), 2: (0.08695652173913043, 0.30916149068322973), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22058823529411764, 0.3445109236284476), 1: (0.14814814814814808, 0.23995897735269547), 2: (0.17647058823529413, 0.3267188693659282), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.14035087719298245, 0.34048711253617653), 1: (0.3148148148148148, 0.31849205954793913), 2: (0.2222222222222222, 0.24642246256829584), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.14814814814814808, 0.25855046248119107), 1: (0.15789473684210534, 0.23453055710717272), 2: (0.35, 0.4713734567901235), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21875, 0.28844186374468067), 1: (0.16666666666666674, 0.308773353642378), 2: (0.07692307692307693, 0.3106156663848971), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13114754098360656, 0.2825062411200628), 1: (0.31578947368421056, 0.20416177348955056), 2: (0.20833333333333334, 0.37637774806892454), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.27450980392156865, 0.39791346100922786), 1: (0.19696969696969696, 0.28416209349009636), 2: (0.2857142857142857, 0.37576177999110333), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.16666666666666666, 0.2909356725146199), 2: (0.0, 0.3333333333333333), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.3333333333333333, 0.3046128707893414), 2: (0.3333333333333333, 0.5555555555555555), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.41666666666666663), 1: (0.1875, 0.3794356684981685), 2: (0.0, 0.25), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.4117647058823529, 0.3169550173010381), 2: (0.5, 0.40909090909090917), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.5), 1: (0.4444444444444444, 0.6230271785827342), 2: (0.4, 0.42000000000000004), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.48888888888888893), 1: (0.4117647058823529, 0.43613445378151267), 2: (0.8, 0.5035714285714286), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.375, 0.5666666666666667), 1: (0.46153846153846156, 0.2863834883065652), 2: (0.25, 0.40183823529411766), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.5), 1: (0.35714285714285715, 0.4886457214464734), 2: (0.5454545454545454, 0.30383707201889015), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16666666666666666, 0.3632478632478633), 1: (0.125, 0.2916666666666667), 2: (0.5714285714285714, 0.19047619047619047), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.375), 1: (0.3125, 0.11119505494505494), 2: (0.25, 0.1375), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.2777777777777778, 0.2750301195747116), 2: (0.0, 0.10416666666666666), 3: (1.0, 1.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.10416666666666667), 1: (0.25, 0.14285714285714282), 2: (0.3333333333333333, 0.39166666666666666), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.2333333333333333), 1: (0.4375, 0.3762517507002801), 2: (0.2857142857142857, 0.5227272727272727), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.25), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.6666666666666666), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.5), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (1.0, 1.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: None, 3: (1.0, 0.0), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (0.0, 0.5), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (1.0, 1.0), 3: (1.0, 0.3333333333333333), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.5), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.5), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: None, 2: None, 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 13
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1457800511508951, 0.16811079634030876), 1: (0.09615384615384616, 0.2377840100924787), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3676092544987147, 0.289553358247112), 1: (0.276595744680851, 0.4738966203485043), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4066666666666666, 0.3475105697286562), 1: (0.3582089552238806, 0.5242336317080695), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3963254593175853, 0.35242619005124626), 1: (0.42, 0.48213780975233933), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.47733333333333333, 0.3430329213934929), 1: (0.3448275862068966, 0.5217510694666213), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4190981432360744, 0.35317517102778373), 1: (0.4230769230769231, 0.500666573398387), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25336927223719674, 0.33244153213932826), 1: (0.21311475409836064, 0.4528041762684749), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21563342318059292, 0.309969292830035), 1: (0.3050847457627119, 0.41105997187065463), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2537688442211054, 0.30083502057673983), 1: (0.26666666666666666, 0.41397322912898754), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21293800539083557, 0.24160110408298632), 1: (0.3333333333333333, 0.4430095139441714), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.208219178082192, 0.22682316649899695), 1: (0.1690140845070422, 0.33530953148415077), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25000000000000006, 0.23781447083820548), 1: (0.17307692307692307, 0.3353516972995153), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2270408163265306, 0.256404947938174), 1: (0.23728813559322032, 0.3733031215928433), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.07228915662650602, 0.16810195006249898), 1: (0.14754098360655737, 0.1534168162473828), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4375, 0.3631671408391744), 1: (0.3604651162790699, 0.3425059209867096), 2: None, 3: (1.0, 1.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4000000000000001, 0.2907398037260242), 1: (0.37037037037037035, 0.35446572608506544), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.31428571428571433, 0.41203652870480767), 1: (0.38144329896907225, 0.3073110467360126), 2: None, 3: (0.0, 1.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5254237288135596, 0.24072595360915175), 1: (0.40909090909090917, 0.3815540409676224), 2: None, 3: (0.3333333333333333, 0.3333333333333333), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4142857142857143, 0.3038240528858378), 1: (0.37500000000000006, 0.36049488457018686), 2: None, 3: (0.0, 0.0), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1917808219178082, 0.3245238448771549), 1: (0.3076923076923078, 0.27662716087308437), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2222222222222222, 0.4088740678925722), 1: (0.26804123711340205, 0.35294849727041844), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2558139534883721, 0.3017455061046825), 1: (0.19000000000000003, 0.3543056978496098), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24050632911392406, 0.26039631361684373), 1: (0.2127659574468085, 0.2622237159336539), 2: None, 3: (0.0, 1.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2235294117647059, 0.290397569909765), 1: (0.23853211009174308, 0.29190141435940864), 2: None, 3: (1.0, 0.25), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16417910447761194, 0.31662396519263314), 1: (0.19801980198019803, 0.26483932329194615), 2: None, 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.17948717948717952, 0.31226697905465434), 1: (0.14705882352941185, 0.262658588371095), 2: None, 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.125, 0.1076923076923077), 1: (0.0, 0.08198273461431357), 2: (0.25, 0.65), 3: (0.0, 0.0), 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.25), 1: (0.3125, 0.484876979638009), 2: (0.0, 0.5317460317460317), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.2333333333333333), 1: (0.625, 0.4031192765567766), 2: (0.16666666666666666, 0.27777777777777773), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.5833333333333334), 1: (0.6842105263157895, 0.450735294117647), 2: (0.42857142857142855, 0.4884353741496598), 3: (1.0, 1.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6, 0.6020833333333333), 1: (0.4782608695652174, 0.49069813143039676), 2: (0.6666666666666666, 0.6666666666666666), 3: (0.0, 0.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.5222222222222223), 1: (0.4, 0.3346666666666666), 2: (0.6666666666666666, 0.2604166666666667), 3: (0.0, 0.0), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.5962962962962962), 1: (0.2222222222222222, 0.21544312169312174), 2: (0.2, 0.6729411764705882), 3: (0.5, 0.5), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.125, 0.3125), 1: (0.21739130434782608, 0.25381989180111403), 2: (0.1111111111111111, 0.380952380952381), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1, 0.42628205128205127), 1: (0.23076923076923078, 0.31102564102564106), 2: (0.4, 0.1875), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.21428571428571427), 1: (0.18181818181818182, 0.18766418766418766), 2: (0.25, 0.125), 3: (0.0, 1.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.125, 0.0), 1: (0.14285714285714285, 0.17846751603867353), 2: (0.0, 0.20340909090909093), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2857142857142857, 0.21428571428571425), 1: (0.08, 0.3233492781728075), 2: (0.42857142857142855, 0.41666666666666663), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16666666666666666, 0.2333333333333333), 1: (0.28, 0.220563025210084), 2: (0.2857142857142857, 0.5170454545454545), 3: (0.0, 1.0), 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (1.0, 0.6666666666666666), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.5, 0.75), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: (0.0, 0.2), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.75, 0.4), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.5), 2: (0.75, 0.5), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.6666666666666666, 0.6666666666666666), 2: (0.5, 0.5), 3: (1.0, 1.0), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.6666666666666666), 2: (0.5, 0.375), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 1.0), 2: (0.0, 0.9), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 1.0), 2: (0.6666666666666666, 0.0), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: None, 2: (0.2, 0.2), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.5, 0.8333333333333333), 3: (0.0, 0.5), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.3333333333333333, 0.3333333333333333), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.0), 3: (0.0, 0.0), 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
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
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: (0.0, 0.0)}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.5, 0.5), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (1.0, 1.0), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 1.0), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
player hand value: 14
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.10029498525073749, 0.15795920043589795), 1: (0.16666666666666669, 0.26399948858194583), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34864864864864864, 0.3065079675651061), 1: (0.16666666666666666, 0.5030488861690712), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3537234042553193, 0.2616690812716671), 1: (0.34285714285714286, 0.5041184193052204), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3730407523510973, 0.2781591927974679), 1: (0.3793103448275862, 0.566523520480745), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.43413173652694603, 0.32296090608802874), 1: (0.3620689655172414, 0.634985413583946), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.46920821114369504, 0.3014952170242612), 1: (0.5079365079365081, 0.5230370502758297), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2556179775280899, 0.31070305820472066), 1: (0.36507936507936506, 0.4625044148612125), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2091836734693878, 0.2768209182181118), 1: (0.1935483870967742, 0.47607232779547165), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2664576802507841, 0.26019023695470217), 1: (0.2714285714285714, 0.4738719458865663), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19756838905775082, 0.1959301290389003), 1: (0.15094339622641503, 0.3559623625739031), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22222222222222218, 0.23007336168603876), 1: (0.2692307692307694, 0.3703665942449223), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18208092485549138, 0.21120208949142633), 1: (0.1538461538461538, 0.37173256544355265), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21388888888888888, 0.22993863014667898), 1: (0.2222222222222222, 0.33355152291982926), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13043478260869565, 0.1484534317159359), 1: (0.08064516129032255, 0.24707944777222976), 2: (0.0, 0.14583333333333334), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.351063829787234, 0.27895647800994294), 1: (0.35294117647058826, 0.31763350306828564), 2: (1.0, 0.7857142857142857), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.36274509803921573, 0.2790932094639949), 1: (0.3372093023255814, 0.33706177847926116), 2: (0.2, 0.6401709401709402), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4716981132075472, 0.2906484885220202), 1: (0.49462365591397855, 0.2718468574098521), 2: (0.2857142857142857, 0.4736313573048267), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5566037735849055, 0.26517540421164076), 1: (0.5454545454545454, 0.33258905272607436), 2: (0.2, 0.5054554334554334), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.41237113402061853, 0.3295851491306568), 1: (0.43037974683544306, 0.32617259727196557), 2: (0.7142857142857143, 0.6809523809523809), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.32558139534883723, 0.28206947309406427), 1: (0.2705882352941177, 0.32863551129393787), 2: (0.0, 0.7142857142857143), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23015873015873017, 0.31601839830341466), 1: (0.19753086419753085, 0.3140945055286802), 2: (0.25, 0.4419191919191919), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.256198347107438, 0.2638461115502647), 1: (0.3152173913043479, 0.2571901917034726), 2: (0.125, 0.3886422821969698), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1326530612244898, 0.18230015551397893), 1: (0.20652173913043478, 0.23752483621773654), 2: (0.6666666666666666, 0.5833333333333334), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19166666666666668, 0.2796706274755057), 1: (0.24418604651162795, 0.22198391165618572), 2: (0.0, 0.4337797619047619), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.16000000000000006, 0.21803601410427265), 1: (0.10869565217391308, 0.2692396751694578), 2: (0.0, 0.25917366946778714), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15384615384615383, 0.20802506575260127), 1: (0.13793103448275862, 0.2465747038795248), 2: (0.0, 0.5158067517278043), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.08333333333333333, 0.22364672364672367), 1: (0.0625, 0.10218253968253968), 2: (0.0, 0.09166666666666667), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.6875), 1: (0.3333333333333333, 0.43995098039215685), 2: (0.4, 0.1893162393162393), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.2), 1: (0.3181818181818182, 0.31255411255411253), 2: (0.4166666666666667, 0.22222222222222224), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7142857142857143, 0.2857142857142857), 1: (0.5384615384615384, 0.2424679487179487), 2: (0.2222222222222222, 0.41507936507936516), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5714285714285714, 0.3333333333333333), 1: (0.5652173913043478, 0.29567415379772355), 2: (0.3076923076923077, 0.3153846153846154), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5714285714285714, 0.37346938775510213), 1: (0.37037037037037035, 0.24216524216524224), 2: (0.5333333333333333, 0.31460317460317455), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.21428571428571427), 1: (0.21052631578947367, 0.3000771158665895), 2: (0.5, 0.4814705882352941), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1, 0.20357142857142857), 1: (0.2, 0.3390922158337019), 2: (0.4444444444444444, 0.1950937950937951), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23076923076923078, 0.34263172724711183), 1: (0.21052631578947367, 0.291812865497076), 2: (0.25, 0.2586016414141414), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.29411764705882354, 0.2698412698412698), 1: (0.5, 0.14399446707139013), 2: (0.125, 0.5381944444444444), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.03333333333333333), 1: (0.24, 0.18083744465528145), 2: (0.14285714285714285, 0.3154761904761904), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.08333333333333333, 0.3888888888888889), 1: (0.20833333333333334, 0.3588307117718883), 2: (0.1, 0.09833333333333334), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3, 0.06000000000000001), 1: (0.3448275862068966, 0.20938496088090403), 2: (0.3, 0.34326298701298696), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.0), 2: (0.0, 0.1111111111111111), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.3333333333333333, 0.3333333333333333), 2: (0.625, 0.1875), 3: (1.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.5), 2: None, 3: (0.0, 1.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.25, 0.0), 2: (1.0, 1.0), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.1875), 2: (0.5, 0.75), 3: (0.0, 0.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.3333333333333333, 0.3333333333333333), 2: (1.0, 0.5), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 1.0), 2: (0.42857142857142855, 0.4642857142857143), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.16666666666666666, 0.16666666666666666), 2: (0.0, 0.3333333333333333), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.16666666666666666, 0.07142857142857142), 2: (0.0, 0.25), 3: (0.0, 1.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.25), 2: (0.25, 0.25), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.4, 0.4), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.16666666666666666), 2: (0.125, 0.0625), 3: None, 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.5), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 1.0), 3: (0.0, 1.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 1.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 0.5), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 1.0), 4: None}
player hand value: 15
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1165644171779141, 0.12943843344314623), 1: (0.1111111111111111, 0.24953951094879606), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3507692307692309, 0.25988927920835675), 1: (0.41509433962264153, 0.46366780782038014), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.367741935483871, 0.26849337931380585), 1: (0.48214285714285715, 0.5670329908321975), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4112676056338027, 0.2761997131414014), 1: (0.4782608695652174, 0.42089844439552077), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.47104247104247116, 0.2870801679819527), 1: (0.4117647058823529, 0.5357450715739893), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4205882352941178, 0.2892104302585399), 1: (0.36538461538461536, 0.5328806449939775), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.26708074534161486, 0.2956486157102688), 1: (0.22448979591836735, 0.4140949122728382), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2521994134897361, 0.2384620182902445), 1: (0.2352941176470588, 0.436450607959769), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21854304635761584, 0.26097765455519223), 1: (0.2545454545454545, 0.3694062858538229), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22530864197530864, 0.21354312834251962), 1: (0.21428571428571427, 0.3173723669275531), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22418879056047197, 0.19746107484407469), 1: (0.30909090909090914, 0.32024154318766757), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20987654320987653, 0.1844918750812649), 1: (0.2028985507246377, 0.3591404986011309), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21269841269841266, 0.2097377657313938), 1: (0.273972602739726, 0.3966498632495503), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.08333333333333333, 0.11344789558595246), 1: (0.07352941176470588, 0.18324796385573924), 2: (0.0, 0.334375), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3191489361702128, 0.25293353876667546), 1: (0.3406593406593407, 0.2881499934531486), 2: (0.16666666666666666, 0.4257936507936508), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.41044776119402987, 0.27016013330574734), 1: (0.3917525773195876, 0.2954990288360975), 2: (0.0, 0.6296296296296297), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.43125, 0.2672948566039559), 1: (0.2191780821917808, 0.2629031974163996), 2: (0.6, 0.36668934240362816), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4388489208633093, 0.2590197159042951), 1: (0.37349397590361444, 0.2871380599069305), 2: (1.0, 0.42000000000000004), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.38666666666666677, 0.2723346154470358), 1: (0.4891304347826087, 0.34806775904976817), 2: (0.16666666666666666, 0.4361111111111111), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21897810218978106, 0.3344564644315924), 1: (0.2571428571428572, 0.2801436482811779), 2: (0.25, 0.6258377100840337), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.273972602739726, 0.3636072735629767), 1: (0.28865979381443296, 0.21519945328876774), 2: (0.3333333333333333, 0.5652657527657527), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2054794520547945, 0.19222800627746406), 1: (0.2261904761904762, 0.2531822159063055), 2: (0.16666666666666666, 0.606967106967107), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22560975609756098, 0.16303686047965302), 1: (0.2571428571428571, 0.22714770189152347), 2: (0.3333333333333333, 0.4448559670781893), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21794871794871795, 0.20903669761549684), 1: (0.21739130434782614, 0.2293898950568478), 2: (0.0, 0.46651785714285715), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19858156028368795, 0.2194094849792295), 1: (0.2112676056338028, 0.2276236728355281), 2: (0.0, 0.398051948051948), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18518518518518526, 0.23597681521257602), 1: (0.3529411764705883, 0.20413478299130602), 2: (0.0, 0.4125631313131313), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1111111111111111, 0.13675213675213677), 1: (0.14285714285714285, 0.1254724111866969), 2: (0.25, 0.1625), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3125, 0.20572916666666666), 1: (0.3333333333333333, 0.3019312468577174), 2: (0.25, 0.20141432641432644), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6, 0.46380952380952384), 1: (0.4444444444444444, 0.2629019129019129), 2: (0.4444444444444444, 0.35185185185185186), 3: (0.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.20777777777777778), 1: (0.40625, 0.2551011029411764), 2: (0.2857142857142857, 0.30612244897959184), 3: (0.5, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.35978835978835977), 1: (0.41379310344827586, 0.27527262010020637), 2: (0.5, 0.41), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4444444444444444, 0.30000000000000004), 1: (0.3548387096774194, 0.3440198511166253), 2: (0.25, 0.10892857142857143), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21428571428571427, 0.2384353741496599), 1: (0.3103448275862069, 0.1815981432360743), 2: (0.5, 0.22083333333333335), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.30312500000000003), 1: (0.25, 0.26708063608218413), 2: (0.3333333333333333, 0.44040404040404035), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.35294117647058826, 0.1583171730230554), 1: (0.15384615384615385, 0.21230769230769225), 2: (0.6666666666666666, 0.2121212121212121), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15384615384615385, 0.15140415140415142), 1: (0.13513513513513514, 0.1320778820778821), 2: (0.16666666666666666, 0.36234567901234566), 3: (0.0, 1.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23809523809523808, 0.025850340136054424), 1: (0.20000000000000004, 0.1802979829924801), 2: (0.5, 0.07575757575757576), 3: (1.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15625, 0.24435763888888887), 1: (0.1935483870967742, 0.2493389911795984), 2: (0.4, 0.1733333333333333), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4117647058823529, 0.21176470588235297), 1: (0.1724137931034483, 0.16174659518980009), 2: (0.18181818181818182, 0.1322314049586777), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.5), 1: (0.0, 0.16666666666666666), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 1.0), 1: (0.6666666666666666, 0.5555555555555555), 2: (0.6666666666666666, 0.3333333333333333), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.3333333333333333, 0.3333333333333333), 3: (0.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6666666666666666, 0.0), 2: (1.0, 0.5), 3: (0.5, 0.5), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.7142857142857143, 0.42857142857142855), 2: (0.5, 0.0), 3: (0.0, 0.3333333333333333), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.16666666666666666, 0.25), 2: (0.0, 0.3333333333333333), 3: (1.0, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.14285714285714285, 0.2857142857142857), 2: (0.25, 0.25), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.16666666666666666, 0.3333333333333333), 2: (1.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.14285714285714285), 2: (0.0, 0.2), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.16666666666666666), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.3333333333333333, 0.0), 2: (0.5, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.25, 0.16666666666666666), 2: None, 3: None, 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (1.0, 1.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.0), 3: None, 4: None}
player hand value: 16
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13559322033898308, 0.139367115799466), 1: (0.13157894736842105, 0.21934688433252403), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.35570469798657733, 0.26667487818565594), 1: (0.37288135593220345, 0.45283335713974987), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3786764705882352, 0.2659712797245578), 1: (0.28301886792452846, 0.509709867217395), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3401360544217686, 0.26025678799450797), 1: (0.42857142857142855, 0.524620698736469), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4444444444444444, 0.27592970952422624), 1: (0.4375, 0.5197612992174572), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.42276422764227645, 0.25722360638005926), 1: (0.375, 0.48746436952891753), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23566878980891712, 0.30169106417849323), 1: (0.2033898305084746, 0.44126074532293225), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20477815699658702, 0.2675224258820241), 1: (0.3275862068965517, 0.4749728072535179), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.24406779661016953, 0.2380456864475146), 1: (0.24999999999999997, 0.3840170657365381), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19780219780219788, 0.18455830545277027), 1: (0.23255813953488372, 0.36512296624796986), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21782178217821782, 0.18828181063720387), 1: (0.2857142857142857, 0.3461065615371211), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21212121212121218, 0.20926376087628454), 1: (0.2857142857142857, 0.35267349273503795), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20224719101123592, 0.21318815288996087), 1: (0.1836734693877551, 0.3592998081680904), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.08571428571428569, 0.11699752628324057), 1: (0.11475409836065571, 0.09505917893113223), 2: (0.0, 0.11111111111111112), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3624161073825504, 0.2181400752074261), 1: (0.2795698924731183, 0.3092997353231142), 2: (0.625, 0.5123015873015873), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3548387096774194, 0.27120988616438), 1: (0.4942528735632183, 0.25802275031589483), 2: (0.25, 0.5396825396825398), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.375, 0.18317112216130446), 1: (0.4666666666666667, 0.2569462766443898), 2: (0.25, 0.4158730158730159), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.37748344370860926, 0.20389464326493334), 1: (0.418918918918919, 0.30545225781506846), 2: (0.2857142857142857, 0.41931972789115646), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.43023255813953487, 0.25819124000367694), 1: (0.4222222222222222, 0.3036077101184029), 2: (0.3333333333333333, 0.6363636363636364), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.29518072289156616, 0.27234853306724455), 1: (0.3181818181818183, 0.2877487233197682), 2: (0.75, 0.5625), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22807017543859648, 0.2850247448490865), 1: (0.26315789473684215, 0.2743500976262132), 2: (0.25, 0.4642857142857142), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2545454545454545, 0.18926503741167175), 1: (0.17977528089887632, 0.23300591517620514), 2: (0.4, 0.398386994949495), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20588235294117646, 0.17671441799002932), 1: (0.1666666666666667, 0.22174214407040074), 2: (0.2857142857142857, 0.4143628747795414), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2413793103448276, 0.17042212685610506), 1: (0.18421052631578946, 0.2287178462063836), 2: (0.4, 0.3987587412587413), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21518987341772142, 0.17568955439835834), 1: (0.18627450980392157, 0.24734817637671225), 2: (0.0, 0.3582887700534759), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.26775956284152996, 0.18405143870551252), 1: (0.1978021978021978, 0.25460802919739217), 2: (0.6, 0.48652236652236647), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15789473684210525, 0.1324465008675535), 1: (0.06451612903225806, 0.10111299754763252), 2: (0.0, 0.1111111111111111), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.35, 0.2683333333333333), 1: (0.375, 0.0581451330532213), 2: (0.4166666666666667, 0.379985754985755), 3: (0.0, 0.5), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.35294117647058826, 0.26554621848739496), 1: (0.36585365853658536, 0.21983159117305456), 2: (0.35714285714285715, 0.16666666666666669), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.1534090909090909), 1: (0.5599999999999998, 0.2000441176470588), 2: (0.3333333333333333, 0.06818181818181816), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.2955555555555555), 1: (0.37777777777777777, 0.23229036503890307), 2: (0.5714285714285714, 0.17857142857142858), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5185185185185185, 0.08774928774928777), 1: (0.40425531914893614, 0.2851063829787233), 2: (0.45454545454545453, 0.2589285714285714), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2631578947368421, 0.17982456140350878), 1: (0.3137254901960784, 0.2836538461538462), 2: (0.375, 0.27058823529411763), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1875, 0.25), 1: (0.08888888888888889, 0.2607930365128507), 2: (0.2857142857142857, 0.08163265306122448), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.1581684981684982), 1: (0.2711864406779661, 0.2783474576271185), 2: (0.16666666666666666, 0.1313131313131313), 3: (1.0, 1.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2903225806451613, 0.09622277364212849), 1: (0.3125, 0.18515011223344557), 2: (0.25, 0.2333333333333333), 3: (0.0, 1.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.35, 0.22000000000000003), 1: (0.08333333333333333, 0.07886754164031205), 2: (0.4, 0.12840909090909092), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1724137931034483, 0.32346743295019154), 1: (0.1951219512195122, 0.20184989568059872), 2: (0.35294117647058826, 0.09019607843137255), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.1875, 0.207421875), 1: (0.2972972972972973, 0.14930161253690666), 2: (0.26666666666666666, 0.14632034632034632), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.3333333333333333), 1: (0.5, 0.1111111111111111), 2: (0.2, 0.06666666666666667), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.6, 0.2), 2: (0.3333333333333333, 0.2222222222222222), 3: (0.5, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.16666666666666666), 1: (0.3333333333333333, 0.07407407407407407), 2: (0.3333333333333333, 0.0), 3: (1.0, 0.5), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6, 0.4), 1: (0.0, 0.35000000000000003), 2: (0.25, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.5714285714285714, 0.25), 2: (0.625, 0.25), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6, 0.8), 2: (0.375, 0.25), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.5), 1: (0.14285714285714285, 0.23809523809523808), 2: (0.4, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.0, 0.125), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 1.0), 1: (0.1111111111111111, 0.2222222222222222), 2: (0.25, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 1.0), 1: (0.0, 0.2857142857142857), 2: (0.0, 0.25), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.5), 1: (0.0, 0.14285714285714285), 2: (0.0, 0.16666666666666666), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.3333333333333333, 0.2222222222222222), 2: (0.0, 0.25), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.2), 2: (0.125, 0.125), 3: (0.0, 0.0), 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (1.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.5), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: None, 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.3333333333333333, 0.3333333333333333), 3: (0.0, 0.0), 4: None}
player hand value: 17
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13028169014084517, 0.11411033770188686), 1: (0.11627906976744186, 0.2790115842109629), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3380782918149465, 0.19697823912192336), 1: (0.46153846153846156, 0.4692869054648369), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3917525773195876, 0.25396788041704005), 1: (0.4, 0.5474523392622456), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4230769230769231, 0.19789368081495604), 1: (0.41379310344827586, 0.48716364614882046), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.44680851063829785, 0.22530998214888798), 1: (0.391304347826087, 0.540991684810438), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4588235294117646, 0.2308037982610207), 1: (0.3939393939393939, 0.5905070190545373), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25233644859813076, 0.27169953863110496), 1: (0.43283582089552236, 0.4716784165201518), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23412698412698424, 0.2830003004282848), 1: (0.2571428571428571, 0.4193998327690762), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2235294117647059, 0.20659047265014663), 1: (0.2363636363636364, 0.4064879570094664), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.18411552346570398, 0.17531988866552017), 1: (0.22807017543859648, 0.3194670880727001), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21505376344086022, 0.18817062631929385), 1: (0.22033898305084745, 0.3265019704014526), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2627450980392159, 0.15101310174567395), 1: (0.27868852459016386, 0.4376567662041929), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2878228782287822, 0.1867738615926329), 1: (0.3148148148148148, 0.3878032715957962), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.08558558558558559, 0.12913220597646827), 1: (0.125, 0.17561685444726371), 2: (0.0, 0.43958333333333327), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34579439252336464, 0.24900567085527925), 1: (0.2894736842105264, 0.18844287862030823), 2: (0.6666666666666666, 0.4341269841269841), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.35483870967741926, 0.1568072746647157), 1: (0.4659090909090909, 0.21707417938890272), 2: (0.7142857142857143, 0.5722571079713937), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.39325842696629215, 0.15890818157157477), 1: (0.3367346938775511, 0.24377733672293603), 2: (0.5, 0.34615384615384615), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.45989304812834225, 0.22327032013491505), 1: (0.43373493975903615, 0.3077786557282716), 2: (0.0, 0.6996336996336997), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.44021739130434784, 0.19588113551919695), 1: (0.4411764705882352, 0.30994645405703586), 2: (0.25, 0.3), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3024390243902441, 0.23445891819868847), 1: (0.28571428571428575, 0.20191147215614597), 2: (0.3333333333333333, 0.39404761904761904), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2536585365853659, 0.22373802198945303), 1: (0.24761904761904768, 0.28984011558063716), 2: (0.5, 0.30883387445887445), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.29439252336448607, 0.19632197159407694), 1: (0.21428571428571427, 0.22376219573734182), 2: (0.5, 0.705622936091686), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22566371681415928, 0.1557071922986212), 1: (0.20000000000000004, 0.165803378654996), 2: (0.2, 0.7169135802469135), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19111111111111115, 0.1473369467028006), 1: (0.2222222222222222, 0.21294962431316758), 2: (0.0, 0.3038690476190476), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21875000000000003, 0.15007400087751574), 1: (0.26881720430107536, 0.2093998516030439), 2: (0.0, 0.47708333333333336), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.15384615384615394, 0.1943599832399187), 1: (0.2500000000000001, 0.19271350815681892), 2: (0.14285714285714285, 0.3951701493994727), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.13157894736842105, 0.02654071075123707), 1: (0.1590909090909091, 0.1323763955342903), 2: (0.0, 0.041666666666666664), 3: (0.0, 0.0), 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3548387096774194, 0.16761543327008224), 1: (0.5000000000000001, 0.18624581939799323), 2: (0.5714285714285714, 0.19642857142857142), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4523809523809524, 0.17993197278911566), 1: (0.425, 0.09768772893772895), 2: (0.5, 0.5), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.27586206896551724, 0.2614788862253366), 1: (0.4444444444444444, 0.14054232804232802), 2: (0.6666666666666666, 0.3333333333333333), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5217391304347827, 0.21906354515050167), 1: (0.43103448275862066, 0.1511595079653156), 2: (0.38461538461538464, 0.15769230769230771), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34210526315789475, 0.2894736842105263), 1: (0.4318181818181818, 0.12727272727272726), 2: (0.3333333333333333, 0.16765873015873015), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3, 0.34051282051282056), 1: (0.2222222222222222, 0.21027777777777779), 2: (0.1875, 0.325), 3: (0.0, 1.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3076923076923077, 0.1982118758434548), 1: (0.3098591549295775, 0.22803061685621748), 2: (0.25, 0.30892857142857144), 3: (0.0, 1.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22580645161290322, 0.21629445822994212), 1: (0.2962962962962963, 0.19950617283950617), 2: (0.3076923076923077, 0.3084693084693085), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.21621621621621623, 0.1559221559221559), 1: (0.19230769230769235, 0.12407407407407403), 2: (0.2222222222222222, 0.16666666666666666), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.358974358974359, 0.0757020757020757), 1: (0.1746031746031746, 0.10495165808258786), 2: (0.3, 0.275), 3: (0.0, 0.5), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.19444444444444445, 0.15849673202614378), 1: (0.234375, 0.18566849816849818), 2: (0.4, 0.22000000000000003), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2619047619047619, 0.14061624649859944), 1: (0.27586206896551724, 0.13793103448275865), 2: (0.2222222222222222, 0.2866161616161616), 3: (1.0, 1.0), 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.0, 0.09523809523809523), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.2, 0.2), 2: (0.42857142857142855, 0.42857142857142855), 3: (1.0, 1.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.6666666666666666), 1: (0.15384615384615385, 0.20512820512820512), 2: (0.2, 0.5), 3: (0.5, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.0), 1: (0.25, 0.21666666666666665), 2: (0.6, 0.1), 3: (0.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5555555555555556, 0.07407407407407407), 2: (0.25, 0.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.3076923076923077, 0.38461538461538464), 2: (0.6, 0.18), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.0, 0.20833333333333331), 2: (0.1111111111111111, 0.25), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.25), 1: (0.42857142857142855, 0.2857142857142857), 2: (0.0, 0.2285714285714286), 3: (0.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.0), 1: (0.0, 0.0), 2: (0.25, 0.2708333333333333), 3: (0.0, 0.25), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.3076923076923077, 0.14285714285714285), 2: (0.0, 0.5), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.3333333333333333, 0.09722222222222221), 2: (0.25, 0.1875), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3333333333333333, 0.3333333333333333), 1: (0.6, 0.0), 2: (0.2, 0.0), 3: (0.25, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.0), 1: (0.25, 0.40625), 2: (0.375, 0.0), 3: (1.0, 0.0), 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.3333333333333333), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.5), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: None, 2: (0.0, 0.5), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.0), 3: (0.3333333333333333, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.5), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: (1.0, 0.5), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.3333333333333333), 2: None, 3: (1.0, 1.0), 4: None}
player hand value: 18
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2304147465437788, 0.11407686545140858), 1: (0.288888888888889, 0.2304168535262914), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5401459854014601, 0.17354176086816078), 1: (0.515625, 0.417057592102885), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5019455252918287, 0.1578436517130196), 1: (0.5098039215686274, 0.5335615172979682), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5936254980079677, 0.20648593365999604), 1: (0.4444444444444444, 0.5235694373165638), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5945945945945946, 0.16724734939020663), 1: (0.5901639344262295, 0.6160889414414993), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6017699115044246, 0.19823930678466087), 1: (0.6226415094339622, 0.5533344943818013), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6315789473684208, 0.2056406197680435), 1: (0.7045454545454547, 0.5521758483954099), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3520408163265308, 0.16037063899831058), 1: (0.37333333333333335, 0.4779074928885607), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3228699551569508, 0.1646962902568285), 1: (0.44, 0.46484493964335954), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.32, 0.18378575688894197), 1: (0.32758620689655166, 0.4066871233982936), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3183856502242152, 0.160866143971786), 1: (0.42857142857142855, 0.37208448801785504), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.26130653266331666, 0.15500891554546928), 1: (0.27450980392156865, 0.42406564698990196), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3744493392070483, 0.13548948758338158), 1: (0.25396825396825395, 0.36061488971652395), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2079646017699115, 0.11555479918311767), 1: (0.18571428571428572, 0.10543177447775605), 2: (0.0, 0.1), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4389140271493214, 0.18227291820642197), 1: (0.5797101449275364, 0.21985392455052888), 2: (0.8333333333333334, 0.49537037037037024), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4976744186046513, 0.15073616802369916), 1: (0.45454545454545453, 0.24797958873508583), 2: (0.375, 0.6217948717948718), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5536723163841806, 0.1760785232627769), 1: (0.5000000000000001, 0.21573556687057502), 2: (0.3333333333333333, 0.6666666666666666), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.589371980676329, 0.1617492492492493), 1: (0.6790123456790124, 0.2664589362741733), 2: (0.6, 0.6261294261294261), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.559808612440191, 0.2092292805315481), 1: (0.5887850467289719, 0.31539740977717595), 2: (0.5, 0.775), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6785714285714285, 0.1910478183606412), 1: (0.5729166666666667, 0.27132338376514037), 2: (0.75, 0.4754595588235294), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3918918918918919, 0.17915825232898416), 1: (0.42391304347826086, 0.26741241295248946), 2: (0.45454545454545453, 0.4535730683457956), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.33809523809523817, 0.17543901281442817), 1: (0.3829787234042554, 0.2915572379435871), 2: (0.3333333333333333, 0.338979538979539), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2786069651741293, 0.11542628204447833), 1: (0.3434343434343434, 0.1659342868938828), 2: (0.3333333333333333, 0.23148148148148148), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3596491228070175, 0.15215418799717492), 1: (0.35869565217391297, 0.13634466096039213), 2: (0.0, 0.2789411976911977), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25837320574162687, 0.1488101297731756), 1: (0.34090909090909094, 0.18425433593017423), 2: (0.5, 0.37904040404040407), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3476394849785409, 0.1334442729292514), 1: (0.2638888888888889, 0.2285190796063049), 2: (0.5, 0.6169806618819776), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.20408163265306123, 0.06593406593406594), 1: (0.16393442622950818, 0.07368421052631578), 2: (0.2, 0.08), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.1607789855072464), 1: (0.5733333333333334, 0.1), 2: (0.3333333333333333, 0.21652421652421655), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6, 0.15306122448979592), 1: (0.5333333333333333, 0.20347222222222222), 2: (0.7692307692307693, 0.34615384615384615), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34782608695652184, 0.1312252964426878), 1: (0.5849056603773586, 0.18583833619210974), 2: (0.5, 0.26666666666666666), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.47999999999999987, 0.15684210526315795), 1: (0.6226415094339623, 0.13321104122990915), 2: (0.4444444444444444, 0.2833333333333333), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5999999999999999, 0.18363636363636368), 1: (0.6896551724137931, 0.1743349753694581), 2: (0.75, 0.25), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5964912280701757, 0.14239766081871352), 1: (0.6710526315789472, 0.12205995758627335), 2: (0.5, 0.3125), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5471698113207547, 0.22523584905660377), 1: (0.5081967213114754, 0.1370712219313955), 2: (0.3333333333333333, 0.25), 3: (0.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3191489361702128, 0.12281505728314238), 1: (0.32, 0.18866666666666673), 2: (0.2857142857142857, 0.18601190476190474), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.22727272727272727, 0.11796536796536795), 1: (0.2702702702702703, 0.16991141991141984), 2: (0.25, 0.23194444444444445), 3: (1.0, 1.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.26153846153846155, 0.11460892049127347), 1: (0.2833333333333333, 0.0921309872922776), 2: (0.14285714285714285, 0.36607142857142855), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.36231884057971014, 0.08971704623878536), 1: (0.28169014084507044, 0.15276273022751893), 2: (0.36363636363636365, 0.14242424242424243), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.34210526315789475, 0.21052631578947367), 1: (0.3194444444444445, 0.13700555979967746), 2: (0.42857142857142855, 0.18367346938775508), 3: (0.0, 0.0), 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.0), 1: (0.1111111111111111, 0.0), 2: (0.6666666666666666, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.5294117647058824, 0.058823529411764705), 2: (0.6153846153846154, 0.05128205128205128), 3: (0.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.4), 1: (0.7, 0.1), 2: (0.5, 0.16666666666666666), 3: (1.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.75, 0.125), 1: (0.5882352941176471, 0.04705882352941177), 2: (0.2857142857142857, 0.07142857142857142), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.5833333333333334), 1: (0.5384615384615384, 0.20512820512820512), 2: (0.3, 0.2), 3: (1.0, 0.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8, 0.2), 1: (0.7, 0.1), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.5384615384615384, 0.07692307692307693), 2: (0.8, 0.2), 3: (1.0, 1.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.25, 0.25), 1: (0.3684210526315789, 0.05263157894736842), 2: (0.36363636363636365, 0.09090909090909091), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.42857142857142855, 0.2857142857142857), 1: (0.75, 0.09687500000000002), 2: (0.3333333333333333, 0.16666666666666666), 3: (1.0, 1.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.36363636363636365, 0.13636363636363635), 2: (0.3, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.26666666666666666, 0.0), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.625, 0.125), 1: (0.35294117647058826, 0.11764705882352941), 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.2), 1: (0.11764705882352941, 0.0), 2: (0.2857142857142857, 0.07142857142857142), 3: None, 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.6666666666666666, 0.0), 2: (0.5, 0.5), 3: (0.0, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6666666666666666, 0.0), 2: (0.4, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.0, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.3333333333333333, 0.0), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: None, 3: (0.5, 0.5), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (1.0, 0.0), 2: (0.3333333333333333, 0.0), 3: (0.5, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (1.0, 0.0), 2: (0.2, 0.2), 3: (0.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.6666666666666666, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: None, 2: (1.0, 0.5), 3: (0.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.5, 0.0), 2: (1.0, 0.0), 3: None, 4: None}
player hand value: 19
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4170403587443946, 0.08071748878923762), 1: (0.3877551020408163, 0.27587233655389665), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5965665236051505, 0.1245077651431354), 1: (0.6101694915254239, 0.4762320640471162), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6707818930041151, 0.1662551440329219), 1: (0.6250000000000001, 0.5454095774334494), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.626050420168067, 0.14097979617378853), 1: (0.5806451612903225, 0.5509586676413348), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6986301369863016, 0.10889719108897195), 1: (0.6393442622950819, 0.5434481588645786), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7285067873303167, 0.13211773666054386), 1: (0.6610169491525423, 0.5626542856999973), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7621359223300971, 0.10652939293715995), 1: (0.7692307692307693, 0.6011373559023426), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6995884773662556, 0.14166885561684622), 1: (0.7674418604651163, 0.5802153876368664), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.47590361445783114, 0.13651904916965155), 1: (0.5087719298245615, 0.42582183611588265), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.47058823529411764, 0.10828877005347594), 1: (0.393939393939394, 0.4251366935103315), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.46766169154228854, 0.13009028929426944), 1: (0.39344262295081966, 0.42851162252044955), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4858490566037736, 0.09734133790737556), 1: (0.4925373134328359, 0.40022640402258897), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4153846153846154, 0.07654520917678809), 1: (0.4339622641509434, 0.37550374394255237), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.3861003861003861, 0.06002574002574002), 1: (0.37931034482758624, 0.19859291175446553), 2: (0.5, 0.2583333333333333), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.654320987654321, 0.10860619073179455), 1: (0.6133333333333333, 0.21917368210971158), 2: (0.16666666666666666, 0.4681216931216931), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6710526315789476, 0.10799220272904482), 1: (0.6888888888888887, 0.2572904511785851), 2: (1.0, 0.45946275946275944), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6650943396226416, 0.16676195921478948), 1: (0.6777777777777778, 0.3430581074370918), 2: (0.0, 0.5), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7000000000000003, 0.12748772869254793), 1: (0.5666666666666665, 0.1986352179952515), 2: (0.7142857142857143, 0.6507936507936508), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6493506493506496, 0.1263962375073486), 1: (0.6296296296296302, 0.24780567865191594), 2: (0.75, 0.6923076923076923), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8287037037037037, 0.1416268418956589), 1: (0.769230769230769, 0.3257373999774548), 2: (0.8333333333333334, 0.5550682773109243), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7428571428571429, 0.11878009630818614), 1: (0.7432432432432432, 0.3436516417372337), 2: (0.6666666666666666, 0.5353535353535352), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.49236641221374045, 0.1580152671755725), 1: (0.5, 0.3297070820612301), 2: (0.3333333333333333, 0.7333333333333334), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.49019607843137253, 0.11087768440709614), 1: (0.5445544554455448, 0.2230656420091187), 2: (0.7, 0.2621527777777778), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.10387430047352554), 1: (0.46511627906976744, 0.1959682323596323), 2: (0.6666666666666666, 0.6051587301587301), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.430327868852459, 0.12495446265938052), 1: (0.5000000000000001, 0.19601596914415872), 2: (1.0, 0.4), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.46616541353383456, 0.1116398591415247), 1: (0.4264705882352941, 0.1917372840994332), 2: (0.2, 0.482085137085137), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.375, 0.07177033492822966), 1: (0.36538461538461536, 0.13782051282051283), 2: (0.25, 0.027777777777777776), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6981132075471698, 0.09869375907111756), 1: (0.6081081081081081, 0.0629692192192192), 2: (0.3333333333333333, 0.1794871794871795), 3: (0.5, 1.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5737704918032787, 0.07445355191256829), 1: (0.6376811594202898, 0.13008971704623878), 2: (0.6923076923076923, 0.3333333333333333), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.090625), 1: (0.7142857142857143, 0.16000000000000003), 2: (0.6923076923076923, 0.07692307692307693), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6857142857142857, 0.08253968253968255), 1: (0.5540540540540538, 0.08958432116326853), 2: (0.5, 0.21875), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7, 0.174), 1: (0.7424242424242423, 0.10457251082251084), 2: (0.6923076923076923, 0.36620879120879124), 3: (0.0, 0.0), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7671232876712328, 0.1780821917808219), 1: (0.7662337662337663, 0.1531093906093907), 2: (0.42857142857142855, 0.21428571428571427), 3: (1.0, 1.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8589743589743589, 0.1432880844645551), 1: (0.6825396825396826, 0.14271541950113373), 2: (0.6666666666666666, 0.2222222222222222), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.43478260869565216, 0.17391304347826092), 1: (0.4523809523809522, 0.08697089947089943), 2: (0.6, 0.5150252525252524), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.38095238095238093, 0.11992945326278658), 1: (0.43037974683544306, 0.11392405063291132), 2: (0.25, 0.26666666666666666), 3: (0.0, 1.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.45121951219512196, 0.06963021243115658), 1: (0.42168674698795183, 0.13108568728696302), 2: (0.6153846153846154, 0.5116550116550116), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.379746835443038, 0.07205452775073029), 1: (0.47619047619047616, 0.1523809523809524), 2: (0.4666666666666667, 0.22666666666666666), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4383561643835616, 0.07534246575342464), 1: (0.38461538461538464, 0.16481720893485585), 2: (0.5555555555555556, 0.08225108225108224), 3: None, 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5555555555555556, 0.1111111111111111), 1: (0.3333333333333333, 0.08333333333333333), 2: (0.3, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.625, 0.125), 1: (0.4375, 0.0625), 2: (0.5, 0.1), 3: (0.5, 0.0), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.6428571428571429, 0.0), 2: (0.6666666666666666, 0.13333333333333333), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.6, 0.0), 2: (0.8181818181818182, 0.09090909090909091), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.47368421052631576, 0.0), 2: (0.625, 0.0), 3: (0.5, 0.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8, 0.0), 1: (0.7, 0.09), 2: (0.6428571428571429, 0.07142857142857142), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8333333333333334, 0.0), 1: (0.8125, 0.28125), 2: (0.7647058823529411, 0.14705882352941177), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.75, 0.0), 1: (0.8125, 0.0625), 2: (0.5714285714285714, 0.0), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4166666666666667, 0.06666666666666668), 1: (0.36, 0.08), 2: (0.45454545454545453, 0.06818181818181818), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2222222222222222, 0.15873015873015872), 1: (0.3333333333333333, 0.20833333333333334), 2: (0.5, 0.16666666666666666), 3: (1.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.2, 0.0), 1: (0.23529411764705882, 0.17647058823529413), 2: (0.45454545454545453, 0.18181818181818182), 3: (1.0, 0.5), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.125), 1: (0.38095238095238093, 0.09523809523809523), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5, 0.0), 1: (0.5, 0.15), 2: (0.45454545454545453, 0.09090909090909091), 3: (1.0, 1.0), 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6666666666666666, 0.6666666666666666), 2: (0.0, 0.3333333333333333), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6666666666666666, 0.0), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6666666666666666, 0.0), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: (0.0, 0.0), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.75, 0.5), 2: (1.0, 0.3333333333333333), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.0, 0.0), 3: (1.0, 0.0), 4: (0.5, 0.0)}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (1.0, 0.3333333333333333), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.6, 0.2), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 1.0), 2: (0.75, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.4, 0.0), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.0), 2: (0.5, 0.0), 3: (0.5, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (0.5, 0.5), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.0, 0.5), 2: (0.0, 0.0), 3: (1.0, 0.0), 4: None}
player hand value: 20
    num of cards: 2
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5370370370370368, 0.03935185185185182), 1: (0.66, 0.27799628255774145), 2: None, 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7807486631016047, 0.05614973262032084), 1: (0.7419354838709677, 0.5063158106423332), 2: None, 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7252252252252253, 0.09234234234234236), 1: (0.75, 0.5888535686686499), 2: None, 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7630331753554505, 0.04739336492890997), 1: (0.7346938775510204, 0.600077941406738), 2: None, 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8139534883720931, 0.08527131782945738), 1: (0.8837209302325582, 0.631589683708858), 2: None, 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8071428571428574, 0.0476190476190476), 1: (0.8181818181818183, 0.5338392847594486), 2: None, 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8467153284671532, 0.08515815085158157), 1: (0.9, 0.5600604548362852), 2: None, 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8526570048309178, 0.06280193236714982), 1: (0.8333333333333334, 0.5822089358428584), 2: None, 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7635467980295568, 0.054187192118226604), 1: (0.8250000000000002, 0.4808789716670317), 2: None, 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5861111111111114, 0.06388888888888887), 1: (0.5555555555555556, 0.4706909231781818), 2: None, 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5734870317002885, 0.08357348703170028), 1: (0.625, 0.398294143807757), 2: None, 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5391304347826084, 0.08115942028985507), 1: (0.5818181818181818, 0.43764432894981004), 2: None, 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.58, 0.09142857142857144), 1: (0.6, 0.4055799079031444), 2: None, 3: None, 4: None}
    num of cards: 3
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4857142857142855, 0.017857142857142863), 1: (0.5000000000000001, 0.13973557119130292), 2: (0.3333333333333333, 0.3333333333333333), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7433628318584071, 0.08849557522123896), 1: (0.6804123711340206, 0.30098168591453395), 2: (0.8333333333333334, 0.762962962962963), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7748091603053437, 0.08015267175572521), 1: (0.788235294117647, 0.23160891582054094), 2: (0.8333333333333334, 0.5284391534391534), 3: None, 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7586206896551724, 0.06130268199233722), 1: (0.8085106382978723, 0.36752956259886943), 2: (0.875, 0.6860544217687075), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7602040816326531, 0.05102040816326531), 1: (0.7575757575757576, 0.2714593805993868), 2: (0.8, 0.6752087912087912), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7734375, 0.0546875), 1: (0.7623762376237623, 0.3920209572852174), 2: (1.0, 0.6751082251082251), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8157894736842105, 0.05639097744360904), 1: (0.8131868131868131, 0.2421618211459169), 2: (1.0, 0.44610294117647054), 3: None, 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8464566929133859, 0.07480314960629919), 1: (0.851063829787234, 0.28211018521244596), 2: (0.8888888888888888, 0.727946127946128), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8181818181818183, 0.0950413223140496), 1: (0.8783783783783784, 0.3426661987026945), 2: (0.6666666666666666, 0.638888888888889), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5662650602409639, 0.0763052208835342), 1: (0.625, 0.1754543040364066), 2: (0.3333333333333333, 0.44485596707818925), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5636363636363634, 0.06909090909090912), 1: (0.5092592592592592, 0.1978654139260857), 2: (0.875, 0.4269230769230769), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.49193548387096786, 0.07661290322580644), 1: (0.4772727272727271, 0.21652600014612988), 2: (0.42857142857142855, 0.5000000000000001), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5393258426966288, 0.07490636704119853), 1: (0.5578947368421052, 0.23462223777701965), 2: (0.625, 0.551368359345333), 3: None, 4: None}
    num of cards: 4
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4583333333333333, 0.0729166666666667), 1: (0.5066666666666667, 0.052475633528265106), 2: (0.3333333333333333, 0.18333333333333335), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7934782608695652, 0.0760869565217391), 1: (0.6956521739130432, 0.1024247491638796), 2: (0.7333333333333333, 0.13597883597883598), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8289473684210527, 0.05263157894736842), 1: (0.7888888888888889, 0.07982804232804232), 2: (0.7857142857142857, 0.2857142857142857), 3: (1.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7634408602150538, 0.053763440860215034), 1: (0.7676767676767676, 0.07450237670825906), 2: (0.6666666666666666, 0.3), 3: None, 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.7875, 0.1125), 1: (0.771084337349398, 0.13124721106648818), 2: (0.8571428571428571, 0.08928571428571429), 3: (1.0, 1.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8586956521739131, 0.07608695652173915), 1: (0.8271604938271605, 0.07079365079365076), 2: (0.8, 0.15625), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8313253012048193, 0.09638554216867468), 1: (0.8494623655913979, 0.14208663200598684), 2: (1.0, 0.2285714285714286), 3: (0.0, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8780487804878049, 0.0975609756097561), 1: (0.7640449438202246, 0.08296352248764677), 2: (0.8333333333333334, 0.38095238095238093), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8604651162790697, 0.05813953488372091), 1: (0.8470588235294118, 0.11482352941176469), 2: (0.875, 0.2977430555555555), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.48314606741573035, 0.02247191011235955), 1: (0.4880952380952381, 0.04132023179642225), 2: (0.75, 0.25), 3: None, 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5853658536585366, 0.04878048780487803), 1: (0.49504950495049505, 0.05451592326486646), 2: (0.375, 0.26041666666666663), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5106382978723406, 0.05319148936170213), 1: (0.5222222222222224, 0.11355119825708063), 2: (0.4166666666666667, 0.14166666666666666), 3: None, 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6081081081081081, 0.06756756756756757), 1: (0.531645569620253, 0.0501205545509343), 2: (0.6842105263157895, 0.09577922077922078), 3: (1.0, 1.0), 4: None}
    num of cards: 5
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.23076923076923078, 0.0), 1: (0.5789473684210527, 0.0), 2: (0.3333333333333333, 0.16666666666666666), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6666666666666666, 0.1111111111111111), 1: (0.8076923076923077, 0.07692307692307693), 2: (0.4444444444444444, 0.0), 3: (1.0, 0.5), 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8571428571428571, 0.14285714285714285), 1: (0.7083333333333334, 0.08333333333333333), 2: (0.3333333333333333, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8181818181818182, 0.09090909090909091), 1: (0.7187499999999999, 0.03125), 2: (0.8, 0.1), 3: (1.0, 1.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.14285714285714285), 1: (0.9259259259259259, 0.07407407407407407), 2: (0.8, 0.1), 3: (0.5, 0.0), 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8, 0.1), 1: (0.92, 0.04), 2: (0.5625, 0.0), 3: None, 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.9333333333333333, 0.06666666666666667), 1: (0.875, 0.125), 2: (0.8, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8125, 0.0), 1: (0.8823529411764706, 0.08823529411764706), 2: (0.8571428571428571, 0.07142857142857142), 3: None, 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.8461538461538461, 0.07692307692307693), 1: (0.8, 0.06666666666666667), 2: (0.8888888888888888, 0.0), 3: None, 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5714285714285714, 0.14285714285714285), 1: (0.5925925925925926, 0.07407407407407407), 2: (0.5555555555555556, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.6428571428571429, 0.07142857142857142), 1: (0.3870967741935484, 0.06451612903225806), 2: (0.5625, 0.03125), 3: None, 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.5555555555555556, 0.0), 1: (0.6153846153846154, 0.038461538461538464), 2: (0.7, 0.0), 3: (0.5, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.4, 0.0), 1: (0.6428571428571427, 0.10714285714285714), 2: (0.7142857142857143, 0.14285714285714285), 3: (1.0, 0.0), 4: None}
    num of cards: 6
      face card rank: A
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.6666666666666666, 0.0), 2: (0.5, 0.0), 3: None, 4: None}
      face card rank: 2
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (1.0, 0.0), 2: (0.6666666666666666, 0.0), 3: None, 4: None}
      face card rank: 3
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: None, 3: (1.0, 0.0), 4: None}
      face card rank: 4
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.8, 0.0), 2: (0.5, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: 5
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 0.0), 1: (0.6666666666666666, 0.0), 2: (1.0, 0.0), 3: None, 4: None}
      face card rank: 6
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (1.0, 0.0), 2: (0.8, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 7
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 1.0), 1: (0.6666666666666666, 0.0), 2: (0.75, 0.25), 3: (0.5, 0.0), 4: None}
      face card rank: 8
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (1.0, 0.0), 1: (1.0, 0.0), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: 9
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.8, 0.2), 2: (1.0, 0.0), 3: (0.5, 0.0), 4: None}
      face card rank: T
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.42857142857142855, 0.14285714285714285), 2: None, 3: (0.3333333333333333, 0.0), 4: None}
      face card rank: J
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: (1.0, 0.0), 3: (0.0, 0.0), 4: None}
      face card rank: Q
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: (0.0, 1.0), 1: (0.5, 0.16666666666666666), 2: (0.5714285714285714, 0.0), 3: (1.0, 0.0), 4: None}
      face card rank: K
        win percentage of stand vs hit for each ace count (0 ~ 4): {0: None, 1: (0.5, 0.0), 2: (0.5, 0.0), 3: None, 4: (1.0, 0.0)}
</pre>

### Decision Matrix (original):
`{2: {2: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 3: {2: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 4: {2: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 5: {2: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 6: {2: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 7: {2: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 8: {2: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 9: {2: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 10: {2: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 11: {2: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: False, 2: False, 3: False, 4: False}, '9': {0: True, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 12: {2: {'A': {0: True, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: True, 3: False, 4: False}, '3': {0: False, 1: False, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: False, 1: False, 2: True, 3: False, 4: False}, '6': {0: False, 1: False, 2: True, 3: False, 4: False}, '7': {0: True, 1: False, 2: True, 3: False, 4: False}, '8': {0: True, 1: False, 2: True, 3: False, 4: False}, '9': {0: True, 1: False, 2: True, 3: False, 4: False}, 'T': {0: True, 1: False, 2: True, 3: False, 4: False}, 'J': {0: True, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: True, 3: False, 4: False}, 'K': {0: True, 1: False, 2: True, 3: False, 4: False}}, 3: {'A': {0: True, 1: True, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: True, 1: False, 2: False, 3: False, 4: False}, '6': {0: True, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: True, 3: False, 4: False}, '8': {0: True, 1: True, 2: True, 3: False, 4: False}, '9': {0: True, 1: True, 2: True, 3: False, 4: False}, 'T': {0: True, 1: True, 2: True, 3: False, 4: False}, 'J': {0: True, 1: True, 2: True, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: True, 3: False, 4: False}, 'K': {0: True, 1: True, 2: True, 3: False, 4: False}}, 4: {'A': {0: False, 1: True, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: True, 3: False, 4: False}, '3': {0: True, 1: True, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: True, 2: True, 3: False, 4: False}, '6': {0: True, 1: True, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: True, 3: False, 4: False}, '8': {0: True, 1: True, 2: False, 3: False, 4: False}, '9': {0: True, 1: True, 2: False, 3: False, 4: False}, 'T': {0: True, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: True, 3: False, 4: False}, 'K': {0: True, 1: False, 2: True, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: True, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: True, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 13: {2: {'A': {0: True, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: True, 2: False, 3: False, 4: False}, '3': {0: False, 1: True, 2: False, 3: False, 4: False}, '4': {0: False, 1: True, 2: False, 3: False, 4: False}, '5': {0: False, 1: True, 2: False, 3: False, 4: False}, '6': {0: False, 1: True, 2: False, 3: False, 4: False}, '7': {0: True, 1: True, 2: False, 3: False, 4: False}, '8': {0: True, 1: True, 2: False, 3: False, 4: False}, '9': {0: True, 1: True, 2: False, 3: False, 4: False}, 'T': {0: True, 1: True, 2: False, 3: False, 4: False}, 'J': {0: True, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: True, 2: False, 3: False, 4: False}, 'K': {0: True, 1: True, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: True, 1: False, 2: False, 3: True, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: True, 2: False, 3: False, 4: False}, '9': {0: True, 1: True, 2: False, 3: False, 4: False}, 'T': {0: True, 1: True, 2: False, 3: True, 4: False}, 'J': {0: True, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: True, 2: False, 3: False, 4: False}, 'K': {0: True, 1: True, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: True, 2: True, 3: False, 4: False}, '2': {0: True, 1: True, 2: True, 3: False, 4: False}, '3': {0: True, 1: False, 2: True, 3: False, 4: False}, '4': {0: True, 1: False, 2: True, 3: False, 4: False}, '5': {0: True, 1: True, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: True, 3: False, 4: False}, '8': {0: True, 1: True, 2: True, 3: False, 4: False}, '9': {0: True, 1: True, 2: False, 3: False, 4: False}, 'T': {0: True, 1: True, 2: False, 3: True, 4: False}, 'J': {0: False, 1: True, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: True, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: True, 3: True, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: True, 3: False, 4: False}, '3': {0: False, 1: False, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: True, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: True, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: True, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: True, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 14: {2: {'A': {0: True, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: True, 2: False, 3: False, 4: False}, '3': {0: False, 1: True, 2: False, 3: False, 4: False}, '4': {0: False, 1: True, 2: False, 3: False, 4: False}, '5': {0: False, 1: True, 2: False, 3: False, 4: False}, '6': {0: False, 1: True, 2: False, 3: False, 4: False}, '7': {0: True, 1: True, 2: False, 3: False, 4: False}, '8': {0: True, 1: True, 2: False, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: True, 2: False, 3: False, 4: False}, 'J': {0: True, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: True, 2: False, 3: False, 4: False}, 'K': {0: True, 1: True, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: True, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: False, 1: False, 2: True, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: True, 2: True, 3: False, 4: False}, '8': {0: True, 1: True, 2: True, 3: False, 4: False}, '9': {0: True, 1: False, 2: True, 3: False, 4: False}, 'T': {0: True, 1: True, 2: False, 3: False, 4: False}, 'J': {0: True, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: True, 1: True, 2: True, 3: False, 4: False}, 'K': {0: True, 1: True, 2: True, 3: False, 4: False}}, 4: {'A': {0: True, 1: True, 2: True, 3: False, 4: False}, '2': {0: True, 1: True, 2: False, 3: False, 4: False}, '3': {0: True, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: False, 1: False, 2: True, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: True, 2: False, 3: False, 4: False}, '8': {0: True, 1: True, 2: False, 3: False, 4: False}, '9': {0: True, 1: True, 2: True, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: True, 1: True, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: True, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: True, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: True, 2: True, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: True, 2: True, 3: False, 4: False}, '8': {0: False, 1: False, 2: True, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: True, 4: False}, 'J': {0: False, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: True, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: True, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: True, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: True, 4: False}}}, 15: {2: {'A': {0: True, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: True, 2: False, 3: False, 4: False}, '3': {0: False, 1: True, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: True, 2: False, 3: False, 4: False}, '6': {0: False, 1: True, 2: False, 3: False, 4: False}, '7': {0: True, 1: True, 2: False, 3: False, 4: False}, '8': {0: False, 1: True, 2: False, 3: False, 4: False}, '9': {0: True, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: True, 2: False, 3: False, 4: False}, 'J': {0: False, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: True, 2: False, 3: False, 4: False}, 'K': {0: False, 1: True, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: True, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: True, 3: False, 4: False}, '3': {0: False, 1: False, 2: True, 3: False, 4: False}, '4': {0: False, 1: True, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: True, 3: False, 4: False}, '7': {0: True, 1: True, 2: True, 3: False, 4: False}, '8': {0: True, 1: False, 2: True, 3: False, 4: False}, '9': {0: False, 1: True, 2: True, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: False, 4: False}, 'J': {0: False, 1: True, 2: True, 3: False, 4: False}, 'Q': {0: True, 1: True, 2: True, 3: False, 4: False}, 'K': {0: True, 1: False, 2: True, 3: False, 4: False}}, 4: {'A': {0: True, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: True, 2: True, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: True, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: True, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: True, 2: False, 3: False, 4: False}, '2': {0: True, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: True, 4: False}, '7': {0: False, 1: True, 2: True, 3: False, 4: False}, '8': {0: False, 1: True, 2: False, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: True, 2: True, 3: False, 4: False}, 'J': {0: False, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: True, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 16: {2: {'A': {0: True, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: True, 2: False, 3: False, 4: False}, '3': {0: False, 1: True, 2: False, 3: False, 4: False}, '4': {0: False, 1: True, 2: False, 3: False, 4: False}, '5': {0: False, 1: True, 2: False, 3: False, 4: False}, '6': {0: False, 1: True, 2: False, 3: False, 4: False}, '7': {0: True, 1: True, 2: False, 3: False, 4: False}, '8': {0: True, 1: True, 2: False, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: True, 2: False, 3: False, 4: False}, 'J': {0: False, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: True, 2: False, 3: False, 4: False}, 'K': {0: True, 1: True, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: True, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: False, 1: False, 2: True, 3: False, 4: False}, '6': {0: False, 1: False, 2: True, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: True, 2: True, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: True, 2: True, 3: False, 4: False}, 'J': {0: False, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: True, 2: True, 3: False, 4: False}, 'K': {0: False, 1: True, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: True, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: True, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: True, 1: True, 2: False, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: True, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: True, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: True, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: True, 2: False, 3: False, 4: False}, '7': {0: False, 1: True, 2: False, 3: False, 4: False}, '8': {0: False, 1: True, 2: False, 3: False, 4: False}, '9': {0: True, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: True, 2: True, 3: False, 4: False}, 'J': {0: False, 1: True, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: True, 3: False, 4: False}, 'K': {0: False, 1: True, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 17: {2: {'A': {0: False, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: True, 2: False, 3: False, 4: False}, '3': {0: False, 1: True, 2: False, 3: False, 4: False}, '4': {0: False, 1: True, 2: False, 3: False, 4: False}, '5': {0: False, 1: True, 2: False, 3: False, 4: False}, '6': {0: False, 1: True, 2: False, 3: False, 4: False}, '7': {0: True, 1: True, 2: False, 3: False, 4: False}, '8': {0: True, 1: True, 2: False, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: True, 2: False, 3: False, 4: False}, 'J': {0: False, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: True, 2: False, 3: False, 4: False}, 'K': {0: False, 1: True, 2: False, 3: False, 4: False}}, 3: {'A': {0: True, 1: True, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: True, 3: False, 4: False}, '6': {0: False, 1: False, 2: True, 3: False, 4: False}, '7': {0: False, 1: False, 2: True, 3: False, 4: False}, '8': {0: False, 1: True, 2: False, 3: False, 4: False}, '9': {0: False, 1: True, 2: True, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: True, 3: False, 4: False}, 'K': {0: True, 1: False, 2: True, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: True, 1: False, 2: True, 3: True, 4: False}, '8': {0: False, 1: False, 2: True, 3: True, 4: False}, '9': {0: False, 1: False, 2: True, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: True, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: True, 3: False, 4: False}}, 5: {'A': {0: False, 1: True, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: True, 1: True, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: True, 2: False, 3: False, 4: False}, '7': {0: False, 1: True, 2: True, 3: False, 4: False}, '8': {0: True, 1: False, 2: True, 3: False, 4: False}, '9': {0: False, 1: False, 2: True, 3: True, 4: False}, 'T': {0: False, 1: False, 2: True, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: True, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: True, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: True, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: True, 2: False, 3: False, 4: False}}}, 18: {2: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: True, 2: False, 3: False, 4: False}, '4': {0: False, 1: True, 2: False, 3: False, 4: False}, '5': {0: False, 1: True, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: True, 2: False, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: True, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: True, 2: False, 3: False, 4: False}, 'K': {0: False, 1: True, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: True, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: False, 1: False, 2: True, 3: False, 4: False}, '6': {0: False, 1: False, 2: True, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: True, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: True, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: True, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: True, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}, 19: {2: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: True, 2: False, 3: False, 4: False}, 'J': {0: False, 1: True, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: True, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: True, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: True, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: True, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: True, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: True, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: True, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: True, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: True, 2: False, 3: False, 4: False}}}, 20: {2: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 3: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: True, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: True, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 4: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 5: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: False, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}, 6: {'A': {0: False, 1: False, 2: False, 3: False, 4: False}, '2': {0: False, 1: False, 2: False, 3: False, 4: False}, '3': {0: False, 1: False, 2: False, 3: False, 4: False}, '4': {0: False, 1: False, 2: False, 3: False, 4: False}, '5': {0: False, 1: False, 2: False, 3: False, 4: False}, '6': {0: False, 1: False, 2: False, 3: False, 4: False}, '7': {0: False, 1: False, 2: False, 3: False, 4: False}, '8': {0: False, 1: False, 2: False, 3: False, 4: False}, '9': {0: False, 1: False, 2: False, 3: False, 4: False}, 'T': {0: False, 1: False, 2: False, 3: False, 4: False}, 'J': {0: False, 1: False, 2: False, 3: False, 4: False}, 'Q': {0: True, 1: False, 2: False, 3: False, 4: False}, 'K': {0: False, 1: False, 2: False, 3: False, 4: False}}}}`

### Percentage Matrix (original):
`{2: {2: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 3: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 4: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 5: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 3: {2: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 3: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 4: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 5: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 4: {2: {'A': {0: (0.13333333333333333, 0.23903833913017072), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.38461538461538464, 0.4541194819403468), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.44, 0.49523368674158846), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.6842105263157895, 0.47539332325286027), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.5, 0.5232636075296768), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.47058823529411764, 0.5072070514602947), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.24, 0.39606311137093114), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.3333333333333333, 0.3767314925592427), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.15384615384615385, 0.42031313603836473), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.041666666666666664, 0.22589992783647814), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.13043478260869565, 0.34840586269670165), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.19047619047619047, 0.29481670154808404), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.10344827586206896, 0.29820765133592286), 1: None, 2: None, 3: None, 4: None}}, 3: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 4: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 5: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 5: {2: {'A': {0: (0.11864406779661016, 0.177804272969106), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.35714285714285715, 0.39637155707300015), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.34782608695652173, 0.5099049340066099), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.4583333333333333, 0.47089127726032715), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.38181818181818183, 0.5250717482487127), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.3888888888888889, 0.457423806873279), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.28378378378378377, 0.40899453622905474), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.20634920634920634, 0.39392388745601925), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.15384615384615385, 0.38575228321695815), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.18840579710144928, 0.27691582219885724), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.2459016393442623, 0.31643899544988907), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.35294117647058826, 0.29384537780770953), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.29545454545454547, 0.29479553757714005), 1: None, 2: None, 3: None, 4: None}}, 3: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 4: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 5: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 6: {2: {'A': {0: (0.06944444444444445, 0.17290503720707878), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.3090909090909091, 0.4161162603841784), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.3142857142857143, 0.4581228079006277), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.375, 0.45112891398170646), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.4444444444444444, 0.5120771228285294), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.38095238095238093, 0.46388903579569324), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.31645569620253156, 0.40197799335172046), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.25423728813559326, 0.37897749174603035), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.31578947368421045, 0.32842290469127744), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.19480519480519481, 0.27150260103649065), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.16883116883116883, 0.30760699379302164), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.25, 0.29460455582025186), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.2875, 0.3040119497570522), 1: None, 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.0, 0.5), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.0, 0.175), 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.0, 0.4444444444444444), 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.0, 0.5185185185185185), 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.0, 0.0), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.0, 0.18162393162393164), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.0, 0.0), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.3333333333333333, 0.4666666666666666), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.0, 0.3046875), 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 4: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 5: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 7: {2: {'A': {0: (0.11851851851851856, 0.18446525130040756), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.3557692307692308, 0.42175996517675507), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.41414141414141414, 0.4174858326281017), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.4787234042553193, 0.4669902098482544), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.44, 0.5188893837771856), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.3947368421052632, 0.5034383839941022), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.28057553956834536, 0.40230076758688155), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.256637168141593, 0.3920450139880368), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.19327731092436976, 0.35467654496280027), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.22900763358778628, 0.2759134901579947), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.16666666666666666, 0.28177875457491464), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.15315315315315314, 0.2868883905743196), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.30188679245283034, 0.286222999615228), 1: None, 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.1111111111111111, 0.18375074871336017), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.0, 0.5733333333333334), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.5, 0.3833333333333333), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.5, 0.13793103448275862), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.0, 0.5481268799562483), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.3333333333333333, 0.4284089854265292), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.0, 0.47619064143876183), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.3333333333333333, 0.30238095238095236), 1: None, 2: None, 3: None, 4: None}, '9': {0: (1.0, 0.22580645161290322), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.4, 0.21819580491307247), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.3333333333333333, 0.4946581196581197), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.0, 0.24007936507936506), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.0, 0.2276107317927171), 1: None, 2: None, 3: None, 4: None}}, 4: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 5: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 8: {2: {'A': {0: (0.1260504201680674, 0.20384742971049094), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.32786885245901654, 0.45138048376766143), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.3650793650793651, 0.4735977184148374), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.3787878787878788, 0.5142752697073047), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.4833333333333332, 0.5382681930168046), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.3983739837398374, 0.5274596073999488), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.25, 0.4990934155985208), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.2753623188405798, 0.4309503473474027), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.26356589147286813, 0.391941695434892), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.1875, 0.2975842421863591), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.1736111111111111, 0.33653719230178053), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.15107913669064757, 0.2936893103346056), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.21604938271604937, 0.3240295146489123), 1: None, 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.0, 0.20408163265306123), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.5, 0.46593468468468463), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.0, 0.6635869565217392), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.5454545454545454, 0.5357110405836044), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.7619047619047619, 0.5538022494544232), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.36363636363636365, 0.582468568114501), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.23076923076923078, 0.48030384498863393), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.3333333333333333, 0.3717861926391801), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.0, 0.3514531698201111), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.14285714285714285, 0.21442670232992816), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.15384615384615385, 0.4149241938166869), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.18181818181818182, 0.28333803877282143), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.14285714285714285, 0.3149638802889577), 1: None, 2: None, 3: None, 4: None}}, 4: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 5: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 9: {2: {'A': {0: (0.13020833333333334, 0.277177373843008), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.27397260273972596, 0.515073138143368), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.3959731543624161, 0.5314525277247333), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.46206896551724136, 0.5577719162323224), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.4046242774566474, 0.5873802022266021), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.4318181818181818, 0.5610867204436993), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.2635135135135135, 0.5870788167083062), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.2650602409638554, 0.5467881736517427), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.2122905027932961, 0.4047450515795757), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.17751479289940833, 0.3575410065395132), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.192090395480226, 0.35718073892112817), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.20430107526881724, 0.3566117603025422), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.2275449101796408, 0.36448772575819277), 1: None, 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.15789473684210525, 0.2810322372669029), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.10526315789473684, 0.5426031976723941), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.5, 0.5694763205828777), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.3333333333333333, 0.4191206705449585), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.5882352941176471, 0.6501863354037266), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.4, 0.6119417061171447), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.16666666666666666, 0.5548557148106689), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.17391304347826086, 0.5517249550805906), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.09090909090909091, 0.484011579516098), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.0, 0.34351067657519263), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.2777777777777778, 0.35405419115573666), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.3157894736842105, 0.380679682289439), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.18518518518518517, 0.33624979763872215), 1: None, 2: None, 3: None, 4: None}}, 4: {'A': {0: (0.0, 0.5555555555555556), 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.0, 0.9166666666666667), 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.0, 1.0), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 5: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 10: {2: {'A': {0: (0.13513513513513514, 0.30310193379474093), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.3485714285714287, 0.5805226295342225), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.40340909090909083, 0.6195861678046782), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.47398843930635837, 0.6015351152428632), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.4072164948453608, 0.6171468726311236), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.4606741573033707, 0.6137139585273333), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.2662337662337662, 0.6355415885245231), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.16574585635359126, 0.5681217208728527), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.18041237113402064, 0.5507762031252192), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.26285714285714296, 0.43237904762547663), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.19642857142857142, 0.42709339439783245), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.19895287958115182, 0.41010013311620896), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.25252525252525254, 0.42538591900868866), 1: None, 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.04, 0.2633740639755678), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.2857142857142857, 0.6885859169145971), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.625, 0.665144025686202), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.4074074074074074, 0.6223380671841926), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.5294117647058824, 0.7258053221288514), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.42857142857142855, 0.635404072638463), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.3333333333333333, 0.6784583802722935), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.15384615384615385, 0.6225982793954781), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.24, 0.6979299938479723), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.20689655172413793, 0.3793485147412033), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.11538461538461539, 0.4074810664632429), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.2647058823529412, 0.4308299984804612), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.2, 0.48580855428477565), 1: None, 2: None, 3: None, 4: None}}, 4: {'A': {0: (0.3333333333333333, 0.07692307692307693), 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: (1.0, 0.8571428571428571), 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.5, 0.3333333333333333), 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.0, 0.8333333333333334), 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: (1.0, 1.0), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.0, 0.4), 1: None, 2: None, 3: None, 4: None}}, 5: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 11: {2: {'A': {0: (0.13397129186602877, 0.3691705061214646), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.33170731707317075, 0.6104069233843824), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.32701421800947855, 0.5835459610539956), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.39252336448598124, 0.6564006157179855), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.4343891402714932, 0.6706510221858538), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.4263959390862944, 0.6168171174212859), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.23076923076923078, 0.6108307849958705), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.27000000000000013, 0.6208349178890251), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.23981900452488686, 0.5564170795731257), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.17727272727272728, 0.4717446798120193), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.2318840579710145, 0.45568287488509496), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.22869955156950691, 0.4984154213078719), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.1863636363636364, 0.47698855438464255), 1: None, 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.13953488372093023, 0.29026947533242337), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.2857142857142857, 0.6093853002490438), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.3448275862068966, 0.5866760957701017), 1: None, 2: None, 3: None, 4: None}, '4': {0: (0.44680851063829785, 0.5909631560911607), 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.5714285714285714, 0.6591659272404614), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.43478260869565216, 0.7267614407108869), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.16666666666666674, 0.6303758869365754), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.2, 0.7056973200774846), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.33962264150943405, 0.6746835593000425), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.27272727272727276, 0.4619982467189612), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.18421052631578946, 0.5924626685538109), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.25, 0.5225566349148052), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.3, 0.4354760919966702), 1: None, 2: None, 3: None, 4: None}}, 4: {'A': {0: (0.5, 0.41666666666666663), 1: None, 2: None, 3: None, 4: None}, '2': {0: (0.0, 1.0), 1: None, 2: None, 3: None, 4: None}, '3': {0: (0.3333333333333333, 1.0), 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: (0.0, 0.5), 1: None, 2: None, 3: None, 4: None}, '6': {0: (0.5, 0.7), 1: None, 2: None, 3: None, 4: None}, '7': {0: (0.2, 0.7), 1: None, 2: None, 3: None, 4: None}, '8': {0: (0.3333333333333333, 0.5416666666666666), 1: None, 2: None, 3: None, 4: None}, '9': {0: (0.25, 0.6875), 1: None, 2: None, 3: None, 4: None}, 'T': {0: (0.0, 0.0), 1: None, 2: None, 3: None, 4: None}, 'J': {0: (0.6666666666666666, 1.0), 1: None, 2: None, 3: None, 4: None}, 'Q': {0: (0.3333333333333333, 0.375), 1: None, 2: None, 3: None, 4: None}, 'K': {0: (0.0, 0.0), 1: None, 2: None, 3: None, 4: None}}, 5: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 12: {2: {'A': {0: (0.13493975903614455, 0.1624061318298178), 1: None, 2: (0.0, 0.2861190025252526), 3: None, 4: None}, '2': {0: (0.36781609195402293, 0.349454463066593), 1: None, 2: (0.5238095238095238, 0.7062794348508635), 3: None, 4: None}, '3': {0: (0.3900709219858156, 0.34899316438820377), 1: None, 2: (0.4, 0.6026038386564703), 3: None, 4: None}, '4': {0: (0.4070080862533694, 0.3755361224626114), 1: None, 2: (0.47058823529411764, 0.5509612269816353), 3: None, 4: None}, '5': {0: (0.4593967517401392, 0.4159446846696459), 1: None, 2: (0.375, 0.6084110122681551), 3: None, 4: None}, '6': {0: (0.4117647058823528, 0.38480040454037095), 1: None, 2: (0.5, 0.5820887445887446), 3: None, 4: None}, '7': {0: (0.22015915119363394, 0.36138111858720345), 1: None, 2: (0.3333333333333333, 0.5732690445743515), 3: None, 4: None}, '8': {0: (0.20947630922693275, 0.32250654659585926), 1: None, 2: (0.34782608695652173, 0.5012884292935444), 3: None, 4: None}, '9': {0: (0.1926121372031661, 0.27167362099957426), 1: None, 2: (0.0, 0.3917821450141018), 3: None, 4: None}, 'T': {0: (0.20518867924528306, 0.2735660089794683), 1: None, 2: (0.2, 0.5020792915931804), 3: None, 4: None}, 'J': {0: (0.2026315789473684, 0.2778691701275279), 1: None, 2: (0.22727272727272727, 0.49391905685611975), 3: None, 4: None}, 'Q': {0: (0.20243902439024397, 0.23505269262078513), 1: None, 2: (0.2916666666666667, 0.38743059092323806), 3: None, 4: None}, 'K': {0: (0.20460358056265987, 0.29379192857730296), 1: None, 2: (0.3333333333333333, 0.5292749134095802), 3: None, 4: None}}, 3: {'A': {0: (0.1320754716981132, 0.23407870298918673), 1: (0.11363636363636363, 0.21373546394599438), 2: (0.09090909090909091, 0.12954545454545457), 3: None, 4: None}, '2': {0: (0.4, 0.3441944429821925), 1: (0.37735849056603776, 0.30044561102419526), 2: (0.46153846153846156, 0.2807692307692308), 3: None, 4: None}, '3': {0: (0.45454545454545453, 0.3832404222179891), 1: (0.37254901960784315, 0.2740223749986086), 2: (0.21052631578947367, 0.4532485058800849), 3: None, 4: None}, '4': {0: (0.5, 0.41153915681541703), 1: (0.38596491228070173, 0.3488886289989283), 2: (0.2727272727272727, 0.41025641025641024), 3: None, 4: None}, '5': {0: (0.3695652173913043, 0.45497454293643746), 1: (0.5399999999999999, 0.3441212492594758), 2: (0.47619047619047616, 0.32668178382464097), 3: None, 4: None}, '6': {0: (0.41071428571428575, 0.4208048913692097), 1: (0.4444444444444444, 0.44141689754199415), 2: (0.42857142857142855, 0.39360639360639355), 3: None, 4: None}, '7': {0: (0.34545454545454546, 0.33485490688137093), 1: (0.33962264150943394, 0.3122948840008997), 2: (0.08695652173913043, 0.30916149068322973), 3: None, 4: None}, '8': {0: (0.22058823529411764, 0.3445109236284476), 1: (0.14814814814814808, 0.23995897735269547), 2: (0.17647058823529413, 0.3267188693659282), 3: None, 4: None}, '9': {0: (0.14035087719298245, 0.34048711253617653), 1: (0.3148148148148148, 0.31849205954793913), 2: (0.2222222222222222, 0.24642246256829584), 3: None, 4: None}, 'T': {0: (0.14814814814814808, 0.25855046248119107), 1: (0.15789473684210534, 0.23453055710717272), 2: (0.35, 0.4713734567901235), 3: None, 4: None}, 'J': {0: (0.21875, 0.28844186374468067), 1: (0.16666666666666674, 0.308773353642378), 2: (0.07692307692307693, 0.3106156663848971), 3: None, 4: None}, 'Q': {0: (0.13114754098360656, 0.2825062411200628), 1: (0.31578947368421056, 0.20416177348955056), 2: (0.20833333333333334, 0.37637774806892454), 3: None, 4: None}, 'K': {0: (0.27450980392156865, 0.39791346100922786), 1: (0.19696969696969696, 0.28416209349009636), 2: (0.2857142857142857, 0.37576177999110333), 3: None, 4: None}}, 4: {'A': {0: (0.0, 0.0), 1: (0.16666666666666666, 0.2909356725146199), 2: (0.0, 0.3333333333333333), 3: None, 4: None}, '2': {0: (0.0, 0.0), 1: (0.3333333333333333, 0.3046128707893414), 2: (0.3333333333333333, 0.5555555555555555), 3: None, 4: None}, '3': {0: (0.25, 0.41666666666666663), 1: (0.1875, 0.3794356684981685), 2: (0.0, 0.25), 3: None, 4: None}, '4': {0: (0.0, 0.0), 1: (0.4117647058823529, 0.3169550173010381), 2: (0.5, 0.40909090909090917), 3: None, 4: None}, '5': {0: (1.0, 0.5), 1: (0.4444444444444444, 0.6230271785827342), 2: (0.4, 0.42000000000000004), 3: None, 4: None}, '6': {0: (0.3333333333333333, 0.48888888888888893), 1: (0.4117647058823529, 0.43613445378151267), 2: (0.8, 0.5035714285714286), 3: None, 4: None}, '7': {0: (0.375, 0.5666666666666667), 1: (0.46153846153846156, 0.2863834883065652), 2: (0.25, 0.40183823529411766), 3: None, 4: None}, '8': {0: (0.0, 0.5), 1: (0.35714285714285715, 0.4886457214464734), 2: (0.5454545454545454, 0.30383707201889015), 3: None, 4: None}, '9': {0: (0.16666666666666666, 0.3632478632478633), 1: (0.125, 0.2916666666666667), 2: (0.5714285714285714, 0.19047619047619047), 3: None, 4: None}, 'T': {0: (0.25, 0.375), 1: (0.3125, 0.11119505494505494), 2: (0.25, 0.1375), 3: None, 4: None}, 'J': {0: (0.0, 0.0), 1: (0.2777777777777778, 0.2750301195747116), 2: (0.0, 0.10416666666666666), 3: (1.0, 1.0), 4: None}, 'Q': {0: (0.0, 0.10416666666666667), 1: (0.25, 0.14285714285714282), 2: (0.3333333333333333, 0.39166666666666666), 3: None, 4: None}, 'K': {0: (0.0, 0.2333333333333333), 1: (0.4375, 0.3762517507002801), 2: (0.2857142857142857, 0.5227272727272727), 3: None, 4: None}}, 5: {'A': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.25), 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: (1.0, 0.6666666666666666), 3: None, 4: None}, '4': {0: None, 1: None, 2: (1.0, 0.5), 3: None, 4: None}, '5': {0: None, 1: (1.0, 0.0), 2: (1.0, 1.0), 3: None, 4: None}, '6': {0: None, 1: (0.0, 0.0), 2: None, 3: (1.0, 0.0), 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: (0.0, 0.5), 4: None}, '9': {0: None, 1: None, 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: None}, 'T': {0: None, 1: (0.0, 0.0), 2: (1.0, 1.0), 3: (1.0, 0.3333333333333333), 4: None}, 'J': {0: None, 1: None, 2: (0.0, 0.5), 3: (0.0, 0.0), 4: None}, 'Q': {0: None, 1: (0.0, 0.5), 2: (1.0, 0.0), 3: None, 4: None}, 'K': {0: (0.0, 0.0), 1: None, 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: None, 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: None, 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: None, 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 13: {2: {'A': {0: (0.1457800511508951, 0.16811079634030876), 1: (0.09615384615384616, 0.2377840100924787), 2: None, 3: None, 4: None}, '2': {0: (0.3676092544987147, 0.289553358247112), 1: (0.276595744680851, 0.4738966203485043), 2: None, 3: None, 4: None}, '3': {0: (0.4066666666666666, 0.3475105697286562), 1: (0.3582089552238806, 0.5242336317080695), 2: None, 3: None, 4: None}, '4': {0: (0.3963254593175853, 0.35242619005124626), 1: (0.42, 0.48213780975233933), 2: None, 3: None, 4: None}, '5': {0: (0.47733333333333333, 0.3430329213934929), 1: (0.3448275862068966, 0.5217510694666213), 2: None, 3: None, 4: None}, '6': {0: (0.4190981432360744, 0.35317517102778373), 1: (0.4230769230769231, 0.500666573398387), 2: None, 3: None, 4: None}, '7': {0: (0.25336927223719674, 0.33244153213932826), 1: (0.21311475409836064, 0.4528041762684749), 2: None, 3: None, 4: None}, '8': {0: (0.21563342318059292, 0.309969292830035), 1: (0.3050847457627119, 0.41105997187065463), 2: None, 3: None, 4: None}, '9': {0: (0.2537688442211054, 0.30083502057673983), 1: (0.26666666666666666, 0.41397322912898754), 2: None, 3: None, 4: None}, 'T': {0: (0.21293800539083557, 0.24160110408298632), 1: (0.3333333333333333, 0.4430095139441714), 2: None, 3: None, 4: None}, 'J': {0: (0.208219178082192, 0.22682316649899695), 1: (0.1690140845070422, 0.33530953148415077), 2: None, 3: None, 4: None}, 'Q': {0: (0.25000000000000006, 0.23781447083820548), 1: (0.17307692307692307, 0.3353516972995153), 2: None, 3: None, 4: None}, 'K': {0: (0.2270408163265306, 0.256404947938174), 1: (0.23728813559322032, 0.3733031215928433), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.07228915662650602, 0.16810195006249898), 1: (0.14754098360655737, 0.1534168162473828), 2: None, 3: None, 4: None}, '2': {0: (0.4375, 0.3631671408391744), 1: (0.3604651162790699, 0.3425059209867096), 2: None, 3: (1.0, 1.0), 4: None}, '3': {0: (0.4000000000000001, 0.2907398037260242), 1: (0.37037037037037035, 0.35446572608506544), 2: None, 3: None, 4: None}, '4': {0: (0.31428571428571433, 0.41203652870480767), 1: (0.38144329896907225, 0.3073110467360126), 2: None, 3: (0.0, 1.0), 4: None}, '5': {0: (0.5254237288135596, 0.24072595360915175), 1: (0.40909090909090917, 0.3815540409676224), 2: None, 3: (0.3333333333333333, 0.3333333333333333), 4: None}, '6': {0: (0.4142857142857143, 0.3038240528858378), 1: (0.37500000000000006, 0.36049488457018686), 2: None, 3: (0.0, 0.0), 4: None}, '7': {0: (0.1917808219178082, 0.3245238448771549), 1: (0.3076923076923078, 0.27662716087308437), 2: None, 3: None, 4: None}, '8': {0: (0.2222222222222222, 0.4088740678925722), 1: (0.26804123711340205, 0.35294849727041844), 2: None, 3: None, 4: None}, '9': {0: (0.2558139534883721, 0.3017455061046825), 1: (0.19000000000000003, 0.3543056978496098), 2: None, 3: None, 4: None}, 'T': {0: (0.24050632911392406, 0.26039631361684373), 1: (0.2127659574468085, 0.2622237159336539), 2: None, 3: (0.0, 1.0), 4: None}, 'J': {0: (0.2235294117647059, 0.290397569909765), 1: (0.23853211009174308, 0.29190141435940864), 2: None, 3: (1.0, 0.25), 4: None}, 'Q': {0: (0.16417910447761194, 0.31662396519263314), 1: (0.19801980198019803, 0.26483932329194615), 2: None, 3: (0.0, 0.0), 4: None}, 'K': {0: (0.17948717948717952, 0.31226697905465434), 1: (0.14705882352941185, 0.262658588371095), 2: None, 3: None, 4: None}}, 4: {'A': {0: (0.125, 0.1076923076923077), 1: (0.0, 0.08198273461431357), 2: (0.25, 0.65), 3: (0.0, 0.0), 4: None}, '2': {0: (0.2, 0.25), 1: (0.3125, 0.484876979638009), 2: (0.0, 0.5317460317460317), 3: None, 4: None}, '3': {0: (0.0, 0.2333333333333333), 1: (0.625, 0.4031192765567766), 2: (0.16666666666666666, 0.27777777777777773), 3: None, 4: None}, '4': {0: (0.5, 0.5833333333333334), 1: (0.6842105263157895, 0.450735294117647), 2: (0.42857142857142855, 0.4884353741496598), 3: (1.0, 1.0), 4: None}, '5': {0: (0.6, 0.6020833333333333), 1: (0.4782608695652174, 0.49069813143039676), 2: (0.6666666666666666, 0.6666666666666666), 3: (0.0, 0.0), 4: None}, '6': {0: (0.6666666666666666, 0.5222222222222223), 1: (0.4, 0.3346666666666666), 2: (0.6666666666666666, 0.2604166666666667), 3: (0.0, 0.0), 4: None}, '7': {0: (0.3333333333333333, 0.5962962962962962), 1: (0.2222222222222222, 0.21544312169312174), 2: (0.2, 0.6729411764705882), 3: (0.5, 0.5), 4: None}, '8': {0: (0.125, 0.3125), 1: (0.21739130434782608, 0.25381989180111403), 2: (0.1111111111111111, 0.380952380952381), 3: None, 4: None}, '9': {0: (0.1, 0.42628205128205127), 1: (0.23076923076923078, 0.31102564102564106), 2: (0.4, 0.1875), 3: None, 4: None}, 'T': {0: (0.2, 0.21428571428571427), 1: (0.18181818181818182, 0.18766418766418766), 2: (0.25, 0.125), 3: (0.0, 1.0), 4: None}, 'J': {0: (0.125, 0.0), 1: (0.14285714285714285, 0.17846751603867353), 2: (0.0, 0.20340909090909093), 3: (0.0, 0.0), 4: None}, 'Q': {0: (0.2857142857142857, 0.21428571428571425), 1: (0.08, 0.3233492781728075), 2: (0.42857142857142855, 0.41666666666666663), 3: None, 4: None}, 'K': {0: (0.16666666666666666, 0.2333333333333333), 1: (0.28, 0.220563025210084), 2: (0.2857142857142857, 0.5170454545454545), 3: (0.0, 1.0), 4: None}}, 5: {'A': {0: (0.0, 0.0), 1: (1.0, 0.6666666666666666), 2: None, 3: None, 4: None}, '2': {0: None, 1: (0.0, 0.0), 2: (0.5, 0.75), 3: None, 4: None}, '3': {0: None, 1: (0.5, 0.0), 2: (0.0, 0.2), 3: None, 4: None}, '4': {0: None, 1: (0.75, 0.4), 2: None, 3: None, 4: None}, '5': {0: None, 1: (0.5, 0.5), 2: (0.75, 0.5), 3: None, 4: None}, '6': {0: (1.0, 0.0), 1: (0.6666666666666666, 0.6666666666666666), 2: (0.5, 0.5), 3: (1.0, 1.0), 4: None}, '7': {0: None, 1: (0.0, 0.6666666666666666), 2: (0.5, 0.375), 3: None, 4: None}, '8': {0: None, 1: (1.0, 1.0), 2: (0.0, 0.9), 3: None, 4: None}, '9': {0: None, 1: (1.0, 1.0), 2: (0.6666666666666666, 0.0), 3: None, 4: None}, 'T': {0: (0.0, 0.0), 1: None, 2: (0.2, 0.2), 3: (0.0, 0.0), 4: None}, 'J': {0: None, 1: None, 2: (0.5, 0.8333333333333333), 3: (0.0, 0.5), 4: None}, 'Q': {0: None, 1: (0.3333333333333333, 0.3333333333333333), 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: (1.0, 0.0), 3: (0.0, 0.0), 4: None}}, 6: {'A': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: (0.0, 0.0)}, '8': {0: None, 1: None, 2: (1.0, 0.0), 3: None, 4: None}, '9': {0: None, 1: None, 2: (0.5, 0.5), 3: None, 4: None}, 'T': {0: None, 1: None, 2: None, 3: None, 4: None}, 'J': {0: None, 1: (1.0, 0.0), 2: (1.0, 1.0), 3: None, 4: None}, 'Q': {0: None, 1: None, 2: (1.0, 1.0), 3: None, 4: None}, 'K': {0: None, 1: None, 2: None, 3: None, 4: None}}}, 14: {2: {'A': {0: (0.10029498525073749, 0.15795920043589795), 1: (0.16666666666666669, 0.26399948858194583), 2: None, 3: None, 4: None}, '2': {0: (0.34864864864864864, 0.3065079675651061), 1: (0.16666666666666666, 0.5030488861690712), 2: None, 3: None, 4: None}, '3': {0: (0.3537234042553193, 0.2616690812716671), 1: (0.34285714285714286, 0.5041184193052204), 2: None, 3: None, 4: None}, '4': {0: (0.3730407523510973, 0.2781591927974679), 1: (0.3793103448275862, 0.566523520480745), 2: None, 3: None, 4: None}, '5': {0: (0.43413173652694603, 0.32296090608802874), 1: (0.3620689655172414, 0.634985413583946), 2: None, 3: None, 4: None}, '6': {0: (0.46920821114369504, 0.3014952170242612), 1: (0.5079365079365081, 0.5230370502758297), 2: None, 3: None, 4: None}, '7': {0: (0.2556179775280899, 0.31070305820472066), 1: (0.36507936507936506, 0.4625044148612125), 2: None, 3: None, 4: None}, '8': {0: (0.2091836734693878, 0.2768209182181118), 1: (0.1935483870967742, 0.47607232779547165), 2: None, 3: None, 4: None}, '9': {0: (0.2664576802507841, 0.26019023695470217), 1: (0.2714285714285714, 0.4738719458865663), 2: None, 3: None, 4: None}, 'T': {0: (0.19756838905775082, 0.1959301290389003), 1: (0.15094339622641503, 0.3559623625739031), 2: None, 3: None, 4: None}, 'J': {0: (0.22222222222222218, 0.23007336168603876), 1: (0.2692307692307694, 0.3703665942449223), 2: None, 3: None, 4: None}, 'Q': {0: (0.18208092485549138, 0.21120208949142633), 1: (0.1538461538461538, 0.37173256544355265), 2: None, 3: None, 4: None}, 'K': {0: (0.21388888888888888, 0.22993863014667898), 1: (0.2222222222222222, 0.33355152291982926), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.13043478260869565, 0.1484534317159359), 1: (0.08064516129032255, 0.24707944777222976), 2: (0.0, 0.14583333333333334), 3: None, 4: None}, '2': {0: (0.351063829787234, 0.27895647800994294), 1: (0.35294117647058826, 0.31763350306828564), 2: (1.0, 0.7857142857142857), 3: None, 4: None}, '3': {0: (0.36274509803921573, 0.2790932094639949), 1: (0.3372093023255814, 0.33706177847926116), 2: (0.2, 0.6401709401709402), 3: None, 4: None}, '4': {0: (0.4716981132075472, 0.2906484885220202), 1: (0.49462365591397855, 0.2718468574098521), 2: (0.2857142857142857, 0.4736313573048267), 3: None, 4: None}, '5': {0: (0.5566037735849055, 0.26517540421164076), 1: (0.5454545454545454, 0.33258905272607436), 2: (0.2, 0.5054554334554334), 3: None, 4: None}, '6': {0: (0.41237113402061853, 0.3295851491306568), 1: (0.43037974683544306, 0.32617259727196557), 2: (0.7142857142857143, 0.6809523809523809), 3: None, 4: None}, '7': {0: (0.32558139534883723, 0.28206947309406427), 1: (0.2705882352941177, 0.32863551129393787), 2: (0.0, 0.7142857142857143), 3: None, 4: None}, '8': {0: (0.23015873015873017, 0.31601839830341466), 1: (0.19753086419753085, 0.3140945055286802), 2: (0.25, 0.4419191919191919), 3: None, 4: None}, '9': {0: (0.256198347107438, 0.2638461115502647), 1: (0.3152173913043479, 0.2571901917034726), 2: (0.125, 0.3886422821969698), 3: None, 4: None}, 'T': {0: (0.1326530612244898, 0.18230015551397893), 1: (0.20652173913043478, 0.23752483621773654), 2: (0.6666666666666666, 0.5833333333333334), 3: None, 4: None}, 'J': {0: (0.19166666666666668, 0.2796706274755057), 1: (0.24418604651162795, 0.22198391165618572), 2: (0.0, 0.4337797619047619), 3: None, 4: None}, 'Q': {0: (0.16000000000000006, 0.21803601410427265), 1: (0.10869565217391308, 0.2692396751694578), 2: (0.0, 0.25917366946778714), 3: None, 4: None}, 'K': {0: (0.15384615384615383, 0.20802506575260127), 1: (0.13793103448275862, 0.2465747038795248), 2: (0.0, 0.5158067517278043), 3: None, 4: None}}, 4: {'A': {0: (0.08333333333333333, 0.22364672364672367), 1: (0.0625, 0.10218253968253968), 2: (0.0, 0.09166666666666667), 3: None, 4: None}, '2': {0: (0.5, 0.6875), 1: (0.3333333333333333, 0.43995098039215685), 2: (0.4, 0.1893162393162393), 3: None, 4: None}, '3': {0: (0.0, 0.2), 1: (0.3181818181818182, 0.31255411255411253), 2: (0.4166666666666667, 0.22222222222222224), 3: None, 4: None}, '4': {0: (0.7142857142857143, 0.2857142857142857), 1: (0.5384615384615384, 0.2424679487179487), 2: (0.2222222222222222, 0.41507936507936516), 3: None, 4: None}, '5': {0: (0.5714285714285714, 0.3333333333333333), 1: (0.5652173913043478, 0.29567415379772355), 2: (0.3076923076923077, 0.3153846153846154), 3: None, 4: None}, '6': {0: (0.5714285714285714, 0.37346938775510213), 1: (0.37037037037037035, 0.24216524216524224), 2: (0.5333333333333333, 0.31460317460317455), 3: None, 4: None}, '7': {0: (0.0, 0.21428571428571427), 1: (0.21052631578947367, 0.3000771158665895), 2: (0.5, 0.4814705882352941), 3: None, 4: None}, '8': {0: (0.1, 0.20357142857142857), 1: (0.2, 0.3390922158337019), 2: (0.4444444444444444, 0.1950937950937951), 3: None, 4: None}, '9': {0: (0.23076923076923078, 0.34263172724711183), 1: (0.21052631578947367, 0.291812865497076), 2: (0.25, 0.2586016414141414), 3: None, 4: None}, 'T': {0: (0.29411764705882354, 0.2698412698412698), 1: (0.5, 0.14399446707139013), 2: (0.125, 0.5381944444444444), 3: None, 4: None}, 'J': {0: (0.4, 0.03333333333333333), 1: (0.24, 0.18083744465528145), 2: (0.14285714285714285, 0.3154761904761904), 3: None, 4: None}, 'Q': {0: (0.08333333333333333, 0.3888888888888889), 1: (0.20833333333333334, 0.3588307117718883), 2: (0.1, 0.09833333333333334), 3: None, 4: None}, 'K': {0: (0.3, 0.06000000000000001), 1: (0.3448275862068966, 0.20938496088090403), 2: (0.3, 0.34326298701298696), 3: None, 4: None}}, 5: {'A': {0: (0.0, 0.0), 1: (0.0, 0.0), 2: (0.0, 0.1111111111111111), 3: None, 4: None}, '2': {0: None, 1: (0.3333333333333333, 0.3333333333333333), 2: (0.625, 0.1875), 3: (1.0, 0.0), 4: None}, '3': {0: None, 1: (0.5, 0.5), 2: None, 3: (0.0, 1.0), 4: None}, '4': {0: None, 1: (0.25, 0.0), 2: (1.0, 1.0), 3: None, 4: None}, '5': {0: (0.0, 0.0), 1: (0.0, 0.1875), 2: (0.5, 0.75), 3: (0.0, 0.0), 4: None}, '6': {0: None, 1: (0.3333333333333333, 0.3333333333333333), 2: (1.0, 0.5), 3: None, 4: None}, '7': {0: None, 1: (0.0, 1.0), 2: (0.42857142857142855, 0.4642857142857143), 3: None, 4: None}, '8': {0: None, 1: (0.16666666666666666, 0.16666666666666666), 2: (0.0, 0.3333333333333333), 3: None, 4: None}, '9': {0: None, 1: (1.0, 0.0), 2: (0.5, 0.0), 3: None, 4: None}, 'T': {0: (0.0, 0.0), 1: (0.16666666666666666, 0.07142857142857142), 2: (0.0, 0.25), 3: (0.0, 1.0), 4: None}, 'J': {0: None, 1: (0.0, 0.25), 2: (0.25, 0.25), 3: None, 4: None}, 'Q': {0: None, 1: None, 2: (0.4, 0.4), 3: None, 4: None}, 'K': {0: None, 1: (0.0, 0.16666666666666666), 2: (0.125, 0.0625), 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: (0.0, 0.5), 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: None, 3: None, 4: None}, '4': {0: None, 1: None, 2: (1.0, 1.0), 3: (0.0, 1.0), 4: None}, '5': {0: None, 1: None, 2: (1.0, 1.0), 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: None, 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}, '9': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, 'T': {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 0.5), 4: None}, 'J': {0: None, 1: (0.0, 0.0), 2: None, 3: None, 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 1.0), 4: None}}}, 15: {2: {'A': {0: (0.1165644171779141, 0.12943843344314623), 1: (0.1111111111111111, 0.24953951094879606), 2: None, 3: None, 4: None}, '2': {0: (0.3507692307692309, 0.25988927920835675), 1: (0.41509433962264153, 0.46366780782038014), 2: None, 3: None, 4: None}, '3': {0: (0.367741935483871, 0.26849337931380585), 1: (0.48214285714285715, 0.5670329908321975), 2: None, 3: None, 4: None}, '4': {0: (0.4112676056338027, 0.2761997131414014), 1: (0.4782608695652174, 0.42089844439552077), 2: None, 3: None, 4: None}, '5': {0: (0.47104247104247116, 0.2870801679819527), 1: (0.4117647058823529, 0.5357450715739893), 2: None, 3: None, 4: None}, '6': {0: (0.4205882352941178, 0.2892104302585399), 1: (0.36538461538461536, 0.5328806449939775), 2: None, 3: None, 4: None}, '7': {0: (0.26708074534161486, 0.2956486157102688), 1: (0.22448979591836735, 0.4140949122728382), 2: None, 3: None, 4: None}, '8': {0: (0.2521994134897361, 0.2384620182902445), 1: (0.2352941176470588, 0.436450607959769), 2: None, 3: None, 4: None}, '9': {0: (0.21854304635761584, 0.26097765455519223), 1: (0.2545454545454545, 0.3694062858538229), 2: None, 3: None, 4: None}, 'T': {0: (0.22530864197530864, 0.21354312834251962), 1: (0.21428571428571427, 0.3173723669275531), 2: None, 3: None, 4: None}, 'J': {0: (0.22418879056047197, 0.19746107484407469), 1: (0.30909090909090914, 0.32024154318766757), 2: None, 3: None, 4: None}, 'Q': {0: (0.20987654320987653, 0.1844918750812649), 1: (0.2028985507246377, 0.3591404986011309), 2: None, 3: None, 4: None}, 'K': {0: (0.21269841269841266, 0.2097377657313938), 1: (0.273972602739726, 0.3966498632495503), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.08333333333333333, 0.11344789558595246), 1: (0.07352941176470588, 0.18324796385573924), 2: (0.0, 0.334375), 3: None, 4: None}, '2': {0: (0.3191489361702128, 0.25293353876667546), 1: (0.3406593406593407, 0.2881499934531486), 2: (0.16666666666666666, 0.4257936507936508), 3: None, 4: None}, '3': {0: (0.41044776119402987, 0.27016013330574734), 1: (0.3917525773195876, 0.2954990288360975), 2: (0.0, 0.6296296296296297), 3: None, 4: None}, '4': {0: (0.43125, 0.2672948566039559), 1: (0.2191780821917808, 0.2629031974163996), 2: (0.6, 0.36668934240362816), 3: None, 4: None}, '5': {0: (0.4388489208633093, 0.2590197159042951), 1: (0.37349397590361444, 0.2871380599069305), 2: (1.0, 0.42000000000000004), 3: None, 4: None}, '6': {0: (0.38666666666666677, 0.2723346154470358), 1: (0.4891304347826087, 0.34806775904976817), 2: (0.16666666666666666, 0.4361111111111111), 3: None, 4: None}, '7': {0: (0.21897810218978106, 0.3344564644315924), 1: (0.2571428571428572, 0.2801436482811779), 2: (0.25, 0.6258377100840337), 3: None, 4: None}, '8': {0: (0.273972602739726, 0.3636072735629767), 1: (0.28865979381443296, 0.21519945328876774), 2: (0.3333333333333333, 0.5652657527657527), 3: None, 4: None}, '9': {0: (0.2054794520547945, 0.19222800627746406), 1: (0.2261904761904762, 0.2531822159063055), 2: (0.16666666666666666, 0.606967106967107), 3: None, 4: None}, 'T': {0: (0.22560975609756098, 0.16303686047965302), 1: (0.2571428571428571, 0.22714770189152347), 2: (0.3333333333333333, 0.4448559670781893), 3: None, 4: None}, 'J': {0: (0.21794871794871795, 0.20903669761549684), 1: (0.21739130434782614, 0.2293898950568478), 2: (0.0, 0.46651785714285715), 3: None, 4: None}, 'Q': {0: (0.19858156028368795, 0.2194094849792295), 1: (0.2112676056338028, 0.2276236728355281), 2: (0.0, 0.398051948051948), 3: None, 4: None}, 'K': {0: (0.18518518518518526, 0.23597681521257602), 1: (0.3529411764705883, 0.20413478299130602), 2: (0.0, 0.4125631313131313), 3: None, 4: None}}, 4: {'A': {0: (0.1111111111111111, 0.13675213675213677), 1: (0.14285714285714285, 0.1254724111866969), 2: (0.25, 0.1625), 3: None, 4: None}, '2': {0: (0.3125, 0.20572916666666666), 1: (0.3333333333333333, 0.3019312468577174), 2: (0.25, 0.20141432641432644), 3: None, 4: None}, '3': {0: (0.6, 0.46380952380952384), 1: (0.4444444444444444, 0.2629019129019129), 2: (0.4444444444444444, 0.35185185185185186), 3: (0.0, 0.0), 4: None}, '4': {0: (0.3333333333333333, 0.20777777777777778), 1: (0.40625, 0.2551011029411764), 2: (0.2857142857142857, 0.30612244897959184), 3: (0.5, 0.0), 4: None}, '5': {0: (0.6666666666666666, 0.35978835978835977), 1: (0.41379310344827586, 0.27527262010020637), 2: (0.5, 0.41), 3: None, 4: None}, '6': {0: (0.4444444444444444, 0.30000000000000004), 1: (0.3548387096774194, 0.3440198511166253), 2: (0.25, 0.10892857142857143), 3: None, 4: None}, '7': {0: (0.21428571428571427, 0.2384353741496599), 1: (0.3103448275862069, 0.1815981432360743), 2: (0.5, 0.22083333333333335), 3: None, 4: None}, '8': {0: (0.25, 0.30312500000000003), 1: (0.25, 0.26708063608218413), 2: (0.3333333333333333, 0.44040404040404035), 3: None, 4: None}, '9': {0: (0.35294117647058826, 0.1583171730230554), 1: (0.15384615384615385, 0.21230769230769225), 2: (0.6666666666666666, 0.2121212121212121), 3: None, 4: None}, 'T': {0: (0.15384615384615385, 0.15140415140415142), 1: (0.13513513513513514, 0.1320778820778821), 2: (0.16666666666666666, 0.36234567901234566), 3: (0.0, 1.0), 4: None}, 'J': {0: (0.23809523809523808, 0.025850340136054424), 1: (0.20000000000000004, 0.1802979829924801), 2: (0.5, 0.07575757575757576), 3: (1.0, 0.0), 4: None}, 'Q': {0: (0.15625, 0.24435763888888887), 1: (0.1935483870967742, 0.2493389911795984), 2: (0.4, 0.1733333333333333), 3: None, 4: None}, 'K': {0: (0.4117647058823529, 0.21176470588235297), 1: (0.1724137931034483, 0.16174659518980009), 2: (0.18181818181818182, 0.1322314049586777), 3: None, 4: None}}, 5: {'A': {0: (0.5, 0.5), 1: (0.0, 0.16666666666666666), 2: None, 3: None, 4: None}, '2': {0: (0.0, 1.0), 1: (0.6666666666666666, 0.5555555555555555), 2: (0.6666666666666666, 0.3333333333333333), 3: None, 4: None}, '3': {0: None, 1: (1.0, 0.0), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}, '4': {0: None, 1: (1.0, 0.0), 2: (0.3333333333333333, 0.3333333333333333), 3: (0.0, 0.0), 4: None}, '5': {0: None, 1: (0.6666666666666666, 0.0), 2: (1.0, 0.5), 3: (0.5, 0.5), 4: None}, '6': {0: (0.5, 0.0), 1: (0.7142857142857143, 0.42857142857142855), 2: (0.5, 0.0), 3: (0.0, 0.3333333333333333), 4: None}, '7': {0: (0.0, 0.0), 1: (0.16666666666666666, 0.25), 2: (0.0, 0.3333333333333333), 3: (1.0, 0.0), 4: None}, '8': {0: None, 1: (0.14285714285714285, 0.2857142857142857), 2: (0.25, 0.25), 3: None, 4: None}, '9': {0: (0.0, 0.0), 1: (0.16666666666666666, 0.3333333333333333), 2: (1.0, 0.0), 3: (0.0, 0.0), 4: None}, 'T': {0: None, 1: (0.0, 0.14285714285714285), 2: (0.0, 0.2), 3: None, 4: None}, 'J': {0: None, 1: (0.0, 0.16666666666666666), 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}, 'Q': {0: None, 1: (0.3333333333333333, 0.0), 2: (0.5, 0.0), 3: (0.0, 0.0), 4: None}, 'K': {0: (0.0, 0.0), 1: (0.25, 0.16666666666666666), 2: None, 3: None, 4: None}}, 6: {'A': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: None, 4: None}, '3': {0: None, 1: None, 2: (1.0, 0.0), 3: None, 4: None}, '4': {0: None, 1: None, 2: None, 3: (1.0, 1.0), 4: None}, '5': {0: None, 1: (0.5, 0.0), 2: (1.0, 0.0), 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: (0.0, 1.0), 3: None, 4: None}, '8': {0: None, 1: None, 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}, 'T': {0: None, 1: None, 2: (0.0, 0.0), 3: (0.0, 0.0), 4: None}, 'J': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, 'Q': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, 'K': {0: None, 1: None, 2: (1.0, 0.0), 3: None, 4: None}}}, 16: {2: {'A': {0: (0.13559322033898308, 0.139367115799466), 1: (0.13157894736842105, 0.21934688433252403), 2: None, 3: None, 4: None}, '2': {0: (0.35570469798657733, 0.26667487818565594), 1: (0.37288135593220345, 0.45283335713974987), 2: None, 3: None, 4: None}, '3': {0: (0.3786764705882352, 0.2659712797245578), 1: (0.28301886792452846, 0.509709867217395), 2: None, 3: None, 4: None}, '4': {0: (0.3401360544217686, 0.26025678799450797), 1: (0.42857142857142855, 0.524620698736469), 2: None, 3: None, 4: None}, '5': {0: (0.4444444444444444, 0.27592970952422624), 1: (0.4375, 0.5197612992174572), 2: None, 3: None, 4: None}, '6': {0: (0.42276422764227645, 0.25722360638005926), 1: (0.375, 0.48746436952891753), 2: None, 3: None, 4: None}, '7': {0: (0.23566878980891712, 0.30169106417849323), 1: (0.2033898305084746, 0.44126074532293225), 2: None, 3: None, 4: None}, '8': {0: (0.20477815699658702, 0.2675224258820241), 1: (0.3275862068965517, 0.4749728072535179), 2: None, 3: None, 4: None}, '9': {0: (0.24406779661016953, 0.2380456864475146), 1: (0.24999999999999997, 0.3840170657365381), 2: None, 3: None, 4: None}, 'T': {0: (0.19780219780219788, 0.18455830545277027), 1: (0.23255813953488372, 0.36512296624796986), 2: None, 3: None, 4: None}, 'J': {0: (0.21782178217821782, 0.18828181063720387), 1: (0.2857142857142857, 0.3461065615371211), 2: None, 3: None, 4: None}, 'Q': {0: (0.21212121212121218, 0.20926376087628454), 1: (0.2857142857142857, 0.35267349273503795), 2: None, 3: None, 4: None}, 'K': {0: (0.20224719101123592, 0.21318815288996087), 1: (0.1836734693877551, 0.3592998081680904), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.08571428571428569, 0.11699752628324057), 1: (0.11475409836065571, 0.09505917893113223), 2: (0.0, 0.11111111111111112), 3: None, 4: None}, '2': {0: (0.3624161073825504, 0.2181400752074261), 1: (0.2795698924731183, 0.3092997353231142), 2: (0.625, 0.5123015873015873), 3: None, 4: None}, '3': {0: (0.3548387096774194, 0.27120988616438), 1: (0.4942528735632183, 0.25802275031589483), 2: (0.25, 0.5396825396825398), 3: None, 4: None}, '4': {0: (0.375, 0.18317112216130446), 1: (0.4666666666666667, 0.2569462766443898), 2: (0.25, 0.4158730158730159), 3: None, 4: None}, '5': {0: (0.37748344370860926, 0.20389464326493334), 1: (0.418918918918919, 0.30545225781506846), 2: (0.2857142857142857, 0.41931972789115646), 3: None, 4: None}, '6': {0: (0.43023255813953487, 0.25819124000367694), 1: (0.4222222222222222, 0.3036077101184029), 2: (0.3333333333333333, 0.6363636363636364), 3: None, 4: None}, '7': {0: (0.29518072289156616, 0.27234853306724455), 1: (0.3181818181818183, 0.2877487233197682), 2: (0.75, 0.5625), 3: None, 4: None}, '8': {0: (0.22807017543859648, 0.2850247448490865), 1: (0.26315789473684215, 0.2743500976262132), 2: (0.25, 0.4642857142857142), 3: None, 4: None}, '9': {0: (0.2545454545454545, 0.18926503741167175), 1: (0.17977528089887632, 0.23300591517620514), 2: (0.4, 0.398386994949495), 3: None, 4: None}, 'T': {0: (0.20588235294117646, 0.17671441799002932), 1: (0.1666666666666667, 0.22174214407040074), 2: (0.2857142857142857, 0.4143628747795414), 3: None, 4: None}, 'J': {0: (0.2413793103448276, 0.17042212685610506), 1: (0.18421052631578946, 0.2287178462063836), 2: (0.4, 0.3987587412587413), 3: None, 4: None}, 'Q': {0: (0.21518987341772142, 0.17568955439835834), 1: (0.18627450980392157, 0.24734817637671225), 2: (0.0, 0.3582887700534759), 3: None, 4: None}, 'K': {0: (0.26775956284152996, 0.18405143870551252), 1: (0.1978021978021978, 0.25460802919739217), 2: (0.6, 0.48652236652236647), 3: None, 4: None}}, 4: {'A': {0: (0.15789473684210525, 0.1324465008675535), 1: (0.06451612903225806, 0.10111299754763252), 2: (0.0, 0.1111111111111111), 3: None, 4: None}, '2': {0: (0.35, 0.2683333333333333), 1: (0.375, 0.0581451330532213), 2: (0.4166666666666667, 0.379985754985755), 3: (0.0, 0.5), 4: None}, '3': {0: (0.35294117647058826, 0.26554621848739496), 1: (0.36585365853658536, 0.21983159117305456), 2: (0.35714285714285715, 0.16666666666666669), 3: None, 4: None}, '4': {0: (0.5, 0.1534090909090909), 1: (0.5599999999999998, 0.2000441176470588), 2: (0.3333333333333333, 0.06818181818181816), 3: None, 4: None}, '5': {0: (0.4, 0.2955555555555555), 1: (0.37777777777777777, 0.23229036503890307), 2: (0.5714285714285714, 0.17857142857142858), 3: None, 4: None}, '6': {0: (0.5185185185185185, 0.08774928774928777), 1: (0.40425531914893614, 0.2851063829787233), 2: (0.45454545454545453, 0.2589285714285714), 3: None, 4: None}, '7': {0: (0.2631578947368421, 0.17982456140350878), 1: (0.3137254901960784, 0.2836538461538462), 2: (0.375, 0.27058823529411763), 3: None, 4: None}, '8': {0: (0.1875, 0.25), 1: (0.08888888888888889, 0.2607930365128507), 2: (0.2857142857142857, 0.08163265306122448), 3: None, 4: None}, '9': {0: (0.4, 0.1581684981684982), 1: (0.2711864406779661, 0.2783474576271185), 2: (0.16666666666666666, 0.1313131313131313), 3: (1.0, 1.0), 4: None}, 'T': {0: (0.2903225806451613, 0.09622277364212849), 1: (0.3125, 0.18515011223344557), 2: (0.25, 0.2333333333333333), 3: (0.0, 1.0), 4: None}, 'J': {0: (0.35, 0.22000000000000003), 1: (0.08333333333333333, 0.07886754164031205), 2: (0.4, 0.12840909090909092), 3: (0.0, 0.0), 4: None}, 'Q': {0: (0.1724137931034483, 0.32346743295019154), 1: (0.1951219512195122, 0.20184989568059872), 2: (0.35294117647058826, 0.09019607843137255), 3: (0.0, 0.0), 4: None}, 'K': {0: (0.1875, 0.207421875), 1: (0.2972972972972973, 0.14930161253690666), 2: (0.26666666666666666, 0.14632034632034632), 3: None, 4: None}}, 5: {'A': {0: (0.3333333333333333, 0.3333333333333333), 1: (0.5, 0.1111111111111111), 2: (0.2, 0.06666666666666667), 3: None, 4: None}, '2': {0: (0.5, 0.0), 1: (0.6, 0.2), 2: (0.3333333333333333, 0.2222222222222222), 3: (0.5, 0.0), 4: None}, '3': {0: (0.3333333333333333, 0.16666666666666666), 1: (0.3333333333333333, 0.07407407407407407), 2: (0.3333333333333333, 0.0), 3: (1.0, 0.5), 4: None}, '4': {0: (0.6, 0.4), 1: (0.0, 0.35000000000000003), 2: (0.25, 0.0), 3: (0.0, 0.0), 4: None}, '5': {0: (0.0, 0.0), 1: (0.5714285714285714, 0.25), 2: (0.625, 0.25), 3: None, 4: None}, '6': {0: None, 1: (0.6, 0.8), 2: (0.375, 0.25), 3: None, 4: None}, '7': {0: (0.5, 0.5), 1: (0.14285714285714285, 0.23809523809523808), 2: (0.4, 0.0), 3: (0.0, 0.0), 4: None}, '8': {0: (1.0, 0.0), 1: (0.0, 0.125), 2: (0.0, 0.0), 3: None, 4: None}, '9': {0: (0.0, 1.0), 1: (0.1111111111111111, 0.2222222222222222), 2: (0.25, 0.0), 3: (1.0, 0.0), 4: None}, 'T': {0: (1.0, 1.0), 1: (0.0, 0.2857142857142857), 2: (0.0, 0.25), 3: None, 4: None}, 'J': {0: (1.0, 0.5), 1: (0.0, 0.14285714285714285), 2: (0.0, 0.16666666666666666), 3: (0.0, 0.0), 4: None}, 'Q': {0: (0.0, 0.0), 1: (0.3333333333333333, 0.2222222222222222), 2: (0.0, 0.25), 3: (0.0, 0.0), 4: None}, 'K': {0: (0.0, 0.0), 1: (0.0, 0.2), 2: (0.125, 0.125), 3: (0.0, 0.0), 4: None}}, 6: {'A': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, '2': {0: None, 1: None, 2: None, 3: (1.0, 0.0), 4: None}, '3': {0: None, 1: (0.0, 0.0), 2: (0.5, 0.0), 3: None, 4: None}, '4': {0: None, 1: None, 2: (1.0, 0.5), 3: None, 4: None}, '5': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, '6': {0: None, 1: None, 2: None, 3: None, 4: None}, '7': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, '8': {0: None, 1: (0.0, 0.0), 2: None, 3: None, 4: None}, '9': {0: None, 1: None, 2: None, 3: (0.0, 0.0), 4: None}, 'T': {0: None, 1: (0.0, 0.0), 2: None, 3: (0.0, 0.0), 4: None}, 'J': {0: None, 1: None, 2: (0.0, 0.0), 3: (1.0, 0.0), 4: None}, 'Q': {0: None, 1: None, 2: None, 3: None, 4: None}, 'K': {0: None, 1: None, 2: (0.3333333333333333, 0.3333333333333333), 3: (0.0, 0.0), 4: None}}}, 17: {2: {'A': {0: (0.13028169014084517, 0.11411033770188686), 1: (0.11627906976744186, 0.2790115842109629), 2: None, 3: None, 4: None}, '2': {0: (0.3380782918149465, 0.19697823912192336), 1: (0.46153846153846156, 0.4692869054648369), 2: None, 3: None, 4: None}, '3': {0: (0.3917525773195876, 0.25396788041704005), 1: (0.4, 0.5474523392622456), 2: None, 3: None, 4: None}, '4': {0: (0.4230769230769231, 0.19789368081495604), 1: (0.41379310344827586, 0.48716364614882046), 2: None, 3: None, 4: None}, '5': {0: (0.44680851063829785, 0.22530998214888798), 1: (0.391304347826087, 0.540991684810438), 2: None, 3: None, 4: None}, '6': {0: (0.4588235294117646, 0.2308037982610207), 1: (0.3939393939393939, 0.5905070190545373), 2: None, 3: None, 4: None}, '7': {0: (0.25233644859813076, 0.27169953863110496), 1: (0.43283582089552236, 0.4716784165201518), 2: None, 3: None, 4: None}, '8': {0: (0.23412698412698424, 0.2830003004282848), 1: (0.2571428571428571, 0.4193998327690762), 2: None, 3: None, 4: None}, '9': {0: (0.2235294117647059, 0.20659047265014663), 1: (0.2363636363636364, 0.4064879570094664), 2: None, 3: None, 4: None}, 'T': {0: (0.18411552346570398, 0.17531988866552017), 1: (0.22807017543859648, 0.3194670880727001), 2: None, 3: None, 4: None}, 'J': {0: (0.21505376344086022, 0.18817062631929385), 1: (0.22033898305084745, 0.3265019704014526), 2: None, 3: None, 4: None}, 'Q': {0: (0.2627450980392159, 0.15101310174567395), 1: (0.27868852459016386, 0.4376567662041929), 2: None, 3: None, 4: None}, 'K': {0: (0.2878228782287822, 0.1867738615926329), 1: (0.3148148148148148, 0.3878032715957962), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.08558558558558559, 0.12913220597646827), 1: (0.125, 0.17561685444726371), 2: (0.0, 0.43958333333333327), 3: None, 4: None}, '2': {0: (0.34579439252336464, 0.24900567085527925), 1: (0.2894736842105264, 0.18844287862030823), 2: (0.6666666666666666, 0.4341269841269841), 3: None, 4: None}, '3': {0: (0.35483870967741926, 0.1568072746647157), 1: (0.4659090909090909, 0.21707417938890272), 2: (0.7142857142857143, 0.5722571079713937), 3: None, 4: None}, '4': {0: (0.39325842696629215, 0.15890818157157477), 1: (0.3367346938775511, 0.24377733672293603), 2: (0.5, 0.34615384615384615), 3: None, 4: None}, '5': {0: (0.45989304812834225, 0.22327032013491505), 1: (0.43373493975903615, 0.3077786557282716), 2: (0.0, 0.6996336996336997), 3: None, 4: None}, '6': {0: (0.44021739130434784, 0.19588113551919695), 1: (0.4411764705882352, 0.30994645405703586), 2: (0.25, 0.3), 3: None, 4: None}, '7': {0: (0.3024390243902441, 0.23445891819868847), 1: (0.28571428571428575, 0.20191147215614597), 2: (0.3333333333333333, 0.39404761904761904), 3: None, 4: None}, '8': {0: (0.2536585365853659, 0.22373802198945303), 1: (0.24761904761904768, 0.28984011558063716), 2: (0.5, 0.30883387445887445), 3: None, 4: None}, '9': {0: (0.29439252336448607, 0.19632197159407694), 1: (0.21428571428571427, 0.22376219573734182), 2: (0.5, 0.705622936091686), 3: None, 4: None}, 'T': {0: (0.22566371681415928, 0.1557071922986212), 1: (0.20000000000000004, 0.165803378654996), 2: (0.2, 0.7169135802469135), 3: None, 4: None}, 'J': {0: (0.19111111111111115, 0.1473369467028006), 1: (0.2222222222222222, 0.21294962431316758), 2: (0.0, 0.3038690476190476), 3: None, 4: None}, 'Q': {0: (0.21875000000000003, 0.15007400087751574), 1: (0.26881720430107536, 0.2093998516030439), 2: (0.0, 0.47708333333333336), 3: None, 4: None}, 'K': {0: (0.15384615384615394, 0.1943599832399187), 1: (0.2500000000000001, 0.19271350815681892), 2: (0.14285714285714285, 0.3951701493994727), 3: None, 4: None}}, 4: {'A': {0: (0.13157894736842105, 0.02654071075123707), 1: (0.1590909090909091, 0.1323763955342903), 2: (0.0, 0.041666666666666664), 3: (0.0, 0.0), 4: None}, '2': {0: (0.3548387096774194, 0.16761543327008224), 1: (0.5000000000000001, 0.18624581939799323), 2: (0.5714285714285714, 0.19642857142857142), 3: None, 4: None}, '3': {0: (0.4523809523809524, 0.17993197278911566), 1: (0.425, 0.09768772893772895), 2: (0.5, 0.5), 3: None, 4: None}, '4': {0: (0.27586206896551724, 0.2614788862253366), 1: (0.4444444444444444, 0.14054232804232802), 2: (0.6666666666666666, 0.3333333333333333), 3: None, 4: None}, '5': {0: (0.5217391304347827, 0.21906354515050167), 1: (0.43103448275862066, 0.1511595079653156), 2: (0.38461538461538464, 0.15769230769230771), 3: None, 4: None}, '6': {0: (0.34210526315789475, 0.2894736842105263), 1: (0.4318181818181818, 0.12727272727272726), 2: (0.3333333333333333, 0.16765873015873015), 3: None, 4: None}, '7': {0: (0.3, 0.34051282051282056), 1: (0.2222222222222222, 0.21027777777777779), 2: (0.1875, 0.325), 3: (0.0, 1.0), 4: None}, '8': {0: (0.3076923076923077, 0.1982118758434548), 1: (0.3098591549295775, 0.22803061685621748), 2: (0.25, 0.30892857142857144), 3: (0.0, 1.0), 4: None}, '9': {0: (0.22580645161290322, 0.21629445822994212), 1: (0.2962962962962963, 0.19950617283950617), 2: (0.3076923076923077, 0.3084693084693085), 3: None, 4: None}, 'T': {0: (0.21621621621621623, 0.1559221559221559), 1: (0.19230769230769235, 0.12407407407407403), 2: (0.2222222222222222, 0.16666666666666666), 3: None, 4: None}, 'J': {0: (0.358974358974359, 0.0757020757020757), 1: (0.1746031746031746, 0.10495165808258786), 2: (0.3, 0.275), 3: (0.0, 0.5), 4: None}, 'Q': {0: (0.19444444444444445, 0.15849673202614378), 1: (0.234375, 0.18566849816849818), 2: (0.4, 0.22000000000000003), 3: None, 4: None}, 'K': {0: (0.2619047619047619, 0.14061624649859944), 1: (0.27586206896551724, 0.13793103448275865), 2: (0.2222222222222222, 0.2866161616161616), 3: (1.0, 1.0), 4: None}}, 5: {'A': {0: (0.0, 0.0), 1: (0.0, 0.09523809523809523), 2: (0.0, 0.0), 3: None, 4: None}, '2': {0: None, 1: (0.2, 0.2), 2: (0.42857142857142855, 0.42857142857142855), 3: (1.0, 1.0), 4: None}, '3': {0: (0.0, 0.6666666666666666), 1: (0.15384615384615385, 0.20512820512820512), 2: (0.2, 0.5), 3: (0.5, 0.0), 4: None}, '4': {0: (0.6666666666666666, 0.0), 1: (0.25, 0.21666666666666665), 2: (0.6, 0.1), 3: (0.0, 0.0), 4: None}, '5': {0: None, 1: (0.5555555555555556, 0.07407407407407407), 2: (0.25, 0.0), 3: None, 4: None}, '6': {0: (1.0, 0.0), 1: (0.3076923076923077, 0.38461538461538464), 2: (0.6, 0.18), 3: None, 4: None}, '7': {0: (0.5, 0.0), 1: (0.0, 0.20833333333333331), 2: (0.1111111111111111, 0.25), 3: None, 4: None}, '8': {0: (0.0, 0.25), 1: (0.42857142857142855, 0.2857142857142857), 2: (0.0, 0.2285714285714286), 3: (0.0, 0.0), 4: None}, '9': {0: (0.3333333333333333, 0.0), 1: (0.0, 0.0), 2: (0.25, 0.2708333333333333), 3: (0.0, 0.25), 4: None}, 'T': {0: (0.0, 0.0), 1: (0.3076923076923077, 0.14285714285714285), 2: (0.0, 0.5), 3: None, 4: None}, 'J': {0: (0.0, 0.0), 1: (0.3333333333333333, 0.09722222222222221), 2: (0.25, 0.1875), 3: (0.0, 0.0), 4: None}, 'Q': {0: (0.3333333333333333, 0.3333333333333333), 1: (0.6, 0.0), 2: (0.2, 0.0), 3: (0.25, 0.0), 4: None}, 'K': {0: (0.2, 0.0), 1: (0.25, 0.40625), 2: (0.375, 0.0), 3: (1.0, 0.0), 4: None}}, 6: {'A': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, '2': {0: None, 1: None, 2: (1.0, 0.3333333333333333), 3: None, 4: None}, '3': {0: None, 1: None, 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: None}, '4': {0: None, 1: (0.0, 0.0), 2: None, 3: None, 4: None}, '5': {0: None, 1: None, 2: (0.0, 0.0), 3: None, 4: None}, '6': {0: None, 1: None, 2: (0.5, 0.0), 3: None, 4: None}, '7': {0: None, 1: (0.0, 0.5), 2: (0.5, 0.0), 3: None, 4: None}, '8': {0: (0.0, 0.0), 1: None, 2: (0.0, 0.5), 3: None, 4: None}, '9': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, 'T': {0: None, 1: None, 2: (1.0, 0.0), 3: (0.3333333333333333, 0.0), 4: None}, 'J': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.5), 3: (0.0, 0.0), 4: None}, 'Q': {0: None, 1: (0.5, 0.0), 2: (1.0, 0.5), 3: (0.0, 0.0), 4: None}, 'K': {0: None, 1: (0.0, 0.3333333333333333), 2: None, 3: (1.0, 1.0), 4: None}}}, 18: {2: {'A': {0: (0.2304147465437788, 0.11407686545140858), 1: (0.288888888888889, 0.2304168535262914), 2: None, 3: None, 4: None}, '2': {0: (0.5401459854014601, 0.17354176086816078), 1: (0.515625, 0.417057592102885), 2: None, 3: None, 4: None}, '3': {0: (0.5019455252918287, 0.1578436517130196), 1: (0.5098039215686274, 0.5335615172979682), 2: None, 3: None, 4: None}, '4': {0: (0.5936254980079677, 0.20648593365999604), 1: (0.4444444444444444, 0.5235694373165638), 2: None, 3: None, 4: None}, '5': {0: (0.5945945945945946, 0.16724734939020663), 1: (0.5901639344262295, 0.6160889414414993), 2: None, 3: None, 4: None}, '6': {0: (0.6017699115044246, 0.19823930678466087), 1: (0.6226415094339622, 0.5533344943818013), 2: None, 3: None, 4: None}, '7': {0: (0.6315789473684208, 0.2056406197680435), 1: (0.7045454545454547, 0.5521758483954099), 2: None, 3: None, 4: None}, '8': {0: (0.3520408163265308, 0.16037063899831058), 1: (0.37333333333333335, 0.4779074928885607), 2: None, 3: None, 4: None}, '9': {0: (0.3228699551569508, 0.1646962902568285), 1: (0.44, 0.46484493964335954), 2: None, 3: None, 4: None}, 'T': {0: (0.32, 0.18378575688894197), 1: (0.32758620689655166, 0.4066871233982936), 2: None, 3: None, 4: None}, 'J': {0: (0.3183856502242152, 0.160866143971786), 1: (0.42857142857142855, 0.37208448801785504), 2: None, 3: None, 4: None}, 'Q': {0: (0.26130653266331666, 0.15500891554546928), 1: (0.27450980392156865, 0.42406564698990196), 2: None, 3: None, 4: None}, 'K': {0: (0.3744493392070483, 0.13548948758338158), 1: (0.25396825396825395, 0.36061488971652395), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.2079646017699115, 0.11555479918311767), 1: (0.18571428571428572, 0.10543177447775605), 2: (0.0, 0.1), 3: None, 4: None}, '2': {0: (0.4389140271493214, 0.18227291820642197), 1: (0.5797101449275364, 0.21985392455052888), 2: (0.8333333333333334, 0.49537037037037024), 3: None, 4: None}, '3': {0: (0.4976744186046513, 0.15073616802369916), 1: (0.45454545454545453, 0.24797958873508583), 2: (0.375, 0.6217948717948718), 3: None, 4: None}, '4': {0: (0.5536723163841806, 0.1760785232627769), 1: (0.5000000000000001, 0.21573556687057502), 2: (0.3333333333333333, 0.6666666666666666), 3: None, 4: None}, '5': {0: (0.589371980676329, 0.1617492492492493), 1: (0.6790123456790124, 0.2664589362741733), 2: (0.6, 0.6261294261294261), 3: None, 4: None}, '6': {0: (0.559808612440191, 0.2092292805315481), 1: (0.5887850467289719, 0.31539740977717595), 2: (0.5, 0.775), 3: None, 4: None}, '7': {0: (0.6785714285714285, 0.1910478183606412), 1: (0.5729166666666667, 0.27132338376514037), 2: (0.75, 0.4754595588235294), 3: None, 4: None}, '8': {0: (0.3918918918918919, 0.17915825232898416), 1: (0.42391304347826086, 0.26741241295248946), 2: (0.45454545454545453, 0.4535730683457956), 3: None, 4: None}, '9': {0: (0.33809523809523817, 0.17543901281442817), 1: (0.3829787234042554, 0.2915572379435871), 2: (0.3333333333333333, 0.338979538979539), 3: None, 4: None}, 'T': {0: (0.2786069651741293, 0.11542628204447833), 1: (0.3434343434343434, 0.1659342868938828), 2: (0.3333333333333333, 0.23148148148148148), 3: None, 4: None}, 'J': {0: (0.3596491228070175, 0.15215418799717492), 1: (0.35869565217391297, 0.13634466096039213), 2: (0.0, 0.2789411976911977), 3: None, 4: None}, 'Q': {0: (0.25837320574162687, 0.1488101297731756), 1: (0.34090909090909094, 0.18425433593017423), 2: (0.5, 0.37904040404040407), 3: None, 4: None}, 'K': {0: (0.3476394849785409, 0.1334442729292514), 1: (0.2638888888888889, 0.2285190796063049), 2: (0.5, 0.6169806618819776), 3: None, 4: None}}, 4: {'A': {0: (0.20408163265306123, 0.06593406593406594), 1: (0.16393442622950818, 0.07368421052631578), 2: (0.2, 0.08), 3: None, 4: None}, '2': {0: (0.5, 0.1607789855072464), 1: (0.5733333333333334, 0.1), 2: (0.3333333333333333, 0.21652421652421655), 3: None, 4: None}, '3': {0: (0.6, 0.15306122448979592), 1: (0.5333333333333333, 0.20347222222222222), 2: (0.7692307692307693, 0.34615384615384615), 3: None, 4: None}, '4': {0: (0.34782608695652184, 0.1312252964426878), 1: (0.5849056603773586, 0.18583833619210974), 2: (0.5, 0.26666666666666666), 3: None, 4: None}, '5': {0: (0.47999999999999987, 0.15684210526315795), 1: (0.6226415094339623, 0.13321104122990915), 2: (0.4444444444444444, 0.2833333333333333), 3: None, 4: None}, '6': {0: (0.5999999999999999, 0.18363636363636368), 1: (0.6896551724137931, 0.1743349753694581), 2: (0.75, 0.25), 3: None, 4: None}, '7': {0: (0.5964912280701757, 0.14239766081871352), 1: (0.6710526315789472, 0.12205995758627335), 2: (0.5, 0.3125), 3: None, 4: None}, '8': {0: (0.5471698113207547, 0.22523584905660377), 1: (0.5081967213114754, 0.1370712219313955), 2: (0.3333333333333333, 0.25), 3: (0.0, 0.0), 4: None}, '9': {0: (0.3191489361702128, 0.12281505728314238), 1: (0.32, 0.18866666666666673), 2: (0.2857142857142857, 0.18601190476190474), 3: None, 4: None}, 'T': {0: (0.22727272727272727, 0.11796536796536795), 1: (0.2702702702702703, 0.16991141991141984), 2: (0.25, 0.23194444444444445), 3: (1.0, 1.0), 4: None}, 'J': {0: (0.26153846153846155, 0.11460892049127347), 1: (0.2833333333333333, 0.0921309872922776), 2: (0.14285714285714285, 0.36607142857142855), 3: None, 4: None}, 'Q': {0: (0.36231884057971014, 0.08971704623878536), 1: (0.28169014084507044, 0.15276273022751893), 2: (0.36363636363636365, 0.14242424242424243), 3: None, 4: None}, 'K': {0: (0.34210526315789475, 0.21052631578947367), 1: (0.3194444444444445, 0.13700555979967746), 2: (0.42857142857142855, 0.18367346938775508), 3: (0.0, 0.0), 4: None}}, 5: {'A': {0: (0.2, 0.0), 1: (0.1111111111111111, 0.0), 2: (0.6666666666666666, 0.0), 3: None, 4: None}, '2': {0: (0.5, 0.0), 1: (0.5294117647058824, 0.058823529411764705), 2: (0.6153846153846154, 0.05128205128205128), 3: (0.0, 0.0), 4: None}, '3': {0: (0.4, 0.4), 1: (0.7, 0.1), 2: (0.5, 0.16666666666666666), 3: (1.0, 0.0), 4: None}, '4': {0: (0.75, 0.125), 1: (0.5882352941176471, 0.04705882352941177), 2: (0.2857142857142857, 0.07142857142857142), 3: None, 4: None}, '5': {0: (0.6666666666666666, 0.5833333333333334), 1: (0.5384615384615384, 0.20512820512820512), 2: (0.3, 0.2), 3: (1.0, 0.0), 4: None}, '6': {0: (0.8, 0.2), 1: (0.7, 0.1), 2: (0.5, 0.0), 3: None, 4: None}, '7': {0: (1.0, 0.0), 1: (0.5384615384615384, 0.07692307692307693), 2: (0.8, 0.2), 3: (1.0, 1.0), 4: None}, '8': {0: (0.25, 0.25), 1: (0.3684210526315789, 0.05263157894736842), 2: (0.36363636363636365, 0.09090909090909091), 3: None, 4: None}, '9': {0: (0.42857142857142855, 0.2857142857142857), 1: (0.75, 0.09687500000000002), 2: (0.3333333333333333, 0.16666666666666666), 3: (1.0, 1.0), 4: None}, 'T': {0: None, 1: (0.36363636363636365, 0.13636363636363635), 2: (0.3, 0.0), 3: (0.0, 0.0), 4: None}, 'J': {0: (0.0, 0.0), 1: (0.26666666666666666, 0.0), 2: (0.5, 0.0), 3: None, 4: None}, 'Q': {0: (0.625, 0.125), 1: (0.35294117647058826, 0.11764705882352941), 2: (0.3333333333333333, 0.0), 3: (0.0, 0.0), 4: None}, 'K': {0: (0.0, 0.2), 1: (0.11764705882352941, 0.0), 2: (0.2857142857142857, 0.07142857142857142), 3: None, 4: None}}, 6: {'A': {0: None, 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, '2': {0: (1.0, 0.0), 1: (0.6666666666666666, 0.0), 2: (0.5, 0.5), 3: (0.0, 0.0), 4: None}, '3': {0: None, 1: (0.6666666666666666, 0.0), 2: (0.4, 0.0), 3: (0.0, 0.0), 4: None}, '4': {0: None, 1: (1.0, 0.0), 2: (0.0, 0.0), 3: (1.0, 0.0), 4: None}, '5': {0: None, 1: (0.3333333333333333, 0.0), 2: (1.0, 0.0), 3: None, 4: None}, '6': {0: None, 1: (1.0, 0.0), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}, '7': {0: None, 1: (1.0, 0.0), 2: None, 3: (0.5, 0.5), 4: None}, '8': {0: (1.0, 0.0), 1: (1.0, 0.0), 2: (0.3333333333333333, 0.0), 3: (0.5, 0.0), 4: None}, '9': {0: (1.0, 0.0), 1: (0.0, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, 'T': {0: (0.0, 0.0), 1: (1.0, 0.0), 2: (0.2, 0.2), 3: (0.0, 0.0), 4: None}, 'J': {0: None, 1: (0.0, 0.0), 2: (0.6666666666666666, 0.0), 3: (1.0, 0.0), 4: None}, 'Q': {0: None, 1: None, 2: (1.0, 0.5), 3: (0.0, 0.0), 4: None}, 'K': {0: (1.0, 0.0), 1: (0.5, 0.0), 2: (1.0, 0.0), 3: None, 4: None}}}, 19: {2: {'A': {0: (0.4170403587443946, 0.08071748878923762), 1: (0.3877551020408163, 0.27587233655389665), 2: None, 3: None, 4: None}, '2': {0: (0.5965665236051505, 0.1245077651431354), 1: (0.6101694915254239, 0.4762320640471162), 2: None, 3: None, 4: None}, '3': {0: (0.6707818930041151, 0.1662551440329219), 1: (0.6250000000000001, 0.5454095774334494), 2: None, 3: None, 4: None}, '4': {0: (0.626050420168067, 0.14097979617378853), 1: (0.5806451612903225, 0.5509586676413348), 2: None, 3: None, 4: None}, '5': {0: (0.6986301369863016, 0.10889719108897195), 1: (0.6393442622950819, 0.5434481588645786), 2: None, 3: None, 4: None}, '6': {0: (0.7285067873303167, 0.13211773666054386), 1: (0.6610169491525423, 0.5626542856999973), 2: None, 3: None, 4: None}, '7': {0: (0.7621359223300971, 0.10652939293715995), 1: (0.7692307692307693, 0.6011373559023426), 2: None, 3: None, 4: None}, '8': {0: (0.6995884773662556, 0.14166885561684622), 1: (0.7674418604651163, 0.5802153876368664), 2: None, 3: None, 4: None}, '9': {0: (0.47590361445783114, 0.13651904916965155), 1: (0.5087719298245615, 0.42582183611588265), 2: None, 3: None, 4: None}, 'T': {0: (0.47058823529411764, 0.10828877005347594), 1: (0.393939393939394, 0.4251366935103315), 2: None, 3: None, 4: None}, 'J': {0: (0.46766169154228854, 0.13009028929426944), 1: (0.39344262295081966, 0.42851162252044955), 2: None, 3: None, 4: None}, 'Q': {0: (0.4858490566037736, 0.09734133790737556), 1: (0.4925373134328359, 0.40022640402258897), 2: None, 3: None, 4: None}, 'K': {0: (0.4153846153846154, 0.07654520917678809), 1: (0.4339622641509434, 0.37550374394255237), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.3861003861003861, 0.06002574002574002), 1: (0.37931034482758624, 0.19859291175446553), 2: (0.5, 0.2583333333333333), 3: None, 4: None}, '2': {0: (0.654320987654321, 0.10860619073179455), 1: (0.6133333333333333, 0.21917368210971158), 2: (0.16666666666666666, 0.4681216931216931), 3: None, 4: None}, '3': {0: (0.6710526315789476, 0.10799220272904482), 1: (0.6888888888888887, 0.2572904511785851), 2: (1.0, 0.45946275946275944), 3: None, 4: None}, '4': {0: (0.6650943396226416, 0.16676195921478948), 1: (0.6777777777777778, 0.3430581074370918), 2: (0.0, 0.5), 3: None, 4: None}, '5': {0: (0.7000000000000003, 0.12748772869254793), 1: (0.5666666666666665, 0.1986352179952515), 2: (0.7142857142857143, 0.6507936507936508), 3: None, 4: None}, '6': {0: (0.6493506493506496, 0.1263962375073486), 1: (0.6296296296296302, 0.24780567865191594), 2: (0.75, 0.6923076923076923), 3: None, 4: None}, '7': {0: (0.8287037037037037, 0.1416268418956589), 1: (0.769230769230769, 0.3257373999774548), 2: (0.8333333333333334, 0.5550682773109243), 3: None, 4: None}, '8': {0: (0.7428571428571429, 0.11878009630818614), 1: (0.7432432432432432, 0.3436516417372337), 2: (0.6666666666666666, 0.5353535353535352), 3: None, 4: None}, '9': {0: (0.49236641221374045, 0.1580152671755725), 1: (0.5, 0.3297070820612301), 2: (0.3333333333333333, 0.7333333333333334), 3: None, 4: None}, 'T': {0: (0.49019607843137253, 0.11087768440709614), 1: (0.5445544554455448, 0.2230656420091187), 2: (0.7, 0.2621527777777778), 3: None, 4: None}, 'J': {0: (0.4, 0.10387430047352554), 1: (0.46511627906976744, 0.1959682323596323), 2: (0.6666666666666666, 0.6051587301587301), 3: None, 4: None}, 'Q': {0: (0.430327868852459, 0.12495446265938052), 1: (0.5000000000000001, 0.19601596914415872), 2: (1.0, 0.4), 3: None, 4: None}, 'K': {0: (0.46616541353383456, 0.1116398591415247), 1: (0.4264705882352941, 0.1917372840994332), 2: (0.2, 0.482085137085137), 3: None, 4: None}}, 4: {'A': {0: (0.375, 0.07177033492822966), 1: (0.36538461538461536, 0.13782051282051283), 2: (0.25, 0.027777777777777776), 3: None, 4: None}, '2': {0: (0.6981132075471698, 0.09869375907111756), 1: (0.6081081081081081, 0.0629692192192192), 2: (0.3333333333333333, 0.1794871794871795), 3: (0.5, 1.0), 4: None}, '3': {0: (0.5737704918032787, 0.07445355191256829), 1: (0.6376811594202898, 0.13008971704623878), 2: (0.6923076923076923, 0.3333333333333333), 3: None, 4: None}, '4': {0: (0.6666666666666666, 0.090625), 1: (0.7142857142857143, 0.16000000000000003), 2: (0.6923076923076923, 0.07692307692307693), 3: None, 4: None}, '5': {0: (0.6857142857142857, 0.08253968253968255), 1: (0.5540540540540538, 0.08958432116326853), 2: (0.5, 0.21875), 3: None, 4: None}, '6': {0: (0.7, 0.174), 1: (0.7424242424242423, 0.10457251082251084), 2: (0.6923076923076923, 0.36620879120879124), 3: (0.0, 0.0), 4: None}, '7': {0: (0.7671232876712328, 0.1780821917808219), 1: (0.7662337662337663, 0.1531093906093907), 2: (0.42857142857142855, 0.21428571428571427), 3: (1.0, 1.0), 4: None}, '8': {0: (0.8589743589743589, 0.1432880844645551), 1: (0.6825396825396826, 0.14271541950113373), 2: (0.6666666666666666, 0.2222222222222222), 3: None, 4: None}, '9': {0: (0.43478260869565216, 0.17391304347826092), 1: (0.4523809523809522, 0.08697089947089943), 2: (0.6, 0.5150252525252524), 3: None, 4: None}, 'T': {0: (0.38095238095238093, 0.11992945326278658), 1: (0.43037974683544306, 0.11392405063291132), 2: (0.25, 0.26666666666666666), 3: (0.0, 1.0), 4: None}, 'J': {0: (0.45121951219512196, 0.06963021243115658), 1: (0.42168674698795183, 0.13108568728696302), 2: (0.6153846153846154, 0.5116550116550116), 3: None, 4: None}, 'Q': {0: (0.379746835443038, 0.07205452775073029), 1: (0.47619047619047616, 0.1523809523809524), 2: (0.4666666666666667, 0.22666666666666666), 3: None, 4: None}, 'K': {0: (0.4383561643835616, 0.07534246575342464), 1: (0.38461538461538464, 0.16481720893485585), 2: (0.5555555555555556, 0.08225108225108224), 3: None, 4: None}}, 5: {'A': {0: (0.5555555555555556, 0.1111111111111111), 1: (0.3333333333333333, 0.08333333333333333), 2: (0.3, 0.0), 3: None, 4: None}, '2': {0: (0.625, 0.125), 1: (0.4375, 0.0625), 2: (0.5, 0.1), 3: (0.5, 0.0), 4: None}, '3': {0: (1.0, 0.0), 1: (0.6428571428571429, 0.0), 2: (0.6666666666666666, 0.13333333333333333), 3: None, 4: None}, '4': {0: (1.0, 0.0), 1: (0.6, 0.0), 2: (0.8181818181818182, 0.09090909090909091), 3: None, 4: None}, '5': {0: (0.5, 0.0), 1: (0.47368421052631576, 0.0), 2: (0.625, 0.0), 3: (0.5, 0.0), 4: None}, '6': {0: (0.8, 0.0), 1: (0.7, 0.09), 2: (0.6428571428571429, 0.07142857142857142), 3: None, 4: None}, '7': {0: (0.8333333333333334, 0.0), 1: (0.8125, 0.28125), 2: (0.7647058823529411, 0.14705882352941177), 3: None, 4: None}, '8': {0: (0.75, 0.0), 1: (0.8125, 0.0625), 2: (0.5714285714285714, 0.0), 3: None, 4: None}, '9': {0: (0.4166666666666667, 0.06666666666666668), 1: (0.36, 0.08), 2: (0.45454545454545453, 0.06818181818181818), 3: None, 4: None}, 'T': {0: (0.2222222222222222, 0.15873015873015872), 1: (0.3333333333333333, 0.20833333333333334), 2: (0.5, 0.16666666666666666), 3: (1.0, 0.0), 4: None}, 'J': {0: (0.2, 0.0), 1: (0.23529411764705882, 0.17647058823529413), 2: (0.45454545454545453, 0.18181818181818182), 3: (1.0, 0.5), 4: None}, 'Q': {0: (0.5, 0.125), 1: (0.38095238095238093, 0.09523809523809523), 2: (0.0, 0.0), 3: None, 4: None}, 'K': {0: (0.5, 0.0), 1: (0.5, 0.15), 2: (0.45454545454545453, 0.09090909090909091), 3: (1.0, 1.0), 4: None}}, 6: {'A': {0: None, 1: (0.6666666666666666, 0.6666666666666666), 2: (0.0, 0.3333333333333333), 3: None, 4: None}, '2': {0: None, 1: (0.6666666666666666, 0.0), 2: (1.0, 0.0), 3: None, 4: None}, '3': {0: None, 1: (0.6666666666666666, 0.0), 2: (0.5, 0.0), 3: None, 4: None}, '4': {0: None, 1: (0.5, 0.0), 2: (0.0, 0.0), 3: None, 4: None}, '5': {0: None, 1: (0.75, 0.5), 2: (1.0, 0.3333333333333333), 3: None, 4: None}, '6': {0: None, 1: (1.0, 0.0), 2: (0.0, 0.0), 3: (1.0, 0.0), 4: (0.5, 0.0)}, '7': {0: (0.0, 0.0), 1: (1.0, 0.3333333333333333), 2: (1.0, 0.0), 3: None, 4: None}, '8': {0: None, 1: (1.0, 0.0), 2: (0.6, 0.2), 3: None, 4: None}, '9': {0: None, 1: (0.0, 1.0), 2: (0.75, 0.0), 3: (1.0, 0.0), 4: None}, 'T': {0: None, 1: (0.4, 0.0), 2: (1.0, 0.0), 3: None, 4: None}, 'J': {0: None, 1: (0.0, 0.0), 2: (0.5, 0.0), 3: (0.5, 0.0), 4: None}, 'Q': {0: (1.0, 0.0), 1: (0.5, 0.5), 2: (1.0, 0.0), 3: None, 4: None}, 'K': {0: None, 1: (0.0, 0.5), 2: (0.0, 0.0), 3: (1.0, 0.0), 4: None}}}, 20: {2: {'A': {0: (0.5370370370370368, 0.03935185185185182), 1: (0.66, 0.27799628255774145), 2: None, 3: None, 4: None}, '2': {0: (0.7807486631016047, 0.05614973262032084), 1: (0.7419354838709677, 0.5063158106423332), 2: None, 3: None, 4: None}, '3': {0: (0.7252252252252253, 0.09234234234234236), 1: (0.75, 0.5888535686686499), 2: None, 3: None, 4: None}, '4': {0: (0.7630331753554505, 0.04739336492890997), 1: (0.7346938775510204, 0.600077941406738), 2: None, 3: None, 4: None}, '5': {0: (0.8139534883720931, 0.08527131782945738), 1: (0.8837209302325582, 0.631589683708858), 2: None, 3: None, 4: None}, '6': {0: (0.8071428571428574, 0.0476190476190476), 1: (0.8181818181818183, 0.5338392847594486), 2: None, 3: None, 4: None}, '7': {0: (0.8467153284671532, 0.08515815085158157), 1: (0.9, 0.5600604548362852), 2: None, 3: None, 4: None}, '8': {0: (0.8526570048309178, 0.06280193236714982), 1: (0.8333333333333334, 0.5822089358428584), 2: None, 3: None, 4: None}, '9': {0: (0.7635467980295568, 0.054187192118226604), 1: (0.8250000000000002, 0.4808789716670317), 2: None, 3: None, 4: None}, 'T': {0: (0.5861111111111114, 0.06388888888888887), 1: (0.5555555555555556, 0.4706909231781818), 2: None, 3: None, 4: None}, 'J': {0: (0.5734870317002885, 0.08357348703170028), 1: (0.625, 0.398294143807757), 2: None, 3: None, 4: None}, 'Q': {0: (0.5391304347826084, 0.08115942028985507), 1: (0.5818181818181818, 0.43764432894981004), 2: None, 3: None, 4: None}, 'K': {0: (0.58, 0.09142857142857144), 1: (0.6, 0.4055799079031444), 2: None, 3: None, 4: None}}, 3: {'A': {0: (0.4857142857142855, 0.017857142857142863), 1: (0.5000000000000001, 0.13973557119130292), 2: (0.3333333333333333, 0.3333333333333333), 3: None, 4: None}, '2': {0: (0.7433628318584071, 0.08849557522123896), 1: (0.6804123711340206, 0.30098168591453395), 2: (0.8333333333333334, 0.762962962962963), 3: None, 4: None}, '3': {0: (0.7748091603053437, 0.08015267175572521), 1: (0.788235294117647, 0.23160891582054094), 2: (0.8333333333333334, 0.5284391534391534), 3: None, 4: None}, '4': {0: (0.7586206896551724, 0.06130268199233722), 1: (0.8085106382978723, 0.36752956259886943), 2: (0.875, 0.6860544217687075), 3: None, 4: None}, '5': {0: (0.7602040816326531, 0.05102040816326531), 1: (0.7575757575757576, 0.2714593805993868), 2: (0.8, 0.6752087912087912), 3: None, 4: None}, '6': {0: (0.7734375, 0.0546875), 1: (0.7623762376237623, 0.3920209572852174), 2: (1.0, 0.6751082251082251), 3: None, 4: None}, '7': {0: (0.8157894736842105, 0.05639097744360904), 1: (0.8131868131868131, 0.2421618211459169), 2: (1.0, 0.44610294117647054), 3: None, 4: None}, '8': {0: (0.8464566929133859, 0.07480314960629919), 1: (0.851063829787234, 0.28211018521244596), 2: (0.8888888888888888, 0.727946127946128), 3: None, 4: None}, '9': {0: (0.8181818181818183, 0.0950413223140496), 1: (0.8783783783783784, 0.3426661987026945), 2: (0.6666666666666666, 0.638888888888889), 3: None, 4: None}, 'T': {0: (0.5662650602409639, 0.0763052208835342), 1: (0.625, 0.1754543040364066), 2: (0.3333333333333333, 0.44485596707818925), 3: None, 4: None}, 'J': {0: (0.5636363636363634, 0.06909090909090912), 1: (0.5092592592592592, 0.1978654139260857), 2: (0.875, 0.4269230769230769), 3: None, 4: None}, 'Q': {0: (0.49193548387096786, 0.07661290322580644), 1: (0.4772727272727271, 0.21652600014612988), 2: (0.42857142857142855, 0.5000000000000001), 3: None, 4: None}, 'K': {0: (0.5393258426966288, 0.07490636704119853), 1: (0.5578947368421052, 0.23462223777701965), 2: (0.625, 0.551368359345333), 3: None, 4: None}}, 4: {'A': {0: (0.4583333333333333, 0.0729166666666667), 1: (0.5066666666666667, 0.052475633528265106), 2: (0.3333333333333333, 0.18333333333333335), 3: None, 4: None}, '2': {0: (0.7934782608695652, 0.0760869565217391), 1: (0.6956521739130432, 0.1024247491638796), 2: (0.7333333333333333, 0.13597883597883598), 3: None, 4: None}, '3': {0: (0.8289473684210527, 0.05263157894736842), 1: (0.7888888888888889, 0.07982804232804232), 2: (0.7857142857142857, 0.2857142857142857), 3: (1.0, 0.0), 4: None}, '4': {0: (0.7634408602150538, 0.053763440860215034), 1: (0.7676767676767676, 0.07450237670825906), 2: (0.6666666666666666, 0.3), 3: None, 4: None}, '5': {0: (0.7875, 0.1125), 1: (0.771084337349398, 0.13124721106648818), 2: (0.8571428571428571, 0.08928571428571429), 3: (1.0, 1.0), 4: None}, '6': {0: (0.8586956521739131, 0.07608695652173915), 1: (0.8271604938271605, 0.07079365079365076), 2: (0.8, 0.15625), 3: None, 4: None}, '7': {0: (0.8313253012048193, 0.09638554216867468), 1: (0.8494623655913979, 0.14208663200598684), 2: (1.0, 0.2285714285714286), 3: (0.0, 0.0), 4: None}, '8': {0: (0.8780487804878049, 0.0975609756097561), 1: (0.7640449438202246, 0.08296352248764677), 2: (0.8333333333333334, 0.38095238095238093), 3: None, 4: None}, '9': {0: (0.8604651162790697, 0.05813953488372091), 1: (0.8470588235294118, 0.11482352941176469), 2: (0.875, 0.2977430555555555), 3: None, 4: None}, 'T': {0: (0.48314606741573035, 0.02247191011235955), 1: (0.4880952380952381, 0.04132023179642225), 2: (0.75, 0.25), 3: None, 4: None}, 'J': {0: (0.5853658536585366, 0.04878048780487803), 1: (0.49504950495049505, 0.05451592326486646), 2: (0.375, 0.26041666666666663), 3: None, 4: None}, 'Q': {0: (0.5106382978723406, 0.05319148936170213), 1: (0.5222222222222224, 0.11355119825708063), 2: (0.4166666666666667, 0.14166666666666666), 3: None, 4: None}, 'K': {0: (0.6081081081081081, 0.06756756756756757), 1: (0.531645569620253, 0.0501205545509343), 2: (0.6842105263157895, 0.09577922077922078), 3: (1.0, 1.0), 4: None}}, 5: {'A': {0: (0.23076923076923078, 0.0), 1: (0.5789473684210527, 0.0), 2: (0.3333333333333333, 0.16666666666666666), 3: None, 4: None}, '2': {0: (0.6666666666666666, 0.1111111111111111), 1: (0.8076923076923077, 0.07692307692307693), 2: (0.4444444444444444, 0.0), 3: (1.0, 0.5), 4: None}, '3': {0: (0.8571428571428571, 0.14285714285714285), 1: (0.7083333333333334, 0.08333333333333333), 2: (0.3333333333333333, 0.0), 3: (1.0, 0.0), 4: None}, '4': {0: (0.8181818181818182, 0.09090909090909091), 1: (0.7187499999999999, 0.03125), 2: (0.8, 0.1), 3: (1.0, 1.0), 4: None}, '5': {0: (1.0, 0.14285714285714285), 1: (0.9259259259259259, 0.07407407407407407), 2: (0.8, 0.1), 3: (0.5, 0.0), 4: None}, '6': {0: (0.8, 0.1), 1: (0.92, 0.04), 2: (0.5625, 0.0), 3: None, 4: None}, '7': {0: (0.9333333333333333, 0.06666666666666667), 1: (0.875, 0.125), 2: (0.8, 0.0), 3: (1.0, 0.0), 4: None}, '8': {0: (0.8125, 0.0), 1: (0.8823529411764706, 0.08823529411764706), 2: (0.8571428571428571, 0.07142857142857142), 3: None, 4: None}, '9': {0: (0.8461538461538461, 0.07692307692307693), 1: (0.8, 0.06666666666666667), 2: (0.8888888888888888, 0.0), 3: None, 4: None}, 'T': {0: (0.5714285714285714, 0.14285714285714285), 1: (0.5925925925925926, 0.07407407407407407), 2: (0.5555555555555556, 0.0), 3: (1.0, 0.0), 4: None}, 'J': {0: (0.6428571428571429, 0.07142857142857142), 1: (0.3870967741935484, 0.06451612903225806), 2: (0.5625, 0.03125), 3: None, 4: None}, 'Q': {0: (0.5555555555555556, 0.0), 1: (0.6153846153846154, 0.038461538461538464), 2: (0.7, 0.0), 3: (0.5, 0.0), 4: None}, 'K': {0: (0.4, 0.0), 1: (0.6428571428571427, 0.10714285714285714), 2: (0.7142857142857143, 0.14285714285714285), 3: (1.0, 0.0), 4: None}}, 6: {'A': {0: None, 1: (0.6666666666666666, 0.0), 2: (0.5, 0.0), 3: None, 4: None}, '2': {0: None, 1: (1.0, 0.0), 2: (0.6666666666666666, 0.0), 3: None, 4: None}, '3': {0: None, 1: (0.5, 0.0), 2: None, 3: (1.0, 0.0), 4: None}, '4': {0: None, 1: (0.8, 0.0), 2: (0.5, 0.0), 3: (0.0, 0.0), 4: None}, '5': {0: (0.0, 0.0), 1: (0.6666666666666666, 0.0), 2: (1.0, 0.0), 3: None, 4: None}, '6': {0: (1.0, 0.0), 1: (1.0, 0.0), 2: (0.8, 0.0), 3: (1.0, 0.0), 4: None}, '7': {0: (1.0, 1.0), 1: (0.6666666666666666, 0.0), 2: (0.75, 0.25), 3: (0.5, 0.0), 4: None}, '8': {0: (1.0, 0.0), 1: (1.0, 0.0), 2: (1.0, 0.0), 3: (1.0, 0.0), 4: None}, '9': {0: None, 1: (0.8, 0.2), 2: (1.0, 0.0), 3: (0.5, 0.0), 4: None}, 'T': {0: None, 1: (0.42857142857142855, 0.14285714285714285), 2: None, 3: (0.3333333333333333, 0.0), 4: None}, 'J': {0: None, 1: (0.5, 0.0), 2: (1.0, 0.0), 3: (0.0, 0.0), 4: None}, 'Q': {0: (0.0, 1.0), 1: (0.5, 0.16666666666666666), 2: (0.5714285714285714, 0.0), 3: (1.0, 0.0), 4: None}, 'K': {0: None, 1: (0.5, 0.0), 2: (0.5, 0.0), 3: None, 4: (1.0, 0.0)}}}}`
