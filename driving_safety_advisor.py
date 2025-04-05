import random
import re
import json
from datetime import datetime
import numpy as np
import requests
import speech_recognition as sr
import pyttsx3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

class AdvancedDrivingSafetyAdvisor:
    def __init__(self):
        # Initialize knowledge base
        self.knowledge_base = self._load_knowledge_base()
        self.user_profile = {
            'name': None,
            'location': None,
            'experience_level': None,
            'vehicle_type': None,
            'common_routes': None
        }
        
        # Initialize NLP components
        self.vectorizer = TfidfVectorizer()
        self._train_vectorizer()
        
        # Initialize voice components
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.voice_enabled = False
        
        # Conversation state
        self.conversation_state = {
            'current_topic': None,
            'awaiting_response': None,
            'last_question': None,
            'user_mood': 'neutral'
        }
        
        # Statistics
        self.stats = {
            'questions_answered': 0,
            'safety_tips_provided': 0,
            'voice_interactions': 0
        }
        
        # Weather API configuration
        self.weather_api_key = "YOUR_OPENWEATHER_API_KEY"  # Replace with actual key
        self.current_weather = None

    def _load_knowledge_base(self):
        """Load expanded driving safety knowledge base"""
        knowledge = {
            # ... [previous knowledge base content] ...
            "emergencies": {
                "breakdown": "If your vehicle breaks down, pull over safely, turn on hazards, and stay visible until help arrives.",
                "accident": "In an accident: 1) Check for injuries 2) Move to safety if possible 3) Exchange information 4) Document the scene.",
                "tire_blowout": "For a tire blowout: 1) Hold wheel firmly 2) Ease off accelerator 3) Steer straight 4) Brake gently when slowed.",
                "engine_fire": "If engine catches fire: 1) Pull over immediately 2) Turn off engine 3) Evacuate all passengers 4) Use extinguisher if safe."
            },
            "new_features": {
                "voice": "You can enable voice mode by saying 'enable voice' or disable with 'disable voice'.",
                "weather": "I can provide weather-specific advice if you share your location (city name)."
            }
        }
        return knowledge

    def enable_voice(self):
        """Enable voice interaction mode"""
        self.voice_enabled = True
        self.engine.say("Voice mode enabled. You can now speak to me.")
        self.engine.runAndWait()
        return "Voice mode enabled. You can now speak to me."

    def disable_voice(self):
        """Disable voice interaction mode"""
        self.voice_enabled = False
        return "Voice mode disabled. Text input only."

    def get_voice_input(self):
        """Capture voice input from user"""
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError:
            return "API unavailable"

    def speak_response(self, text):
        """Convert text response to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def get_current_weather(self, location):
        """Fetch current weather using OpenWeather API"""
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.weather_api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                self.current_weather = {
                    'temp': data['main']['temp'],
                    'conditions': data['weather'][0]['main'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed']
                }
                return f"Current weather in {location}: {self.current_weather['conditions']}, {self.current_weather['temp']}°C"
            else:
                return "Could not fetch weather data"
        except Exception as e:
            return f"Weather API error: {str(e)}"

    def get_weather_specific_advice(self):
        """Provide driving advice based on current weather"""
        if not self.current_weather:
            return "I don't have current weather data. Please share your location."
            
        conditions = self.current_weather['conditions'].lower()
        
        advice = {
            'rain': "When driving in rain: 1) Reduce speed 2) Increase following distance 3) Use headlights 4) Avoid sudden maneuvers.",
            'snow': "In snowy conditions: 1) Use winter tires 2) Accelerate/brake gently 3) Keep windshield clear 4) Carry emergency supplies.",
            'fog': "In fog: 1) Use low beams/fog lights 2) Reduce speed 3) Follow road markings 4) Keep windows defogged.",
            'extreme heat': "In hot weather: 1) Check tire pressure 2) Watch for overheating 3) Stay hydrated 4) Use sunshade when parked.",
            'high winds': "In windy conditions: 1) Firm grip on wheel 2) Watch for debris 3) Be extra cautious with high-profile vehicles."
        }
        
        for condition in advice:
            if condition in conditions:
                return advice[condition]
        
        return "Current weather conditions appear normal. Remember basic safety rules."

    def process_command(self, user_input):
        """Process special commands"""
        user_input = user_input.lower()
        
        if "enable voice" in user_input:
            return self.enable_voice()
        elif "disable voice" in user_input:
            return self.disable_voice()
        elif "my location is" in user_input:
            location = user_input.replace("my location is", "").strip()
            self.user_profile['location'] = location
            weather_report = self.get_current_weather(location)
            return f"{weather_report}. {self.get_weather_specific_advice()}"
        elif "weather advice" in user_input:
            if self.user_profile.get('location'):
                return self.get_weather_specific_advice()
            return "Please share your location first (e.g., 'My location is London')"
        
        return None

    def respond(self, user_input):
        """Main response handler with new features"""
        # Check for special commands first
        command_response = self.process_command(user_input)
        if command_response:
            return command_response
            
        # ... [rest of the response logic from previous version] ...
        
        # Add weather context to responses when available
        if self.current_weather and "weather" not in user_input.lower():
            response += f"\n\nWeather note: {self.get_weather_specific_advice()}"
        
        return response

def main():
    advisor = AdvancedDrivingSafetyAdvisor()
    print("🚗 Advanced Driving Safety Advisor")
    print("Type 'enable voice' for voice interaction or 'quit' to exit\n")
    
    while True:
        try:
            if advisor.voice_enabled:
                user_input = advisor.get_voice_input()
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    advisor.speak_response("Goodbye and safe driving!")
                    break
            else:
                user_input = input("You: ")
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("🚗 Advisor: Safe travels! Remember to drive safely.")
                    break
            
            response = advisor.respond(user_input)
            
            if advisor.voice_enabled:
                print(f"Advisor: {response}")
                advisor.speak_response(response)
                advisor.stats['voice_interactions'] += 1
            else:
                print(f"🚗 Advisor: {response}")
                
        except KeyboardInterrupt:
            print("\n🚗 Advisor: Session ended. Drive safely!")
            break
        except Exception as e:
            print(f"🚗 Advisor: Error occurred - {str(e)}")

if __name__ == "__main__":
    main()