import os
import dotenv
dotenv.load_dotenv()

class Config(object):
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:////tmp/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY', '')
    LOCATION = os.getenv('LOCATION', '')
    UNITS = os.getenv('UNITS', 'imperial')
    PIHOLE_HOST = os.getenv('PIHOLE_HOST', '')
    PIHOLE_API_TOKEN= os.getenv('PIHOLE_API_TOKEN', '')
    HOMEASSISTANT_HOST = os.getenv('HOMEASSISTANT_HOST', '')
    HOMEASSISTANT_TOKEN = os.getenv('HOMEASSISTANT_TOKEN', '')