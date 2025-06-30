# Import Flask and helper functions for rendering templates and handling requests
from flask import Flask, render_template_string, request

# Create a Flask application instance
app = Flask(__name__)

# Example of variable substitution and filter usage
# Testing: http://127.0.0.1:5002/hello/Lisa
@app.route('/hello/<name>')
def hello(name):
    # This template uses the 'upper' filter to display the name in uppercase
    template = """
    <h1>Hello, {{ name|upper }}!</h1>
    """
    return render_template_string(template, name=name)

# Example of control structures (if/else and for loop)
# Testing: http://127.0.0.1:5002/fruits
@app.route('/fruits')
def fruits():
    fruits = ['apple', 'banana', 'cherry']
    # This template loops through the fruits list and shows the count
    template = """
    <ul>
    {% for fruit in fruits %}
        <li>{{ fruit }}</li>
    {% endfor %}
    </ul>
    {% if fruits %}
        <p>You have {{ fruits|length }} fruits.</p>
    {% else %}
        <p>No fruits found.</p>
    {% endif %}
    """
    return render_template_string(template, fruits=fruits)

# Example of template inheritance using render_template_string
# Testing: http://127.0.0.1:5002/child
@app.route('/child')
def child():
    # Base template with a content block and a footer
    base = """
    {% block content %} {% endblock %}
    <footer>Footer goes here.</footer>
    """
    # Child template extends the base and overrides the content block
    child = """
    {% extends base %}
    {% block content %}
        <h2>This is the child template!</h2>
    {% endblock %}
    """
    return render_template_string(child, base=base)

# Example of macro usage
# Testing: http://127.0.0.1:5002/macro
@app.route('/macro')
def macro():
    # Macro defines a reusable code block for greeting
    template = """
    {% macro say_hello(name) %}
        <p>Hello, {{ name }}!</p>
    {% endmacro %}
    {{ say_hello('Alice') }}
    {{ say_hello('Bob') }}
    """
    return render_template_string(template)

# Example of including another template (simulated with a variable)
# Testing: http://127.0.0.1:5002/include
@app.route('/include')
def include():
    header = "<header><h1>Header Section</h1></header>"
    # This shows the syntax for including a template (not supported in render_template_string)
    template = """
    {% include 'header' %}
    <main>Main content goes here.</main>
    """
    return render_template_string(header + '<main>Main content goes here.</main>')

# Example of using a custom filter (reverse string)
# Testing: http://127.0.0.1:5002/reverse/hello
def reverse_filter(s):
    return s[::-1]
app.jinja_env.filters['reverse'] = reverse_filter

@app.route('/reverse/<word>')
def reverse(word):
    # This template uses the custom 'reverse' filter to reverse the string
    template = """
    <h1>Reversed: {{ word|reverse }}</h1>
    """
    return render_template_string(template, word=word)

# Example of math and logic in templates
# Testing: http://127.0.0.1:5002/math/5/3
@app.route('/math/<int:x>/<int:y>')
def math(x, y):
    # This template does math and logic directly in Jinja2
    template = """
    <p>{{ x }} + {{ y }} = {{ x + y }}</p>
    <p>{{ x }} > {{ y }}? {% if x > y %}Yes{% else %}No{% endif %}</p>
    """
    return render_template_string(template, x=x, y=y)

# Example of whitespace control
# Testing: http://127.0.0.1:5002/whitespace
@app.route('/whitespace')
def whitespace():
    # The -%} and {%- symbols trim whitespace in the output
    template = """
    <ul>
    {% for i in range(3) -%} // -}  {# This will not add extra whitespace #}
    {%- if i %} // -%  {# This will not add extra whitespace #}
        <li>{{ i }}</li>
    {%- endfor %}
    </ul>
    """
    return render_template_string(template)

# Example of escaping and safe filter
# Testing: http://127.0.0.1:5002/escape
@app.route('/escape')
def escape():
    html = '<b>This is bold</b>'
    # Shows the difference between escaped and safe HTML
    template = """
    <p>Escaped: {{ html }}</p>
    <p>Safe: {{ html|safe }}</p>
    """
    return render_template_string(template, html=html)

# Example of using the default filter
# Testing: http://127.0.0.1:5002/default
@app.route('/default')
def default():
    # Shows how to use the default filter for missing values
    template = """
    <p>Name: {{ name|default('Guest') }}</p>
    """
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
