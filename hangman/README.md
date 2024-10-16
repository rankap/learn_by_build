# Building a Hangman Game in Python: Step-by-Step Tutorial

In this tutorial, we’re going to create a simple Hangman game in Python. Hangman is a popular word-guessing game where the player tries to guess a word letter by letter, within a limited number of guesses.

By the end of this tutorial, you'll learn how to:
- Work with loops, conditionals, and user input
- Use lists, strings, and basic Python functions
- Implement basic game logic in Python

Let’s get started!

---

Let's break down the Hangman game code step by step and explain the reasoning behind each part. The goal is to understand not just *what* the code does, but also *why* we're doing it.

---

## Step 1: **Importing the `random` Module**

```python
import random
```

**Why?**
We need to randomly select a word from our word list. Python’s `random` module provides the `choice()` function, which lets us choose a random element from a list. Since Hangman requires a random word for the player to guess, this module is essential.

---

## Step 2: **Defining a List of Words**

```python
word_list = ['python', 'java', 'swift', 'hangman', 'programming', 'developer', 'keyboard', 'monitor']
```

**Why?**
The game needs a list of words for the player to guess. This list can be as short or long as you like. Each time the game starts, it picks a random word from this list for the player to guess.

---

## Step 3: **Function to Select a Random Word**

```python
def get_random_word(word_list):
    return random.choice(word_list)
```

**Why?**
The `get_random_word()` function uses `random.choice()` to pick one word from the `word_list`. This allows the game to choose a different word each time, adding variety to the gameplay.

- **Function Definition (`def`)**: We define the function `get_random_word()` to make the code more modular. Whenever we want a random word, we can just call this function instead of repeating the same line of code.
- **`random.choice()`**: Picks one word from the list, ensuring randomness for each game session.

---

## Step 4: **Main Game Logic**

Now let’s move to the core part of the game, where we handle the guessing and checking of letters.

```python
def play_hangman():
    word = get_random_word(word_list)  # Pick a random word
    word_letters = set(word)  # The unique letters in the word
    guessed_letters = set()   # The letters the user has guessed
    wrong_guesses = 0
    max_guesses = 6           # Number of wrong guesses allowed

    print("Welcome to Hangman!")
```

### Breaking This Down:

1. **Random Word**: 
   ```python
   word = get_random_word(word_list)
   ```
   - **Why?**: We need to pick a word for the player to guess. The function call `get_random_word(word_list)` selects that word.
   
2. **Track Letters in the Word**:
   ```python
   word_letters = set(word)
   ```
   - **Why?**: We convert the word into a set of its unique letters (`set(word)`). This helps us keep track of which letters the player still needs to guess. For example, if the word is “python,” the set will contain `{'p', 'y', 't', 'h', 'o', 'n'}`. Each time the player guesses correctly, we remove the guessed letter from this set.

3. **Track Guessed Letters**:
   ```python
   guessed_letters = set()
   ```
   - **Why?**: We initialize an empty set to store all the letters the player has guessed so far. This ensures that the player can’t guess the same letter twice without being warned.
   
4. **Wrong Guess Counter**:
   ```python
   wrong_guesses = 0
   max_guesses = 6
   ```
   - **Why?**: We initialize `wrong_guesses` to 0. Each time the player guesses wrong, we increment this counter. Once it reaches the `max_guesses` (in this case, 6 wrong guesses), the game is over.
   
5. **Game Introduction**:
   ```python
   print("Welcome to Hangman!")
   ```
   - **Why?**: Just a friendly message to the player when the game starts!

---

## Step 5: **Game Loop**

The following section contains a loop that continues until the game ends (either the player wins or they run out of guesses).

```python
    while wrong_guesses < max_guesses and word_letters:
        print(f"\nYou have {max_guesses - wrong_guesses} guesses left.")
        print("Guessed letters:", " ".join(guessed_letters))
        
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word:", " ".join(word_display))
        
        guess = input("Guess a letter: ").lower()
```

### Breaking This Down:

1. **While Loop Condition**:
   ```python
   while wrong_guesses < max_guesses and word_letters:
   ```
   - **Why?**: This loop keeps the game running until either:
     - The player runs out of guesses (`wrong_guesses >= max_guesses`).
     - The player correctly guesses all the letters (`word_letters` becomes empty).

