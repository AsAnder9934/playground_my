def get_coin_balances(lst1, lst2):
    coins_one = 3
    coins_two = 3
    for action1, action2 in zip(lst1, lst2):

        if action1 == 'share' and action2 == 'share':
            coins_one += 2
            coins_two += 2
        elif action1 == 'share' and action2 == 'steal':
            coins_one -= 1
            coins_two += 3
        elif action1 == 'steal' and action2 == 'share':
            coins_one += 3
            coins_two -= 1
    return coins_one, coins_two