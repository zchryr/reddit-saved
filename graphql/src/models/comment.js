const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const commentSchema = new Schema({
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
  is_submitter: {
    type: Boolean,
    required: true,
  },
  link_id: {
    type: String,
    required: true,
  },
  parent_id: {
    type: String,
    required: true,
  },
  permalink: {
    type: String,
    required: true,
  },
  comment_link: {
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
});

module.exports = mongoose.model("Comment", commentSchema);
