class comment(object):
    def __init__(self, author, body, body_html, created_utc, distinguished, edited, cid,
                 is_submitter, link_id, parent_id, permalink, saved, score,
                 stickied, submission, subreddit, subreddit_id) -> None:
        self.type = "comment"
        self.author = author
        self.body = body
        self.body_html = body_html
        self.created_utc = created_utc
        self.distinguished = distinguished
        self.edited = edited
        self.id = cid
        self.is_submitter = is_submitter
        self.link_id = link_id
        self.parent_id = parent_id
        self.permalink = permalink
        self.comment_link = "https://reddit.com" + permalink
        self.saved = saved
        self.score = score
        self.stickied = stickied
        self.submission = submission
        self.subreddit = "r/" + subreddit
        self.subreddit_id = subreddit_id
