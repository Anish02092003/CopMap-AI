def generate_alert(location: str, people_count: int, crowd_density: str):
    alerts = []

    if crowd_density == "HIGH":
        alerts.append(f"High crowd density detected at {location}")

    if people_count > 40:
        alerts.append(f"Potential overcrowding risk at {location}")

    return alerts
