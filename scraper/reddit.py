from mimetypes import common_types
import praw

# My libs.
from submission import Submission
from comment import Comment
from mongo import MongoClient

class Reddit:
    def __init__(self, args, client_id, client_secret, username, password, limit) -> None:
        self.reddit_client = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            password=password,
            user_agent="ScrapeSaved/0.0.1",
            username=username,
        )
        self.limit = limit
        self.MONGO_CLIENT = MongoClient(args.connection_url, args.protocol, args.port,
                                        args.db_username, args.db_password, args.database_name,
                                        args.ssl, args.tls_ca_file, args.username)

    def get_saved(self):
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
                    self.MONGO_CLIENT.insert_one(submission.__dict__)
                except AttributeError as error:
                    print("Save was deleted or removed.")
                    continue
            elif isinstance(save, praw.models.reddit.comment.Comment):
                try:
                    comment = Comment(save.author.name, save.body, save.body_html, save.created_utc,
                                      save.distinguished, save.edited, save.id, save.is_submitter,
                                      save.link_id, save.parent_id, save.permalink, save.saved,
                                      save.score, save.stickied, save.submission.id,
                                      save.subreddit.display_name, save.subreddit.id)
                    self.MONGO_CLIENT.insert_one(comment.__dict__)
                except AttributeError as error:
                    print("Save was deleted or removed.")
                    continue
