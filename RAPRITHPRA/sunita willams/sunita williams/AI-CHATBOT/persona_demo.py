#!/usr/bin/env python3
"""
Indian Farmer Persona Demo

This script demonstrates the persona system for Indian farmers.
"""

import os
import sys
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Load environment variables
load_dotenv()

# Initialize colorama
init()

# Import the farmer personas
from farmer_personas import IndianFarmerPersonas

def demo_personas():
    """Demonstrate different farmer personas with sample queries."""
    
    print(f"{Fore.CYAN}🧑‍🌾 Indian Farmer Persona System Demo{Style.RESET_ALL}")
    print("=" * 50)
    
    personas = IndianFarmerPersonas()
    
    # Sample farming queries in Hindi and English mix (typical Indian farmer communication)
    sample_queries = [
        "मेरी गेहूं की फसल में कीट लग गए हैं, क्या करूं?",  # Wheat pest problem
        "Organic farming कैसे शुरू करूं? Traditional methods के साथ",  # Organic farming
        "Drip irrigation system लगवाना है, cost कितना आएगा?",  # Technology query
        "Cotton export करने के लिए क्या documents चाहिए?",  # Business query
        "Climate change का farming पर क्या effect होगा?",  # Research query
        "PM-KISAN scheme के लिए कैसे apply करूं?",  # Government scheme
        "Monsoon delay हो रहा है, kya karna chahiye?",  # Weather concern
        "Soil testing कहाँ कराऊं और कितना cost आएगा?"  # Soil health
    ]
    
    # Demo different personas responding to queries
    for i, query in enumerate(sample_queries, 1):
        print(f"\n{Fore.YELLOW}Sample Query {i}:{Style.RESET_ALL} {query}")
        print("-" * 60)
        
        # Get auto-selected persona response
        response = personas.get_persona_response(query, "auto")
        
        print(f"{Fore.GREEN}Persona Selected:{Style.RESET_ALL} {response['persona_info']['name']}")
        print(f"{Fore.CYAN}Region:{Style.RESET_ALL} {response['persona_info']['region']}")
        print(f"{Fore.CYAN}Experience:{Style.RESET_ALL} {response['persona_info']['experience']}")
        print(f"{Fore.CYAN}Specialization:{Style.RESET_ALL} {', '.join(response['persona_info']['specialization'][:2])}")
        
        if response.get('practical_tip'):
            print(f"\n{Fore.MAGENTA}💡 Practical Tip:{Style.RESET_ALL} {response['practical_tip']}")
        
        if response.get('cultural_touch'):
            print(f"{Fore.MAGENTA}🕉️ Cultural Context:{Style.RESET_ALL} {response['cultural_touch']}")
        
        if response.get('seasonal_advice'):
            print(f"{Fore.MAGENTA}🌾 Seasonal Advice:{Style.RESET_ALL} {response['seasonal_advice']}")
        
        print("=" * 60)

def demo_government_schemes():
    """Demo government schemes information."""
    
    print(f"\n{Fore.CYAN}📋 Government Schemes for Indian Farmers{Style.RESET_ALL}")
    print("=" * 50)
    
    personas = IndianFarmerPersonas()
    
    # Show all schemes
    schemes_info = personas.get_government_scheme_info()
    
    print(f"{Fore.YELLOW}Available Schemes:{Style.RESET_ALL}")
    for scheme, description in schemes_info['all_schemes'].items():
        print(f"• {Fore.GREEN}{scheme}:{Style.RESET_ALL} {description}")
    
    print(f"\n{Fore.CYAN}General Advice:{Style.RESET_ALL} {schemes_info['advice']}")

def demo_seasonal_calendar():
    """Demo seasonal farming calendar."""
    
    print(f"\n{Fore.CYAN}🌾 Indian Crop Calendar{Style.RESET_ALL}")
    print("=" * 30)
    
    personas = IndianFarmerPersonas()
    
    # Get current seasonal advice
    seasonal_info = personas.get_crop_calendar_advice()
    
    print(f"Current Season: {Fore.YELLOW}{seasonal_info['current_season'].title()}{Style.RESET_ALL}")
    print(f"Duration: {seasonal_info['season_details']['season']}")
    print(f"Recommended Crops: {', '.join(seasonal_info['recommended_crops'])}")
    print(f"Current Activities: {', '.join(seasonal_info['current_activities'])}")
    print(f"\n{Fore.GREEN}Timing Advice:{Style.RESET_ALL} {seasonal_info['timing_advice']}")

