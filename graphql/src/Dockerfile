# Base image.
FROM 16.15.0-alpine3.15

# Work directory.
WORKDIR /app

# Updates.
RUN apk update && \
    apk upgrade

# Unprivileged user setup.
RUN addgroup -S node && \
    adduser -G node -S node
USER node

# Node packages.
COPY package.json yarn.lock ./

# Install.
RUN yarn install --frozen-lockfile --no-cache --production

# Node production.
ENV NODE_ENV production

CMD [“dumb-init”, “node”, “index.js”]