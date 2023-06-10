"""Serve the schema over HTTP using flask and flask-graphql."""
import argparse
from flask import Flask
from flask_graphql import GraphQLView
import schema

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000,
                        help='Port to run the server on')
    args = parser.parse_args()

    app = Flask(__name__)
    app.add_url_rule('/', view_func=GraphQLView.as_view('graphql',
                     schema=schema.schema, graphiql=True))

    app.run(debug=True, port=args.port)
