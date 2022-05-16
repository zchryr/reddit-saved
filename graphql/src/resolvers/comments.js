const Comment = require("../models/comment");

module.exports = {
  comments: async () => {
    try {
      const comments = await Comment.find();
      return comments;
    } catch (err) {
      throw err;
    }
  },
};

// return Comment.find().then((result) => {
//   return result;
// });
