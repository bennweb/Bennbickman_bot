services:
  - type: web
    name: bennbickman-bot
    env: python
    branch: main
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python main.py"
    envVars:
      - key: BOT_TOKEN
        sync: false
      - key: MONGO_DB_URI
        sync: false
      - key: API_ID
        sync: false
      - key: API_HASH
        sync: false
      - key: LOG_CHANNEL
        sync: false
