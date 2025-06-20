#!/usr/bin/env python3
"""
Environment Setup Script

This script helps you set up your .env file with the correct API keys.
"""

import os
from colorama import Fore, Style, init

# Initialize colorama
init()

def create_env_file():
    """Create or update the .env file with the API keys."""
    
    # Your new API key
    new_api_key = "AIzaSyAVa1ozh8qoKxvlLkIyDrgs_UGNSoStddE"
    
    env_content = f"""# Environment Variables for AI Chatbot
# =============================================================================
# GEMINI API KEY (Required for AI features)
# =============================================================================
GEMINI_API_KEY={new_api_key}

# =============================================================================
# YOUTUBE API KEY (Optional - for educational video recommendations)
# =============================================================================
# Get from: https://developers.google.com/youtube/v3/getting-started
YOUTUBE_API_KEY=

# =============================================================================
# FLASK SETTINGS
# =============================================================================
FLASK_ENV=development
FLASK_DEBUG=True

# =============================================================================
# DATABASE SETTINGS
# =============================================================================
DATABASE_URL=sqlite:///app.db

# =============================================================================
# USAGE NOTES
# =============================================================================
# 1. This file contains your API keys - keep it secure
# 2. Never commit this file to version control
# 3. Restart your application after updating this file
"""

    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print(f"{Fore.GREEN}✓ Successfully created .env file with your API key!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}API Key: {new_api_key[:8]}...{new_api_key[-4:]}{Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}Next steps:{Style.RESET_ALL}")
        print("1. Run: python test_gemini_api.py (to test your setup)")
        print("2. Run: python iti_app.py (to start your application)")
        
        return True
        
    except Exception as e:
        print(f"{Fore.RED}❌ Error creating .env file: {e}{Style.RESET_ALL}")
        return False

def show_manual_setup():
    """Show manual setup instructions."""
    print(f"\n{Fore.CYAN}Manual Setup Instructions:{Style.RESET_ALL}")
    print("If the automatic setup doesn't work, create a file named '.env' manually:")
    print()
    print(f"{Fore.YELLOW}1. Create a new file named '.env' in this directory{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}2. Add the following content:{Style.RESET_ALL}")
    print()
    print("GEMINI_API_KEY=AIzaSyAVa1ozh8qoKxvlLkIyDrgs_UGNSoStddE")
    print("YOUTUBE_API_KEY=")
    print("FLASK_ENV=development")
    print("FLASK_DEBUG=True")
    print("DATABASE_URL=sqlite:///app.db")
    print()

if __name__ == "__main__":
    print(f"{Fore.CYAN}🚀 AI Chatbot Environment Setup{Style.RESET_ALL}")
    print("Setting up your environment with the new API key...\n")
    
    if create_env_file():
        print(f"\n{Fore.GREEN}🎉 Setup complete!{Style.RESET_ALL}")
    else:
        show_manual_setup() 