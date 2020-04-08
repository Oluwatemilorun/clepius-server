import uuid
from datetime import datetime

def generate_patient_id():
    id = str(uuid.uuid4())[:4]
    year = str(datetime.today().year)[-2:]
    return f'PAT/{year}/{id}'



