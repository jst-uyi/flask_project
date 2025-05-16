from flask import Flask, render_template, abort, request
from models import db, Title, Genre
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hulu.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    per_page = 10
    pagination = Title.query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('index.html', titles=pagination.items, pagination=pagination)

@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    page = request.args.get('page', 1, type=int)
    per_page = 10

    if query:
        results = Title.query.filter(Title.title.ilike(f'%{query}%'))
        pagination = results.paginate(page=page, per_page=per_page, error_out=False)
        return render_template('search_results.html', query=query, titles=pagination.items, pagination=pagination)
    else:
        return render_template('search_results.html', query=query, titles=[], pagination=None)

@app.route('/titles/<title_id>')
def title_detail(title_id):
    title = Title.query.get(title_id)
    if not title:
        abort(404)
    return render_template('title_detail.html', title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
