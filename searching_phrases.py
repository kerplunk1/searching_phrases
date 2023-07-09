from flask import Flask, render_template, request
from nlp import vizualize
from pdf import get_text

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	if request.method == 'POST':
		phrase = request.form['phrase']
		filename = request.files['filename']	
		text = get_text(filename)
	return vizualize(phrase, text)

# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port=5000, debug=True)