
# Shutdown Scheduler

Shutdown Scheduler is a simple GUI application built with Python's Tkinter library. It allows users to set a timer to automatically shut down their computer after a specified duration.

## Features
- User-friendly interface to set a shutdown timer.
- Cross-platform support: Works on Windows, Linux, and macOS.
- Confirmation dialog to ensure accidental shutdowns are avoided.
- Customizable shutdown timer in seconds.

## Requirements
- Python 3.x
- Tkinter (usually included with standard Python installations)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/ACRZeuss/Shutdown-Scheduler.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Shutdown-Scheduler
   ```

## Usage
1. Run the application:
   ```sh
   python main.py
   ```
2. Enter the shutdown timer duration in seconds.
3. Confirm the shutdown request.

## Building the Executable
To build the executable with a custom icon, use PyInstaller:
```sh
pyinstaller --onefile --windowed --icon=app_icon.ico main.py
```

The executable will be created in the `dist` directory.

## License
This project is licensed under the MIT License.
