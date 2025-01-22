import numpy as np

# Create a 3x3 array of random integers between 0 and 9
array = np.random.randint(0, 10, (3, 3))

print("Here's your matrix of chaos:")
print(array)

# Transpose it because why not?
transposed = array.T
print("\nBehold! The matrix flipped on its side (transposed):")
print(transposed)

# Find the max value and its position
max_value = np.max(array)
max_position = np.unravel_index(np.argmax(array), array.shape)
print(f"\nThe matrix's boss (max value) is {max_value}, chilling at position {max_position}.")

# Replace all evens with 0 because odds are cooler
odds_rule = np.where(array % 2 == 0, 0, array)
print("\nEvicting even numbers. Odds, you run the show now:")
print(odds_rule)
s