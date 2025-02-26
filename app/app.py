import streamlit as st

st.title("Growth Mindset Challenge: Web App with Streamlit")

# 📌 Sir Zia Khan's Image
st.image("C:/Users/HARD BANK/Pictures/pic/zia.jpg", width=550, caption="Sir Zia Khan")

# 📌 App Title
st.title(" Python Learning App 🚀")

# 📌 Categories for Learning
category = st.sidebar.radio("📂 Select Category:", ["Basic", "Intermediate", "Advanced", "Expert"])

# 📌 Topics Dictionary
topics = {
    "Basic": {
        "Python Introduction": ["What is Python?", "Installing Python", "Hello World Program"],
        "Variables & Data Types": ["Variables", "Strings", "Integers & Floats", "Booleans", "Type Conversion"],
        "Operators & Expressions": ["Arithmetic Operators", "Comparison Operators", "Logical Operators"],
        "Control Flow": ["If Statements", "For Loops", "While Loops"],
        "Functions": ["Defining Functions", "Function Parameters", "Return Statement"],
        "Lists": ["Creating Lists", "List Methods", "List Comprehension"],
        "Dictionaries": ["Creating Dictionaries", "Accessing Values", "Dictionary Methods"],
        "Input & Output": ["Getting User Input", "Printing Output", "File Handling Basics"],
    },
    "Intermediate": {
        "OOP Concepts": ["Classes & Objects", "Methods", "Inheritance"],
        "Exception Handling": ["Try-Except Blocks", "Custom Exceptions"],
    },
    "Advanced": {
        "Web Scraping": ["Using requests", "BeautifulSoup Basics"],
        "Databases": ["SQLite in Python", "Connecting to MySQL"],
    },
    "Expert": {
        "Web Development": ["Flask Basics", "Django Basics"],
        "Machine Learning": ["NumPy & Pandas", "Scikit-Learn"],
    }
}

# 📌 Sidebar Topic Selection
selected_topic = st.sidebar.selectbox("📚 Select a Topic:", list(topics[category].keys()))

# 📌 Subtopics Dropdown
selected_subtopic = st.sidebar.selectbox("📌 Select a Subtopic:", topics[category][selected_topic])

