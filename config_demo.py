
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

app_mode = os.getenv("APP_MODE", "development")
api_base_url = os.getenv("API_BASE_URL")
timeout_text = os.getenv("TIMEOUT_SECONDS", "10")

# Validate the application mode.
allowed_modes = {"development", "testing", "production"}

if app_mode not in allowed_modes:
    raise ValueError(
        f"Invalid APP_MODE: {app_mode!r}. "
        f"Allowed values: {sorted(allowed_modes)}"
    )

# Validate that the URL has a scheme and hostname.
if not api_base_url:
    raise ValueError("API_BASE_URL is required.")

parsed_url = urlparse(api_base_url)

if parsed_url.scheme not in {"http", "https"} or not parsed_url.hostname:
    raise ValueError("API_BASE_URL must be a valid HTTP or HTTPS URL.")

# Environment variables are strings, so convert the timeout.
try:
    timeout_seconds = int(timeout_text)
except ValueError as exc:
    raise ValueError("TIMEOUT_SECONDS must be an integer.") from exc

if timeout_seconds <= 0:
    raise ValueError("TIMEOUT_SECONDS must be greater than zero.")

print("Configuration is valid.")
print(f"Application mode: {app_mode}")
print(f"API base URL: {api_base_url}")
print(f"Timeout: {timeout_seconds} seconds")
