#!/usr/bin/env python3
"""
Password Validator Application
A Python application that validates passwords based on specific security requirements.

Requirements:
- Password must be exactly 16 characters long
- Must contain at least one uppercase letter (A-Z)
- Must contain at least one lowercase letter (a-z)
- Must contain at least one number (0-9)
- Must contain at least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?)

Author: Password Security Tool
Version: 1.0
"""

import re
import sys
from typing import Tuple


class PasswordValidator:
    """
    A class to handle password validation based on security policies.
    
    This class encapsulates all password validation logic and provides
    methods to check various password requirements.
    """
    
    def __init__(self):
        """
        Initialize the PasswordValidator with predefined security requirements.
        
        Sets up the required password length and defines what constitutes
        valid special characters for the password policy.
        """
        # Define the required password length (16 characters)
        self.required_length = 16
        
        # Define acceptable special characters for password validation
        self.special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Create regex patterns for each requirement type
        self.uppercase_pattern = re.compile(r'[A-Z]')      # Pattern to match uppercase letters
        self.lowercase_pattern = re.compile(r'[a-z]')      # Pattern to match lowercase letters
        self.number_pattern = re.compile(r'[0-9]')         # Pattern to match numbers
        self.special_pattern = re.compile(f'[{re.escape(self.special_characters)}]')  # Pattern for special chars
    
    def check_length(self, password: str) -> bool:
        """
        Check if the password meets the length requirement.
        
        Args:
            password (str): The password string to validate
            
        Returns:
            bool: True if password is exactly 16 characters, False otherwise
        """
        return len(password) == self.required_length
    
    def check_uppercase(self, password: str) -> bool:
        """
        Check if the password contains at least one uppercase letter.
        
        Args:
            password (str): The password string to validate
            
        Returns:
            bool: True if password contains uppercase letter, False otherwise
        """
        return bool(self.uppercase_pattern.search(password))
    
    def check_lowercase(self, password: str) -> bool:
        """
        Check if the password contains at least one lowercase letter.
        
        Args:
            password (str): The password string to validate
            
        Returns:
            bool: True if password contains lowercase letter, False otherwise
        """
        return bool(self.lowercase_pattern.search(password))
    
    def check_numbers(self, password: str) -> bool:
        """
        Check if the password contains at least one numeric digit.
        
        Args:
            password (str): The password string to validate
            
        Returns:
            bool: True if password contains a number, False otherwise
        """
        return bool(self.number_pattern.search(password))
    
    def check_special_characters(self, password: str) -> bool:
        """
        Check if the password contains at least one special character.
        
        Args:
            password (str): The password string to validate
            
        Returns:
            bool: True if password contains special character, False otherwise
        """
        return bool(self.special_pattern.search(password))
    
    def validate_password(self, password: str) -> Tuple[bool, list]:
        """
        Perform comprehensive password validation against all requirements.
        
        This method checks the password against all defined security requirements
        and returns both a boolean result and a list of specific failures.
        
        Args:
            password (str): The password string to validate
            
        Returns:
            Tuple[bool, list]: A tuple containing:
                - bool: True if password meets all requirements, False otherwise
                - list: List of specific requirement failures (empty if all pass)
        """
        # Initialize list to store any validation failures
        failures = []
        
        # Check each requirement and add failures to the list
        if not self.check_length(password):
            failures.append(f"Password must be exactly {self.required_length} characters long")
            
        if not self.check_uppercase(password):
            failures.append("Password must contain at least one uppercase letter (A-Z)")
            
        if not self.check_lowercase(password):
            failures.append("Password must contain at least one lowercase letter (a-z)")
            
        if not self.check_numbers(password):
            failures.append("Password must contain at least one number (0-9)")
            
        if not self.check_special_characters(password):
            failures.append(f"Password must contain at least one special character ({self.special_characters})")
        
        # Return True if no failures, False otherwise, along with the failure list
        return len(failures) == 0, failures
    
    def get_password_requirements(self) -> str:
        """
        Return a formatted string describing all password requirements.
        
        Returns:
            str: Formatted string listing all password policy requirements
        """
        requirements = f"""
Password Requirements:
━━━━━━━━━━━━━━━━━━━━━━
• Must be exactly {self.required_length} characters long
• Must contain at least one uppercase letter (A-Z)
• Must contain at least one lowercase letter (a-z)  
• Must contain at least one number (0-9)
• Must contain at least one special character: {self.special_characters}
━━━━━━━━━━━━━━━━━━━━━━
        """
        return requirements.strip()


def display_welcome_message():
    """
    Display a welcome message and application information to the user.
    
    This function provides an introduction to the password validator application
    and explains what the user can expect from the tool.
    """
    print("=" * 60)
    print("           PASSWORD VALIDATOR APPLICATION")
    print("=" * 60)
    print("Welcome to the Password Security Validator!")
    print("This application will help you create secure passwords")
    print("that meet enterprise security standards.")
    print("=" * 60)


def get_user_input() -> str:
    """
    Safely get password input from the user.
    
    This function prompts the user for password input and handles
    potential input errors gracefully.
    
    Returns:
        str: The password string entered by the user
    """
    try:
        # Prompt user for password input
        password = input("\nPlease enter your password: ").strip()
        return password
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except EOFError:
        # Handle EOF errors
        print("\n\nInput error occurred.")
        sys.exit(1)


def display_validation_result(is_valid: bool, failures: list):
    """
    Display the password validation results to the user.
    
    Args:
        is_valid (bool): Whether the password passed validation
        failures (list): List of specific validation failures
    """
    print("\n" + "=" * 50)
    print("           VALIDATION RESULTS")
    print("=" * 50)
    
    if is_valid:
        # Display success message for valid passwords
        print("✅ SUCCESS: Password meets all security requirements!")
        print("Your password is strong and secure.")
    else:
        # Display error message and specific failures for invalid passwords
        print("❌ ERROR: Password does not meet the policy")
        print("\nSpecific issues found:")
        print("-" * 30)
        for i, failure in enumerate(failures, 1):
            print(f"{i}. {failure}")
    
    print("=" * 50)


def main():
    """
    Main application function that orchestrates the password validation process.
    
    This function serves as the entry point for the application and coordinates
    all the different components including user input, validation, and output.
    """
    # Display welcome message to introduce the application
    display_welcome_message()
    
    # Create an instance of the password validator
    validator = PasswordValidator()
    
    # Display password requirements to the user
    print(validator.get_password_requirements())
    
    # Main application loop to handle multiple password attempts
    while True:
        try:
            # Get password input from user
            password = get_user_input()
            
            # Check if user wants to exit the application
            if password.lower() in ['exit', 'quit', 'q']:
                print("\nThank you for using Password Validator. Goodbye!")
                break
            
            # Validate the entered password
            is_valid, failures = validator.validate_password(password)
            
            # Display validation results
            display_validation_result(is_valid, failures)
            
            # Ask user if they want to try another password
            print("\nWould you like to validate another password?")
            continue_choice = input("Enter 'y' for yes, any other key to exit: ").strip().lower()
            
            if continue_choice != 'y':
                print("\nThank you for using Password Validator. Goodbye!")
                break
                
        except Exception as e:
            # Handle any unexpected errors gracefully
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again or contact support if the problem persists.")


# Application entry point
if __name__ == "__main__":
    """
    Entry point for the application when run as a script.
    
    This block ensures that the main() function is only called when
    the script is run directly, not when imported as a module.
    """
    main()