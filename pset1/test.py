# # Define a standard deck of cards
# suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
# deck = [(rank, suit) for rank in ranks for suit in suits]

# # Function to generate combinations
# def generate_combinations(cards, r):
#     if r == 0:
#         return [[]]
#     if not cards:
#         return []
#     head, tail = cards[0], cards[1:]
#     without_head = generate_combinations(tail, r)
#     with_head = [[head] + rest for rest in generate_combinations(tail, r - 1)]
#     return without_head + with_head

# # Generate combinations of 2 to 12 cards
# for r in range(2, 13):
#     print(f"Combinations of {r} cards:")
#     combinations = generate_combinations(deck, r)
#     for combo in combinations:
#         print(combo)
#     print()

# fifteen_combs = [[1, 1, 1, 1, 2, 2, 2, 2, 3], [1, 1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 1, 2, 2, 3, 4], [1, 1, 1, 1, 2, 2, 7], [1, 1, 1, 1, 2, 3, 3, 3], [1, 1, 1, 1, 2, 3, 6], [1, 1, 1, 1, 2, 4, 5], [1, 1, 1, 1, 2, 9], [1, 1, 1, 1, 3, 3, 5], [1, 1, 1, 1, 3, 4, 4], [1, 1, 1, 1, 3, 8], [1, 1, 1, 1, 4, 7], [1, 1, 1, 1, 5, 6], [1, 1, 1, 1, 11], [1, 1, 1, 2, 2, 2, 2, 4], [1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 1, 2, 2, 2, 6], [1, 1, 1, 2, 2, 3, 5], [1, 1, 1, 2, 2, 4, 4], [1, 1, 1, 2, 2, 8], [1, 1, 1, 2, 3, 3, 4], [1, 1, 1, 2, 3, 7], [1, 1, 1, 2, 4, 6], [1, 1, 1, 2, 5, 5], [1, 1, 1, 2, 10], [1, 1, 1, 3, 3, 3, 3], [1, 1, 1, 3, 3, 6], [1, 1, 1, 3, 4, 5], [1, 1, 1, 3, 9], [1, 1, 1, 4, 4, 4], [1, 1, 1, 4, 8], [1, 1, 1, 5, 7], [1, 1, 1, 6, 6], [1, 1, 2, 2, 2, 2, 5], [1, 1, 2, 2, 2, 3, 4], [1, 1, 2, 2, 2, 7], [1, 1, 2, 2, 3, 3, 3], [1, 1, 2, 2, 3, 6], [1, 1, 2, 2, 4, 5], [1, 1, 2, 2, 9], [1, 1, 2, 3, 3, 5], [1, 1, 2, 3, 4, 4], [1, 1, 2, 3, 8], [1, 1, 2, 4, 7], [1, 1, 2, 5, 6], [1, 1, 2, 11], [1, 1, 3, 3, 3, 4], [1, 1, 3, 3, 7], [1, 1, 3, 4, 6], [1, 1, 3, 5, 5], [1, 1, 3, 10], [1, 1, 4, 4, 5], [1, 1, 4, 9], [1, 1, 5, 8], [1, 1, 6, 7], [1, 2, 2, 2, 2, 3, 3], [1, 2, 2, 2, 2, 6], [1, 2, 2, 2, 3, 5], [1, 2, 2, 2, 4, 4], [1, 2, 2, 2, 8], [1, 2, 2, 3, 3, 4], [1, 2, 2, 3, 7], [1, 2, 2, 4, 6], [1, 2, 2, 5, 5], [1, 2, 2, 10], [1, 2, 3, 3, 3, 3], [1, 2, 3, 3, 6], [1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 4, 4, 4], [1, 2, 4, 8], [1, 2, 5, 7], [1, 2, 6, 6], [1, 3, 3, 3, 5], [1, 3, 3, 4, 4], [1, 3, 3, 8], [1, 3, 4, 7], [1, 3, 5, 6], [1, 3, 11], [1, 4, 4, 6], [1, 4, 5, 5], [1, 4, 10], [1, 5, 9], [1, 6, 8], [1, 7, 7], [2, 2, 2, 2, 3, 4], [2, 2, 2, 2, 7], [2, 2, 2, 3, 3, 3], [2, 2, 2, 3, 6], [2, 2, 2, 4, 5], [2, 2, 2, 9], [2, 2, 3, 3, 5], [2, 2, 3, 4, 4], [2, 2, 3, 8], [2, 2, 4, 7], [2, 2, 5, 6], [2, 2, 11], [2, 3, 3, 3, 4], [2, 3, 3, 7], [2, 3, 4, 6], [2, 3, 5, 5], [2, 3, 10], [2, 4, 4, 5], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 3, 3, 6], [3, 3, 4, 5], [3, 3, 9], [3, 4, 4, 4], [3, 4, 8], [3, 5, 7], [3, 6, 6], [4, 4, 7], [4, 5, 6], [4, 11], [5, 5, 5], [5, 10], [6, 9], [7, 8]]
# updated_fifteen_combs = []
# for item in fifteen_combs:
#     num_one = item.count(1)
#     num_eleven = item.count(11)
#     if (num_one + num_eleven) <= 4:
#         updated_fifteen_combs.append(item)
# print(updated_fifteen_combs)
# print(len(updated_fifteen_combs))

