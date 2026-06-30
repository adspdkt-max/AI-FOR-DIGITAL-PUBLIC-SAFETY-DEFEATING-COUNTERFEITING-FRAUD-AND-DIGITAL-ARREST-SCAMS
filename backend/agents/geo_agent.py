crime_locations = [
    {"city": "Chennai", "cases": 120},
    {"city": "Bangalore", "cases": 95},
    {"city": "Mumbai", "cases": 150},
    {"city": "Delhi", "cases": 180},
    {"city": "Hyderabad", "cases": 80}
]

def analyze_hotspots():

    hotspot = max(crime_locations, key=lambda x: x["cases"])

    return {
        "total_cities": len(crime_locations),
        "crime_data": crime_locations,
        "highest_risk_city": hotspot["city"],
        "cases": hotspot["cases"]
    }
