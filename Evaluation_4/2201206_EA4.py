#with depth limitation
import math
import random

def heuristic_value(current_stones):
    return -current_stones

def get_next_move(current_stones, depth):
    if depth == 0 or current_stones <= 0:
        return heuristic_value(current_stones), 0
    if current_stones <= 0:
        return -1, 0  # AI loses
    elif current_stones == 1:
        return 1, 1  # AI wins
    elif current_stones == 2:
        return 2, 2  # AI wins

    alpha = -math.inf
    beta = math.inf
    best_move = 0
    for move in [1, 2]:
        value = min_value(current_stones - move, alpha, beta, depth - 1)
        if value > alpha:
            alpha = value
            best_move = move
    return best_move, alpha

def max_value(current_stones, alpha, beta, depth):
    if depth == 0 or current_stones <= 0:
        return heuristic_value(current_stones)
    if current_stones <= 0:
        return -1  # AI loses
    elif current_stones == 1:
        return 1  # AI wins
    elif current_stones == 2:
        return -1  # AI loses

    value = -math.inf
    for move in [1, 2]:
        value = max(value, min_value(current_stones - move, alpha, beta, depth - 1))
        if value >= beta:
            return value
        alpha = max(alpha, value)
    return value

def min_value(current_stones, alpha, beta, depth):
    if depth == 0 or current_stones <= 0:
        return heuristic_value(current_stones)
    if current_stones <= 0:
        return 1  # AI wins
    elif current_stones == 1:
        return -1  # AI loses
    elif current_stones == 2:
        return 1  # AI wins

    value = math.inf
    for move in [1, 2]:
        value = min(value, max_value(current_stones - move, alpha, beta, depth - 1))
        if value <= alpha:
            return value
        beta = min(beta, value)
    return value

def play_game():
    current_stones = 50
    depth = 10  # or whatever depth you want
    player_turn = random.choice([True, False])  # True for AI, False for human

    while current_stones > 0:
        print("Stones left:", current_stones)
        if player_turn:  # AI's turn
            move, _ = get_next_move(current_stones, depth)
            print("AI removes", move, "stone(s).")
            current_stones -= move
            if current_stones <= 0:
                print("Player 1 wins.")
                break
        else:  # Human's turn
            move = int(input("Enter number of stones to remove (1 or 2): "))
            current_stones -= move
            if current_stones <= 0:
                print("AI wins.")
                break
        player_turn = not player_turn  # Switch turns

if __name__ == "__main__":
    play_game()


# # with no depth limitation 
# import math
# import random

# def heuristic_value(current_stones):
#     return -current_stones

# def get_next_move(current_stones):
#     if current_stones <= 0:
#         return -1, 0  # AI loses
#     elif current_stones == 1:
#         return 1, 1  # AI wins
#     elif current_stones == 2:
#         return 2, 2  # AI wins

#     alpha = -math.inf
#     beta = math.inf
#     best_move = 0
#     for move in [1, 2]:
#         value = min_value(current_stones - move, alpha, beta)
#         if value > alpha:
#             alpha = value
#             best_move = move
#     return best_move, alpha

# def max_value(current_stones, alpha, beta):
#     if current_stones <= 0:
#         return -1  # AI loses
#     elif current_stones == 1:
#         return 1  # AI wins
#     elif current_stones == 2:
#         return -1  # AI loses

#     value = -math.inf
#     for move in [1, 2]:
#         value = max(value, min_value(current_stones - move, alpha, beta))
#         if value >= beta:
#             return value
#         alpha = max(alpha, value)
#     return value

# def min_value(current_stones, alpha, beta):
#     if current_stones <= 0:
#         return 1  # AI wins
#     elif current_stones == 1:
#         return -1  # AI loses
#     elif current_stones == 2:
#         return 1  # AI wins

#     value = math.inf
#     for move in [1, 2]:
#         value = min(value, max_value(current_stones - move, alpha, beta))
#         if value <= alpha:
#             return value
#         beta = min(beta, value)
#     return value

# def play_game():
#     current_stones = 50
#     player_turn = random.choice([True, False])  # True for AI, False for human

#     while current_stones > 0:
#         print("Stones left:", current_stones)
#         if player_turn:  # AI's turn
#             move, _ = get_next_move(current_stones)
#             print("AI removes", move, "stone(s).")
#             current_stones -= move
#             if current_stones <= 0:
#                 print("Player 1 wins.")
#                 break
#         else:  # Human's turn
#             move = int(input("Enter number of stones to remove (1 or 2): "))
#             current_stones -= move
#             if current_stones <= 0:
#                 print("AI wins.")
#                 break
#         player_turn = not player_turn  # Switch turns

# if __name__ == "__main__":
#     play_game()