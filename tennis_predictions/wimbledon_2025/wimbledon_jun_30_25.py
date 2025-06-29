import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print("🎾 WIMBLEDON 2025 - TODAY'S PREDICTIONS (June 30, 2025) 🎾")
print("=" * 60)
print(f"⏰ Generated at: {datetime.now().strftime('%H:%M')} London Time")
print("🏆 Tournament Day 1 - First Round Matches")
print("=" * 60)

# TODAY'S KEY MATCHES - June 30, 2025
todays_matches = {
    # MEN'S SINGLES - Key matches today
    "men": [
        {
            "court": "Centre Court", 
            "time": "1:30 PM",
            "player1": "Carlos Alcaraz", 
            "player2": "Fabio Fognini",
            "p1_seed": 2, 
            "p2_seed": None,
            "p1_ranking": 2, 
            "p2_ranking": 65,
            "p1_age": 21, 
            "p2_age": 37,
            "p1_grass_pct": 0.75, 
            "p2_grass_pct": 0.45,
            "p1_form": 10, 
            "p2_form": 5,
            "match_type": "🌟 OPENING MATCH - Defending Champion!"
        },
        {
            "court": "No. 1 Court",
            "time": "1:30 PM", 
            "player1": "Alexander Zverev",
            "player2": "Arthur Rinderknech",
            "p1_seed": 3,
            "p2_seed": None,
            "p1_ranking": 3,
            "p2_ranking": 78,
            "p1_age": 27,
            "p2_age": 29,
            "p1_grass_pct": 0.40,
            "p2_grass_pct": 0.35,
            "p1_form": 7,
            "p2_form": 5,
            "match_type": "Third seed opener"
        },
        {
            "court": "Court 2",
            "time": "11:00 AM",
            "player1": "Jack Draper",
            "player2": "Sebastian Baez", 
            "p1_seed": 4,
            "p2_seed": None,
            "p1_ranking": 4,
            "p2_ranking": 45,
            "p1_age": 22,
            "p2_age": 23,
            "p1_grass_pct": 0.60,
            "p2_grass_pct": 0.25,
            "p1_form": 8,
            "p2_form": 6,
            "match_type": "🇬🇧 British No. 1"
        },
        {
            "court": "Court 3",
            "time": "11:00 AM",
            "player1": "Novak Djokovic",
            "player2": "Alexandre Muller",
            "p1_seed": 6,
            "p2_seed": None,
            "p1_ranking": 6,
            "p2_ranking": 85,
            "p1_age": 37,
            "p2_age": 27,
            "p1_grass_pct": 0.84,
            "p2_grass_pct": 0.30,
            "p1_form": 6,
            "p2_form": 4,
            "match_type": "🏆 7-time Champion"
        },
        {
            "court": "Court 14",
            "time": "11:00 AM",
            "player1": "Taylor Fritz",
            "player2": "Giovanni Mpetshi Perricard",
            "p1_seed": 5,
            "p2_seed": None,
            "p1_ranking": 5,
            "p2_ranking": 58,
            "p1_age": 26,
            "p2_age": 21,
            "p1_grass_pct": 0.38,
            "p2_grass_pct": 0.45,
            "p1_form": 6,
            "p2_form": 7,
            "match_type": "💥 Big Serving Battle"
        }
    ],
    
    # WOMEN'S SINGLES - Key matches today  
    "women": [
        {
            "court": "No. 1 Court",
            "time": "3:00 PM",
            "player1": "Aryna Sabalenka",
            "player2": "Carson Bristine",
            "p1_seed": 1,
            "p2_seed": None,
            "p1_ranking": 1,
            "p2_ranking": 120,
            "p1_age": 26,
            "p2_age": 20,
            "p1_grass_pct": 0.55,
            "p2_grass_pct": 0.40,
            "p1_form": 8,
            "p2_form": 6,
            "match_type": "🌟 World No. 1"
        },
        {
            "court": "Centre Court",
            "time": "3:30 PM",
            "player1": "Emma Raducanu",
            "player2": "Lucky Loser/Qualifier",
            "p1_seed": None,
            "p2_seed": None,
            "p1_ranking": 45,
            "p2_ranking": 95,
            "p1_age": 21,
            "p2_age": 25,
            "p1_grass_pct": 0.65,
            "p2_grass_pct": 0.35,
            "p1_form": 7,
            "p2_form": 5,
            "match_type": "🇬🇧 British No. 1 - Home Crowd Favorite"
        },
        {
            "court": "Court 1",
            "time": "4:30 PM",
            "player1": "Jasmine Paolini",
            "player2": "Sara Errani",
            "p1_seed": 4,
            "p2_seed": None,
            "p1_ranking": 4,
            "p2_ranking": 85,
            "p1_age": 28,
            "p2_age": 37,
            "p1_grass_pct": 0.50,
            "p2_grass_pct": 0.45,
            "p1_form": 8,
            "p2_form": 5,
            "match_type": "🇮🇹 Italian Derby"
        }
    ]
}

