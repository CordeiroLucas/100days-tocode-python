# Python Lists | Randomization
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
print(random.choice(friends))

# Option 2
randIndex = random.randint(0,len(friends)-1)
print(friends[randIndex])