# # 120
# # 152
# sixteen_combs = [[1, 1, 1, 1, 2, 2, 2, 2, 4], [1, 1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 1, 1, 2, 2, 2, 6], [1, 1, 1, 1, 2, 2, 3, 5], [1, 1, 1, 1, 2, 2, 4, 4], [1, 1, 1, 1, 2, 2, 8], [1, 1, 1, 1, 2, 3, 3, 4], [1, 1, 1, 1, 2, 3, 7], [1, 1, 1, 1, 2, 4, 6], [1, 1, 1, 1, 2, 5, 5], [1, 1, 1, 1, 2, 10], [1, 1, 1, 1, 3, 3, 3, 3], [1, 1, 1, 1, 3, 3, 6], [1, 1, 1, 1, 3, 4, 5], [1, 1, 1, 1, 3, 9], [1, 1, 1, 1, 4, 4, 4], [1, 1, 1, 1, 4, 8], [1, 1, 1, 1, 5, 7], [1, 1, 1, 1, 6, 6], [1, 1, 1, 2, 2, 2, 2, 5], [1, 1, 1, 2, 2, 2, 3, 4], [1, 1, 1, 2, 2, 2, 7], [1, 1, 1, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 3, 6], [1, 1, 1, 2, 2, 4, 5], [1, 1, 1, 2, 2, 9], [1, 1, 1, 2, 3, 3, 5], [1, 1, 1, 2, 3, 4, 4], [1, 1, 1, 2, 3, 8], [1, 1, 1, 2, 4, 7], [1, 1, 1, 2, 5, 6], [1, 1, 1, 2, 11], [1, 1, 1, 3, 3, 3, 4], [1, 1, 1, 3, 3, 7], [1, 1, 1, 3, 4, 6], [1, 1, 1, 3, 5, 5], [1, 1, 1, 3, 10], [1, 1, 1, 4, 4, 5], [1, 1, 1, 4, 9], [1, 1, 1, 5, 8], [1, 1, 1, 6, 7], [1, 1, 2, 2, 2, 2, 3, 3], [1, 1, 2, 2, 2, 2, 6], [1, 1, 2, 2, 2, 3, 5], [1, 1, 2, 2, 2, 4, 4], [1, 1, 2, 2, 2, 8], [1, 1, 2, 2, 3, 3, 4], [1, 1, 2, 2, 3, 7], [1, 1, 2, 2, 4, 6], [1, 1, 2, 2, 5, 5], [1, 1, 2, 2, 10], [1, 1, 2, 3, 3, 3, 3], [1, 1, 2, 3, 3, 6], [1, 1, 2, 3, 4, 5], [1, 1, 2, 3, 9], [1, 1, 2, 4, 4, 4], [1, 1, 2, 4, 8], [1, 1, 2, 5, 7], [1, 1, 2, 6, 6], [1, 1, 3, 3, 3, 5], [1, 1, 3, 3, 4, 4], [1, 1, 3, 3, 8], [1, 1, 3, 4, 7], [1, 1, 3, 5, 6], [1, 1, 3, 11], [1, 1, 4, 4, 6], [1, 1, 4, 5, 5], [1, 1, 4, 10], [1, 1, 5, 9], [1, 1, 6, 8], [1, 1, 7, 7], [1, 2, 2, 2, 2, 3, 4], [1, 2, 2, 2, 2, 7], [1, 2, 2, 2, 3, 3, 3], [1, 2, 2, 2, 3, 6], [1, 2, 2, 2, 4, 5], [1, 2, 2, 2, 9], [1, 2, 2, 3, 3, 5], [1, 2, 2, 3, 4, 4], [1, 2, 2, 3, 8], [1, 2, 2, 4, 7], [1, 2, 2, 5, 6], [1, 2, 2, 11], [1, 2, 3, 3, 3, 4], [1, 2, 3, 3, 7], [1, 2, 3, 4, 6], [1, 2, 3, 5, 5], [1, 2, 3, 10], [1, 2, 4, 4, 5], [1, 2, 4, 9], [1, 2, 5, 8], [1, 2, 6, 7], [1, 3, 3, 3, 6], [1, 3, 3, 4, 5], [1, 3, 3, 9], [1, 3, 4, 4, 4], [1, 3, 4, 8], [1, 3, 5, 7], [1, 3, 6, 6], [1, 4, 4, 7], [1, 4, 5, 6], [1, 4, 11], [1, 5, 5, 5], [1, 5, 10], [1, 6, 9], [1, 7, 8], [2, 2, 2, 2, 3, 5], [2, 2, 2, 2, 4, 4], [2, 2, 2, 2, 8], [2, 2, 2, 3, 3, 4], [2, 2, 2, 3, 7], [2, 2, 2, 4, 6], [2, 2, 2, 5, 5], [2, 2, 2, 10], [2, 2, 3, 3, 3, 3], [2, 2, 3, 3, 6], [2, 2, 3, 4, 5], [2, 2, 3, 9], [2, 2, 4, 4, 4], [2, 2, 4, 8], [2, 2, 5, 7], [2, 2, 6, 6], [2, 3, 3, 3, 5], [2, 3, 3, 4, 4], [2, 3, 3, 8], [2, 3, 4, 7], [2, 3, 5, 6], [2, 3, 11], [2, 4, 4, 6], [2, 4, 5, 5], [2, 4, 10], [2, 5, 9], [2, 6, 8], [2, 7, 7], [3, 3, 3, 3, 4], [3, 3, 3, 7], [3, 3, 4, 6], [3, 3, 5, 5], [3, 3, 10], [3, 4, 4, 5], [3, 4, 9], [3, 5, 8], [3, 6, 7], [4, 4, 4, 4], [4, 4, 8], [4, 5, 7], [4, 6, 6], [5, 5, 6], [5, 11], [6, 10], [7, 9], [8, 8]]
# updated_sixteen_combs = []
# for item in sixteen_combs:
#     num_one = item.count(1)
#     num_eleven = item.count(11)
#     if (num_one + num_eleven) <= 4:
#         updated_sixteen_combs.append(item)
# print(updated_sixteen_combs)
# print(len(updated_sixteen_combs))


