import uuid
from datetime import datetime

def generate_staff_id():
    id = str(uuid.uuid4())[:4]
    year = str(datetime.today().year)[-2:]
    return f'STA/{year}/{id}'



