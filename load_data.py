import pandas as pd
from app import app, db
from models import Title, Genre
import re

df = pd.read_csv('hulu_titles.csv')
poster_df = pd.read_csv('poster_links.csv')

poster_map = dict(zip(poster_df['title'], poster_df['poster_url']))

with app.app_context():
    db.drop_all()
    db.create_all()
    genre_dict = {}

    for _, row in df.iterrows():
        poster_url = poster_map.get(row['title'], None)  # fallback to None if not found

        title = Title(
            id=row['show_id'],
            type=row['type'],
            title=row['title'],
            country=row['country'],
            date_added=row['date_added'],
            release_year=int(row['release_year']) if not pd.isnull(row['release_year']) else None,
            rating=row['rating'],
            duration=row['duration'],
            description=row['description'],
            poster_url=poster_url
        )

        genres = [g.strip() for g in str(row['listed_in']).split(',')]
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
