from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Frontend development", "author": "Arthur"},
    {"id": 2, "title": "Backend development", "author": "Author 1"},
    {"id": 3, "title": "Devops", "author": "Ikiebe emmanuel"}
]

@app.route('/')
def home():
    return "Welcome to my first ever basic python API, read the documentation for usage"

# API endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# API endpoint to get a specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# API endpoint to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201

# API endpoint to update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(request.json)
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# API endpoint to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
