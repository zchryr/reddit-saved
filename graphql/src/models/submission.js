const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const submissionSchema = new Schema({
  type: {
    type: String,
    required: true,
  },
  author: {
    type: String,
    required: true,
  },
  clicked: {
    type: Boolean,
    required: true,
  },
  created_utc: {
    type: Number,
    required: true,
  },
  distinguished: {
    type: String,
    required: false,
    default: null,
  },
  edited: {
    type: Boolean,
    required: true,
  },
  reddit_id: {
    type: String,
    required: true,
  },
  is_original_content: {
    type: Boolean,
    required: true,
  },
  is_self: {
    type: Boolean,
    required: true,
  },
  link_flair_text: {
    type: String,
    required: true,
  },
  locked: {
    type: Boolean,
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  num_comments: {
    type: Number,
    required: true,
  },
  over_18: {
    type: Boolean,
    required: true,
  },
  permalink: {
    type: String,
    required: true,
  },
  submission_link: {
    type: String,
    required: true,
  },
  saved: {
    type: Boolean,
    required: true,
  },
  score: {
    type: Number,
    required: true,
  },
  selftext: {
    type: String,
    required: true,
  },
  spoiler: {
    type: Boolean,
    required: true,
  },
  stickied: {
    type: Boolean,
    required: true,
  },
  subreddit: {
    type: String,
    required: true,
  },
  subreddit_id: {
    type: String,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  upvote_ratio: {
    type: Number,
    required: true,
  },
  url: {
    type: String,
    required: true,
  },
});

module.exports = mongoose.model("Submission", submissionSchema);
