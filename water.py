def calculate_water(bars_list):
    if len(bars_list) < 3:
        return 0
    water = 0

    for bar in range(1, len(bars_list) - 1):

        left_side_amir = bars_list[:bar]
        right_side_amir = bars_list[bar:]
        left_max_amir = max(left_side_amir)
        right_max_amir = max(right_side_amir)

        min_bar = min(left_max_amir, right_max_amir)

        calculated_water = min_bar - bars_list[bar]
        if calculated_water > 0:
            water += calculated_water

    return water
