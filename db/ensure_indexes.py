"""Création centralisée des index MongoDB nécessaires au TP7."""
from db.connection import get_collection


def ensure_indexes() -> None:
    alerts = get_collection("alerts")
    alerts.create_index("alert_id", unique=True, sparse=True)
    alerts.create_index("risk_score")
    alerts.create_index("timestamp")
    alerts.create_index([("user_id", 1), ("risk_score", -1)])
    alerts.create_index("risk_level")
    alerts.create_index("department")
