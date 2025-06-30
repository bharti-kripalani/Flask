from flask import Flask, render_template_string

app = Flask(__name__)

# 1. upper filter
# Testing: http://127.0.0.1:5003/upper/hello
@app.route('/upper/<word>')
def upper(word):
    template = "<p>Upper: {{ çword|upper }}</p>"
    return render_template_string(template, word=word)

# 2. lower filter
# Testing: http://127.0.0.1:5003/lower/HELLO
@app.route('/lower/<word>')
def lower(word):
    template = "<p>Lower: {{ word|lower }}</p>"
    return render_template_string(template, word=word)

# 3. title filter
# Testing: http://127.0.0.1:5003/title/hello%20world
@app.route('/title/<text>')
def title(text):
    template = "<p>Title: {{ text|title }}</p>"
    return render_template_string(template, text=text)

# 4. capitalize filter
# Testing: http://127.0.0.1:5003/capitalize/hello
@app.route('/capitalize/<word>')
def capitalize(word):
    template = "<p>Capitalize: {{ word|capitalize }}</p>"
    return render_template_string(template, word=word)

# 5. length filter
# Testing: http://127.0.0.1:5003/length
@app.route('/length')
def length():
    items = ['a', 'b', 'c', 'd']
    template = "<p>Length: {{ items|length }}</p>"
    return render_template_string(template, items=items)

# 6. join filter
# Testing: http://127.0.0.1:5003/join
@app.route('/join')
def join():
    items = ['a', 'b', 'c']
    template = "<p>Join: {{ items|join(':') }}</p>"
    # The join filter concatenates items with a separator
    # Note: 'join' is not a built-in filter in Jinja2, but you can use it with a custom filter or directly in the template
    # Here we use a custom filter to demonstrate
    return render_template_string(template, items=items)

# 7. replace filter
# Testing: http://127.0.0.1:5003/replace/banana
@app.route('/replace/<word>')
def replace(word):
    template = "<p>Replace: {{ word|replace('a', 'o') }}</p>"
    return render_template_string(template, word=word)

# 8. trim filter
# Testing: http://127.0.0.1:5003/trim
@app.route('/trim')
def trim():
    text = '   hello   '
    template = "<p>Trim: '{{ text|trim }}'</p>"
    # The trim filter in Jinja2 removes whitespace from the beginning and end of a string.
    return render_template_string(template, text=text)

# 9. round filter
# Testing: http://127.0.0.1:5003/round/3.14159
@app.route('/round/<float:num>')
def round_num(num):
    template = "<p>Round: {{ num|round(2) }}</p>"
    return render_template_string(template, num=num)

# 10. sort filter
# Testing: http://127.0.0.1:5003/sort
@app.route('/sort')
def sort():
    items = [3, 1, 2]
    template = "<p>Sort: {{ items|sort }}</p>"
    return render_template_string(template, items=items)

# 11. reverse filter
# Testing: http://127.0.0.1:5003/reverse
@app.route('/reverse')
def reverse():
    items = [1, 2, 3]
    # Join the reversed list into a string for display
    template = "<p>Reverse: {{ items|reverse|join(', ') }}</p>"
    return render_template_string(template, items=items)

# 12. default filter
# Testing: http://127.0.0.1:5003/default
@app.route('/default')
def default():
    template = "<p>Default: {{ name|default('Hello Guest') }}</p>"
    return render_template_string(template)

# 13. safe filter
# Testing: http://127.0.0.1:5003/safe
@app.route('/safe')
def safe():
    html = '<b>String Text</b>'
    template = "<p>Escaped: {{ html }}</p><p>Safe: {{ html|safe }}</p>"
    return render_template_string(template, html=html)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
