"""Python library to interact with Reddit."""
import sys
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
        self.unsave_choice = args.unsave
        self.limit = limit
        self.mongo_client = MongoClient(connection_url=args.connection_url, protocol=args.protocol,
                                        port=args.port, db_username=args.db_username,
                                        db_password=args.db_password, db_name=args.database_name,
                                        ssl=args.ssl, reddit_username=args.reddit_username)

        self.exiting_saves = self.mongo_client.col.find({ id: True })

    def main(self):
        """Go through the saved Reddit posts, checks for duplicates save to MongoDB,
           and unsaves them if successful."""

        LOGGER.info("Collecting existing saves.")
        self.mongo_client.get_existing()

        LOGGER.info("Hitting Reddit API to get saves.")
        try:
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
                        if self.mongo_client.check_existing(submission.id) is False:
                            try:
                                self.mongo_client.insert_one(submission.__dict__)
                                LOGGER.info("Saved post ID: " + str(save.id) + " successfully!")
                            except Exception as error:
                                LOGGER.error("Failed to save ID: " + str(save.id) + " to MongoDB.")
                                LOGGER.error("Exception: " + str(error))
                            else:
                                try:
                                    self.unsave(submission.id, "submission")
                                except Exception as unsave_error:
                                    LOGGER.error("Failed to unsave: " + str(submission.id) +
                                                 " post.")
                                    LOGGER.error("Exception: " + str(unsave_error))
                        else:
                            LOGGER.info("Post: " + str(submission.id) +
                                        " already exists in the database.")
                            self.unsave(submission.id, "submission")
                            continue
                    except AttributeError as error:
                        LOGGER.info("Save ID: " + str(save.id) + "was deleted or removed.")
                        continue
                elif isinstance(save, praw.models.reddit.comment.Comment):
                    try:
                        comment = Comment(save.author.name, save.body, save.body_html,
                                          save.created_utc, save.distinguished, save.edited,
                                          save.id, save.is_submitter, save.link_id, save.parent_id,
                                          save.permalink, save.saved, save.score, save.stickied,
                                          save.submission.id, save.subreddit.display_name,
                                          save.subreddit.id)
                        if self.mongo_client.check_existing(comment.id) is False:
                            try:
                                self.mongo_client.insert_one(comment.__dict__)
                                LOGGER.info("Saved comment ID: " + str(save.id) + " successfully!")
                            except Exception as error:
                                LOGGER.error("Failed to save ID: " + str(save.id) + " to MongoDB.")
                                LOGGER.error("Exception: " + str(error))
                            else:
                                try:
                                    self.unsave(comment.id, "comment")
                                except Exception as unsave_error:
                                    LOGGER.error("Failed to unsave: " + str(submission.id)
                                                + " comment.")
                                    LOGGER.error("Exception: " + str(unsave_error))
                        else:
                            LOGGER.info("Comment: " + str(comment.id) +
                                        " already exists in the database.")
                            self.unsave(comment.id, "comment")
                            continue
                    except AttributeError as error:
                        LOGGER.info("Save ID: " + str(save.id) + "was deleted or removed.")
                        continue
        except AttributeError as error:
            LOGGER.info("No Reddit saves to archive.")
            sys.exit(0)

    def unsave(self, save_id, save_type):
        """Unsaves Reddit submission/comment given the ID."""
        if self.unsave == "yes": # pylint: disable=W0143
            if save_type == "submission":
                unsave_submission = self.reddit_client.submission(save_id)
                unsave_submission.unsave()
                LOGGER.info("Unsaved post ID: " + str(save_id) + " successfully!")
            elif save_type == "comment":
                unsave_comment = self.reddit_client.comment(save_id)
                unsave_comment.unsave()
                LOGGER.info("Unsaved comment ID: " + str(save_id) + " successfully!")
