import argparse

# My libs.
from reddit import *

parser = argparse.ArgumentParser(description="Saving saved Reddit posts/comments.")
parser.add_argument('-client_id', type=str, required=True, help='Reddit app client_id')
parser.add_argument('-client_secret', type=str, required=True, help='Reddit app client_secret')
parser.add_argument('-username', type=str, required=True, help='Reddit account username')
parser.add_argument('-password', type=str, required=True, help='Reddit account password')
parser.add_argument('-limit', type=int, help='Limit of API requests made to Reddit.')
args = parser.parse_args()

r = reddit(args.client_id, args.client_secret, args.username, args.password, args.limit)
r.getSaved()

# TODO 
# Progress bar?
# Better logging
# √ Move Reddit API functionality to it's own class
# API for un-saving post after it's save to Mongo
#  - try/except / whatever checking if DB save was successful?
#     - retry? just don't unsave and try again next time?
# √ Credentials via CLI args
# Track (deleted count, number of requests) and summarize in logs / notifications
# Mattermost / Slack / Discord support
# Args input handling, make sure strings are strings and int is int
# Some sort of verification that script can even auth to Reddit with creds.