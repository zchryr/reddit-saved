// Local.
const mongo = require("./mongo");
const reddit = require("./reddit");
const graphQlSchema = require("./schema/index");
const graphQlResolvers = require("./resolvers/index");

// Libraries.
const mongoose = require("mongoose");
const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const { graphqlHTTP } = require("express-graphql");

// Environment.
const environment = process.env.NODE_ENV || "development";
let graphiql = false;
if (environment === "development") {
  graphiql = true;
}

const db_uri =
  mongo["protocol"] +
  "://" +
  mongo["connection_url"] +
  "/" +
  reddit["username"];

app.use(bodyParser.json());

app.use(
  "/graphql",
  graphqlHTTP({
    schema: graphQlSchema,
    rootValue: graphQlResolvers,
    graphiql: graphiql,
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

async function closeGracefully(signal) {
  await fastify.close();
  process.exit();
}
process.on("SIGINT", closeGracefully);
