dp = [[-1 for i in range(3001)] for j in range(1001)]

def carry_bananas(distance, bananas, max_load):
	if (bananas <= distance):
		return 0

	if (bananas <= max_load):
		return bananas - distance

	if (distance == 0):
		return bananas

	if (dp[distance][bananas] != -1):
		return dp[distance][bananas]

	max_count = -2**32

	trip_count = ((2 * bananas) // max_load) - 1 if(bananas % max_load == 0) else ((2 * bananas) // max_load) + 1

	for i in range(1, distance + 1):
		current_count = carry_bananas(distance - i, bananas - trip_count * i, max_load)

		if (current_count > max_count):
			max_count = current_count

			dp[distance][bananas] = max_count

	return max_count

if __name__ == '__main__':
    print(carry_bananas(1000, 3000, 1000))
