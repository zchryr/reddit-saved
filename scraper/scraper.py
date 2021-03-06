"""Python library for parsing CLI arguments."""
import argparse

# Local libraries.
from reddit import Reddit

PARSER = argparse.ArgumentParser(description="Saving saved Reddit posts/comments.")

# Reddit API args.
PARSER.add_argument('-client_id', type=str, required=True, help='Reddit app client_id')
PARSER.add_argument('-client_secret', type=str, required=True, help='Reddit app client_secret')
PARSER.add_argument('-reddit_username', type=str, required=True, help='Reddit account username')
PARSER.add_argument('-reddit_password', type=str, required=True, help='Reddit account password')
PARSER.add_argument('-limit', help='Limit of API requests made to Reddit. None if not specified.',
                    default=None)

# MongoDB args.
PARSER.add_argument('-connection_url', type=str, required=True, help='MongoDB connection URL')
PARSER.add_argument('-protocol', type=str, required=True, help='MongoDB protocol')
PARSER.add_argument('-db_username', type=str, required=True, help='MongoDB authentication username')
PARSER.add_argument('-db_password', type=str, required=True, help='MongoDB user password')

# Other args.
PARSER.add_argument('-unsave', type=str, required=False, default='yes',
                    help='Choose whether to unsave post/comment after saving to MongoDB. ' +
                    "Default: 'yes', Options: 'yes' | 'no'")

ARGS = PARSER.parse_args()

if ARGS.limit is None:
    R = Reddit(ARGS,
               ARGS.client_id,
               ARGS.client_secret,
               ARGS.reddit_username,
               ARGS.reddit_password,
               None)
else:
    R = Reddit(ARGS,
               ARGS.client_id,
               ARGS.client_secret,
               ARGS.reddit_username,
               ARGS.reddit_password,
               int(ARGS.limit))

R.main()
