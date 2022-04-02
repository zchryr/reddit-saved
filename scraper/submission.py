class submission(object):
    def __init__(self, author, clicked, created_utc, distinguished, edited,
            sid, is_original_content, is_self, link_flair_text,
            locked, name, num_comments, over_18, permalink, saved, score,
            selftext, spoiler, stickied, subreddit, subreddit_id, title,
            upvote_ratio, url) -> None:
        self.type = "submission"
        self.author = author
        self.clicked = clicked
        self.created_utc = created_utc
        self.distinguished = distinguished
        self.edited = edited
        self.id = sid
        self.is_original_content = is_original_content
        self.is_self = is_self
        self.link_flair_text = link_flair_text
        self.locked = locked
        self.name = name
        self.num_comments = num_comments
        self.over_18 = over_18
        self.permalink = permalink
        self.submission_link = "https://reddit.com" + permalink
        self.saved = saved
        self.score = score
        self.selftext = selftext
        self.spoiler = spoiler
        self.stickied = stickied
        self.subreddit = "r/" + subreddit
        self.subreddit_id = subreddit_id
        self.title = title
        self.upvote_ratio = upvote_ratio
        self.url = url
