from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import io
import sys
from contextlib import redirect_stdout
import subprocess
import tempfile
from flask import session, redirect, url_for, flash
import secrets
from competitive_problems import PROBLEMS
print(secrets.token_hex(32))
# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
print("GOOGLE_API_KEY:", GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Language-specific configurations
LANGUAGE_CONFIGS = {
    'python': {
        'extension': 'py',
        'runtime': 'python',
        'comment': '#'
    },
    'javascript': {
        'extension': 'js',
        'runtime': 'node',
        'comment': '//'
    },
    'java': {
        'extension': 'java',
        'runtime': 'java',
        'comment': '//'
    },
    'cpp': {
        'extension': 'cpp',
        'runtime': 'g++',
        'comment': '//'
    },
    'c': {
        'extension': 'c',
        'runtime': 'gcc',
        'comment': '//'
    },
    'ruby': {
        'extension': 'rb',
        'runtime': 'ruby',
        'comment': '#'
    },
    'php': {
        'extension': 'php',
        'runtime': 'php',
        'comment': '//'
    },
    'go': {
        'extension': 'go',
        'runtime': 'go run',
        'comment': '//'
    },
    'rust': {
        'extension': 'rs',
        'runtime': 'rustc',
        'comment': '//'
    },
    'swift': {
        'extension': 'swift',
        'runtime': 'swift',
        'comment': '//'
    }
}
@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('auth'))
    return render_template('index.html')

USERS = {}

USER_PROGRESS = {} 


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form.get('username')
        password = request.form.get('password')
        if action == 'login':
            if username in USERS and USERS[username] == password:
                session['user'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password.', 'danger')
        elif action == 'register':
            if username in USERS:
                flash('Username already exists.', 'danger')
            else:
                USERS[username] = password
                flash('Registration successful! Please log in.', 'success')
    return render_template('auth.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth'))
@app.route('/analyze', methods=['POST'])
def analyze_code():
    try:
        code = request.json.get('code', '')
        language = request.json.get('language', 'python')
        
        if language not in LANGUAGE_CONFIGS:
            return jsonify({
                "error": f"Unsupported language: {language}",
                "feedback": f"Sorry, {language} is not currently supported.",
                "improved_code": ""
            }), 400

        # Create the prompt for Gemini
        prompt = f"""You are CodeCritic Junior, a professional coding mentor specializing in {language}. Analyze this {language} code and provide a detailed analysis in the following JSON format:

{{
    "feedback": "Detailed feedback about code style, efficiency, and best practices specific to {language}. Include specific examples and explanations. Format the feedback with:
    1. Main points as numbered lists (1., 2., 3., etc.)
    2. Sub-points with dashes (-)
    3. Clear separation between sections
    4. Specific examples from the code
    5. Recommendations for improvement",
    "improved_code": "A complete, improved version of the code with comments explaining key improvements"
}}

Code to analyze:
{code}

Keep the feedback professional and educational, suitable for beginners. Focus on:
1. Code structure and organization
2. Variable naming and readability
3. Algorithm efficiency
4. {language}-specific best practices and conventions
5. Potential edge cases and error handling
6. Language-specific features and optimizations
7. Security considerations
8. Performance implications

The improved code should be a complete, working solution with clear comments explaining the improvements. Use {LANGUAGE_CONFIGS[language]['comment']} for comments."""

        # Get response from Gemini
        response = model.generate_content(prompt)
        
        # Try to parse the response as JSON
        try:
            # Clean the response text to ensure it's valid JSON
            response_text = response.text.strip()
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.endswith('```'):
                response_text = response_text[:-3]
            response_text = response_text.strip()
            
            result = json.loads(response_text)
            
            # Ensure both required fields are present
            if 'feedback' not in result or 'improved_code' not in result:
                raise ValueError("Response missing required fields")
                
        except (json.JSONDecodeError, ValueError) as e:
            # If JSON parsing fails, create a structured response
            result = {
                "feedback": "Error processing the response. Here's the raw feedback:\n\n" + response.text,
                "improved_code": "Error: Could not generate improved code. Please try again."
            }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "feedback": "An error occurred while analyzing the code.",
            "improved_code": "Please try again later."
        }), 500

