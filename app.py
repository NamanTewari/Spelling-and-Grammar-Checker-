from flask import Flask, request, render_template
from Model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell', methods=['POST', 'GET'])
def spell():
    if request.method == 'POST':
        text = request.form.get('text', '')
        if not text:
            return render_template('index.html', error="No text provided")
        try:
            corrected_text = spell_checker_module.correct_spell(text)
            corrected_grammar, _ = spell_checker_module.correct_grammar(text)
            return render_template('index.html', corrected_text=corrected_text, corrected_grammar=corrected_grammar)
        except Exception as e:
            return render_template('index.html', error=f"Error processing text: {str(e)}")
    return render_template('index.html')

@app.route('/grammar', methods=['POST', 'GET'])
def grammar():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file provided")
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="No file selected")
        try:
            readable_file = file.read().decode('utf-8', errors='ignore')
            corrected_text = spell_checker_module.correct_spell(readable_file)
            corrected_grammar, _ = spell_checker_module.correct_grammar(readable_file)
            return render_template('index.html', corrected_text=corrected_text, corrected_grammar=corrected_grammar)
        except Exception as e:
            return render_template('index.html', error=f"Error processing file: {str(e)}")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)