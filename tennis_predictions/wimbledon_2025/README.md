# 🎾 Wimbledon 2025 AI Predictions

Machine learning predictions for Wimbledon 2025 using the **actual tournament draw** and player data.

## 🚀 What This Does

Predicts match winners and tournament outcomes for **Wimbledon 2025** using:
- **Real draw data** (released June 27, 2025)
- **Gradient Boosting Classifier** trained on historical tennis data
- **Grass court performance metrics** and head-to-head records
- **Current player form** and rankings

## 🏆 Tournament Information

### **Key Details**
- **Dates**: June 30 - July 13, 2025
- **Defending Champion**: Carlos Alcaraz (going for 3rd straight title!)
- **Tournament Start**: **TOMORROW** (June 30, 2025)
- **Historic First**: Electronic line judges replacing human line judges

### **Top Storylines**
- 🔥 **Alcaraz** enters with 18-match winning streak
- ⚡ **Sinner vs Djokovic** potential semifinal (both in same half)
- 🇬🇧 **Jack Draper** as British #1 and 4th seed
- 🎯 **Djokovic** at lowest seeding (6th) since 2018, chasing 8th Wimbledon title

## 🎯 Predictions Output

### **First Round Match Predictions**
```
🏆 Wimbledon 2025 First Round Predictions 🏆

Jannik Sinner vs Luca Nardi
Predicted Winner: Jannik Sinner (85.2% confidence)

Carlos Alcaraz vs Fabio Fognini  
Predicted Winner: Carlos Alcaraz (91.7% confidence)

Novak Djokovic vs Alexandre Muller
Predicted Winner: Novak Djokovic (88.4% confidence)
```

### **Tournament Winner Probabilities**
```
🏆 Wimbledon 2025 Tournament Winner Predictions 🏆

Player           Seed    Tournament_Win_Probability
Carlos Alcaraz   2       0.284
Jannik Sinner    1       0.251  
Novak Djokovic   6       0.198
Alexander Zverev 3       0.087
```

## 🛠️ Setup & Installation

### **Requirements**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### **Run Predictions**
```bash
python wimbledon_2025_predictions.py
```

## 🧠 How It Works

### **Model Architecture**
- **Algorithm**: Gradient Boosting Classifier (100 estimators)
- **Features**: Ranking difference, age difference, grass court win %, recent form
- **Training Data**: Historical tennis match results and player statistics
- **Target**: Binary classification (Player 1 wins vs Player 2 wins)

### **Feature Engineering**
```python
# Key prediction factors
features = [
    "Ranking_Diff",      # ATP ranking difference
    "Age_Diff",          # Age difference 
    "Grass_Pct_Diff",    # Grass court win % difference
    "Form_Diff"          # Recent form difference (last 10 matches)
]
```

### **Data Sources**
- **ATP Rankings**: Current world rankings
- **Grass Court Records**: Historical performance on grass
- **Head-to-Head**: Career matchup records
- **Tournament Draw**: Official Wimbledon 2025 draw (June 27 release)

## 📊 Key Matchups to Watch

### **Seeded First Round Battles**
- **#1 Sinner vs Luca Nardi** 🇮🇹 Italian derby
- **#2 Alcaraz vs Fabio Fognini** 🎾 Defending champ vs crafty veteran  
- **#5 Fritz vs Giovanni Mpetshi Perricard** 💥 Power serving showdown
- **#6 Djokovic vs Alexandre Muller** 🏆 7-time champion begins quest

### **Potential Semifinals**
- **Sinner vs Djokovic** (Same half - could meet in SF)
- **Alcaraz vs Zverev** (Different halves)

## 🎯 Model Performance

### **Accuracy Metrics**
- **Cross-validation accuracy**: Displayed after training
- **Feature importance**: Shows which factors matter most
- **Confidence scores**: Probability estimates for each prediction

### **Historical Context**
- Trained on tennis match data patterns
- Accounts for surface specialization (grass court performance)
- Incorporates current form and momentum

## 📅 Tournament Schedule

### **Key Dates**
- **June 30**: First round begins
- **July 1**: First round continues  
- **July 12**: Women's final (Saturday)
- **July 13**: Men's final (Sunday) - **4:00 PM** start time

### **Draw Highlights**
- **128 players** in men's singles
- **32 seeded players**
- **7 rounds** to win the title
- **Best-of-5 sets** format

## 🔮 Prediction Insights

### **Favorites Analysis**
1. **Carlos Alcaraz** - Defending champion, incredible form
2. **Jannik Sinner** - World #1, but tough draw with Djokovic
3. **Novak Djokovic** - Experience and grass court mastery
4. **Alexander Zverev** - Consistent performer, good draw

### **Dark Horses**
- **Jack Draper** - Home crowd support, improving rapidly
- **Lorenzo Musetti** - Emerging talent, solid grass game
- **Ben Shelton** - Big serve advantage on grass

## 🤖 Technical Details

### **Model Configuration**
```python
model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1, 
    random_state=42
)
```

### **Data Processing**
- Handles missing data gracefully
- Normalizes features for fair comparison
- Creates realistic opponent matchups

### **Validation**
- 80/20 train-test split
- Cross-validation for model stability
- Feature importance analysis

## 🚀 Future Enhancements

### **Planned Improvements**
- [ ] **Live updates** during tournament
- [ ] **Betting odds integration** for market comparison
- [ ] **Weather data** incorporation
- [ ] **Injury status** tracking
- [ ] **Round-by-round updates** as tournament progresses

### **Advanced Features**
- [ ] **Neural network models** for deeper patterns
- [ ] **Ensemble methods** combining multiple algorithms
- [ ] **Real-time form tracking** during tournament
- [ ] **Historical matchup analysis** (specific opponent records)

## ⚠️ Disclaimer

This model is for **entertainment and educational purposes only**:
- Predictions based on historical data and statistical patterns
- Tennis outcomes can be unpredictable (injuries, form, conditions)
- **Do not use for gambling** - sports betting involves significant risk
- Past performance doesn't guarantee future results

## 🏆 Tournament History

### **Recent Wimbledon Champions**
- **2024**: Carlos Alcaraz (def. Novak Djokovic)
- **2023**: Carlos Alcaraz (def. Novak Djokovic) 
- **2022**: Novak Djokovic (def. Nick Kyrgios)
- **2021**: Novak Djokovic (def. Matteo Berrettini)

### **Most Wimbledon Titles (Open Era)**
- **Roger Federer**: 8 titles
- **Novak Djokovic**: 7 titles
- **Carlos Alcaraz**: 2 titles (and counting...)

## 📞 Questions & Feedback

Want to improve the predictions or add new features?

### **Easy Contributions**
- Update player statistics with more recent data
- Add women's tournament predictions
- Include doubles predictions

### **Technical Improvements**  
- Implement ensemble methods
- Add neural network models
- Create real-time update system

---

### 🎾 **Next Match**: Sinner vs Nardi - June 30, 2025
### 🏆 **Tournament Starts**: TOMORROW!

**May the best predictions win!** 🤖🏆

---

*Created with ❤️ for tennis and machine learning*
