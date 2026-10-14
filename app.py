
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from weather import get_weather
from fertilizer import fertilizer_recommendation

app = Flask(__name__)

from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

print("Random Forest model loaded successfully!")
print("Expected features:", model.n_features_in_)


# Telugu names for common crop labels
CROP_TE = {
    "rice": "వరి",
    "maize": "మొక్కజొన్న",
    "chickpea": "శనగ",
    "kidneybeans": "రాజ్మా",
    "pigeonpeas": "కందులు",
    "mothbeans": "మాత్ బీన్స్",
    "mungbean": "పెసలు",
    "blackgram": "మినుములు",
    "lentil": "మసూర్ పప్పు",
    "pomegranate": "దానిమ్మ",
    "banana": "అరటి",
    "mango": "మామిడి",
    "grapes": "ద్రాక్ష",
    "watermelon": "పుచ్చకాయ",
    "muskmelon": "ఖర్బూజా",
    "apple": "ఆపిల్",
    "orange": "నారింజ",
    "papaya": "బొప్పాయి",
    "coconut": "కొబ్బరి",
    "cotton": "పత్తి",
    "jute": "జనపనార",
    "coffee": "కాఫీ"
}


def make_explanation(lang, crop, N, P, K, ph,
                     temp, humidity, rainfall, fertilizer):
    crop_te = CROP_TE.get(str(crop).lower(), str(crop))

    if lang == "te":
        return (
            f"మీరు ఇచ్చిన నేల వివరాలు: నైట్రోజన్ {N}, "
            f"ఫాస్ఫరస్ {P}, పొటాషియం {K}, pH {ph}. "
            f"మీరు ఎంచుకున్న నగరానికి సంబంధించిన వాతావరణ సమాచారం "
            f"ప్రకారం ఉష్ణోగ్రత {temp:.1f}°C, తేమ {humidity}%, "
            f"వర్షపాతం {rainfall} మి.మీ.గా నమోదైంది. "
            f"ఈ ఏడు వివరాలను శిక్షణ పొందిన మెషిన్ లెర్నింగ్ మోడల్‌కు "
            f"ఇచ్చినప్పుడు అది '{crop_te}' ({crop}) పంటను అంచనా వేసింది. "
            f"ఎరువుల సూచన మీ NPK విలువలను 50 అనే ప్రాథమిక పరిమితితో "
            f"పోల్చి రూపొందించబడింది: {fertilizer}. "
            f"ఇది ఒక ప్రాథమిక సూచన మాత్రమే; పంట వేయడానికి ముందు "
            f"నేల పరీక్ష, పంట కాలం, నీటి లభ్యత మరియు స్థానిక వ్యవసాయ "
            f"అధికారుల సలహాను కూడా పరిగణించండి. ఈ అంచనా దిగుబడికి హామీ కాదు."
        )

    return (
        f"You entered soil values of Nitrogen {N}, Phosphorus {P}, "
        f"Potassium {K}, and pH {ph}. The weather service reported "
        f"{temp:.1f}°C temperature, {humidity}% humidity, and "
        f"{rainfall} mm rainfall for the selected city. The trained "
        f"machine-learning model used these seven features to predict "
        f"{crop}. The fertilizer suggestion is based on comparing your "
        f"NPK values with the simple threshold of 50: {fertilizer}. "
        f"This is an initial estimate, not a guarantee of crop yield. "
        f"Before planting or applying fertilizer, also consider a soil "
        f"test, crop season, water availability, and local agricultural "
        f"expert advice."
    )


@app.route("/")
def home():
    return render_template("index.html", lang="en")


@app.route("/predict", methods=["POST"])
def predict():
    lang = request.form.get("lang", "en")
    if lang not in ("en", "te"):
        lang = "en"

    city = request.form.get("city", "").strip()

    if not city:
        return render_template(
            "index.html",
            lang=lang,
            error=(
                "దయచేసి నగరం పేరు నమోదు చేయండి."
                if lang == "te"
                else "Please enter a city name."
            )
        )

    try:
        N = float(request.form.get("N", ""))
        P = float(request.form.get("P", ""))
        K = float(request.form.get("K", ""))
        ph = float(request.form.get("ph", ""))

        if not all(np.isfinite(v) for v in (N, P, K, ph)):
            raise ValueError

        if min(N, P, K) < 0 or not 0 <= ph <= 14:
            raise ValueError

    except (ValueError, TypeError):
        message = (
            "N, P, K విలువలు ఋణాత్మకంగా ఉండకూడదు; pH 0 నుంచి 14 మధ్య ఉండాలి."
            if lang == "te"
            else "Enter valid numbers. N, P and K cannot be negative, and pH must be between 0 and 14."
        )
        return render_template("index.html", lang=lang, error=message)

    try:
        temp, humidity, rainfall = get_weather(city)
    except RuntimeError as exc:
        print(f"Weather error: {exc}")
        message = (
            "వాతావరణ సమాచారం పొందలేకపోయాం. నగరం పేరు, ఇంటర్నెట్ లేదా API సెట్టింగులను తనిఖీ చేయండి."
            if lang == "te"
            else "Unable to get weather data. Check the city name, internet connection, or API settings."
        )
        return render_template("index.html", lang=lang, error=message)

    features = pd.DataFrame(
        [[N, P, K, temp, humidity, ph, rainfall]],
        columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"])
    crop = str(model.predict(features)[0])
    fertilizer_details = fertilizer_recommendation(N, P, K, lang)

    fertilizer_summary = ", ".join(item["name"] for item in fertilizer_details)
    explanation = make_explanation(
        lang, crop, N, P, K, ph,
        temp, humidity, rainfall, fertilizer_summary
    )

    return render_template(
        "index.html",
        lang=lang,
        crop=crop,
        crop_te=CROP_TE.get(crop.lower(), crop),
        fertilizer_details=fertilizer_details,
        temp=round(temp, 2),
        humidity=humidity,
        rainfall=rainfall,
        explanation=explanation
    )


if __name__ == "__main__":
    app.run(debug=True)
