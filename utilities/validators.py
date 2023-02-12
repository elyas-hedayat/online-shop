from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_file_size(file):
    max_size_kb = 200

    if file.size > max_size_kb * 1024:
        raise ValidationError(f"files cannot be larger than {max_size_kb}KB")


phone_number_regex = RegexValidator(
    regex=r"^(\+98|0)?9\d{9}$", message=("unvalid phonenumber")
)
