import time
import random

def generate_user_data():
    """Генерирует набор данных для нового пользователя."""
    timestamp = int(time.time())
    return {
        "name": f"Kapton_{timestamp}",
        "email": f"rystuk_qa_{timestamp}@gmail.com",
        "password": f"Pass_{timestamp}"
        }