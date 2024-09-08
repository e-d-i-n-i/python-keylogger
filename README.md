# Background Keylogger ⌨️

A Python-based keylogger designed to run in the background on Windows without displaying a command console. This tool records keystrokes and logs them to a file.

## Features

- Runs in the background without showing a command console.
- Logs keystrokes to a file, with automatic file naming based on the current date.
- Configurable to handle various special keys and modifiers.

## Installation

### Prerequisites

- Python 3.x
- PyInstaller
- PyWin32 (for Windows Service)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/e-d-i-n-i/python-keylogger.git
   cd python-keylogger
   ```

2. **Install Required Packages**

   Install the necessary Python packages using pip:

   ```bash
   pip install pynput pywin32
   ```

3. **Convert Python Script to Executable**

   Use PyInstaller to create an executable. Ensure you have your icon in the `icons` subdirectory.

   ```bash
   pyinstaller --onefile --windowed --icon=icons/question.ico --name=Keylogger main.py
   ```

4. **Install as Windows Service (Optional)**

   If you want the keylogger to run as a Windows service:

   ```bash
   python service.py install
   python service.py start
   ```

   Replace `service.py` with the name of your service management script.

## Usage

- **Running the Executable:** Simply run the generated executable. It will start logging keystrokes in the background.
- **Stopping the Service:** If installed as a service, stop it via Task Manager or using:

  ```bash
  python service.py stop
  ```

- **Viewing Logs:** Logs are stored in files named `log_YYYY-MM-DD.txt` in the same directory as the executable.

## Troubleshooting

- **No Log File Created:** Ensure that the executable has write permissions in the directory.
- **Service Not Running:** Verify that the service is correctly installed and started using Task Manager or the command line.

## Contributing

Feel free to submit issues, pull requests, or suggestions. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This keylogger is intended for educational purposes and should be used responsibly. Unauthorized use of keyloggers is illegal and unethical. Ensure you have permission before deploying this tool.
