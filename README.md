# 🌾 Harvest Helper — Smart Crop Recommendation System

Harvest Helper is a Machine Learning-based web application that recommends a suitable crop based on soil nutrient values and weather conditions. It also provides preliminary fertilizer guidance to help users understand their soil nutrient requirements.

## 🚀 Features

- **Crop Recommendation:** Predicts a suitable crop using a trained Random Forest classification model.
- **Weather Integration:** Retrieves current temperature, humidity, and rainfall data for a selected city.
- **Fertilizer Guidance:** Provides rule-based fertilizer suggestions with explanations and next steps.
- **Bilingual Interface:** Supports English and Telugu.
- **Input Validation:** Validates soil nutrient values and pH before making predictions.
- **Responsive UI:** Green-and-white interface designed for usability across screen sizes.

## 🛠️ Technologies Used

- Python
- Flask
- NumPy
- Scikit-learn
- HTML and CSS
- Requests
- OpenWeatherMap API

## 📥 Project Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd harvest-helper
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your GitHub repository URL.

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the weather API key

Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

Set the key in PowerShell:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY"
```

Use your own key locally. Never commit API keys or other secrets to GitHub.

### 5. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## 🧪 Model Information

- **Algorithm:** Random Forest Classifier
- **Training samples:** 2,200
- **Input features:** Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, soil pH, and rainfall
- **Output:** Predicted crop label

## ⚠️ Important Disclaimer

Crop predictions and fertilizer suggestions are preliminary estimates, not guarantees of crop yield or fertilizer requirements. Actual decisions should consider soil test results, crop variety, season, irrigation, and advice from local agricultural experts.

## 👨‍💻 Author

Developed as a Python and Machine Learning project to explore agricultural decision support using a web application.
