# Guide de déploiement Koyeb — TP7_secure

1. Pousser la branche GitHub contenant l'application Flask.
2. Dans Koyeb, créer une nouvelle application depuis le dépôt GitHub.
3. Choisir un service Web avec la commande de démarrage `gunicorn main:app`.
4. Définir les variables d'environnement : `MONGO_URI`, `DB_NAME`, `JWT_SECRET`, `EMAIL_SENDER`, `EMAIL_APP_PASSWORD`, `OTP_RECIPIENT`, `SESSION_LIFETIME_SECONDS`, `RATE_LIMIT_STORAGE_URI`, `FLASK_ENV=production`, `AUTH_RATE_LIMIT`.
5. Vérifier que Koyeb active automatiquement HTTPS sur le domaine fourni.
6. Tester `/login`, `/dashboard` et les exports CSV après injection des secrets.
7. Insérer ici l'URL finale et une capture d'écran de preuve de déploiement lorsque le service est publié : **URL à compléter après déploiement réel**.
