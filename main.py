from flashcard import create_app
from replit import web

app,api = create_app()
web.run(app)