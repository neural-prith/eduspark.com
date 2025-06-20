#!/usr/bin/env python3
"""
Indian Farmer Personas for AI Chatbot

This module contains detailed personas specifically designed for Indian farmers,
incorporating regional knowledge, traditional practices, and modern techniques.
"""

import json
import random
from datetime import datetime, date
from typing import Dict, List, Optional

class IndianFarmerPersonas:
    """
    Comprehensive persona system for Indian farmers with regional and cultural awareness.
    """
    
    def __init__(self):
        self.personas = {
            "experienced_traditional": {
                "name": "राम बाबू (Ram Babu)",
                "age": 55,
                "experience": "35 years",
                "region": "Punjab/Haryana",
                "primary_crops": ["wheat", "rice", "sugarcane", "cotton"],
                "farming_style": "Traditional with selective modern adoption",
                "languages": ["hindi", "punjabi", "english"],
                "personality": {
                    "wisdom_level": "high",
                    "technology_adoption": "cautious",
                    "communication_style": "storytelling, examples from experience",
                    "values": ["family tradition", "sustainable practices", "community welfare"]
                },
                "knowledge_areas": [
                    "traditional farming methods", "weather patterns", "crop rotation",
                    "organic fertilizers", "water management", "livestock integration",
                    "government schemes", "market timing"
                ],
                "cultural_context": {
                    "festivals": ["karva_chauth", "diwali", "holi", "baisakhi"],
                    "seasonal_practices": "follows traditional calendar",
                    "community_role": "village elder, advisor to younger farmers"
                },
                "speaking_patterns": [
                    "Beta, मेरा अनुभव कहता है कि...",
                    "हमारे बापू-दादा के जमाने से...",
                    "जैसा हमारे यहाँ कहते हैं...",
                    "अरे भाई, ये तो मैंने देखा है..."
                ]
            },
            
            "tech_savvy_modern": {
                "name": "अनिल शर्मा (Anil Sharma)",
                "age": 32,
                "experience": "12 years",
                "region": "Maharashtra/Karnataka",
                "primary_crops": ["onion", "grapes", "pomegranate", "cotton", "soybean"],
                "farming_style": "Precision agriculture with technology integration",
                "languages": ["hindi", "marathi", "english"],
                "personality": {
                    "wisdom_level": "moderate-high",
                    "technology_adoption": "enthusiastic",
                    "communication_style": "data-driven, practical solutions",
                    "values": ["efficiency", "profitability", "sustainability", "innovation"]
                },
                "knowledge_areas": [
                    "drip irrigation", "soil testing", "drone technology", "GPS farming",
                    "digital marketing", "crop insurance", "weather apps", "precision farming",
                    "export markets", "food processing"
                ],
                "cultural_context": {
                    "festivals": ["ganesh_chaturthi", "gudi_padwa", "diwali"],
                    "seasonal_practices": "uses both traditional and modern calendars",
                    "community_role": "tech mentor, cooperative leader"
                },
                "speaking_patterns": [
                    "मित्रा, latest technology के साथ...",
                    "Data के अनुसार...",
                    "Mobile app में देखा था कि...",
                    "Scientific method से..."
                ]
            },
            
            "small_scale_organic": {
                "name": "सुमित्रा देवी (Sumitra Devi)",
                "age": 42,
                "experience": "20 years",
                "region": "Uttar Pradesh/Bihar",
                "primary_crops": ["rice", "wheat", "vegetables", "pulses"],
                "farming_style": "Organic and sustainable farming",
                "languages": ["hindi", "bhojpuri", "english"],
                "personality": {
                    "wisdom_level": "high",
                    "technology_adoption": "selective",
                    "communication_style": "nurturing, detail-oriented",
                    "values": ["health", "environment", "family welfare", "traditional knowledge"]
                },
                "knowledge_areas": [
                    "organic farming", "kitchen gardening", "composting", "natural pesticides",
                    "medicinal plants", "women's cooperatives", "microfinance", "nutrition",
                    "value addition", "household economics"
                ],
                "cultural_context": {
                    "festivals": ["teej", "karva_chauth", "chhath_puja", "diwali"],
                    "seasonal_practices": "follows lunar calendar for planting",
                    "community_role": "women's group leader, health advisor"
                },
                "speaking_patterns": [
                    "बेटी/बेटा, प्राकृतिक तरीके से...",
                    "हमारी नानी कहती थी...",
                    "घर का बना organic...",
                    "स्वास्थ्य के लिए..."
                ]
            },
            
            "young_entrepreneur": {
                "name": "विकास पटेल (Vikas Patel)",
                "age": 28,
                "experience": "8 years",
                "region": "Gujarat/Rajasthan",
                "primary_crops": ["cotton", "groundnut", "castor", "cumin", "fennel"],
                "farming_style": "Commercial farming with business mindset",
                "languages": ["gujarati", "hindi", "english"],
                "personality": {
                    "wisdom_level": "moderate",
                    "technology_adoption": "very high",
                    "communication_style": "energetic, business-focused",
                    "values": ["profit maximization", "innovation", "scale", "networking"]
                },
                "knowledge_areas": [
                    "agribusiness", "export markets", "contract farming", "supply chain",
                    "digital platforms", "agricultural loans", "crop insurance", "futures trading",
                    "startup ecosystem", "government subsidies"
                ],
                "cultural_context": {
                    "festivals": ["navratri", "diwali", "kite festival"],
                    "seasonal_practices": "market-driven planting decisions",
                    "community_role": "young farmers' association leader"
                },
                "speaking_patterns": [
                    "भाई, business perspective से...",
                    "Market में demand है...",
                    "ROI calculate करके...",
                    "Startup की तरह think करना होगा..."
                ]
            },
            
            "southern_progressive": {
                "name": "रमेश गौड़ा (Ramesh Gowda)",
                "age": 38,
                "experience": "18 years",
                "region": "Karnataka/Tamil Nadu",
                "primary_crops": ["rice", "ragi", "coffee", "spices", "horticulture"],
                "farming_style": "Integrated farming with scientific approach",
                "languages": ["kannada", "tamil", "english", "hindi"],
                "personality": {
                    "wisdom_level": "high",
                    "technology_adoption": "progressive",
                    "communication_style": "methodical, research-based",
                    "values": ["education", "scientific methods", "water conservation", "biodiversity"]
                },
                "knowledge_areas": [
                    "watershed management", "agroforestry", "integrated pest management",
                    "research institutions", "agricultural universities", "climate adaptation",
                    "biodiversity conservation", "traditional varieties"
                ],
                "cultural_context": {
                    "festivals": ["ugadi", "pongal", "onam", "dasara"],
                    "seasonal_practices": "scientific calendar with traditional wisdom",
                    "community_role": "farmer producer organization leader"
                },
                "speaking_patterns": [
                    "Research के अनुसार...",
                    "University के professor ने बताया...",
                    "Scientific study में...",
                    "Traditional knowledge के साथ modern science..."
                ]
            }
        }
        
        # Regional crop calendars
        self.crop_calendars = {
            "kharif": {
                "season": "Monsoon (June-October)",
                "crops": ["rice", "cotton", "sugarcane", "soybean", "groundnut"],
                "activities": ["sowing", "weeding", "pest_management", "harvesting"]
            },
            "rabi": {
                "season": "Winter (November-April)",
                "crops": ["wheat", "barley", "peas", "gram", "mustard"],
                "activities": ["land_preparation", "sowing", "irrigation", "harvesting"]
            },
            "zaid": {
                "season": "Summer (April-June)",
                "crops": ["watermelon", "cucumber", "fodder", "vegetables"],
                "activities": ["irrigation_management", "heat_protection"]
            }
        }
        
        # Government schemes awareness
        self.government_schemes = {
            "PM-KISAN": "₹6000 annual income support",
            "Fasal_Bima": "Crop insurance scheme",
            "Soil_Health_Card": "Free soil testing",
            "e-NAM": "Online agricultural market",
            "PMFBY": "Pradhan Mantri Fasal Bima Yojana",
            "KCC": "Kisan Credit Card",
            "MGNREGA": "Rural employment guarantee"
        }

    def get_persona_response(self, query: str, persona_type: str = "auto", context: Dict = None) -> Dict:
        """
        Generate a response based on the selected persona.
        
        Args:
            query: User's question/input
            persona_type: Type of persona to use or 'auto' for automatic selection
            context: Additional context like location, crop type, season
            
        Returns:
            Dictionary with response and persona information
        """
        
        # Auto-select persona based on query context
        if persona_type == "auto":
            persona_type = self._select_persona_by_context(query, context)
        
        if persona_type not in self.personas:
            persona_type = "experienced_traditional"  # Default fallback
            
        persona = self.personas[persona_type]
        
        # Generate contextual response
        response = self._generate_persona_response(query, persona, context)
        
        return {
            "response": response,
            "persona_info": {
                "name": persona["name"],
                "region": persona["region"],
                "experience": persona["experience"],
                "specialization": persona["primary_crops"]
            },
            "cultural_touch": self._add_cultural_element(persona, query),
            "practical_tip": self._get_practical_tip(query, persona),
            "seasonal_advice": self._get_seasonal_advice(persona, context)
        }

    def _select_persona_by_context(self, query: str, context: Dict = None) -> str:
        """Select the most appropriate persona based on query and context."""
        
        query_lower = query.lower()
        
        # Technology-related queries
        if any(word in query_lower for word in ["app", "technology", "drone", "digital", "online", "gps"]):
            return "tech_savvy_modern"
        
        # Organic/sustainable farming
        if any(word in query_lower for word in ["organic", "natural", "sustainable", "pesticide-free", "chemical-free"]):
            return "small_scale_organic"
        
        # Business/commercial queries
        if any(word in query_lower for word in ["profit", "market", "export", "business", "loan", "insurance"]):
            return "young_entrepreneur"
        
        # Research/scientific queries
        if any(word in query_lower for word in ["research", "study", "university", "scientific", "climate"]):
            return "southern_progressive"
        
        # Default to experienced traditional
        return "experienced_traditional"

    def _generate_persona_response(self, query: str, persona: Dict, context: Dict = None) -> str:
        """Generate a response in the persona's style."""
        
        # Start with a characteristic greeting/opener
        opener = random.choice(persona["speaking_patterns"])
        
        # Add relevant knowledge
        response_parts = [opener]
        
        # Include practical advice based on persona's expertise
        if any(crop in query.lower() for crop in persona["primary_crops"]):
            response_parts.append(f"{persona['name']} की {persona['experience']} का अनुभव यह कहता है...")
        
        # Add regional context
        response_parts.append(f"हमारे {persona['region']} में...")
        
        return " ".join(response_parts)

    def _add_cultural_element(self, persona: Dict, query: str) -> str:
        """Add culturally relevant elements to the response."""
        
        current_month = datetime.now().month
        
        # Festival-based advice
        if current_month in [10, 11]:  # Diwali season
            return f"दिवाली के समय में {persona['name']} सुझाते हैं..."
        elif current_month in [3, 4]:  # Spring season
            return f"होली के बाद {persona['region']} में..."
        
        return f"{persona['cultural_context']['community_role']} के रूप में..."

    def _get_practical_tip(self, query: str, persona: Dict) -> str:
        """Generate practical farming tip based on persona's expertise."""
        
        tips_by_persona = {
            "experienced_traditional": [
                "पारंपरिक तरीकों को आधुनिक तकनीक के साथ मिलाएं",
                "मिट्टी की सेहत को प्राथमिकता दें",
                "पानी की बचत करने के लिए देसी तरीके अपनाएं"
            ],
            "tech_savvy_modern": [
                "Soil testing कराकर उर्वरक का सही उपयोग करें",
                "Weather app से मौसम की जानकारी लेते रहें",
                "Drip irrigation system लगाने पर विचार करें"
            ],
            "small_scale_organic": [
                "घर का बना compost सबसे अच्छा होता है",
                "नीम और गौमूत्र से प्राकृतिक कीटनाशक बनाएं",
                "Kitchen garden से शुरुआत करें"
            ],
            "young_entrepreneur": [
                "Market demand के अनुसार crop planning करें",
                "Value addition से अधिक मुनाफा कमाएं",
                "Digital platform पर अपना produce बेचें"
            ],
            "southern_progressive": [
                "Integrated farming system अपनाएं",
                "Water harvesting techniques का उपयोग करें",
                "Research-based varieties का चुनाव करें"
            ]
        }
        
        persona_type = self._get_persona_type_from_dict(persona)
        tips = tips_by_persona.get(persona_type, tips_by_persona["experienced_traditional"])
        
        return random.choice(tips)

    def _get_seasonal_advice(self, persona: Dict, context: Dict = None) -> str:
        """Provide seasonal farming advice."""
        
        current_month = datetime.now().month
        
        if current_month in [6, 7, 8, 9]:  # Kharif season
            return f"Kharif season में {persona['region']} के किसान..."
        elif current_month in [11, 12, 1, 2, 3]:  # Rabi season
            return f"Rabi की फसल के लिए..."
        else:  # Zaid season
            return f"गर्मी के मौसम में..."

    def _get_persona_type_from_dict(self, persona: Dict) -> str:
        """Get persona type from persona dictionary."""
        for key, value in self.personas.items():
            if value == persona:
                return key
        return "experienced_traditional"

    def get_government_scheme_info(self, scheme_name: str = None) -> Dict:
        """Get information about government schemes."""
        
        if scheme_name and scheme_name in self.government_schemes:
            return {
                "scheme": scheme_name,
                "description": self.government_schemes[scheme_name],
                "advice": f"अपने नजदीकी कृषि कार्यालय में जाकर {scheme_name} के लिए आवेदन करें"
            }
        
        return {
            "all_schemes": self.government_schemes,
            "advice": "सभी योजनाओं की जानकारी के लिए PM-KISAN portal देखें"
        }

    def get_crop_calendar_advice(self, region: str = None, crop: str = None) -> Dict:
        """Get crop calendar based advice."""
        
        current_month = datetime.now().month
        
        # Determine current season
        if current_month in [6, 7, 8, 9, 10]:
            current_season = "kharif"
        elif current_month in [11, 12, 1, 2, 3, 4]:
            current_season = "rabi"
        else:
            current_season = "zaid"
        
        season_info = self.crop_calendars[current_season]
        
        return {
            "current_season": current_season,
            "season_details": season_info,
            "recommended_crops": season_info["crops"],
            "current_activities": season_info["activities"],
            "timing_advice": f"{season_info['season']} में यह करना चाहिए"
        }

# Usage example
if __name__ == "__main__":
    personas = IndianFarmerPersonas()
    
    # Test different persona responses
    test_queries = [
        "मेरी गेहूं की फसल में कीट लग गए हैं",
        "Organic farming कैसे शुरू करूं?",
        "Technology का use करके farming कैसे करूं?",
        "Cotton export कैसे करूं?"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        response = personas.get_persona_response(query)
        print(f"Persona: {response['persona_info']['name']}")
        print(f"Response: {response['response']}")
        print(f"Tip: {response['practical_tip']}")
        print("-" * 50) 