def demo_persona_characteristics():
    """Show characteristics of each persona."""
    
    print(f"\n{Fore.CYAN}👥 Detailed Persona Characteristics{Style.RESET_ALL}")
    print("=" * 45)
    
    personas = IndianFarmerPersonas()
    
    for persona_key, persona_data in personas.personas.items():
        print(f"\n{Fore.YELLOW}{persona_data['name']} ({persona_key}){Style.RESET_ALL}")
        print(f"Age: {persona_data['age']} | Experience: {persona_data['experience']}")
        print(f"Region: {persona_data['region']}")
        print(f"Primary Crops: {', '.join(persona_data['primary_crops'][:4])}")
        print(f"Farming Style: {persona_data['farming_style']}")
        print(f"Tech Adoption: {persona_data['personality']['technology_adoption']}")
        print(f"Communication: {persona_data['personality']['communication_style']}")
        print(f"Values: {', '.join(persona_data['personality']['values'][:3])}")
        print(f"Languages: {', '.join(persona_data['languages'])}")
        
        print(f"{Fore.MAGENTA}Sample Speech:{Style.RESET_ALL}")
        print(f"  \"{persona_data['speaking_patterns'][0]}\"")
        
        print(f"{Fore.MAGENTA}Knowledge Areas:{Style.RESET_ALL}")
        print(f"  {', '.join(persona_data['knowledge_areas'][:4])}")
        
        print("-" * 50)

def interactive_demo():
    """Interactive demo where user can test queries."""
    
    print(f"\n{Fore.CYAN}🎯 Interactive Persona Testing{Style.RESET_ALL}")
    print("=" * 35)
    print("Type your farming question in Hindi/English mix (like real Indian farmers)")
    print("Type 'exit' to quit, 'help' for sample questions")
    
    personas = IndianFarmerPersonas()
    
    while True:
        user_query = input(f"\n{Fore.GREEN}Your Question:{Style.RESET_ALL} ").strip()
        
        if user_query.lower() == 'exit':
            break
        elif user_query.lower() == 'help':
            print(f"\n{Fore.YELLOW}Sample Questions:{Style.RESET_ALL}")
            print("• मेरी धान की फसल में disease हो गई है")
            print("• Technology का use करके profit कैसे बढ़ाऊं?")
            print("• Organic pesticide कैसे बनाऊं घर पर?")
            print("• Cotton market में price कब बढ़ेगी?")
            print("• Water saving techniques कौन से हैं?")
            continue
        
        if not user_query:
            continue
        
        print(f"\n{Fore.CYAN}Processing your question...{Style.RESET_ALL}")
        response = personas.get_persona_response(user_query, "auto")
        
        print(f"\n{Fore.GREEN}Response from {response['persona_info']['name']}:{Style.RESET_ALL}")
        print(f"Region: {response['persona_info']['region']}")
        print(f"Specialization: {', '.join(response['persona_info']['specialization'][:2])}")
        
        # Simulate the enhanced response (since we're not using the full chatbot)
        print(f"\n{Fore.YELLOW}[This would be the AI-generated response based on the persona]{Style.RESET_ALL}")
        
        if response.get('practical_tip'):
            print(f"\n💡 {Fore.MAGENTA}Practical Tip:{Style.RESET_ALL} {response['practical_tip']}")
        
        print(f"\n{Fore.CYAN}Persona Context Applied:{Style.RESET_ALL}")
        print(f"• Cultural sensitivity for {response['persona_info']['region']}")
        print(f"• {response['persona_info']['experience']} farming experience")
        print(f"• Expertise in {', '.join(response['persona_info']['specialization'][:2])}")

if __name__ == "__main__":
    print(f"{Fore.CYAN}🇮🇳 Indian Farmer AI Persona System{Style.RESET_ALL}")
    print("Culturally-aware AI responses for Indian farming community")
    print()
    
    # Run all demos
    demo_personas()
    demo_government_schemes()
    demo_seasonal_calendar()
    demo_persona_characteristics()
    
    # Interactive demo
    try:
        interactive_demo()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.GREEN}Thank you for trying the Indian Farmer Persona System!{Style.RESET_ALL}")
        print("Now integrate this into your main chatbot for culturally-aware responses.") 