# combs_list = [[[1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 1, 2, 2, 4], [1, 1, 1, 1, 2, 3, 3], [1, 1, 1, 1, 2, 6], [1, 1, 1, 1, 3, 5], [1, 1, 1, 1, 4, 4], [1, 1, 1, 1, 8], [1, 1, 1, 2, 2, 2, 3], [1, 1, 1, 2, 2, 5], [1, 1, 1, 2, 3, 4], [1, 1, 1, 2, 7], [1, 1, 1, 3, 3, 3], [1, 1, 1, 3, 6], [1, 1, 1, 4, 5], [1, 1, 1, 9], [1, 1, 2, 2, 2, 4], [1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 6], [1, 1, 2, 3, 5], [1, 1, 2, 4, 4], [1, 1, 2, 8], [1, 1, 3, 3, 4], [1, 1, 3, 7], [1, 1, 4, 6], [1, 1, 5, 5], [1, 1, 10], [1, 2, 2, 2, 2, 3], [1, 2, 2, 2, 5], [1, 2, 2, 3, 4], [1, 2, 2, 7], [1, 2, 3, 3, 3], [1, 2, 3, 6], [1, 2, 4, 5], [1, 2, 9], [1, 3, 3, 5], [1, 3, 4, 4], [1, 3, 8], [1, 4, 7], [1, 5, 6], [1, 11], [2, 2, 2, 2, 4], [2, 2, 2, 3, 3], [2, 2, 2, 6], [2, 2, 3, 5], [2, 2, 4, 4], [2, 2, 8], [2, 3, 3, 4], [2, 3, 7], [2, 4, 6], [2, 5, 5], [2, 10], [3, 3, 3, 3], [3, 3, 6], [3, 4, 5], [3, 9], [4, 4, 4], [4, 8], [5, 7], [6, 6]], 
# [[1, 1, 1, 1, 2, 2, 2, 3], [1, 1, 1, 1, 2, 2, 5], [1, 1, 1, 1, 2, 3, 4], [1, 1, 1, 1, 2, 7], [1, 1, 1, 1, 3, 3, 3], [1, 1, 1, 1, 3, 6], [1, 1, 1, 1, 4, 5], [1, 1, 1, 1, 9], [1, 1, 1, 2, 2, 2, 4], [1, 1, 1, 2, 2, 3, 3], [1, 1, 1, 2, 2, 6], [1, 1, 1, 2, 3, 5], [1, 1, 1, 2, 4, 4], [1, 1, 1, 2, 8], [1, 1, 1, 3, 3, 4], [1, 1, 1, 3, 7], [1, 1, 1, 4, 6], [1, 1, 1, 5, 5], [1, 1, 1, 10], [1, 1, 2, 2, 2, 2, 3], [1, 1, 2, 2, 2, 5], [1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 7], [1, 1, 2, 3, 3, 3], [1, 1, 2, 3, 6], [1, 1, 2, 4, 5], [1, 1, 2, 9], [1, 1, 3, 3, 5], [1, 1, 3, 4, 4], [1, 1, 3, 8], [1, 1, 4, 7], [1, 1, 5, 6], [1, 1, 11], [1, 2, 2, 2, 2, 4], [1, 2, 2, 2, 3, 3], [1, 2, 2, 2, 6], [1, 2, 2, 3, 5], [1, 2, 2, 4, 4], [1, 2, 2, 8], [1, 2, 3, 3, 4], [1, 2, 3, 7], [1, 2, 4, 6], [1, 2, 5, 5], [1, 2, 10], [1, 3, 3, 3, 3], [1, 3, 3, 6], [1, 3, 4, 5], [1, 3, 9], [1, 4, 4, 4], [1, 4, 8], [1, 5, 7], [1, 6, 6], [2, 2, 2, 2, 5], [2, 2, 2, 3, 4], [2, 2, 2, 7], [2, 2, 3, 3, 3], [2, 2, 3, 6], [2, 2, 4, 5], [2, 2, 9], [2, 3, 3, 5], [2, 3, 4, 4], [2, 3, 8], [2, 4, 7], [2, 5, 6], [2, 11], [3, 3, 3, 4], [3, 3, 7], [3, 4, 6], [3, 5, 5], [3, 10], [4, 4, 5], [4, 9], [5, 8], [6, 7]],
# [[1, 1, 1, 1, 2, 2, 2, 4], [1, 1, 1, 1, 2, 2, 3, 3], [1, 1, 1, 1, 2, 2, 6], [1, 1, 1, 1, 2, 3, 5], [1, 1, 1, 1, 2, 4, 4], [1, 1, 1, 1, 2, 8], [1, 1, 1, 1, 3, 3, 4], [1, 1, 1, 1, 3, 7], [1, 1, 1, 1, 4, 6], [1, 1, 1, 1, 5, 5], [1, 1, 1, 1, 10], [1, 1, 1, 2, 2, 2, 2, 3], [1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 2, 2, 3, 4], [1, 1, 1, 2, 2, 7], [1, 1, 1, 2, 3, 3, 3], [1, 1, 1, 2, 3, 6], [1, 1, 1, 2, 4, 5], [1, 1, 1, 2, 9], [1, 1, 1, 3, 3, 5], [1, 1, 1, 3, 4, 4], [1, 1, 1, 3, 8], [1, 1, 1, 4, 7], [1, 1, 1, 5, 6], [1, 1, 1, 11], [1, 1, 2, 2, 2, 2, 4], [1, 1, 2, 2, 2, 3, 3], [1, 1, 2, 2, 2, 6], [1, 1, 2, 2, 3, 5], [1, 1, 2, 2, 4, 4], [1, 1, 2, 2, 8], [1, 1, 2, 3, 3, 4], [1, 1, 2, 3, 7], [1, 1, 2, 4, 6], [1, 1, 2, 5, 5], [1, 1, 2, 10], [1, 1, 3, 3, 3, 3], [1, 1, 3, 3, 6], [1, 1, 3, 4, 5], [1, 1, 3, 9], [1, 1, 4, 4, 4], [1, 1, 4, 8], [1, 1, 5, 7], [1, 1, 6, 6], [1, 2, 2, 2, 2, 5], [1, 2, 2, 2, 3, 4], [1, 2, 2, 2, 7], [1, 2, 2, 3, 3, 3], [1, 2, 2, 3, 6], [1, 2, 2, 4, 5], [1, 2, 2, 9], [1, 2, 3, 3, 5], [1, 2, 3, 4, 4], [1, 2, 3, 8], [1, 2, 4, 7], [1, 2, 5, 6], [1, 2, 11], [1, 3, 3, 3, 4], [1, 3, 3, 7], [1, 3, 4, 6], [1, 3, 5, 5], [1, 3, 10], [1, 4, 4, 5], [1, 4, 9], [1, 5, 8], [1, 6, 7], [2, 2, 2, 2, 3, 3], [2, 2, 2, 2, 6], [2, 2, 2, 3, 5], [2, 2, 2, 4, 4], [2, 2, 2, 8], [2, 2, 3, 3, 4], [2, 2, 3, 7], [2, 2, 4, 6], [2, 2, 5, 5], [2, 2, 10], [2, 3, 3, 3, 3], [2, 3, 3, 6], [2, 3, 4, 5], [2, 3, 9], [2, 4, 4, 4], [2, 4, 8], [2, 5, 7], [2, 6, 6], [3, 3, 3, 5], [3, 3, 4, 4], [3, 3, 8], [3, 4, 7], [3, 5, 6], [3, 11], [4, 4, 6], [4, 5, 5], [4, 10], [5, 9], [6, 8], [7, 7]],
# [[1, 1, 1, 1, 2, 2, 2, 2, 3], [1, 1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 1, 2, 2, 3, 4], [1, 1, 1, 1, 2, 2, 7], [1, 1, 1, 1, 2, 3, 3, 3], [1, 1, 1, 1, 2, 3, 6], [1, 1, 1, 1, 2, 4, 5], [1, 1, 1, 1, 2, 9], [1, 1, 1, 1, 3, 3, 5], [1, 1, 1, 1, 3, 4, 4], [1, 1, 1, 1, 3, 8], [1, 1, 1, 1, 4, 7], [1, 1, 1, 1, 5, 6], [1, 1, 1, 2, 2, 2, 2, 4], [1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 1, 2, 2, 2, 6], [1, 1, 1, 2, 2, 3, 5], [1, 1, 1, 2, 2, 4, 4], [1, 1, 1, 2, 2, 8], [1, 1, 1, 2, 3, 3, 4], [1, 1, 1, 2, 3, 7], [1, 1, 1, 2, 4, 6], [1, 1, 1, 2, 5, 5], [1, 1, 1, 2, 10], [1, 1, 1, 3, 3, 3, 3], [1, 1, 1, 3, 3, 6], [1, 1, 1, 3, 4, 5], [1, 1, 1, 3, 9], [1, 1, 1, 4, 4, 4], [1, 1, 1, 4, 8], [1, 1, 1, 5, 7], [1, 1, 1, 6, 6], [1, 1, 2, 2, 2, 2, 5], [1, 1, 2, 2, 2, 3, 4], [1, 1, 2, 2, 2, 7], [1, 1, 2, 2, 3, 3, 3], [1, 1, 2, 2, 3, 6], [1, 1, 2, 2, 4, 5], [1, 1, 2, 2, 9], [1, 1, 2, 3, 3, 5], [1, 1, 2, 3, 4, 4], [1, 1, 2, 3, 8], [1, 1, 2, 4, 7], [1, 1, 2, 5, 6], [1, 1, 2, 11], [1, 1, 3, 3, 3, 4], [1, 1, 3, 3, 7], [1, 1, 3, 4, 6], [1, 1, 3, 5, 5], [1, 1, 3, 10], [1, 1, 4, 4, 5], [1, 1, 4, 9], [1, 1, 5, 8], [1, 1, 6, 7], [1, 2, 2, 2, 2, 3, 3], [1, 2, 2, 2, 2, 6], [1, 2, 2, 2, 3, 5], [1, 2, 2, 2, 4, 4], [1, 2, 2, 2, 8], [1, 2, 2, 3, 3, 4], [1, 2, 2, 3, 7], [1, 2, 2, 4, 6], [1, 2, 2, 5, 5], [1, 2, 2, 10], [1, 2, 3, 3, 3, 3], [1, 2, 3, 3, 6], [1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 4, 4, 4], [1, 2, 4, 8], [1, 2, 5, 7], [1, 2, 6, 6], [1, 3, 3, 3, 5], [1, 3, 3, 4, 4], [1, 3, 3, 8], [1, 3, 4, 7], [1, 3, 5, 6], [1, 3, 11], [1, 4, 4, 6], [1, 4, 5, 5], [1, 4, 10], [1, 5, 9], [1, 6, 8], [1, 7, 7], [2, 2, 2, 2, 3, 4], [2, 2, 2, 2, 7], [2, 2, 2, 3, 3, 3], [2, 2, 2, 3, 6], [2, 2, 2, 4, 5], [2, 2, 2, 9], [2, 2, 3, 3, 5], [2, 2, 3, 4, 4], [2, 2, 3, 8], [2, 2, 4, 7], [2, 2, 5, 6], [2, 2, 11], [2, 3, 3, 3, 4], [2, 3, 3, 7], [2, 3, 4, 6], [2, 3, 5, 5], [2, 3, 10], [2, 4, 4, 5], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 3, 3, 6], [3, 3, 4, 5], [3, 3, 9], [3, 4, 4, 4], [3, 4, 8], [3, 5, 7], [3, 6, 6], [4, 4, 7], [4, 5, 6], [4, 11], [5, 5, 5], [5, 10], [6, 9], [7, 8]],
# [[1, 1, 1, 1, 2, 2, 2, 2, 4], [1, 1, 1, 1, 2, 2, 2, 3, 3], [1, 1, 1, 1, 2, 2, 2, 6], [1, 1, 1, 1, 2, 2, 3, 5], [1, 1, 1, 1, 2, 2, 4, 4], [1, 1, 1, 1, 2, 2, 8], [1, 1, 1, 1, 2, 3, 3, 4], [1, 1, 1, 1, 2, 3, 7], [1, 1, 1, 1, 2, 4, 6], [1, 1, 1, 1, 2, 5, 5], [1, 1, 1, 1, 2, 10], [1, 1, 1, 1, 3, 3, 3, 3], [1, 1, 1, 1, 3, 3, 6], [1, 1, 1, 1, 3, 4, 5], [1, 1, 1, 1, 3, 9], [1, 1, 1, 1, 4, 4, 4], [1, 1, 1, 1, 4, 8], [1, 1, 1, 1, 5, 7], [1, 1, 1, 1, 6, 6], [1, 1, 1, 2, 2, 2, 2, 5], [1, 1, 1, 2, 2, 2, 3, 4], [1, 1, 1, 2, 2, 2, 7], [1, 1, 1, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 3, 6], [1, 1, 1, 2, 2, 4, 5], [1, 1, 1, 2, 2, 9], [1, 1, 1, 2, 3, 3, 5], [1, 1, 1, 2, 3, 4, 4], [1, 1, 1, 2, 3, 8], [1, 1, 1, 2, 4, 7], [1, 1, 1, 2, 5, 6], [1, 1, 1, 2, 11], [1, 1, 1, 3, 3, 3, 4], [1, 1, 1, 3, 3, 7], [1, 1, 1, 3, 4, 6], [1, 1, 1, 3, 5, 5], [1, 1, 1, 3, 10], [1, 1, 1, 4, 4, 5], [1, 1, 1, 4, 9], [1, 1, 1, 5, 8], [1, 1, 1, 6, 7], [1, 1, 2, 2, 2, 2, 3, 3], [1, 1, 2, 2, 2, 2, 6], [1, 1, 2, 2, 2, 3, 5], [1, 1, 2, 2, 2, 4, 4], [1, 1, 2, 2, 2, 8], [1, 1, 2, 2, 3, 3, 4], [1, 1, 2, 2, 3, 7], [1, 1, 2, 2, 4, 6], [1, 1, 2, 2, 5, 5], [1, 1, 2, 2, 10], [1, 1, 2, 3, 3, 3, 3], [1, 1, 2, 3, 3, 6], [1, 1, 2, 3, 4, 5], [1, 1, 2, 3, 9], [1, 1, 2, 4, 4, 4], [1, 1, 2, 4, 8], [1, 1, 2, 5, 7], [1, 1, 2, 6, 6], [1, 1, 3, 3, 3, 5], [1, 1, 3, 3, 4, 4], [1, 1, 3, 3, 8], [1, 1, 3, 4, 7], [1, 1, 3, 5, 6], [1, 1, 3, 11], [1, 1, 4, 4, 6], [1, 1, 4, 5, 5], [1, 1, 4, 10], [1, 1, 5, 9], [1, 1, 6, 8], [1, 1, 7, 7], [1, 2, 2, 2, 2, 3, 4], [1, 2, 2, 2, 2, 7], [1, 2, 2, 2, 3, 3, 3], [1, 2, 2, 2, 3, 6], [1, 2, 2, 2, 4, 5], [1, 2, 2, 2, 9], [1, 2, 2, 3, 3, 5], [1, 2, 2, 3, 4, 4], [1, 2, 2, 3, 8], [1, 2, 2, 4, 7], [1, 2, 2, 5, 6], [1, 2, 2, 11], [1, 2, 3, 3, 3, 4], [1, 2, 3, 3, 7], [1, 2, 3, 4, 6], [1, 2, 3, 5, 5], [1, 2, 3, 10], [1, 2, 4, 4, 5], [1, 2, 4, 9], [1, 2, 5, 8], [1, 2, 6, 7], [1, 3, 3, 3, 6], [1, 3, 3, 4, 5], [1, 3, 3, 9], [1, 3, 4, 4, 4], [1, 3, 4, 8], [1, 3, 5, 7], [1, 3, 6, 6], [1, 4, 4, 7], [1, 4, 5, 6], [1, 4, 11], [1, 5, 5, 5], [1, 5, 10], [1, 6, 9], [1, 7, 8], [2, 2, 2, 2, 3, 5], [2, 2, 2, 2, 4, 4], [2, 2, 2, 2, 8], [2, 2, 2, 3, 3, 4], [2, 2, 2, 3, 7], [2, 2, 2, 4, 6], [2, 2, 2, 5, 5], [2, 2, 2, 10], [2, 2, 3, 3, 3, 3], [2, 2, 3, 3, 6], [2, 2, 3, 4, 5], [2, 2, 3, 9], [2, 2, 4, 4, 4], [2, 2, 4, 8], [2, 2, 5, 7], [2, 2, 6, 6], [2, 3, 3, 3, 5], [2, 3, 3, 4, 4], [2, 3, 3, 8], [2, 3, 4, 7], [2, 3, 5, 6], [2, 3, 11], [2, 4, 4, 6], [2, 4, 5, 5], [2, 4, 10], [2, 5, 9], [2, 6, 8], [2, 7, 7], [3, 3, 3, 3, 4], [3, 3, 3, 7], [3, 3, 4, 6], [3, 3, 5, 5], [3, 3, 10], [3, 4, 4, 5], [3, 4, 9], [3, 5, 8], [3, 6, 7], [4, 4, 4, 4], [4, 4, 8], [4, 5, 7], [4, 6, 6], [5, 5, 6], [5, 11], [6, 10], [7, 9], [8, 8]]]

# length_list = []
# for i in combs_list:
#     for comb in i:
#         length_list.append(len(comb))

# print(length_list)
# print("average is:", sum(length_list)/len(length_list))
