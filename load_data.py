import pandas as pd
from app import app, db
from models import Title, Genre


df = pd.read_csv('hulu_titles.csv', header=0, names=[
    'id','type','title','country','date_added','release_year','rating','duration','genres','description'
])



with app.app_context():
    db.drop_all()
    db.create_all()
    genre_dict = {}
    for _, row in df.iterrows():
        title = Title(
            id=row['id'],
            type=row['type'],
            title=row['title'],
            country=row['country'],
            date_added=row['date_added'],
            release_year=int(row['release_year']) if not pd.isnull(row['release_year']) else None,
            rating=row['rating'],
            duration=row['duration'],
            description=row['description']
        )
        # Handle genres
        genres = [g.strip() for g in str(row['genres']).split(',')]
        for genre_name in genres:
            if genre_name not in genre_dict:
                genre = Genre(name=genre_name)
                db.session.add(genre)
                db.session.flush()
                genre_dict[genre_name] = genre
            title.genres.append(genre_dict[genre_name])
        db.session.add(title)
    db.session.commit()
    print("Loaded", len(df), "records.")
