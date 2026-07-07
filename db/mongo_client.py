"""
db/mongo_client.py
Index MongoDB complémentaires pour TP7.
"""
from db.connection import get_collection


def ensure_alerts_indexes() -> None:
    """Crée les index utiles de la collection alerts."""
    alerts = get_collection("alerts")
    alerts.create_index("user_id")
    alerts.create_index("timestamp")
    alerts.create_index("risk_level")
