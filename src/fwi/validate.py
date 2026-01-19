def validate(temp,rh,rain):
    if not (0 <= temp <= 50):
        return "Temperature must be between 0 and 50"
    if not (0 <= rh <= 100):
        return "Relative Humidity must be between 0 and 100"
    if not (0 <= rain <= 50):
        return "Rain cannot be negative"
    return "Valid"