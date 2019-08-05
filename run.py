# std
import argparse

# locals
from src import app

arg_parser = argparse.ArgumentParser(description='Run sentiment analysis demo server')

arg_parser.add_argument('--port', 
                        dest='port', default=5000, type=int,
                        help='Port to run'
)

arg_parser.add_argument('-d', '--debug',
                        dest='debug', default=False, action='store_true',
                        help='Run in debug mode or not'
)

args = arg_parser.parse_args()

app.run(port=args.port, debug=args.debug)