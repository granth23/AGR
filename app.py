from flask import Flask, request, redirect, url_for, render_template
import json

app = Flask(__name__)

def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def load_text():
    with open('custom.json', 'r') as file:
        return json.load(file)

def save_text(data):
    with open('custom.json', 'w') as file:
        json.dump(data, file, indent=4)


@app.route('/qwertyuiop/pass', methods=['GET', 'POST'])
def admin_pass():
    if request.method == 'POST':
        updated_data = {}
        for page in request.form:
            updated_data[page] = request.form[page]
        save_data(updated_data)
        return redirect(url_for('show_page', page='page1'))
    return render_template('admin.html', page_data=load_data())


@app.route('/qwertyuiop/text', methods=['GET', 'POST'])
def admin_text():
    if request.method == 'POST':
        updated_data = {}
        for page in request.form:
            updated_data[page] = request.form[page]
        save_text(updated_data)
        return redirect(url_for('show_page', page='page1'))
    return render_template('admin.html', page_data=load_text())


@app.route('/<page>', methods=['GET', 'POST'])
def show_page(page):
    custom_text = load_text()[page]
    if page in load_data().keys():
        if request.method == 'POST':
            data = request.form['data']
            if data == load_data()[page]:
                if page == 'page5':
                    return redirect(url_for('show_page', page='page1'))
                else:
                    next_page = 'page' + str(int(page[-1]) + 1)
                    return redirect(url_for('show_page', page=next_page))
        return render_template('page.html', page=page, custom_text=custom_text)
    else:
        return redirect(url_for('show_page', page='page1'))

if __name__ == '__main__':
    app.run(debug=True)
