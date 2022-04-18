import praw

# Local libraries.
from submission import Submission
from comment import Comment
from mongo import MongoClient
from logger import Logger
LOGGER = Logger

class Reddit:
    """Class to get saved Reddit posts, put them in a MongoDB, and unsave them."""
    def __init__(self, args, client_id, client_secret, reddit_username, reddit_password,
                 limit) -> None:
        self.reddit_client = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            password=reddit_password,
            user_agent="ScrapeSaved/0.0.1",
            username=reddit_username,
        )
        self.limit = limit
        self.mongo_client = MongoClient(connection_url=args.connection_url, protocol=args.protocol,
                                        port=args.port, db_username=args.db_username,
                                        db_password=args.db_password, db_name=args.database_name,
                                        ssl=args.ssl, reddit_username=args.reddit_username)

    def get_saved(self):
        """Go through the saved Reddit posts, save to MongoDB, and unsave them if successful."""
        LOGGER.info("Hitting Reddit API to get saves.")
        for save in self.reddit_client.user.me().saved(limit=self.limit):
            if isinstance(save, praw.models.reddit.submission.Submission):
                try:
                    submission = Submission(save.author.name, save.clicked, save.created_utc,
                                            save.distinguished, save.edited, save.id,
                                            save.is_original_content, save.is_self,
                                            save.link_flair_text, save.locked, save.name,
                                            save.num_comments, save.over_18, save.permalink,
                                            save.saved, save.score, save.selftext, save.spoiler,
                                            save.stickied, save.subreddit.display_name,
                                            save.subreddit.id, save.title, save.upvote_ratio,
                                            save.url)
                    try:
                        self.mongo_client.insert_one(submission.__dict__)
                        LOGGER.info("Saved post ID: " + str(save.id) + " successfully!")
                    except Exception as error:
                        LOGGER.error("Failed to save ID: " + str(save.id) + " to MongoDB.")
                        LOGGER.error("Exception: " + str(error))
                    else:
                        # Unsave Reddit post.
                        print()
                except AttributeError as error:
                    LOGGER.info("Save ID: " + str(save.id) + "was deleted or removed.")
                    continue
            elif isinstance(save, praw.models.reddit.comment.Comment):
                try:
                    comment = Comment(save.author.name, save.body, save.body_html, save.created_utc,
                                      save.distinguished, save.edited, save.id, save.is_submitter,
                                      save.link_id, save.parent_id, save.permalink, save.saved,
                                      save.score, save.stickied, save.submission.id,
                                      save.subreddit.display_name, save.subreddit.id)
                    try:
                        self.mongo_client.insert_one(comment.__dict__)
                        LOGGER.info("Saved comment ID: " + str(save.id) + " successfully!")
                    except Exception as error:
                        LOGGER.error("Failed to save ID: " + str(save.id) + " to MongoDB.")
                        LOGGER.error("Exception: " + str(error))
                    else:
                        # Unsave Reddit comment.
                        print()
                except AttributeError as error:
                    LOGGER.info("Save ID: " + str(save.id) + "was deleted or removed.")
                    continue
