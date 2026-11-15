import os
import redis
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parent.parent.parent/".env")
redis_client = redis.Redis(host = os.getenv("REDIS_HOST"), port = int(os.getenv("REDIS_PORT")), username=os.getenv("REDIS_USERNAME"), password=os.getenv("REDIS_PASSWORD"), decode_responses=True, ssl=False)
