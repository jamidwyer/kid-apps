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

subs = ['nova', 'progressive', 'economics', 'uspolitics', 'roanoke', 'virginia', 'lgbt', 'rva', 'dailyshow', 'atheism', 'freeatheism', 'democrats', 'UMukhasimAutoNews', 'nytimes', 'chapotraphouse', 'bluemidterm2018', 'enoughtrumpspam', 'liberal', 'political_revolution', 'thehillauto', 'waexauto', 'unremovable', 'thenewcoldwar', 'technology', 'autonewspaper', 'autotldr', 'esist', 'marchagainsttrump', 'politicalvideo', 'keepournetfree', 'goodlongposts', 'badgovnofreedom', 'good_cake', 'democracy', 'fcc', 'worldnews', 'nottheonion', 'newsbotbot', 'wayofthebern', 'sandersforpresident', 'impeach_trump', 'fuckthealtright', 'environment', 'keep_track', 'PoliticalVideos', 'climate', 'latimesauto', 'cnet_all_rss', 'women', 'netneutrality', 'cornbreadliberals', 'greed', 'huffpoauto', 'watchingcongress', 'restorethefourth', 'libs', 'trussiagate', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'skydtech']

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['ed gillespie', '^(?!.*west virginia governor).*virginia governor.*$']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.elections.virginia.gov/citizen-portal/index.html) \n\n"
            "[**Ralph Northam**](http://ralphnortham.com/) is running to be Governor of Virginia. \n\n"
            "[Donate](https://act.myngp.com/northam/homepage) | "
            "[Reddit](https://www.reddit.com/r/RalphNortham/) | "
            "[Facebook](https://www.facebook.com/ralph.northam) | "
            "[Twitter](https://twitter.com/RalphNortham) \n\n"
            "Northam supports universal health care, paid family leave, college affordability, equal pay for equal work, renewable energy, LGBT equality, and common-sense gun safety laws. \n\n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better. It's a lot of "
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
