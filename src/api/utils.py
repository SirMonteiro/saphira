import random
import string
from uuid import UUID

from .models import Student

datetime_url_format = "%Y-%m-%dT%H:%M"

def generate_unique_code(length=3):
    characters = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choices(characters, k=length))
        if not Student.objects.filter(code=code).exists():
            break
    return code

def generate_token_code():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=5))

class UUIDConverter:
    regex = '[0-9a-fA-F-]+'  # Regex para UUID com hífens

    def to_python(self, value):
        return UUID(value)

    def to_url(self, value):
        return str(value)