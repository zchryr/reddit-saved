// Local.
const mongo = require("./mongo");
const reddit = require("./reddit");
const Comment = require("./models/comment");
const Submission = require("./models/submission");

// Libraries
const mongoose = require("mongoose");
const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const { graphqlHTTP } = require("express-graphql");
const { buildSchema } = require("graphql");

const db_uri =
  mongo["protocol"] +
  "://" +
  mongo["connection_url"] +
  ":" +
  mongo["port"] +
  "/" +
  reddit["username"];

app.use(bodyParser.json());

app.use(
  "/graphql",
  graphqlHTTP({
    schema: buildSchema(`
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
    `),
    rootValue: {
      comments: () => {
        return Comment.find().then((result) => {
          return result;
        });
      },
      submissions: () => {
        return Submission.find().then((result) => {
          return result;
        });
      },
    },
    graphiql: true,
  })
);

mongoose
  .connect(db_uri, {
    auth: {
      username: mongo["user"],
      password: mongo["password"],
    },
    authSource: "admin",
    useUnifiedTopology: true,
    useNewUrlParser: true,
  })
  .then(() => {
    console.log("Successfully connected to MongoDB!");
    app.listen(3000);
  })
  .catch((err) => {
    console.log(`Failed to connect to MongoDB. Error: ${err}`);
  });
