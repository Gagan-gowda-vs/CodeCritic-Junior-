const learningContent = {
    python: [
        {
            title: "Basic Syntax & I/O",
            description: "Understanding Python's basic syntax and input/output operations",
            concepts: [
                {
                    title: "Input/Output Operations",
                    description: "Using input() and print() functions for basic I/O operations",
                    code: `# Basic input/output
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Multiple inputs
numbers = input("Enter numbers (space-separated): ").split()
numbers = list(map(int, numbers))
print(f"Sum: {sum(numbers)}")

# Type casting
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
print(f"Age: {age}, Height: {height}")`,
                    language: "python",
                    animation: "io-animation",
                    exercise: {
                        question: "Write a program that takes two numbers as input and prints their sum, difference, product, and quotient.",
                        solution: `num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")`
                    }
                }
            ]
        },
        {
            title: "Control Flow",
            description: "Understanding Python's control flow statements",
            concepts: [
                {
                    title: "Conditional Statements",
                    description: "Using if, elif, and else for decision making",
                    code: `# Basic if-else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Using elif
score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Your grade is {grade}")`,
                    language: "python",
                    animation: "conditional-animation",
                    exercise: {
                        question: "Write a program that checks if a number is positive, negative, or zero.",
                        solution: `num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")`
                    }
                },
                {
                    title: "Loops",
                    description: "Using for and while loops for iteration",
                    code: `# For loop
for i in range(5):
    print(i)  # Prints 0 to 4

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue  # Skip current iteration
    if i == 7:
        break     # Exit loop
    print(i)`,
                    language: "python",
                    animation: "loops-animation",
                    exercise: {
                        question: "Write a program that prints the Fibonacci sequence up to n terms.",
                        solution: `n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b`
                    }
                }
            ]
        },
        {
            title: "Data Types & Operations",
            description: "Working with Python's built-in data types",
            concepts: [
                {
                    title: "Numbers and Strings",
                    description: "Working with numeric and string data types",
                    code: `# Numbers
num1 = 10      # Integer
num2 = 3.14    # Float
result = num1 + num2

# Strings
text = "Hello, Python!"
print(text[0:5])  # Slicing
print(len(text))  # Length
print(text.upper())  # Methods
print(text.split(","))  # Split

# Boolean operations
is_valid = True
is_empty = False
result = is_valid and not is_empty`,
                    language: "python",
                    animation: "data-types-animation",
                    exercise: {
                        question: "Write a program that checks if a string is a palindrome.",
                        solution: `text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")`
                    }
                }
            ]
        },
        {
            title: "Data Structures",
            description: "Understanding Python's built-in data structures",
            concepts: [
                {
                    title: "Lists and Tuples",
                    description: "Working with lists (mutable) and tuples (immutable)",
                    code: `# Lists
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.pop()
numbers.sort()
print(numbers[::-1])  # Reverse

# Tuples
coordinates = (10, 20)
x, y = coordinates  # Unpacking
print(f"X: {x}, Y: {y}")`,
                    language: "python",
                    animation: "lists-tuples-animation",
                    exercise: {
                        question: "Write a program that finds the second largest number in a list.",
                        solution: `numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = sorted(numbers)
print(f"Second largest: {sorted_numbers[-2]}")`
                    }
                },
                {
                    title: "Dictionaries and Sets",
                    description: "Working with dictionaries and sets",
                    code: `# Dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person.get("name"))
print(person.keys())
print(person.values())

# Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))`,
                    language: "python",
                    animation: "dicts-sets-animation",
                    exercise: {
                        question: "Write a program that counts the frequency of each word in a sentence.",
                        solution: `sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)`
                    }
                }
            ]
        },
        {
            title: "Functions",
            description: "Creating and using functions in Python",
            concepts: [
                {
                    title: "Function Basics",
                    description: "Defining and using functions",
                    code: `# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default parameters
def calculate_area(length, width=1):
    return length * width

# Lambda function
square = lambda x: x ** 2

# Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)`,
                    language: "python",
                    animation: "functions-animation",
                    exercise: {
                        question: "Write a recursive function to calculate the nth Fibonacci number.",
                        solution: `def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)`
                    }
                }
            ]
        },
        {
            title: "Built-in Functions",
            description: "Using Python's built-in functions",
            concepts: [
                {
                    title: "Common Built-in Functions",
                    description: "Using Python's built-in functions for common operations",
                    code: `# Basic functions
numbers = [5, 2, 8, 1, 9]
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

# Enumerate and zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for i, name in enumerate(names):
    print(f"{i}: {name}")

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")`,
                    language: "python",
                    animation: "builtin-functions-animation",
                    exercise: {
                        question: "Write a program that finds the most common element in a list.",
                        solution: `from collections import Counter
numbers = [1, 2, 2, 3, 3, 3, 4]
counter = Counter(numbers)
print(counter.most_common(1)[0][0])`
                    }
                }
            ]
        },
        {
            title: "Standard Libraries",
            description: "Using Python's standard libraries",
            concepts: [
                {
                    title: "Common Libraries",
                    description: "Using Python's standard libraries for various operations",
                    code: `# Math library
import math
print(math.sqrt(16))
print(math.gcd(12, 18))
print(math.factorial(5))

# itertools
from itertools import combinations, permutations
numbers = [1, 2, 3]
print(list(combinations(numbers, 2)))
print(list(permutations(numbers)))

# collections
from collections import Counter, defaultdict
words = ["apple", "banana", "apple", "orange"]
counter = Counter(words)
print(counter)`,
                    language: "python",
                    animation: "libraries-animation",
                    exercise: {
                        question: "Write a program that finds all prime numbers up to n using the Sieve of Eratosthenes.",
                        solution: `def sieve(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]`
                    }
                }
            ]
        },
        {
            title: "Algorithmic Concepts",
            description: "Implementing common algorithms in Python",
            concepts: [
                {
                    title: "Searching and Sorting",
                    description: "Implementing common searching and sorting algorithms",
                    code: `# Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Custom sorting
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 90},
    {"name": "Charlie", "grade": 75}
]
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)`,
                    language: "python",
                    animation: "algorithms-animation",
                    exercise: {
                        question: "Implement the bubble sort algorithm.",
                        solution: `def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr`
                    }
                }
            ]
        },
        {
            title: "String Algorithms",
            description: "Working with string manipulation algorithms",
            concepts: [
                {
                    title: "String Operations",
                    description: "Implementing common string algorithms",
                    code: `# Palindrome check
def is_palindrome(s):
    return s == s[::-1]

# Anagram check
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Character frequency
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq`,
                    language: "python",
                    animation: "string-algorithms-animation",
                    exercise: {
                        question: "Write a program that finds the longest substring without repeating characters.",
                        solution: `def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length`
                    }
                }
            ]
        },
        {
            title: "Object-Oriented Programming",
            description: "Understanding OOP concepts in Python",
            concepts: [
                {
                    title: "Classes and Objects",
                    description: "Creating and using classes and objects",
                    code: `class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name}"
    
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! You are now {self.age} years old"

# Creating objects
person = Person("Alice", 25)
print(person.greet())
print(person.have_birthday())`,
                    language: "python",
                    animation: "classes-animation",
                    exercise: {
                        question: "Create a BankAccount class with methods for deposit, withdraw, and check balance.",
                        solution: `class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    
    def check_balance(self):
        return self.balance`
                    }
                }
            ]
        },
        {
            title: "Exception Handling",
            description: "Handling errors and exceptions in Python",
            concepts: [
                {
                    title: "Try-Except Blocks",
                    description: "Using try-except blocks for error handling",
                    code: `# Basic try-except
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")`,
                    language: "python",
                    animation: "exception-animation",
                    exercise: {
                        question: "Write a program that handles file operations with proper exception handling.",
                        solution: `try:
    with open("file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"An error occurred: {e}")`
                    }
                }
            ]
        }
    ],
    javascript: [
        {
            title: "JavaScript Basics",
            description: "Master the fundamental concepts of JavaScript programming",
            concepts: [
                {
                    title: "Console Output and Variables",
                    description: "Learn how to output messages to the console and work with different types of variables in JavaScript.",
                    code: `// Console output
console.log("Hello, World!");

// Variables
let name = "John";      // Mutable variable
const age = 25;         // Immutable variable
var city = "New York";  // Legacy variable declaration

// Data types
let number = 42;        // Number
let text = "Hello";     // String
let isTrue = true;      // Boolean
let nothing = null;     // Null
let notDefined;         // Undefined

// Type conversion
let str = "123";
let num = Number(str);  // String to Number
let strNum = String(42); // Number to String
let int = parseInt("42.7"); // String to Integer`,
                    language: "javascript",
                    animation: "js-basics-animation",
                    exercise: {
                        question: "Create variables to store your name, age, and favorite programming language. Then print them using console.log().",
                        solution: `const name = "Alice";
const age = 30;
const language = "JavaScript";

console.log(\`My name is \${name}, I am \${age} years old, and my favorite programming language is \${language}.\`);`
                    }
                }
            ]
        },
        {
            title: "Operators and Control Flow",
            description: "Understand how to use different types of operators and control the flow of your program",
            concepts: [
                {
                    title: "Operators",
                    description: "Learn about different types of operators in JavaScript",
                    code: `// Arithmetic operators
let sum = 5 + 3;    // Addition
let diff = 5 - 3;   // Subtraction
let product = 5 * 3; // Multiplication
let quotient = 5 / 3; // Division
let remainder = 5 % 3; // Modulus

// Assignment operators
let x = 5;
x += 3;  // x = x + 3
x -= 2;  // x = x - 2
x *= 2;  // x = x * 2
x /= 2;  // x = x / 2

// Comparison operators
let isEqual = 5 === 5;    // Strict equality
let isNotEqual = 5 !== 3; // Strict inequality
let isGreater = 5 > 3;    // Greater than
let isLess = 3 < 5;       // Less than

// Logical operators
let and = true && false;  // AND
let or = true || false;   // OR
let not = !true;          // NOT`,
                    language: "javascript",
                    animation: "js-operators-animation",
                    exercise: {
                        question: "Write a program that checks if a number is even and positive using logical operators.",
                        solution: `function checkNumber(num) {
    return num > 0 && num % 2 === 0;
}

console.log(checkNumber(4));  // true
console.log(checkNumber(-2)); // false
console.log(checkNumber(3));  // false`
                    }
                },
                {
                    title: "Control Flow",
                    description: "Learn how to control the flow of your program",
                    code: `// If-else statement
let age = 18;
if (age >= 18) {
    console.log("You are an adult");
} else {
    console.log("You are a minor");
}

// Else-if statement
let score = 85;
if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 80) {
    console.log("Grade: B");
} else if (score >= 70) {
    console.log("Grade: C");
} else {
    console.log("Grade: F");
}

// Switch statement
let day = "Monday";
switch(day) {
    case "Monday":
        console.log("Start of the week");
        break;
    case "Friday":
        console.log("End of the week");
        break;
    default:
        console.log("Mid-week");
}

// Ternary operator
let isAdult = age >= 18 ? "Adult" : "Minor";
console.log(isAdult);`,
                    language: "javascript",
                    animation: "js-control-flow-animation",
                    exercise: {
                        question: "Write a program that determines the season based on the month using a switch statement.",
                        solution: `function getSeason(month) {
    switch(month) {
        case 12:
        case 1:
        case 2:
            return "Winter";
        case 3:
        case 4:
        case 5:
            return "Spring";
        case 6:
        case 7:
        case 8:
            return "Summer";
        case 9:
        case 10:
        case 11:
            return "Autumn";
        default:
            return "Invalid month";
    }
}

console.log(getSeason(3));  // Spring
console.log(getSeason(8));  // Summer`
                    }
                }
            ]
        },
        {
            title: "Loops and Iteration",
            description: "Learn different ways to repeat code execution in JavaScript",
            concepts: [
                {
                    title: "Basic Loops",
                    description: "Understand different types of loops in JavaScript",
                    code: `// For loop
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// While loop
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}

// Do-while loop
let x = 0;
do {
    console.log(x);
    x++;
} while (x < 5);

// For...of loop (arrays)
const fruits = ["apple", "banana", "orange"];
for (const fruit of fruits) {
    console.log(fruit);
}

// For...in loop (objects)
const person = { name: "John", age: 30 };
for (const key in person) {
    console.log(\`\${key}: \${person[key]}\`);
}

// Break and continue
for (let i = 0; i < 10; i++) {
    if (i === 5) break;     // Exit loop
    if (i % 2 === 0) continue; // Skip even numbers
    console.log(i);
}`,
                    language: "javascript",
                    animation: "js-loops-animation",
                    exercise: {
                        question: "Write a program that finds the first even number in an array using a loop.",
                        solution: `function findFirstEven(numbers) {
    for (let num of numbers) {
        if (num % 2 === 0) {
            return num;
        }
    }
    return null;
}

const numbers = [1, 3, 5, 2, 4, 6];
console.log(findFirstEven(numbers)); // 2`
                    }
                }
            ]
        },
        {
            title: "Functions",
            description: "Learn how to create and use functions in JavaScript",
            concepts: [
                {
                    title: "Function Basics",
                    description: "Understand different ways to create functions in JavaScript",
                    code: `// Function declaration
function greet(name) {
    return "Hello, " + name + "!";
}

// Function expression
const greet2 = function(name) {
    return "Hello, " + name + "!";
};

// Arrow function
const greet3 = (name) => {
    return "Hello, " + name + "!";
};

// Arrow function with implicit return
const greet4 = name => "Hello, " + name + "!";

// Default parameters
function greet5(name = "Guest") {
    return "Hello, " + name + "!";
}

// Recursion
function factorial(n) {
    if (n === 0 || n === 1) return 1;
    return n * factorial(n - 1);
}

// Callbacks
function processUserInput(callback) {
    const name = "John";
    callback(name);
}

processUserInput(greet);`,
                    language: "javascript",
                    animation: "js-functions-animation",
                    exercise: {
                        question: "Write a recursive function to calculate the nth Fibonacci number.",
                        solution: `function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(5));  // 5
console.log(fibonacci(10)); // 55`
                    }
                }
            ]
        },
        {
            title: "Arrays and Array Methods",
            description: "Learn how to work with arrays and use powerful array methods",
            concepts: [
                {
                    title: "Array Basics",
                    description: "Understand array operations and methods",
                    code: `// Array declaration
const numbers = [1, 2, 3, 4, 5];

// Array methods
numbers.push(6);        // Add to end
numbers.pop();          // Remove from end
numbers.unshift(0);     // Add to beginning
numbers.shift();        // Remove from beginning

// Searching
const index = numbers.indexOf(3);  // Find index
const exists = numbers.includes(4); // Check existence

// Slicing
const slice1 = numbers.slice(1, 3);  // [2, 3]
const slice2 = numbers.splice(1, 2); // Remove elements

// Sorting
numbers.sort((a, b) => a - b);  // Numeric sort

// Higher-order functions
const doubled = numbers.map(x => x * 2);
const evens = numbers.filter(x => x % 2 === 0);
const sum = numbers.reduce((acc, curr) => acc + curr, 0);
numbers.forEach(x => console.log(x));`,
                    language: "javascript",
                    animation: "js-arrays-animation",
                    exercise: {
                        question: "Write a function that takes an array of numbers and returns a new array with only the even numbers, doubled.",
                        solution: `function doubleEvens(numbers) {
    return numbers
        .filter(num => num % 2 === 0)
        .map(num => num * 2);
}

const result = doubleEvens([1, 2, 3, 4, 5, 6]);
console.log(result); // [4, 8, 12]`
                    }
                }
            ]
        },
        {
            title: "Strings and String Methods",
            description: "Learn how to work with strings in JavaScript",
            concepts: [
                {
                    title: "String Operations",
                    description: "Understand string manipulation and methods",
                    code: `const str = "Hello, World!";

// String properties and access
console.log(str.length);        // Length
console.log(str[0]);           // First character
console.log(str.charAt(0));    // First character

// String methods
const words = str.split(", ");  // Split into array
const joined = words.join(" "); // Join array elements

const sub = str.slice(0, 5);    // "Hello"
const sub2 = str.substring(0, 5); // "Hello"

const index = str.indexOf("World"); // Find position
const exists = str.includes("Hello"); // Check existence

const newStr = str.replace("World", "JavaScript"); // Replace

// Template literals
const name = "Alice";
const age = 25;
const message = \`Hello, \${name}! You are \${age} years old.\`;`,
                    language: "javascript",
                    animation: "js-strings-animation",
                    exercise: {
                        question: "Write a function that checks if a string is a palindrome.",
                        solution: `function isPalindrome(str) {
    const cleanStr = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    return cleanStr === cleanStr.split('').reverse().join('');
}

console.log(isPalindrome("A man, a plan, a canal: Panama")); // true
console.log(isPalindrome("race a car")); // false`
                    }
                }
            ]
        },
        {
            title: "Objects and Object Methods",
            description: "Learn how to create and manipulate objects in JavaScript",
            concepts: [
                {
                    title: "Object Basics",
                    description: "Understand object creation and manipulation",
                    code: `// Object literal
const person = {
    name: "John",
    age: 30,
    city: "New York",
    greet: function() {
        return "Hello, " + this.name;
    }
};

// Property access
console.log(person.name);        // Dot notation
console.log(person["age"]);      // Bracket notation

// Iteration
for (const key in person) {
    console.log(key + ": " + person[key]);
}

const keys = Object.keys(person);    // Get keys
const values = Object.values(person); // Get values

// Nested objects
const student = {
    name: "Alice",
    grades: {
        math: 90,
        science: 85,
        history: 88
    }
};

// hasOwnProperty
console.log(person.hasOwnProperty("name")); // true

// Object destructuring
const { name, age } = person;
console.log(name, age);`,
                    language: "javascript",
                    animation: "js-objects-animation",
                    exercise: {
                        question: "Create an object representing a book with properties for title, author, and year. Add a method to get the book's age.",
                        solution: `const book = {
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    year: 1925,
    getAge: function() {
        const currentYear = new Date().getFullYear();
        return currentYear - this.year;
    }
};

console.log(book.getAge()); // Returns the age of the book`
                    }
                }
            ]
        },
        {
            title: "Sets and Maps",
            description: "Learn how to use Sets and Maps for efficient data storage",
            concepts: [
                {
                    title: "Sets and Maps",
                    description: "Understand Set and Map data structures",
                    code: `// Set - unique values
const uniqueNumbers = new Set();
uniqueNumbers.add(1);
uniqueNumbers.add(2);
uniqueNumbers.add(1); // Won't add duplicate
console.log(uniqueNumbers.has(1)); // true
uniqueNumbers.delete(1);

// Map - key-value pairs
const userMap = new Map();
userMap.set("name", "John");
userMap.set("age", 30);
console.log(userMap.get("name")); // "John"
console.log(userMap.has("age"));  // true
userMap.delete("age");

// Converting between data structures
const arr = [1, 2, 2, 3, 3, 4];
const uniqueSet = new Set(arr);
const uniqueArr = Array.from(uniqueSet);`,
                    language: "javascript",
                    animation: "js-sets-maps-animation",
                    exercise: {
                        question: "Write a function that takes an array of numbers and returns a Set containing only the unique numbers.",
                        solution: `function getUniqueNumbers(numbers) {
    return new Set(numbers);
}

const numbers = [1, 2, 2, 3, 4, 4, 5];
const unique = getUniqueNumbers(numbers);
console.log([...unique]); // [1, 2, 3, 4, 5]`
                    }
                }
            ]
        },
        {
            title: "Math and Number Utilities",
            description: "Learn how to use JavaScript's Math object and number utilities",
            concepts: [
                {
                    title: "Math Operations",
                    description: "Understand mathematical operations and utilities",
                    code: `// Math methods
console.log(Math.floor(3.7));   // 3
console.log(Math.ceil(3.2));    // 4
console.log(Math.round(3.5));   // 4
console.log(Math.max(1, 2, 3)); // 3
console.log(Math.min(1, 2, 3)); // 1
console.log(Math.pow(2, 3));    // 8
console.log(Math.sqrt(16));     // 4

// Number utilities
console.log(Number.isInteger(5));    // true
console.log(parseInt("42"));         // 42
console.log(parseFloat("3.14"));     // 3.14

// Random numbers
const random = Math.random();        // 0 to 1
const randomInt = Math.floor(Math.random() * 10); // 0 to 9`,
                    language: "javascript",
                    animation: "js-math-animation",
                    exercise: {
                        question: "Write a function that generates a random integer between two given numbers (inclusive).",
                        solution: `function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(randomInt(1, 10)); // Random number between 1 and 10`
                    }
                }
            ]
        },
        {
            title: "Important Built-ins for CP",
            description: "Learn essential JavaScript built-in functions for competitive programming",
            concepts: [
                {
                    title: "Built-in Functions",
                    description: "Understand important built-in functions for CP",
                    code: `// Array creation
const arr = Array.from({length: 5}, (_, i) => i + 1);
console.log(Array.isArray(arr)); // true

// JSON utilities
const obj = {a: 1, b: 2};
const str = JSON.stringify(obj);
const parsed = JSON.parse(str);

// Array initialization
const filled = new Array(5).fill(0);

// Spread operator
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const merged = [...arr1, ...arr2];

// Object cloning
const original = {a: 1, b: 2};
const clone = {...original};

// Optional chaining
const user = {
    name: "John",
    address: {
        city: "New York"
    }
};
console.log(user?.address?.city); // "New York"
console.log(user?.phone?.number); // undefined`,
                    language: "javascript",
                    animation: "js-builtins-animation",
                    exercise: {
                        question: "Write a function that deep clones an object using JSON methods.",
                        solution: `function deepClone(obj) {
    return JSON.parse(JSON.stringify(obj));
}

const original = {a: 1, b: {c: 2}};
const clone = deepClone(original);
console.log(clone); // {a: 1, b: {c: 2}}`
                    }
                }
            ]
        },
        {
            title: "Recursion and Backtracking",
            description: "Learn how to implement recursive algorithms and backtracking",
            concepts: [
                {
                    title: "Recursion",
                    description: "Understand recursive function structure and implementation",
                    code: `// Basic recursion
function factorial(n) {
    if (n === 0 || n === 1) return 1;
    return n * factorial(n - 1);
}

// Recursive sum of digits
function sumDigits(n) {
    if (n < 10) return n;
    return (n % 10) + sumDigits(Math.floor(n / 10));
}

// Backtracking example: Generate all permutations
function generatePermutations(arr) {
    const result = [];
    
    function backtrack(current, remaining) {
        if (remaining.length === 0) {
            result.push([...current]);
            return;
        }
        
        for (let i = 0; i < remaining.length; i++) {
            current.push(remaining[i]);
            const newRemaining = remaining.filter((_, index) => index !== i);
            backtrack(current, newRemaining);
            current.pop();
        }
    }
    
    backtrack([], arr);
    return result;
}`,
                    language: "javascript",
                    animation: "js-recursion-animation",
                    exercise: {
                        question: "Write a recursive function to find the greatest common divisor (GCD) of two numbers.",
                        solution: `function gcd(a, b) {
    if (b === 0) return a;
    return gcd(b, a % b);
}

console.log(gcd(48, 18)); // 6
console.log(gcd(60, 48)); // 12`
                    }
                }
            ]
        },
        {
            title: "Searching and Sorting",
            description: "Learn common searching and sorting algorithms",
            concepts: [
                {
                    title: "Searching Algorithms",
                    description: "Understand linear and binary search",
                    code: `// Linear search
function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) return i;
    }
    return -1;
}

// Binary search
function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (arr[mid] === target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    
    return -1;
}

// Custom sorting
const numbers = [5, 2, 8, 1, 9];
numbers.sort((a, b) => a - b); // Ascending
numbers.sort((a, b) => b - a); // Descending`,
                    language: "javascript",
                    animation: "js-search-sort-animation",
                    exercise: {
                        question: "Implement the bubble sort algorithm.",
                        solution: `function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    return arr;
}

const numbers = [5, 2, 8, 1, 9];
console.log(bubbleSort(numbers)); // [1, 2, 5, 8, 9]`
                    }
                }
            ]
        },
        {
            title: "Time and Space Complexity",
            description: "Understand time and space complexity in JavaScript",
            concepts: [
                {
                    title: "Complexity Analysis",
                    description: "Learn how to analyze algorithm complexity",
                    code: `// O(n) - Linear time
function linearTime(n) {
    for (let i = 0; i < n; i++) {
        console.log(i);
    }
}

// O(log n) - Logarithmic time
function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    
    return -1;
}

// O(n^2) - Quadratic time
function quadraticTime(n) {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            console.log(i, j);
        }
    }
}

// Space complexity examples
function constantSpace(n) {  // O(1)
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += i;
    }
    return sum;
}

function linearSpace(n) {    // O(n)
    const arr = [];
    for (let i = 0; i < n; i++) {
        arr.push(i);
    }
    return arr;
}`,
                    language: "javascript",
                    animation: "js-complexity-animation",
                    exercise: {
                        question: "Analyze the time and space complexity of a function that finds duplicates in an array.",
                        solution: `function findDuplicates(arr) {
    const seen = new Set();
    const duplicates = new Set();
    
    for (const num of arr) {
        if (seen.has(num)) {
            duplicates.add(num);
        } else {
            seen.add(num);
        }
    }
    
    return Array.from(duplicates);
}

// Time Complexity: O(n)
// Space Complexity: O(n)`
                    }
                }
            ]
        }
    ],
    java: [
        {
            title: "Advanced Java",
            description: "Explore advanced Java concepts and patterns",
            concepts: [
                {
                    title: "Generics",
                    description: "Type-safe collections and methods using generics.",
                    code: `public class Box<T> {
    private T content;
    
    public void setContent(T content) {
        this.content = content;
    }
    
    public T getContent() {
        return content;
    }
}

Box<String> stringBox = new Box<>();
stringBox.setContent("Hello");`,
                    language: "java",
                    animation: "generics-animation",
                    exercise: {
                        question: "Create a generic method that finds the maximum element in an array.",
                        solution: `public static <T extends Comparable<T>> T findMax(T[] array) {
    if (array == null || array.length == 0) {
        throw new IllegalArgumentException("Array is empty or null");
    }
    T max = array[0];
    for (T element : array) {
        if (element.compareTo(max) > 0) {
            max = element;
        }
    }
    return max;
}`
                    }
                },
                {
                    title: "Streams API",
                    description: "Functional-style operations on collections using streams.",
                    code: `List<String> names = Arrays.asList("John", "Jane", "Adam", "Eve");
List<String> filteredNames = names.stream()
    .filter(name -> name.startsWith("J"))
    .map(String::toUpperCase)
    .collect(Collectors.toList());`,
                    language: "java",
                    animation: "streams-animation",
                    exercise: {
                        question: "Create a stream pipeline that calculates the average of even numbers.",
                        solution: `public static double averageOfEvens(List<Integer> numbers) {
    return numbers.stream()
        .filter(n -> n % 2 == 0)
        .mapToInt(Integer::intValue)
        .average()
        .orElse(0.0);
}`
                    }
                }
            ]
        },
        {
            title: "Java Basics",
            description: "Start your journey with Java programming",
            concepts: [
                {
                    title: "Introduction to Java",
                    explanation: "Java is a class-based, object-oriented programming language designed to be platform-independent.",
                    code: `// Java is case-sensitive and requires semicolons
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}`,
                    animation: "java-intro-animation"
                },
                {
                    title: "Classes and Objects",
                    explanation: "Java is an object-oriented programming language where everything is an object.",
                    code: `// Class definition
public class Person {
    private String name;
    private int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method
    public void greet() {
        System.out.println("Hello, " + name);
    }
}`,
                    animation: "java-classes-animation"
                }
            ]
        }
    ]
};

