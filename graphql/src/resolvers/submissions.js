const Submission = require("../models/submission");

module.exports = {
  submissions: async () => {
    try {
      const submissions = await Submission.find();
      return submissions;
    } catch (err) {
      throw err;
    }
  },
};

// submissions: () => {
//   return Submission.find().then((result) => {
//     return result;
//   });
// },
