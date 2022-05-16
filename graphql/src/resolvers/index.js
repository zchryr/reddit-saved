const commentsResolver = require("./comments");
const submissionsResolver = require("./submissions");

const rootResolver = {
  ...commentsResolver,
  ...submissionsResolver,
};

module.exports = rootResolver;
