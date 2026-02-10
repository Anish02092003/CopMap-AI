## System Architecture

![Architecture](docs/architecture.png)

Sample Outputs
Crowd Detection
POST /detect


Response:

{
  "location": "Market Road",
  "analysis": {
    "people_count": 5,
    "crowd_density": "LOW"
  },
  "alerts": [],
  "suspicious_activity": []
}

Patrol Log Storage
POST /patrol-log

{
  "message": "Patrol log stored",
  "id": 1
}

Intelligence Summary
GET /intelligence-summary

{
  "summary": "Patrol Intelligence Summary:\n- Crowd gathering before cricket match\n- Festival shopping crowd increasing\n\nRecommendation: Increase monitoring in frequently crowded areas."
}
