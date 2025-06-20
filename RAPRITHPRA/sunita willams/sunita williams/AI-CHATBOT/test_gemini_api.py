#!/usr/bin/env python3
"""
Gemini API Test Script

This script helps you test your Gemini API configuration and find working models.
Run this script before using your main application to verify everything is working.
"""

import os
import sys
import time
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Initialize colorama
init()

def test_gemini_api():
    """Test the Gemini API configuration and available models."""
    print(f"{Fore.CYAN}=== Gemini API Configuration Test ==={Style.RESET_ALL}\n")
    
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print(f"{Fore.RED}❌ GEMINI_API_KEY not found in environment variables{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}To fix this:{Style.RESET_ALL}")
        print("1. Create a .env file in your project directory")
        print("2. Add: GEMINI_API_KEY=your_api_key_here")
        print("3. Get a free API key from: https://ai.google.dev/gemini-api")
        return False
    
    print(f"{Fore.GREEN}✓ API key found{Style.RESET_ALL}")
    print(f"API key preview: {api_key[:8]}...{api_key[-4:]}")
    
    # Try to import the library
    try:
        import google.generativeai as genai
        print(f"{Fore.GREEN}✓ google-generativeai library imported successfully{Style.RESET_ALL}")
    except ImportError:
        print(f"{Fore.RED}❌ google-generativeai library not found{Style.RESET_ALL}")
        print("Install it with: pip install google-generativeai")
        return False
    
    # Configure the API
    try:
        genai.configure(api_key=api_key)
        print(f"{Fore.GREEN}✓ API configured successfully{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to configure API: {e}{Style.RESET_ALL}")
        return False
    
    # Test different models
    test_models = [
        "gemini-2.0-flash-lite",
        "gemini-2.0-flash", 
        "gemini-1.5-flash",
        "gemini-1.5-flash-8b",
        "gemini-pro"
    ]
    
    print(f"\n{Fore.CYAN}Testing available models...{Style.RESET_ALL}")
    
    working_models = []
    
    for model_name in test_models:
        print(f"\n🧪 Testing model: {model_name}")
        
        try:
            # Create model
            model = genai.GenerativeModel(
                model_name=model_name,
                generation_config={
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "top_k": 32,
                    "max_output_tokens": 100,
                    "candidate_count": 1,
                }
            )
            
            # Test with a simple prompt
            start_time = time.time()
            response = model.generate_content("Say 'Hello, I am working!' in a friendly way.")
            end_time = time.time()
            
            if response and response.text:
                response_time = end_time - start_time
                print(f"{Fore.GREEN}✓ {model_name}: Working!{Style.RESET_ALL}")
                print(f"  Response time: {response_time:.2f}s")
                print(f"  Response: {response.text[:100]}...")
                working_models.append(model_name)
            else:
                print(f"{Fore.YELLOW}⚠ {model_name}: Empty response{Style.RESET_ALL}")
                
        except Exception as e:
            error_str = str(e).lower()
            if "quota" in error_str or "429" in error_str:
                print(f"{Fore.RED}❌ {model_name}: Quota exceeded{Style.RESET_ALL}")
                print(f"  Try again in a few minutes or get a new API key")
            elif "not found" in error_str or "model" in error_str:
                print(f"{Fore.YELLOW}⚠ {model_name}: Not available{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ {model_name}: {str(e)[:100]}{Style.RESET_ALL}")
    
    # Summary
    print(f"\n{Fore.CYAN}=== Test Results ==={Style.RESET_ALL}")
    
    if working_models:
        print(f"{Fore.GREEN}✓ Working models found: {len(working_models)}{Style.RESET_ALL}")
        for model in working_models:
            print(f"  • {model}")
        
        print(f"\n{Fore.GREEN}Recommended model for your app: {working_models[0]}{Style.RESET_ALL}")
        
        # Rate limit information
        print(f"\n{Fore.CYAN}Free Tier Limits:{Style.RESET_ALL}")
        print("• 15 requests per minute")
        print("• 1,500 requests per day") 
        print("• 1 million tokens per day")
        
        return True
    else:
        print(f"{Fore.RED}❌ No working models found{Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}Troubleshooting steps:{Style.RESET_ALL}")
        print("1. Check if your API key is valid")
        print("2. Wait a few minutes if you hit rate limits")
        print("3. Get a new API key from: https://ai.google.dev/gemini-api")
        print("4. Ensure you have internet connectivity")
        
        return False

def test_rate_limits():
    """Test rate limiting functionality."""
    print(f"\n{Fore.CYAN}=== Rate Limit Test ==={Style.RESET_ALL}")
    
    # This would test multiple rapid requests
    # (commented out to avoid hitting limits during testing)
    print("Rate limiting test skipped (to avoid quota usage)")
    print("The app includes built-in rate limiting for production use")

if __name__ == "__main__":
    print(f"{Fore.CYAN}Gemini API Test Tool{Style.RESET_ALL}")
    print("This tool helps verify your Gemini API setup\n")
    
    if test_gemini_api():
        print(f"\n{Fore.GREEN}🎉 Your Gemini API is configured correctly!{Style.RESET_ALL}")
        print("You can now run your main application.")
    else:
        print(f"\n{Fore.RED}💥 API configuration issues found{Style.RESET_ALL}")
        print("Please fix the issues above before running your application.")
        sys.exit(1) 