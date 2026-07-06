# CLAUDE.md - ScreenTime Analysis Project

## Project Overview
This repository contains the "Screen Guide" application, which monitors screen time, categorizes content, evaluates productivity, and provides guidance to manage screen time effectively.

### Features (from README)
1. Monitor screen and track daily/weekly screen time.
2. Categorize on-screen content (study, skills, games, entertainment, etc.).
3. Evaluate productivity and provide management tips.
4. Allow creating 'Blockers' for specific content:
   - Completely turn off the tab/app when targeted content is detected.
   - Convince the user to turn off the app via user-suggested methods and instructions.
5. Includes a screen time management chatbot and goal streak setting.

### Tech Stack
- Python for core logic and terminal commands
- Tkinter for GUI development
- Machine learning for content categorization (entertainment, skills, study, etc.)
- Local storage for daily/weekly screen data
- Chatbot API for conversational interface

## Development Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Tkinter (usually comes with Python on Windows/macOS, may need separate install on Linux)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ScreenTime_Analysis
   ```
2. Install required Python packages (if any are specified in a requirements.txt):
   ```bash
   pip install -r requirements.txt
   ```
   Note: As of now, there is no requirements.txt. You may need to create one based on the imports in the source code.

## Running the Application
Since there is no main entry point defined yet, you would typically run the main Python script once it's created. For example:
```bash
python main.py
```
or
```bash
python screenguide.py
```
Adjust based on the actual entry point file.

## Testing
Currently, there are no tests. As you develop, consider adding unit tests using a framework like `pytest` or `unittest`.

To run tests (once they exist):
```bash
# For pytest
pytest

# For unittest
python -m unittest discover
```

## Code Style
- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code.
- Use descriptive variable and function names.
- Keep functions and classes focused on a single responsibility.
- Write docstrings for public modules, classes, and functions.

## Git Workflow
1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit with clear messages:
   ```bash
   git commit -m "Add feature: your feature description"
   ```
3. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
4. Open a pull request for review.

## Common Tasks
### Adding Dependencies
If you add new Python packages, update `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### Running the Application
Once you have a main script, run it with Python:
```bash
python path/to/main.py
```

### Debugging
- Use Python's built-in `pdb` or your IDE's debugger.
- Check console output for logs and error messages.

## Notes for Claude Code
- When asked to implement features, refer to the README for feature descriptions.
- Follow the existing code style (once code exists).
- Ensure any new code is tested appropriately.
- Keep commits focused and atomic.

## License
This project is currently without a license. Please add one if you intend to share or distribute the code.

---
*This file is intended to guide Claude Code in assisting with development of the ScreenTime Analysis project.*