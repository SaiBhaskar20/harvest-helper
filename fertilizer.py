
THRESHOLD = 50

def fertilizer_recommendation(N, P, K, lang="en"):
    recommendations = []

    if N < THRESHOLD:
        if lang == "te":
            recommendations.append({
                "name": "యూరియా (Urea) — Nitrogen నైట్రోజన్",
                "reason": (
                    f"మీ N విలువ {N}. ఇది మన ప్రాథమిక "
                    f"పరిమితి {THRESHOLD} కంటే తక్కువగా ఉంది."
                ),
                "benefit": (
                    "నైట్రోజన్ మొక్కల ఆకులు, కాండం పెరుగుదలకు "
                    "మరియు క్లోరోఫిల్ తయారీకి సహాయపడుతుంది."
                ),
                "action": (
                    "నేల పరీక్ష మరియు పంట అవసరాల ఆధారంగా "
                    "నైట్రోజన్ ఎరువు అవసరాన్ని నిర్ధారించండి."
                )
            })
        else:
            recommendations.append({
                "name": "Urea — Nitrogen",
                "reason": (
                    f"Your N value is {N}, below our preliminary "
                    f"threshold of {THRESHOLD}."
                ),
                "benefit": (
                    "Nitrogen supports leaf and stem growth "
                    "and chlorophyll production."
                ),
                "action": (
                    "Confirm the need for nitrogen using a soil "
                    "test and crop-specific guidance."
                )
            })

    if P < THRESHOLD:
        if lang == "te":
            recommendations.append({
                "name": "DAP (డైఅమోనియం ఫాస్ఫేట్) — ఫాస్ఫరస్",
                "reason": (
                    f"మీ P విలువ {P}. ఇది మన ప్రాథమిక "
                    f"పరిమితి {THRESHOLD} కంటే తక్కువగా ఉంది."
                ),
                "benefit": (
                    "ఫాస్ఫరస్ వేర్ల అభివృద్ధికి, మొక్కలో శక్తి "
                    "బదిలీకి మరియు పునరుత్పత్తి ప్రక్రియలకు సహాయపడుతుంది."
                ),
                "action": (
                    "DAPలో నైట్రోజన్ కూడా ఉంటుంది. మొత్తం ఎరువుల "
                    "ప్రణాళికలో ఆ నైట్రోజన్‌ను కూడా లెక్కించాలి."
                )
            })
        else:
            recommendations.append({
                "name": "DAP (Diammonium Phosphate) — Phosphorus",
                "reason": (
                    f"Your P value is {P}, below our preliminary "
                    f"threshold of {THRESHOLD}."
                ),
                "benefit": (
                    "Phosphorus supports root development, energy "
                    "transfer, and reproductive processes."
                ),
                "action": (
                    "DAP also contains nitrogen, so include that "
                    "nitrogen in the overall fertilizer plan."
                )
            })

    if K < THRESHOLD:
        if lang == "te":
            recommendations.append({
                "name": "MOP (మ్యూరియేట్ ఆఫ్ పొటాష్) — పొటాషియం (పొటాష్)",
                "reason": (
                    f"మీ K విలువ {K}. ఇది మన ప్రాథమిక "
                    f"పరిమితి {THRESHOLD} కంటే తక్కువగా ఉంది. "
                    "అందుకే ప్రాథమిక నియమం ప్రకారం MOP సూచించబడింది."
                ),
                "benefit": (
                    "పొటాషియం మొక్కలో నీటి నియంత్రణకు, పోషకాల "
                    "రవాణాకు మరియు ఎంజైమ్‌ల పనితీరుకు సహాయపడుతుంది. "
                    "కొన్ని పంటల్లో నాణ్యతను మెరుగుపరచడంలో కూడా పాత్ర ఉంటుంది."
                ),
                "action": (
                    "పంట రకం, నేల పరీక్ష, ఎరువు లేబుల్ మరియు "
                    "స్థానిక వ్యవసాయ నిపుణుల సలహా ఆధారంగా మాత్రమే "
                    "వాడే మోతాదును నిర్ణయించండి."
                )
            })
        else:
            recommendations.append({
                "name": "MOP (Muriate of Potash) — Potassium (Potash)",
                "reason": (
                    f"Your K value is {K}, below our preliminary "
                    f"threshold of {THRESHOLD}. Our basic rule "
                    "therefore suggests MOP."
                ),
                "benefit": (
                    "Potassium supports water regulation, nutrient "
                    "movement, and enzyme activity. It can also "
                    "support crop quality in some crops."
                ),
                "action": (
                    "Decide the application rate only after considering "
                    "the crop, soil test, product label, and local "
                    "agricultural guidance."
                )
            })

    
    if not recommendations:
        if lang == "te":
            recommendations.append({
                "name": "NPK పోషక విలువలు ప్రాథమిక పరిమితికి సరిపోతున్నాయి",
                "reason": (
                    "మీరు ఇచ్చిన నైట్రోజన్ (N), ఫాస్ఫరస్ (P), "
                    "పొటాషియం (K) విలువలు మన అప్లికేషన్‌లో "
                    "ఉపయోగిస్తున్న 50 అనే ప్రాథమిక పరిమితికి "
                    "సమానంగా లేదా అంతకంటే ఎక్కువగా ఉన్నాయి."
                ),
                "benefit": (
                    "ఈ ప్రాథమిక తనిఖీ ప్రకారం ఈ మూడు పోషక విలువలు "
                    "మన అప్లికేషన్ నిర్దేశించిన పరిమితికి సరిపోతున్నాయి. "
                    "అయితే, దీనివల్ల నేలలో అన్ని పోషకాలు పూర్తిగా "
                    "సరిపోతున్నాయని నిర్ధారణ కాదు."
                ),
                "action": (
                    "మరింత నమ్మకమైన అంచనాకు నేల పరీక్షను పునరావృతం చేయండి. "
                    "అవసరమైతే వ్యవసాయ నిపుణుడిని సంప్రదించండి మరియు "
                    "పంట-ప్రత్యేక సలహాను అనుసరించండి."
                )
            })
        else:
            recommendations.append({
                "name": "NPK Values Meet the Basic Threshold",
                "reason": (
                    "Your Nitrogen (N), Phosphorus (P), and Potassium (K) "
                    "values are equal to or above the preliminary "
                    "threshold of 50 used by this application."
                ),
                "benefit": (
                    "These three nutrient values meet the application's "
                    "basic threshold. However, this does not confirm "
                    "that all soil nutrients are sufficient."
                ),
                "action": (
                    "Review a soil test for a more reliable assessment. "
                    "Consult an agricultural expert when needed and "
                    "follow crop-specific advice."
                )
            })
    return recommendations