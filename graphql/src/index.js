// Local.
const mongo = require("./mongo");
const reddit = require("./reddit");
const graphQlSchema = require("./schema/index");
const graphQlResolvers = require("./resolvers/index");

// Libraries
const mongoose = require("mongoose");
const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const { graphqlHTTP } = require("express-graphql");

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
    schema: graphQlSchema,
    rootValue: graphQlResolvers,
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