def predict_match(p1_name, p2_name, p1_ranking, p2_ranking, p1_age, p2_age, 
                 p1_grass_pct, p2_grass_pct, p1_form, p2_form):
    """Predict match outcome using simplified ML approach"""
    
    # Calculate feature differences
    ranking_diff = p2_ranking - p1_ranking  # Positive = Player 1 is better ranked
    age_diff = p1_age - p2_age
    grass_pct_diff = p1_grass_pct - p2_grass_pct
    form_diff = p1_form - p2_form
    
    # Simple weighted prediction (simulating trained model)
    # Higher positive score = Player 1 more likely to win
    prediction_score = (
        ranking_diff * 0.004 +      # Ranking weight
        grass_pct_diff * 0.6 +      # Grass experience weight  
        form_diff * 0.08 +          # Recent form weight
        age_diff * -0.01            # Age factor (slightly favor younger)
    )
    
    # Convert to probability (sigmoid-like function)
    player1_prob = 1 / (1 + np.exp(-prediction_score * 8))
    player2_prob = 1 - player1_prob
    
    # Determine winner
    winner = p1_name if player1_prob > 0.5 else p2_name
    confidence = max(player1_prob, player2_prob)
    
    return {
        "winner": winner,
        "confidence": confidence,
        "player1_prob": player1_prob,
        "player2_prob": player2_prob,
        "prediction_factors": {
            "ranking_advantage": "Player 1" if ranking_diff > 0 else "Player 2",
            "grass_advantage": "Player 1" if grass_pct_diff > 0 else "Player 2", 
            "form_advantage": "Player 1" if form_diff > 0 else "Player 2"
        }
    }

# Generate predictions for today's matches
print("\n🏆 MEN'S SINGLES PREDICTIONS - TODAY 🏆\n")

for i, match in enumerate(todays_matches["men"], 1):
    pred = predict_match(
        match["player1"], match["player2"],
        match["p1_ranking"], match["p2_ranking"],
        match["p1_age"], match["p2_age"],
        match["p1_grass_pct"], match["p2_grass_pct"],
        match["p1_form"], match["p2_form"]
    )
    
    print(f"Match {i}: {match['court']} - {match['time']}")
    print(f"🎾 {match['player1']} vs {match['player2']}")
    print(f"📝 {match['match_type']}")
    print(f"🏆 PREDICTED WINNER: {pred['winner']} ({pred['confidence']:.1%} confidence)")
    print(f"📊 Probability: {match['player1']} {pred['player1_prob']:.1%} | {match['player2']} {pred['player2_prob']:.1%}")
    
    # Show key advantages
    factors = pred['prediction_factors']
    print(f"🔍 Key Factors:")
    print(f"   • Ranking: {factors['ranking_advantage']}")
    print(f"   • Grass Court: {factors['grass_advantage']}")  
    print(f"   • Recent Form: {factors['form_advantage']}")
    print("-" * 50)

print("\n🏆 WOMEN'S SINGLES PREDICTIONS - TODAY 🏆\n")

for i, match in enumerate(todays_matches["women"], 1):
    pred = predict_match(
        match["player1"], match["player2"],
        match["p1_ranking"], match["p2_ranking"], 
        match["p1_age"], match["p2_age"],
        match["p1_grass_pct"], match["p2_grass_pct"],
        match["p1_form"], match["p2_form"]
    )
    
    print(f"Match {i}: {match['court']} - {match['time']}")
    print(f"🎾 {match['player1']} vs {match['player2']}")
    print(f"📝 {match['match_type']}")
    print(f"🏆 PREDICTED WINNER: {pred['winner']} ({pred['confidence']:.1%} confidence)")
    print(f"📊 Probability: {match['player1']} {pred['player1_prob']:.1%} | {match['player2']} {pred['player2_prob']:.1%}")
    print("-" * 50)

# Summary of key predictions
print("\n🎯 TODAY'S TOP PREDICTIONS SUMMARY 🎯\n")

key_predictions = [
    "🌟 ALCARAZ vs Fognini: Defending champion heavily favored",
    "🇬🇧 DRAPER vs Baez: British hope with grass court advantage", 
    "🏆 DJOKOVIC vs Muller: 7-time champion starts title quest",
    "💥 FRITZ vs Perricard: Upset potential - big servers battle",
    "🌟 SABALENKA vs Bristine: World No. 1 should dominate",
    "🇬🇧 RADUCANU: Home crowd will boost British No. 1"
]

for prediction in key_predictions:
    print(f"   {prediction}")

print(f"\n📺 WATCH LIVE:")
print(f"   • BBC iPlayer (UK)")
print(f"   • ESPN (US)")  
print(f"   • Streaming on official platforms")

print(f"\n⏰ KEY TIMES (London):")
print(f"   • 11:00 AM: Outside courts begin")
print(f"   • 1:30 PM: Centre Court & No. 1 Court")
print(f"   • 3:00 PM: Afternoon session")

print(f"\n🎾 MUST-WATCH MATCHES:")
print(f"   1. Alcaraz vs Fognini (Centre Court, 1:30 PM)")
print(f"   2. Djokovic vs Muller (Court 3, 11:00 AM)")  
print(f"   3. Draper vs Baez (Court 2, 11:00 AM)")

print(f"\n🔮 PREDICTION CONFIDENCE:")
print(f"   • High Confidence: Alcaraz, Sabalenka, Djokovic")
print(f"   • Medium Confidence: Draper, Zverev")
print(f"   • Potential Upsets: Fritz vs Perricard")

print(f"\n🏆 Enjoy Day 1 of Wimbledon 2025! 🏆")
print("=" * 60)