# QuantumTraderConfig.py

# API Configuration
API_KEYS = {
    'kraken': {
        'api_key': 'SYJ7BtonLlbqoz3om0dEW36LjSw0A2dQyCRdpBSYcZjWQ0vXCi8ECrPg',
        'api_secret': 'ZFlKg0Zkc+JLOXAfMdU7ng/b+ABX83UkSBk/AiUaMKq51Wo650fLg7F/nPU5YIaU8mVeD9zPHKMm0mdNX3unbA=='
    },
    # Add other exchanges' API keys here if needed
}

# Database Configuration (if you plan to use a database for storing historical data, etc.)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_database_user',
    'password': 'your_database_password',
    'database': 'your_database_name'
}

# AI Model Parameters (placeholders for now, adjust based on your model's requirements)
AI_MODEL_PARAMS = {
    'learning_rate': 0.01,
    'epochs': 100,
    # Add other necessary parameters for your model
}

# Trading Strategy Settings (placeholders for now, adjust as you develop your strategies)
TRADING_STRATEGY_PARAMS = {
    'target_daily_profit': 0.15,
    'max_risk_per_trade': 0.01,
    # Add other strategy parameters as needed
}

# Logging Configuration
LOGGING_CONFIG = {
    'log_file': 'quantumtrader.log',
    'log_level': 'INFO',
    # Configure as needed
}