// Function to generate HTML for a concept
function generateConceptHTML(concept) {
    return `
        <div class="concept-card fade-in">
            <h3>${concept.title}</h3>
            <p>${concept.explanation}</p>
            <div class="code-snippet">
                <pre><code class="language-${getLanguageClass(concept.code)}">${concept.code}</code></pre>
            </div>
            <div class="animation-container" id="${concept.animation}">
                <!-- Animation will be loaded here -->
            </div>
        </div>
    `;
}

// Function to get language class for syntax highlighting
function getLanguageClass(code) {
    if (code.includes("System.out.println")) return "java";
    if (code.includes("console.log")) return "javascript";
    return "python";
}

// Function to show language content
function showLanguageContent(language) {
    // Update active state of language buttons
    document.querySelectorAll('.list-group-item').forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('onclick').includes(language)) {
            item.classList.add('active');
        }
    });

    const contentDiv = document.getElementById('language-content');
    const languageContent = learningContent[language];
    
    if (!languageContent) {
        contentDiv.innerHTML = `
            <div class="alert alert-info">
                <h4>Coming Soon!</h4>
                <p>We're working hard to bring you comprehensive tutorials for ${language.toUpperCase()}. Check back soon!</p>
            </div>
        `;
        return;
    }

    let html = '';
    languageContent.forEach(section => {
        html += `
            <div class="section-card fade-in">
                <h2>${section.title}</h2>
                <p class="section-description">${section.description}</p>
                <div class="concepts-container">
                    ${section.concepts.map(concept => `
                        <div class="concept-card">
                            <h3>${concept.title}</h3>
                            <p>${concept.description}</p>
                            <div class="code-snippet">
                                <pre><code class="language-${concept.language || language}">${concept.code}</code></pre>
                            </div>
                            <div class="animation-container" id="${concept.animation}">
                                <!-- Animation will be loaded here -->
                            </div>
                            ${concept.exercise ? `
                                <div class="exercise-container">
                                    <h4>Exercise</h4>
                                    <p>${concept.exercise.question}</p>
                                    <button class="show-solution" onclick="this.nextElementSibling.style.display='block'">Show Solution</button>
                                    <div class="solution" style="display: none;">
                                        <pre><code class="language-${concept.language || language}">${concept.exercise.solution}</code></pre>
                                    </div>
                                </div>
                            ` : ''}
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    });

    contentDiv.innerHTML = html;
    contentDiv.classList.add('active');
    hljs.highlightAll();
    loadAnimations(language);
}

// Function to load animations
function loadAnimations(language) {
    // This function will be implemented to load and play animations
    // based on the language and concept being displayed
    console.log(`Loading animations for ${language}`);
}

// Show Python content by default
document.addEventListener('DOMContentLoaded', function() {
    showLanguageContent('python');
}); 