# Clipboard Monitor for Token Detection on macOS

This Python script monitors the macOS clipboard in real-time to detect cryptocurrency token addresses ending with `pump`. When a valid token is copied to the clipboard, the script automatically opens a webpage in the default browser, appending the detected token to a predefined URL.

## Features
- **Real-Time Clipboard Monitoring**: Continuously checks the clipboard for updates.
- **Token Validation**: Detects 43-character alphanumeric strings ending with `pump`.
- **Automatic Webpage Launch**: Opens a URL like `https://neo.bullx.io/terminal?chainId=1399811149&address=<token>` in the default browser.

## Requirements
- macOS
- Python 3.7 or higher
- Python libraries: `pyperclip`

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/clipboard-monitor.git
   cd clipboard-monitor
   ```

2. **Set Up Python Environment**
   It’s recommended to use a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**
   ```bash
   python clipboard_monitor.py
   ```

## How It Works
1. **Monitor Clipboard**: The script continuously watches the clipboard for changes.
2. **Validate Tokens**: Matches clipboard content against a pattern:
   - 43 characters long
   - Ends with `pump`
3. **Open Webpage**: When a valid token is detected, the script opens:
   ```
   https://neo.bullx.io/terminal?chainId=1399811149&address=<detected-token>
   ```

## Example

### Valid Token
When you copy a string like this:
```
3vWoEFW9HzHUemY5usqyDyfCzf1QutWVmSrsdEaKpump
```

The script will open:
```
https://neo.bullx.io/terminal?chainId=1399811149&address=3vWoEFW9HzHUemY5usqyDyfCzf1QutWVmSrsdEaKpump
```

### Invalid Token
Strings that do not match the pattern (e.g., not 43 characters or missing `pump` at the end) are ignored.

## Customization
- **Modify Token Pattern**: Update the `token_pattern` variable in the script to change the validation rules.
- **Adjust URL**: Change the `url` construction logic in the script to match your requirements.

## Known Issues
- The script currently runs in an infinite loop. To stop it, use `Ctrl+C` in the terminal.
- Clipboard monitoring may consume minimal system resources when running continuously.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you'd like to suggest improvements.


Happy monitoring! 🚀
