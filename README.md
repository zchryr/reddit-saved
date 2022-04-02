# Reddit Saved

## Setup
TODO.

## Motivation
I constantly save posts/comments while using Reddit, almost always with the intention of a "save to read later" or similar. Not only do I rarely go back to these saves, but the format for them is not very organized or categorized. It's not always very easy to search for something I know I've saved. I'd like to build a set of services to scrape the saves, store them, alert me on new saves, categorize saves, and probably quite a bit more. I'd like to do this in the hopes that I'm able to make better use out of what I save while using Reddit.

## The Future
So far I've written a scraper to grab the saves using Reddit's API, and store them in MongoDB.

### Trigger scraper
I'll need to trigger this scraper on a schedule so to always grab any new saves I've made. Lambda? Kubernetes?

### Notifications
Once the scraper runs and grabs new saves, I'd like to be notified that there are new saves to review. When I say "review", I'm thinking of having the ability to categorize, snooze (like in Outlook), delete, etc the new saves.

Supported notification platforms: Mattermost, Slack, Discord, possibly more...

### Website
I think having a website to have these saves, categories, and whatever else there is would be good.

### APIs
Ideally the services that power the website should also have some APIs, so a power user would be able to extract the data from MongoDB. MVC, etc.

## Services

### scraper
Python scripts to use Reddit's API and get a user's saved posts and save them to a MongoDB.