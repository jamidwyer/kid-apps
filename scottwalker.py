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

subs = ['racine', 'kenosha', 'politicalrevolutionwi', 'bluemidterm2018', 'enoughtrumpspam', 'indepthstories', 'democrats', 'chapotraphouse', 'liberal', 'keepournetfree', 'thenewcoldwar', 'politicalvideo', 'badlawyer', 'wayofthebern', 'sandersforpresident', 'impeach_trump', 'anythinggoesnews', 'russialago', 'tytpolitics', 'cornbreadliberals', 'political_revolution', 'thehillauto', 'esist', 'waexauto', 'unremovable', 'good_cake', 'technology', 'autonewspaper', 'autotldr', 'marchagainsttrump', 'goodlongposts', 'latimesauto', 'badgovnofreedom', 'libs', 'democracy', 'stupid_watergate', 'fcc', 'netneutrality', 'worldnews', 'news', 'nottheonion', 'breakingnews24hr', 'worldpolitics', 'newsbotbot', 'fuckthealtright', 'collapse', 'environment', 'progressive', 'UMukhasimAutoNews', 'inthenews', 'hotandtrending', 'keep_track', 'thecolorisblue', 'PoliticalVideos', 'climate', 'donaldtrumpwhitehouse', 'nofilternews', 'cnet_all_rss', 'women', 'newsy', 'cnnauto', 'huffpoauto', 'cbsauto', 'greed', 'watchingcongress', 'restorethefourth', 'trussiagate', '538auto', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'datauncensored', 'skydtech', 'atheism', 'uspolitics', 'lgbtnews', 'atheismrebooted', 'enoughlibertarianspam', 'conspiratard', 'gogopgo', 'nypostauto', 'economics', 'phillyauto', 'freeatheism', 'nytimes', 'ecointernet', 'leftcentral', 'thedavidpakmanshow', 'trumpforrussia']

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['scott walker', 'governor walker', 'wisconsin governor', 'wi gov', 'wi governor\'s']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://myvote.wi.gov/en-us/registertovote) \n\n"
            "[**Bob Harlow**](https://bobharlow.net/) is running to be Governor of Wisconsin. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/harlow-for-wisconsin) | "
            "[Facebook](https://www.facebook.com/HarlowForWisconsin/) | "
            "[Twitter](https://twitter.com/bobharlow_) \n\n"
            "Harlow supports universal health care and public schools. \n\n\n"

        "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")
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
