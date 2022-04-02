import argparse

# My libs.
from reddit import Reddit

parser = argparse.ArgumentParser(description="Saving saved Reddit posts/comments.")

# Reddit API args.
parser.add_argument('-client_id', type=str, required=True, help='Reddit app client_id')
parser.add_argument('-client_secret', type=str, required=True, help='Reddit app client_secret')
parser.add_argument('-username', type=str, required=True, help='Reddit account username')
parser.add_argument('-password', type=str, required=True, help='Reddit account password')
parser.add_argument('-limit', help='Limit of API requests made to Reddit. None if not specified.', default=None)

# MongoDB args.
parser.add_argument('-connection_url', type=str, required=True, help='MongoDB connection URL')
parser.add_argument('-protocol', type=str, required=True, help='MongoDB protocol')
parser.add_argument('-port', type=int, required=True, help='MongoDB listening port')
parser.add_argument('-db_username', type=str, required=True, help='MongoDB authentication username')
parser.add_argument('-db_password', type=str, required=True, help='MongoDB user password')
parser.add_argument('-database_name', type=str, required=True, help='MongoDB database name to be used')
parser.add_argument('-ssl', type=bool, required=True, help='MongoDB TLS configuration')
parser.add_argument('-tls_ca_file', type=str, required=True, help='Location of MongoDB TLS CA file.')

args = parser.parse_args()

if args.limit is None:
    r = Reddit(args, args.client_id, args.client_secret, args.username, args.password, None)
else:
    r = Reddit(args, args.client_id, args.client_secret, args.username, args.password, int(args.limit))

r.getSaved()