@app.route('/run', methods=['POST'])
def run_code():
    try:
        code = request.json.get('code', '')
        language = request.json.get('language', 'python')
        if language == 'python':
            with tempfile.NamedTemporaryFile(suffix='.py', delete=False, mode='w', encoding='utf-8') as temp:
                temp.write(code)
                temp_path = temp.name
            try:
                process = subprocess.run(
                    ['python', temp_path],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                output = process.stdout + process.stderr
            finally:
                os.unlink(temp_path)
            return jsonify({'output': output, 'success': process.returncode == 0})
        # ...other languages...
    except Exception as e:
        return jsonify({'output': str(e), 'success': False}), 500

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message')
        context = data.get('context', '')

        if not message:
            return jsonify({'error': 'No message provided'}), 400

        # Add context to the prompt if provided
        if context:
            prompt = f"""You are CodeCritic Junior, a professional coding mentor. The user is viewing the following content on their page:

---PAGE CONTENT START---
{context}
---PAGE CONTENT END---

Now, answer the user's question below, using the above content as context if relevant.

User's message: {message}

Please structure your response with:
1. A clear introduction
2. Main points with proper formatting
3. Code examples in markdown code blocks if relevant
4. A concise conclusion

Remember to:
- Use proper spacing between paragraphs
- Format code with proper syntax highlighting
- Use bullet points for lists
- Keep the response focused and professional
"""
        else:
            prompt = f"""You are CodeCritic Junior, a professional coding mentor. Please provide a clear, well-formatted response to the following question or request. 
Format your response with proper spacing, bullet points, and code blocks where appropriate. 
Keep the response professional and educational.

User's message: {message}

Please structure your response with:
1. A clear introduction
2. Main points with proper formatting
3. Code examples in markdown code blocks if relevant
4. A concise conclusion

Remember to:
- Use proper spacing between paragraphs
- Format code with proper syntax highlighting
- Use bullet points for lists
- Keep the response focused and professional
"""

        # Generate response using Gemini
        response = model.generate_content(prompt)

        # Format the response
        formatted_response = response.text.replace('\n', '<br>')
        formatted_response = formatted_response.replace('```', '<pre><code>')
        formatted_response = formatted_response.replace('```', '</code></pre>')

        return jsonify({'response': formatted_response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/submit-solution', methods=['POST'])
def submit_solution():
    if 'user' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    category = data.get('category')
    problem_id = data.get('problem_id')
    code = data.get('code')
    language = data.get('language')
    
    if not all([category, problem_id, code, language]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if category not in PROBLEMS or problem_id not in PROBLEMS[category]:
        return jsonify({'error': 'Problem not found'}), 404
    
    problem = PROBLEMS[category][problem_id]
    test_cases = problem.get('test_cases', [])
    
    # Create a temporary file with the code
    with tempfile.NamedTemporaryFile(suffix=f'.{LANGUAGE_CONFIGS[language]["extension"]}', delete=False, mode='w', encoding='utf-8') as temp:
        temp.write(code)
        temp_path = temp.name
    
    try:
        results = []
        all_passed = True
        
        for test_case in test_cases:
            if language == 'python':
                # Add necessary imports and test case
                test_code = f"""
import sys
from typing import List, Optional
import json

{code}

# Test case
test_input = {json.dumps(test_case['input'])}
test_output = {json.dumps(test_case['output'])}

# Run the solution
result = None
try:
    # Get the function name from the problem ID
    function_name = {{
        'two_sum': 'twoSum',
        'max_subarray': 'maxSubArray',
        'rotate_array': 'rotate',
        'product_except_self': 'productExceptSelf',
        'find_duplicate': 'findDuplicate',
        'longest_palindrome': 'longestPalindrome',
        'valid_parentheses': 'isValid',
        'longest_common_prefix': 'longestCommonPrefix',
        'reverse_words': 'reverseWords',
        'valid_anagram': 'isAnagram'
    }}.get('{problem_id}')

    if not function_name:
        raise ValueError(f"Unknown problem ID: {problem_id}")

    # Call the appropriate function with the test input
    if function_name == 'twoSum':
        result = twoSum(test_input['nums'], test_input['target'])
    elif function_name == 'maxSubArray':
        result = maxSubArray(test_input['nums'])
    elif function_name == 'rotate':
        rotate(test_input['nums'], test_input['k'])
        result = test_input['nums']
    elif function_name == 'productExceptSelf':
        result = productExceptSelf(test_input['nums'])
    elif function_name == 'findDuplicate':
        result = findDuplicate(test_input['nums'])
    elif function_name == 'longestPalindrome':
        result = longestPalindrome(test_input['s'])
    elif function_name == 'isValid':
        result = isValid(test_input['s'])
    elif function_name == 'longestCommonPrefix':
        result = longestCommonPrefix(test_input['strs'])
    elif function_name == 'reverseWords':
        result = reverseWords(test_input['s'])
    elif function_name == 'isAnagram':
        result = isAnagram(test_input['s'], test_input['t'])

    # Compare with expected output
    print(json.dumps({{
        'input': test_input,
        'expected': test_output,
        'actual': result,
        'passed': str(result) == str(test_output)
    }}))
except Exception as e:
    print(json.dumps({{
        'input': test_input,
        'error': str(e),
        'passed': False
    }}))
"""
                with open(temp_path, 'w') as f:
                    f.write(test_code)
                
                process = subprocess.run(
                    ['python', temp_path],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                if process.stderr:
                    results.append({
                        'input': test_case['input'],
                        'error': process.stderr,
                        'passed': False
                    })
                    all_passed = False
                    continue
                
                try:
                    result = json.loads(process.stdout.strip())
                    results.append(result)
                    if not result['passed']:
                        all_passed = False
                except json.JSONDecodeError:
                    results.append({
                        'input': test_case['input'],
                        'error': 'Invalid output format',
                        'passed': False
                    })
                    all_passed = False
            
            # Add support for other languages here
            else:
                return jsonify({
                    'error': f'Language {language} not supported yet'
                }), 400
        
        if all_passed:
            # Update user progress
            username = session['user']
            if username not in USER_PROGRESS:
                USER_PROGRESS[username] = set()
            USER_PROGRESS[username].add(f"{category}/{problem_id}")
            
            return jsonify({
                'success': True,
                'message': 'All test cases passed!',
                'results': results
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Some test cases failed',
                'results': results
            })
            
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500
    finally:
        os.unlink(temp_path)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('auth'))
    return render_template('dashboard.html')

@app.route('/ar_bubblesort')
@app.route('/bubble-sort-visualizer')
def bubble_sort_visualizer():
    return render_template('bubble_sort_visualizer.html')
@app.route('/merge-sort-visualizer')
def merge_sort_visualizer():
    return render_template('merge_sort_visualizer.html')
@app.route('/selection-sort-visualizer')
def selection_sort_visualizer():
    return render_template('selection_sort_visualizer.html')
@app.route('/quick')
def quick_sort_visualizer():
    return render_template('quick_sort_visualizer.html')



@app.route('/linear-search-visualizer')
def linear_search_visualizer():
    return render_template('linear_search_visualizer.html')

@app.route('/binary-search-visualizer')
def binary_search_visualizer():
    return render_template('binary_search_visualizer.html')

@app.route('/backtracking-visualizer')
def backtracking_visualizer():
    return render_template('backtracking_visualizer.html')


@app.route('/generate-flowchart', methods=['POST'])
def generate_flowchart():
    try:
        code = request.json.get('code', '')
        language = request.json.get('language', 'python')
        
        if language not in LANGUAGE_CONFIGS:
            return jsonify({
                "error": f"Unsupported language: {language}",
                "flowchart": None
            }), 400

        # Create the prompt for Gemini to generate flowchart data
        prompt = f"""You are a code visualization expert. Analyze this {language} code and generate a detailed flowchart in Mermaid.js syntax that shows:
1. The main program flow
2. Function calls and their relationships
3. Decision points and loops
4. Input and output points
5. Variable transformations

Code to analyze:
{code}

Format your response as a JSON object with the following structure:
{{
    "flowchart": "A valid Mermaid.js flowchart syntax. Example:
    flowchart TD
        A[Start] --> B{{Is condition true?}}
        B -->|Yes| C[Process 1]
        B -->|No| D[Process 2]
        C --> E[End]
        D --> E",
    "explanation": "Detailed explanation of the code flow"
}}

The flowchart should:
1. Use proper Mermaid.js syntax
2. Start with 'flowchart TD' or 'flowchart LR'
3. Use proper node shapes ([] for processes, {{}} for decisions, () for inputs/outputs)
4. Use proper arrow syntax (--> for normal flow, -->|text| for labeled flows)
5. Be clear and easy to understand for beginners"""

        # Get response from Gemini
        response = model.generate_content(prompt)
        
        # Try to parse the response as JSON
        try:
            # Clean the response text to ensure it's valid JSON
            response_text = response.text.strip()
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.endswith('```'):
                response_text = response_text[:-3]
            response_text = response_text.strip()
            
            result = json.loads(response_text)
            
            # Validate the flowchart syntax
            if not result.get('flowchart', '').startswith('flowchart'):
                result['flowchart'] = 'flowchart TD\n    ' + result.get('flowchart', '')
            
        except (json.JSONDecodeError, ValueError) as e:
            result = {
                "error": "Could not generate flowchart data",
                "flowchart": None
            }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "flowchart": None
        }), 500

def format_feedback_html(feedback, improved_code):
    # Add headings and basic formatting
    html = "<div>"
    html += "<h3 style='margin-bottom:8px;'>Feedback</h3>"
    # Convert numbered lists and dashes to HTML lists
    lines = feedback.split('\n')
    in_ol = False
    in_ul = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('1.') or stripped.startswith('2.') or stripped.startswith('3.') or stripped.startswith('4.') or stripped.startswith('5.') or stripped.startswith('6.') or stripped.startswith('7.') or stripped.startswith('8.') or stripped.startswith('9.'):
            if not in_ol:
                html += "<ol style='margin-left:18px;'>"
                in_ol = True
            html += f"<li>{stripped[2:].strip()}</li>"
        elif stripped.startswith('-'):
            if not in_ul:
                html += "<ul style='margin-left:24px;'>"
                in_ul = True
            html += f"<li>{stripped[1:].strip()}</li>"
        else:
            if in_ol:
                html += "</ol>"
                in_ol = False
            if in_ul:
                html += "</ul>"
                in_ul = False
            if stripped:
                html += f"<div style='margin-bottom:6px;'>{stripped}</div>"
    if in_ol:
        html += "</ol>"
    if in_ul:
        html += "</ul>"
    html += "</div>"

    html += "<h3 style='margin-top:18px;margin-bottom:8px;'>Improved Code</h3>"
    html += "<pre style='background:#f6f8fa;padding:10px;border-radius:6px;overflow-x:auto;'><code>"
    html += improved_code
    html += "</code></pre>"
    return html

@app.route('/competitive-coding')
def competitive_coding():
    if 'user' not in session:
        return redirect(url_for('auth'))
    return render_template('competitive_coding.html', problems=PROBLEMS)

@app.route('/problem/<category>/<problem_id>')
def problem_page(category, problem_id):
    if 'user' not in session:
        return redirect(url_for('auth'))
    
    if category not in PROBLEMS or problem_id not in PROBLEMS[category]:
        flash('Problem not found', 'danger')
        return redirect(url_for('competitive_coding'))
    
    problem = PROBLEMS[category][problem_id]
    return render_template('problem.html', 
                         problem=problem,
                         category=category,
                         problem_id=problem_id)

if __name__ == '__main__':

    app.run(debug=True)
