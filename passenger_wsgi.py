import os
import sys

# Set the application root directory
app_root = os.path.dirname(__file__)
sys.path.insert(0, app_root)

# Import the FastAPI application
from main import app as application
