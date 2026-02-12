# ============================================================================
# HIGHER AND LOWER GAME - A Fun Celebrity Follower Guessing Game
# ============================================================================
# This is a guessing game where players compare Instagram follower counts
# of famous personalities and try to correctly guess who has more followers.
# ============================================================================

# IMPORTS
# ============================================================================
import random  # For randomly selecting celebrities from the database
from replit import clear  # For clearing the console screen between rounds
from art import logo, vs  # For ASCII art visual elements
from game_data import data  # Import the celebrity database


# FUNCTION DEFINITIONS
# ============================================================================

def get_random_account():
  """
  Retrieves a random celebrity account from the game database.
  
  Purpose: Ensures variety in gameplay by randomly selecting different
           celebrities each round instead of following a fixed sequence.
  
  Parameters: None  
  
  Returns: 
    dict - A dictionary containing celebrity information with keys:
           - "name": Celebrity's name
           - "follower_count": Number of Instagram followers (in millions)
           - "description": Celebrity's profession/description
           - "country": Country of origin  
  
  Example:
    account = get_random_account()
    # Returns: {'name': 'Cristiano Ronaldo', 'follower_count': 615, ...}
  """
  return random.choice(data)


def format_data(account):
  """
  Converts raw account data into a readable, formatted string.
  
  Purpose: Makes the game more user-friendly by presenting account
           information in a clear, conversational format.
  
  Parameters:
    account (dict) - Celebrity account data containing name, description,
                    and country information.
  
  Returns:
    str - Formatted string in the pattern: 
          "Name, a description, from Country"  
  
  Example Input:
    {'name': 'Cristiano Ronaldo', 'description': 'footballer', 
     'country': 'Portugal', 'follower_count': 615}
  
  Example Output:
    "Cristiano Ronaldo, a footballer, from Portugal"
  """
  # Extract individual fields from the account dictionary
  name = account["name"]
  description = account["description"]
  country = account["country"]
  
  # Format and return as a readable string
  # Note: follower_count is intentionally omitted to avoid spoiling the game
  return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
  """
  Validates the player's guess against the actual follower counts.
  
  Purpose: Determines if the player made the correct choice and provides
           the boolean result to update game state.
  
  Parameters:
    guess (str)         - Player's choice: either "a" or "b"
    a_followers (int)   - Follower count for person A (in millions)
    b_followers (int)   - Follower count for person B (in millions)
  
  Returns:
    bool - True if the guess was correct, False if incorrect  
  
  Logic:
    1. If person A has MORE followers and player guessed 'a' → Correct ✓
    2. If person B has MORE followers and player guessed 'b' → Correct ✓
    3. Otherwise → Incorrect ✗
  
  Example:
    check_answer("a", 615, 280)  # Returns True (A has more followers)
    check_answer("a", 280, 615)  # Returns False (B has more followers)
  """
  # Check if person A has more followers than person B
  if a_followers > b_followers:
    # If A has more followers, return True only if player guessed 'a'
    return guess == "a"
  else:
    # If B has more (or equal) followers, return True only if player guessed 'b'
    return guess == "b"


def game():
  """
  Main game function that runs the complete game loop.
  
  Purpose: Controls the entire game experience including:
           - Displaying the logo
           - Managing game rounds
           - Tracking player score
           - Handling user input
           - Determining game end conditions  
  
  Parameters: None  
  
  Returns: None (plays the game until player loses)
  
  Game Flow:
    1. Display the welcome logo
    2. Initialize game variables (score and continue flag)
    3. Get first two random celebrities
    4. LOOP until player guesses wrong:
       a. Ensure we never compare the same person twice
       b. Display both celebrities
       c. Get player's guess
       d. Check if the guess is correct
       e. Clear screen and show result
       f. If correct: increment score and continue
       g. If wrong: end game and show final score
  """
  
  # Display the game logo for visual appeal
  print(logo)
  
  # Initialize game variables
  score = 0  # Track the number of correct guesses
  game_should_continue = True  # Flag to control the main game loop  
  
  # Get initial two random celebrities for the first round
  account_a = get_random_account()
  account_b = get_random_account()

  # Main game loop - continues until player makes a wrong guess
  while game_should_continue:
    
    # Move person B to position A for the next round
    # (This creates continuity between rounds)
    account_a = account_b
    
    # Get a new person for position B
    account_b = get_random_account()

    # Ensure we never compare the same person twice in a row
    # Keep generating new B's until we get someone different from A
    while account_a == account_b:
      account_b = get_random_account()

    # Display the two celebrities to compare
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)  # Display the "VS" ASCII art
    print(f"Against B: {format_data(account_b)}.")
    
    # Get player's guess
    # .lower() converts to lowercase so 'A' and 'a' are treated the same
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Extract follower counts for validation
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    # Check if the player's guess is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen for the next round (improves visual presentation)
    clear()
    
    # Redisplay the logo for consistency
    print(logo)
    
    # Handle the result of the guess
    if is_correct:
      # Player guessed correctly
      score += 1  # Increase score by 1
      print(f"You're right! Current score: {score}.")
      # Loop continues to next round
    else:
      # Player guessed incorrectly - game over
      game_should_continue = False  # Exit the main game loop
      print(f"Sorry, that's wrong. Final score: {score}")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================
# Start the game when the script is run
game()