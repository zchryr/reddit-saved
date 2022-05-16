module.exports = {
  user: process.env.MONGO_USER,
  password: process.env.MONGO_PASSWORD,
  connection_url: process.env.MONGO_URL,
  port: process.env.MONGO_PORT,
  protocol: process.env.MONGO_PROTOCOL,
  db_name: process.env.MONGO_DB_NAME,
  ssl: process.env.MONGO_SSL,
};
