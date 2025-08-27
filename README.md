# CodeCritic Junior 👨‍🏫

A beginner-friendly coding improvement platform that provides AI-powered feedback and code improvements using the Gemini API.

## Features

- Modern, dark-themed UI
- Real-time code analysis
- Beginner-friendly feedback
- Code improvement suggestions
- Syntax highlighting
- Copy-to-clipboard functionality
- Responsive design

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your Gemini API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
5. Run the application:
   ```bash
   python app.py
   ```
6. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Paste your Python code into the input area
2. Click "Get Feedback"
3. View the AI feedback and improved code suggestions
4. Use the copy buttons to copy the feedback or improved code

## Example Code to Test

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)
```

## Technologies Used

- Flask (Backend)
- HTML/CSS/Bootstrap (Frontend)
- Gemini API (AI Analysis)
- Highlight.js (Syntax Highlighting)

## License

MIT License

## Credits

Built for Hackathon 2024 🔥 