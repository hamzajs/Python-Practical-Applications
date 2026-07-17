# ==================== EMAIL VALIDATOR PROGRAM ====================
# This program validates email addresses using regular expressions (regex)
# Supported email domains: gmail, yahoo, hotmail, outlook
# Supported extensions: .com, .edu

# ==================== IMPORTS ====================
# Import the 're' module for regular expression pattern matching
import re 

# ==================== EMAIL VALIDATION FUNCTION ====================
# Function to validate email format using regex pattern
# Pattern breakdown:
#   ^[\w.-]+         - Start: One or more word characters, dots, or hyphens
#   @                - Literal @ symbol required
#   (gmail|yahoo|hotmail|outlook) - Domain must be one of these providers
#   \.               - Literal dot before extension
#   (com|edu)        - Extension must be either .com or .edu
#   $                - End of string (no characters after extension)
def checkEmail(email):
    # Apply regex pattern to validate the email format
    search = re.search(r"^[\w.-]+@(gmail|yahoo|hotmail|outlook)\.(com|edu)$", email)
    # Return True if pattern matches, False otherwise
    return bool(search)

# ==================== MAIN PROGRAM FUNCTION ====================
# Main function that controls the interactive email validation loop
def main():
    # ==================== MAIN VALIDATION LOOP ====================
    # Continuously prompt user for email addresses until they quit
    while True:
        # STEP 1: Get user input - Request email address (type 'q' to quit)
        email = input("Enter to check is email or not(q for quit): ").strip()

        # STEP 2: Check exit condition - Break loop if user enters 'q'
        if email == 'q':
            break
        
        # STEP 3: Validate email - Call validation function
        is_email = checkEmail(email)
        
        # STEP 4: Display result - Show validation outcome
        if is_email:
            print("This is Email")
        else:
            print("This is not Email")

# ==================== ENTRY POINT ====================
# Execute the main function only when script runs directly (not when imported)
if __name__ == "__main__":
    main()