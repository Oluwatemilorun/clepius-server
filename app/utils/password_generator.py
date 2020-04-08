from uuid import uuid4

def generate_initial_password():
    return str(uuid4)[:12]