from datetime import datetime


def detect_suspicious(location: str, people_count: int):
    suspicious_flags = []

    current_hour = datetime.now().hour

    
    if people_count > 0 and (current_hour >= 23 or current_hour <= 4):
        suspicious_flags.append(
            f"Unusual movement detected at {location} during late-night hours"
        )

    
    if people_count > 50:
        suspicious_flags.append(
            f"Possible stampede risk at {location}"
        )

    
    if location.lower() == "police hq" and people_count > 3:
        suspicious_flags.append(
            "Unauthorized gathering near restricted zone"
        )

    return suspicious_flags