2. **Display Remaining Guesses**:
   ```python
   print(f"\nYou have {max_guesses - wrong_guesses} guesses left.")
   ```
   - **Why?**: Display the number of guesses the player has left. This keeps the player informed about how many chances they still have.

3. **Display Guessed Letters**:
   ```python
   print("Guessed letters:", " ".join(guessed_letters))
   ```
   - **Why?**: Show the letters the player has already guessed. This prevents them from guessing the same letter multiple times and helps track their progress.

4. **Display Word Progress**:
   ```python
   word_display = [letter if letter in guessed_letters else '_' for letter in word]
   print("Current word:", " ".join(word_display))
   ```
   - **Why?**: This displays the word in its current state. Each letter that has been guessed correctly is shown, and the unguessed letters are represented by underscores (`_`).
   - **How?**: We use a list comprehension to create a list where each letter is shown if it has been guessed, or `_` is shown if it hasn’t. For example, if the word is “python” and the player has guessed “p” and “h,” the display will show `p _ _ h _ _`.

5. **Get the Player’s Guess**:
   ```python
   guess = input("Guess a letter: ").lower()
   ```
   - **Why?**: Prompt the player to input their guess. The `input()` function captures the player’s input, and we use `.lower()` to convert it to lowercase (to handle case-insensitive guessing).

---

## Step 6: **Check the Player’s Guess**

Now we need to check if the guess is correct or not, and update the game accordingly.

```python
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print(f"Good job! {guess} is in the word.")
        else:
            guessed_letters.add(guess)
            wrong_guesses += 1
            print(f"{guess} is not in the word.")
```

### Breaking This Down:

1. **Check for Repeated Guesses**:
   ```python
   if guess in guessed_letters:
       print("You already guessed that letter.")
   ```
   - **Why?**: If the player has already guessed the letter before, we inform them and don’t penalize them for repeating the guess.

2. **Correct Guess**:
   ```python
   elif guess in word_letters:
       guessed_letters.add(guess)
       word_letters.remove(guess)
       print(f"Good job! {guess} is in the word.")
   ```
   - **Why?**: If the guessed letter is in the word, we:
     - Add it to `guessed_letters`.
     - Remove it from `word_letters` (since the player no longer needs to guess this letter).
     - Congratulate the player for guessing correctly.

3. **Wrong Guess**:
   ```python
   else:
       guessed_letters.add(guess)
       wrong_guesses += 1
       print(f"{guess} is not in the word.")
   ```
   - **Why?**: If the guessed letter is not in the word, we:
     - Add it to `guessed_letters` (so they don’t guess it again).
     - Increment `wrong_guesses` by 1 to track the wrong guesses.
     - Inform the player that their guess was incorrect.

---

## Step 7: **End of the Game**

After the loop ends, we check if the player won or lost:

```python
    if not word_letters:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nYou ran out of guesses. The word was: {word}")
```

### Breaking This Down:

1. **Player Wins**:
   ```python
   if not word_letters:
       print(f"\nCongratulations! You guessed the word: {word}")
   ```
   - **Why?**: If `word_letters` is empty, that means the player has guessed all the letters correctly, so they win.

2. **Player Loses**:
   ```python
   else:
       print(f"\nYou ran out of guesses. The word was: {word}")
   ```
   - **Why?**: If the player used all their guesses without guessing the word, they lose, and the word is revealed.

---

## Step 8: **Allow the Player to Play Again**

Finally, we ask the player if

 they want to play again after finishing one round of Hangman:

```python
def main():
    while True:
        play_hangman()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
```

### Breaking This Down:

1. **Game Loop**:
   ```python
   while True:
       play_hangman()
       ...
   ```
   - **Why?**: The loop allows the player to keep playing new games until they decide to stop.

2. **Play Again Check**:
   ```python
   play_again = input("\nDo you want to play again? (y/n): ").lower()
   if play_again != 'y':
       print("Thanks for playing!")
       break
   ```
   - **Why?**: After each game, we ask the player if they want to play again. If they type “y,” a new game starts. If they type anything else, the game ends and thanks them for playing.

---

## Conclusion

In this tutorial, we’ve built a complete Hangman game from scratch. The game is structured around essential Python concepts like loops, conditionals, sets, lists, and functions. With just a few enhancements, you can expand the game to include features like ASCII art, difficulty settings, or even reading words from a file. This is an excellent project to practice Python fundamentals in a fun and interactive way!
