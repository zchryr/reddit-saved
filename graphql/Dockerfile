# Base image.
FROM node:18.7.0-alpine3.15

# Build arg.
ARG environment

# Work directory.
WORKDIR /app

# Updates.
RUN apk update && \
    apk upgrade

# Node packages.
COPY package.json yarn.lock ./

# Install.
RUN yarn install --frozen-lockfile --no-cache --production

# Dumb init.
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.1/dumb-init_1.1.1_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init

# Unprivileged user setup.
RUN addgroup -S rs-graphql && \
    adduser -G rs-graphql -S rs-graphql

# Prod files.
COPY --chown=rs-graphql:rs-graphql /src .

# Set user.
USER rs-graphql

# Node production.
ENV NODE_ENV ${environment}

CMD ["dumb-init", "node", "index.js"]