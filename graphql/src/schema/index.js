const { buildSchema } = require("graphql");

module.exports = buildSchema(`
  type Comment {
    type: String!
    author: String!
    clicked: Boolean!
    created_utc: Int!
    distinguished: String
    edited: Boolean!
    reddit_id: String!
    is_submitter: Boolean!
    link_id: String!
    parent_id: String!
    permalink: String!
    comment_link: String!
    saved: Boolean!
    score: Int!
    stickied: Boolean!
    subreddit: String!
    subreddit_id: String!
  }

  type Submission {
    type: String!
    author: String!
    clicked: Boolean!
    created_utc: Int!
    distinguished: String
    edited: Boolean!
    reddit_id: String!
    is_original_content: Boolean!
    is_self: Boolean!
    link_flair_text: String!
    locked: Boolean!
    name: String!
    num_comments: Int!
    over_18: Boolean!
    permalink: String!
    submission_link: String!
    saved: Boolean!
    score: Int!
    selftext: String!
    spoiler: Boolean!
    stickied: Boolean!
    subreddit: String!
    subreddit_id: String!
    title: String!
    upvote_ratio: Float!
    url: String!
  }

  type RootQuery {
    comments: [Comment]
    submissions: [Submission]
  }
  schema {
    query: RootQuery
  }
`);
