import praw

# My libs.
from submission import *
from comment import *
from mongo import *

class reddit:
    def __init__(self, args, client_id, client_secret, username, password, limit) -> None:
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            password=password,
            user_agent="ScrapeSaved/0.0.1",
            username=username,
        )
        self.limit = limit
        self.m = mongoClient(args.connectionURL, args.protocol, args.port, args.dbUsername, args.dbPassword, args.databaseName, args.ssl, args.tlsCAFile, args.username)

    def getSaved(self):
        for save in self.reddit.user.me().saved(limit=self.limit):
            if (isinstance(save, praw.models.reddit.submission.Submission)):
                try:
                    s = submission(save.author.name, save.clicked, save.created_utc, save.distinguished, save.edited,
                            save.id, save.is_original_content, save.is_self, save.link_flair_text, save.locked,
                            save.name, save.num_comments, save.over_18, save.permalink, save.saved, save.score,
                            save.selftext, save.spoiler, save.stickied, save.subreddit.display_name, save.subreddit.id,
                            save.title, save.upvote_ratio, save.url)
                    self.m.insertOne(s.__dict__)
                except AttributeError as e:
                    print("Save was deleted or removed.")
                    continue
            elif (isinstance(save, praw.models.reddit.comment.Comment)):
                try:
                    c = comment(save.author.name, save.body, save.body_html, save.created_utc, save.distinguished,
                            save.edited, save.id, save.is_submitter, save.link_id, save.parent_id, save.permalink,
                            save.saved, save.score, save.stickied, save.submission.id, save.subreddit.display_name,
                            save.subreddit.id)
                    self.m.insertOne(c.__dict__)
                except AttributeError as e:
                    print("Save was deleted or removed.")
                    continue
