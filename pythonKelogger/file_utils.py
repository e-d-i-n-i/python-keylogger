from datetime import datetime

# Global variable to store the current log file name
current_log_file = None

def get_log_file():
    """Generates or retrieves the current log file based on today's date."""
    global current_log_file
    today_date = datetime.now().strftime('%Y-%m-%d')  # Get today's date in YYYY-MM-DD format
    log_filename = f"log_{today_date}.txt"

    # If the log file is not set yet or the date has changed, update it
    if current_log_file != log_filename:
        current_log_file = log_filename

    return current_log_file
