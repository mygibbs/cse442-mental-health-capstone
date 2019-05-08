web: rm app.db; rm -rf migrations/; flask db init; flask db migrate -m "nuke"; flask db upgrade; gunicorn run:app
