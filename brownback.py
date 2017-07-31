#!/usr/bin/python
import praw
import pdb
import re
import os

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subs = ['news', 'eckansasnews', 'worldpolitics', 'progressive', 'economics', 'kansas', 'kansascity', 'atheism', 'freeatheism', 'democrats', 'UMukhasimAutoNews', 'nytimes', 'chapotraphouse', 'bluemidterm2018', 'enoughtrumpspam', 'liberal', 'political_revolution', 'thehillauto', 'waexauto', 'unremovable', 'politicaltweets', 'thenewcoldwar', 'technology', 'autonewspaper', 'autotldr', 'esist', 'marchagainsttrump', 'politicalvideo', 'keepournetfree', 'goodlongposts', 'badgovnofreedom', 'good_cake', 'democracy', 'fcc', 'worldnews', 'nottheonion', 'newsbotbot', 'wayofthebern', 'sandersforpresident', 'impeach_trump', 'fuckthealtright', 'environment', 'keep_track', 'PoliticalVideos', 'climate', 'latimesauto', 'cnet_all_rss', 'women', 'netneutrality', 'cornbreadliberals', 'greed', 'huffpoauto', 'watchingcongress', 'restorethefourth', 'libs', 'indivisibleguide', 'trussiagate', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'skydtech']

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['brownback', 'colyer', 'congressman bacon', 'rep bacon', 'kansas governor']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://www.kdor.ks.gov/apps/voterreg/default.aspx) \n\n"
            "[**Joshua Svaty**](https://joshuasvaty.com/) is running to be Governor of Kansas. \n\n"
            "[Donate](https://joshuasvaty.com/donate/) | "
            "[Facebook](https://www.facebook.com/SvatyforKansas/) | "
            "[Twitter](https://twitter.com/JoshuaSvaty) \n\n"
            "Svaty supports renewable energy. \n\n\n"

            "[**Carl Brewer**](https://www.brewerforkansas.com/issues) is running to be Governor of Kansas. \n\n"
            "[Donate](https://www.brewerforkansas.com/donate) | "
            "[Facebook](https://www.facebook.com/BrewerforKansas/) | "
            "[Twitter](https://twitter.com/BrewerForKansas) \n\n"
            "Brewer supports public schools. \n\n\n"

            "^(I'm a bot and I'm learning. Let me know if I can do better. It's a lot of "
            "work to add all this info, but if you prefer a different candidate, let me know, and I'll add them.)")
        submission.reply(text)
        print("Bot replying to : ", submission.title)

        # Store the current id into our list
        posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
