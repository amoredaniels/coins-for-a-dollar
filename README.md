# Tossing Coins for a Dollar Game.

## Instructions 
- For this activity, you will create a Coin class. 
- Create the appropriate getter/setter, and a __str__ method.  
- The program should have three instances a quarter, a dime, and a nickel. 


When the game begins, your starting balance is $0.  During each round of the game, the program will toss the simulated coins.  When a coin is tossed, the value of the coin is added to your balance if it lands heads-up.  

For example, if the quarter lands heads-up, 25 cents is added to your balance.  Nothing is added to your balance for coins that land tails-up.  The game is over when your balance reaches one dollar or more.  If your balance is exactly one dollar, you win the game.  You lose if your balance is more than one dollar.

Example: 
```
Sum balance: $0.00

tossing the coins. . .
Here are the sides:
Quarter:  Heads
Nickel:  Heads
Dime:  Tails

Sum balance: $0.30

tossing the coins. . .
Here are the sides:
Quarter:  Tails
Nickel:  Tails
Dime:  Heads

Sum balance: $0.40

tossing the coins. . .
Here are the sides:
Quarter:  Tails
Nickel:  Heads
Dime:  Tails

Sum balance: $0.45

tossing the coins. . .
Here are the sides:
Quarter:  Heads
Nickel:  Heads
Dime:  Tails

Sum balance: $0.75

tossing the coins. . .
Here are the sides:
Quarter:  Tails
Nickel:  Tails
Dime:  Tails

Sum balance: $0.75

tossing the coins. . .
Here are the sides:
Quarter:  Heads
Nickel:  Heads
Dime:  Heads

Sum balance: $1.15

Game over. You lose.
```
