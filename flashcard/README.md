# How to Build a Flashcard Quiz App in Python

In this tutorial, we’re going to build a simple **Flashcard Quiz App** in Python. Flashcard apps are a great way to help with learning, and this project will help you practice essential Python concepts like lists, dictionaries, loops, and user input handling.

---

## What We’re Building

The Flashcard Quiz App will present a set of flashcards to the user, asking a question on each one. The user will type an answer, and the app will check if it’s correct. At the end of the quiz, the app will provide the user’s score.

### Key Python Concepts Covered:
- Lists and dictionaries
- Loops
- Functions
- Conditionals (`if`, `else`)
- User input handling

---

## Step 1: **Setting Up the Flashcards**

We’ll use a **dictionary** to store our flashcards, where each key is a question, and each value is the correct answer. 

Here’s a simple set of flashcards:

```python
flashcards = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote '1984'?": "George Orwell",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}
```

- **Why a dictionary?**: We use a dictionary because it allows us to easily store each question-answer pair.

---

## Step 2: **Building the Main Quiz Loop**

We’ll create a function to handle the main quiz loop, which will go through the flashcards one by one, ask the user the question, and check if their answer is correct.

Here’s the basic logic for the quiz:

```python
def quiz_user(flashcards):
    score = 0  # Initialize the score to 0
    total_questions = len(flashcards)  # Total number of questions

    for question, correct_answer in flashcards.items():
        user_answer = input(question + " ").strip()  # Ask the user the question
        if user_answer.lower() == correct_answer.lower():  # Check if the answer is correct
            print("Correct!")
            score += 1  # Increment the score if the answer is correct
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
    
    return score, total_questions
```

### Breaking Down the Function:

1. **Score Tracking**:
   ```python
   score = 0
   ```
   - **Why?**: We initialize the score to 0 to track how many questions the user answers correctly.

2. **Loop Through Flashcards**:
   ```python
   for question, correct_answer in flashcards.items():
   ```
   - **Why?**: The loop goes through each question-answer pair in the `flashcards` dictionary. The `.items()` method allows us to get both the question and the correct answer in each iteration.

3. **Getting the User’s Answer**:
   ```python
   user_answer = input(question + " ").strip()
   ```
   - **Why?**: We use `input()` to ask the user each question. We also use `.strip()` to remove any extra spaces before or after their answer.

4. **Checking if the Answer is Correct**:
   ```python
   if user_answer.lower() == correct_answer.lower():
   ```
   - **Why?**: We compare the user’s answer to the correct answer, ignoring case sensitivity by using `.lower()`. If the answer is correct, we increment the score; otherwise, we show the correct answer.

5. **Returning the Results**:
   ```python
   return score, total_questions
   ```
   - **Why?**: After the loop, we return both the user’s score and the total number of questions so that we can display their final results.

---

## Step 3: **Displaying the Final Score**

Once the quiz is complete, we’ll show the user how many questions they got right and give them a percentage score.

Here’s the code for that:

```python
def display_score(score, total_questions):
    print(f"\nYou got {score} out of {total_questions} correct!")
    percentage = (score / total_questions) * 100
    print(f"Your score: {percentage:.2f}%")
```

### Breaking It Down:

1. **Displaying the Score**:
   ```python
   print(f"\nYou got {score} out of {total_questions} correct!")
   ```
   - **Why?**: This simply prints the user’s raw score (how many questions they got right out of the total).

2. **Calculating the Percentage**:
   ```python
   percentage = (score / total_questions) * 100
   ```
   - **Why?**: This calculates the percentage of correct answers by dividing the score by the total number of questions and multiplying by 100.

---

## Step 4: **Putting It All Together**

Now, let’s bring everything together into the main function and make the app run.

Here’s the full code for the Flashcard Quiz App:

```python
import random

flashcards = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote '1984'?": "George Orwell",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}

def quiz_user(flashcards):
    score = 0
    total_questions = len(flashcards)

    for question, correct_answer in flashcards.items():
        user_answer = input(question + " ").strip()
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
    
    return score, total_questions

def display_score(score, total_questions):
    print(f"\nYou got {score} out of {total_questions} correct!")
    percentage = (score / total_questions) * 100
    print(f"Your score: {percentage:.2f}%")

def main():
    print("Welcome to the Flashcard Quiz!")
    score, total_questions = quiz_user(flashcards)
    display_score(score, total_questions)

if __name__ == "__main__":
    main()
```

### How It Works:

- The `main()` function starts by welcoming the user to the quiz.
- It then calls the `quiz_user()` function to handle the quiz itself and returns the score and total questions.
- Finally, it displays the user’s score using `display_score()`.

---

## Step 5: **Additional Features (Optional)**

Now that the basic Flashcard Quiz App is complete, here are some ideas for enhancing it:

1. **Shuffle the Questions**:
   - Use `random.shuffle()` to randomize the order of the questions each time the user takes the quiz.
   ```python
   questions = list(flashcards.items())
   random.shuffle(questions)
   ```

2. **Add More Flashcards**:
   - You can add more flashcards to your dictionary to make the quiz longer and more challenging.

3. **Multiple-Choice Format**:
   - Instead of asking the user to type out answers, you could turn the game into a multiple-choice quiz, where they select from a list of options.

4. **Track High Scores**:
   - Keep track of the user’s best scores across multiple games by saving their scores to a file or database.

---

## Conclusion

Congratulations! You’ve just built a **Flashcard Quiz App** using Python. This project introduced you to working with dictionaries, loops, functions, and user input. It’s a great way to practice fundamental Python skills while building something fun and educational.

From here, feel free to add your own flashcards, enhance the game with new features, or even create different types of quizzes!

Happy coding! 🎉
