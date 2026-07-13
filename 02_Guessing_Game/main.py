import random

# ==================== GAME SETUP ====================
print("=" * 45)
print("🎮 Welcome to the Secret Name Guessing Game 🎮")
print("=" * 45)

player_name = input("What is your name? ")
print(f"\nGood Luck, {player_name}! Let's start the game...")
print("-" * 45)

# ==================== GAME INITIALIZATION ====================
# Initialize game data: Define list of possible names and set maximum allowed attempts
names = ["ahmad", "huda", "sara", "hamza", "sulieman", "nada", "qais", "omar"]
count = 12

# Randomly select a secret name and initialize an empty list to track guessed letters
secret_name = random.choice(names)
guessed_letter = []

# ==================== GAME LOOP ====================
# Main game loop: Continue playing while the player has remaining attempts
while count > 0:

    # STEP 1: Display current progress - Show correctly guessed letters and blanks for remaining letters
    print("\nSecret Name: ", end="")
    for letter in secret_name:
        if letter in guessed_letter:
            print(letter, end='')
        else:
            print("_", end='')
            
    print("\n")

    # STEP 2: Check win condition - Verify if all letters of the secret name have been guessed correctly
    if all(letter in guessed_letter for letter in secret_name):
        print("\nCongratulations, you won")
        break    

    # STEP 3: Get player input - Request a letter guess from the player
    guess = input("\n\nEnter the letter you guess: ").lower().strip()

    # STEP 4: Check for duplicate guess - Verify if the letter was already guessed before
    if guess in guessed_letter:
        print(f"You already guessed the letter '{guess}'! Try a different one.")
        print("-" * 30)
        continue

    guessed_letter.append(guess)

    # STEP 5: Validate guess - If the letter is not in the secret name, decrement attempts and display feedback
    if guess not in secret_name:
        count -= 1
        print("Wrong guess, try again!")
        print(f"Your remaining attempts are: {count}")
        print("-" * 30)

# ==================== GAME RESULT ====================
# Display game result: Show loss message if player exhausted all attempts
if count == 0:
    print(f"💀 You lost, {player_name}! the name was: {secret_name}")