# 📌 Function to Show Content
def show_content(category, topic, subtopic):
    st.subheader(f"📖 {topic} - {subtopic}")

    # ✅ Basic Category
    if category == "Basic":
        if topic == "Python Introduction":
            if subtopic == "What is Python?":
                st.write("Python is a high-level, interpreted programming language.")
            elif subtopic == "Installing Python":
                st.write("Download Python from [python.org](https://www.python.org/) and install it.")
                st.code("python --version", language="bash")
            elif subtopic == "Hello World Program":
                st.code('print("Hello, World!")', language="python")

        elif topic == "Variables & Data Types":
            if subtopic == "Variables":
                st.write("Variables store values in memory.")
                st.code('x = 10\ny = "Hello"\nprint(x, y)', language="python")
            elif subtopic == "Strings":
                st.write("Strings are sequences of characters.")
                st.code('my_string = "Hello, World!"\nprint(my_string)', language="python")
            elif subtopic == "Integers & Floats":
                st.write("Integers are whole numbers, floats are decimal numbers.")
                st.code('a = 5\nb = 3.14\nprint(a, b)', language="python")
            elif subtopic == "Booleans":
                st.write("Booleans can be True or False.")
                st.code('is_active = True\nprint(is_active)', language="python")
            elif subtopic == "Type Conversion":
                st.write("Type conversion allows you to change the data type of a variable.")
                st.code('num_str = "10"\nnum_int = int(num_str)\nprint(num_int)', language="python")

        elif topic == "Operators & Expressions":
            st.write("Operators perform operations on variables and values.")
            st.code('a = 10\nb = 5\nprint(a + b, a - b, a * b, a / b)', language="python")

        elif topic == "Control Flow":
            if subtopic == "If Statements":
                st.write("If statements are used for conditional execution.")
                st.code('if a > b:\n    print("a is greater than b")', language="python")
            elif subtopic == "For Loops":
                st.write("For loops iterate over a sequence.")
                st.code('for i in range(5):\n    print(i)', language="python")
            elif subtopic == "While Loops":
                st.write("While loops execute as long as a condition is true.")
                st.code('while a < 15:\n    a += 1\n    print(a)', language="python")

        elif topic == "Functions":
            if subtopic == "Defining Functions":
                st.write("Functions are defined using the `def` keyword.")
                st.code('def greet(name):\n    return f"Hello, {name}"\nprint(greet("Alice"))', language="python")
            elif subtopic == "Function Parameters":
                st.write("Functions can accept parameters.")
                st.code('def add(x, y):\n    return x + y\nprint(add(5, 3))', language="python")
            elif subtopic == "Return Statement":
                st.write("Functions can return values using the `return` keyword.")
                st.code('def square(x):\n    return x * x\nprint(square(4))', language="python")

        elif topic == "Lists":
            if subtopic == "Creating Lists":
                st.write("Lists are created using square brackets.")
                st.code('my_list = [1, 2, 3, 4]\nprint(my_list)', language="python")
            elif subtopic == "List Methods":
                st.write("Lists have various methods like append and remove.")
                st.code('my_list.append(5)\nprint(my_list)', language="python")
            elif subtopic == "List Comprehension":
                st.write("List comprehension provides a concise way to create lists.")
                st.code('squares = [x**2 for x in range(10)]\nprint(squares)', language="python")

        elif topic == "Dictionaries":
            if subtopic == "Creating Dictionaries":
                st.write("Dictionaries are created using curly braces.")
                st.code('my_dict = {"name": "Alice", "age": 25}\nprint(my_dict)', language="python")
            elif subtopic == "Accessing Values":
                st.write("Values in a dictionary can be accessed using keys.")
                st.code('print(my_dict["name"])', language="python")
            elif subtopic == "Dictionary Methods":
                st.write("Dictionaries have methods like keys and values.")
                st.code('print(my_dict.keys())\nprint(my_dict.values())', language="python")

        elif topic == "Input & Output":
            if subtopic == "Getting User Input":
                st.write("You can get input from the user using the input() function.")
                st.code('user_input = input("Enter your name: ")\nprint(user_input)', language="python")
            elif subtopic == "Printing Output":
                st.write("You can print output to the console using the print() function.")
                st.code('print("Hello, World!")', language="python")
            elif subtopic == "File Handling Basics":
                st.write("Basic file handling involves reading from and writing to files.")
                st.code('with open("file.txt", "w") as f:\n    f.write("Hello, World!")', language="python")

    # ✅ Intermediate Category
    elif category == "Intermediate":
        if topic == "OOP Concepts":
            if subtopic == "Classes & Objects":
                st.write("Python supports object-oriented programming (OOP).")
                st.code("class Person:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        print(f'Hello, {self.name}')\n\np = Person('Alice')\np.greet()", language="python")
            elif subtopic == "Methods":
                st.write("Methods are functions defined within a class.")
                st.code("class Dog:\n    def bark(self):\n        print('Woof!')\n\nmy_dog = Dog()\nmy_dog.bark()", language="python")
            elif subtopic == "Inheritance":
                st.write("Inheritance allows one class to inherit properties from another.")
                st.code("class Animal:\n    def speak(self):\n        print('Animal sound')\n\nclass Dog(Animal):\n    def speak(self):\n        print('Bark')\n\nmy_dog = Dog()\nmy_dog.speak()", language="python")

    # ✅ Advanced Category
    elif category == "Advanced":
        if topic == "Web Scraping":
            if subtopic == "Using requests":
                st.write("We use `requests` to fetch web data.")
                st.code("import requests\nresponse = requests.get('https://example.com')\nprint(response.text)", language="python")
            elif subtopic == "BeautifulSoup Basics":
                st.write("BeautifulSoup is used for parsing HTML and XML documents.")
                st.code("from bs4 import BeautifulSoup\nsoup = BeautifulSoup('<html></html>', 'html.parser')\nprint(soup.prettify())", language="python")

    # ✅ Expert Category
    elif category == "Expert":
        if topic == "Web Development":
            if subtopic == "Flask Basics":
                st.write("Flask is a micro web framework for Python.")
                st.code("from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef home():\n    return 'Hello, Flask!'\napp.run(debug=True)", language="python")
            elif subtopic == "Django Basics":
                st.write("Django is a high-level Python web framework.")
                st.code("from django.shortcuts import render\n\ndef index(request):\n    return render(request, 'index.html')", language="python")

    else:
        st.write("❓ No content available.")

# 📌 Show the selected topic's content
show_content(category, selected_topic, selected_subtopic)
