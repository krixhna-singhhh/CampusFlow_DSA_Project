from datetime import datetime


def non_empty(value: str, field_name: str) -> str:
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} cannot be empty.")
    return cleaned


def validate_priority(value: int) -> int:
    if value not in {1, 2, 3, 4, 5}:
        raise ValueError("Priority must be an integer from 1 (low) to 5 (high).")
    return value


def validate_deadline(value: str) -> str:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("Deadline must use YYYY-MM-DD format.") from exc
    return value


def validate_positive_float(value: float, field_name: str) -> float:
    if value <= 0:
        raise ValueError(f"{field_name} must be greater than 0.")
    return value
