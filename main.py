from flask import Flask, redirect, url_for, render_template, request, jsonify
from books_list import books
from flaskext.mysql import MySQL


mysql = MySQL()

app = Flask(__name__)
app.secret_key = "abc123"
app.debug = True

# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'booksdb'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# mysql.init_app(app)
# conn = mysql.connect()
#
#
# @app.route('/BookData')
# def book_data():
#     cursor = conn.cursor()
#     cursor.execute('SELECT BookID,BookName FROM books')
#     booklist = cursor.fetchall()
#     return render_template("bookdata.html", booklist=booklist)


@app.route("/")
def default():
    return redirect(url_for("home"))


@app.route("/home", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        if 'select' in request.form:
            id = request.form.get("book")
            return redirect(url_for("api_id", id=int(id)))
        elif 'show_all' in request.form:
            return redirect(url_for("api_all"))
    return render_template("index.html")


@app.route('/main/books/all', methods=['POST', 'GET'])
def api_all():
    return jsonify(books)


@app.route('/main/books/<id>', methods=['GET', 'POST'])
def api_id(id):
    if 'return' in request.form:
        return redirect(url_for('home'))

    book = books[int(id)]
    #tempid = book['id']
    title = book['title']
    author = book['author']
    published = book['published']
    first_sentence = book['first_sentence']

    return render_template("book.html", title=title, author=author, id=id, first_sentence=first_sentence, published=published)


if __name__ == "__main__":
    app.run(debug=True)