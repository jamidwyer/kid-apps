# coding: utf-8
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

subs = ['kentucky', 'kentucky6th', 'lexington', 'miamiheraldauto', 'bluemidterm2018', 'indepthstories', 'democrats', 'chapotraphouse', 'enoughtrumpspam', 'keepournetfree', 'politicalvideo', 'wayofthebern', 'impeach_trump', 'russialago', 'liberal', 'tytpolitics', 'political_revolution', 'thehillauto', 'cornbreadliberals', 'thenewcoldwar', 'esist', 'waexauto', 'unremovable', 'good_cake', 'technology', 'autonewspaper', 'sandersforpresident', 'autotldr', 'marchagainsttrump', 'goodlongposts', 'badgovnofreedom', 'libs', 'stupid_watergate', 'democracy', 'fcc', 'worldnews', 'nottheonion', 'breakingnews24hr', 'newsbotbot', 'fuckthealtright', 'environment', 'inthenews', 'hotandtrending', 'UMukhasimAutoNews', 'keep_track', 'PoliticalVideos', 'climate', 'cnet_all_rss', 'women', 'greed', 'huffpoauto', 'watchingcongress', 'restorethefourth', 'trussiagate', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'skydtech']

# Get the values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['wesley morgan', 'rep. morgan', 'rep morgan', 'representative morgan', 'congressman morgan']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://vrsws.sos.ky.gov/ovrweb/) \n\n"
        "No progressive candidate is running to represent Kentucky State House District 81. Know someone who should [run](https://www.runforoffice.org/elected_offices/33152-state-representative-ky-81/interest_form)? \n\n"

        "[Map of Kentucky State House District 81](http://www.lrc.ky.gov/GIS/HH001M01/District%20Maps/District%2081%20(HH001M01).pdf) \n\n"

        "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people.)")

        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
