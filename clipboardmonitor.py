import pyperclip
import webbrowser
import time
import re

def check_clipboard():
    previous_text = ""
    # Regex to match a 43-character alphanumeric token ending with "pump"
    token_pattern = r"^[a-zA-Z0-9]{38}pump$"

    while True:
        try:
            # Get current clipboard content
            current_text = pyperclip.paste().strip()
            if current_text != previous_text:
                previous_text = current_text

                # Check if clipboard content matches the token pattern
                if re.match(token_pattern, current_text):
                    print(f"Detected token: {current_text}")
                    
                    # Construct the URL using the detected token
                    url = f"https://neo.bullx.io/terminal?chainId=1399811149&address={current_text}"
                    print(f"Opening webpage: {url}")
                    
                    # Open the URL in the default web browser
                    webbrowser.open(url)
        except Exception as e:
            print(f"Error: {e}")

        # Check clipboard every 0.5 seconds
        time.sleep(0.5)

# Run the clipboard monitoring function
if __name__ == "__main__":
    check_clipboard()
