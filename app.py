# app.py

from flask import Flask, request, render_template_string
from alg import process_input

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>Алгосы</title>
</head>
<body>
<h1>Найдём компоненту связности, содержащую вершину 1</h1>
<form method="post">
    <textarea name="input_data" rows="10" cols="60" 
      placeholder="Ввод: N M, затем M строк с u v">{{request.form.input_data or ''}}</textarea><br>
    <button type="submit">Вычислить</button>
</form>

{% if output %}
<h2>Результат:</h2>
<pre>{{output}}</pre>
{% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    if request.method == 'POST':
        data = request.form.get('input_data', '')
        output = process_input(data)
    return render_template_string(TEMPLATE, output=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
