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
            terms = ['andy barr', 'rep. barr', 'rep barr', 'representative barr', 'congressman barr', 'kentucky\'s 6th congressional district', 'ky-6', 'ky-06', 'Kentucky\’s 6th Congressional District', 'Canceling healthcare subsidies will hurt Americans in pro-Trump states the most', 'Fighter pilot candidate in Kentucky', 'Democrats Turn To Veterans For 2018 Races']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://sos.tn.gov/products/elections/register-vote) \n\n"
        "[**Reggie Thomas**](http://www.reggie4ky.com/) is running against Andy Barr. \n\n "
        "[Donate](https://act.myngp.com/Forms/6846395089445325568) | "
        "[Facebook](https://www.facebook.com/ReggieThomasKY/) | "
        "[Twitter](https://twitter.com/ReggieThomasKY) \n\n "
        "Thomas supports universal health care and public schools. \n\n"

        "[**Amy McGrath**](https://www.amymcgrathforcongress.com/) is running against Andy Barr. \n\n "
        "[Donate](https://secure.actblue.com/donate/amy-mcgrath-for-congress) | "
        "[Reddit](https://www.reddit.com/r/AmyMcGrath/) | "
        "[Facebook](https://www.facebook.com/AmyMcGrathKY/) | "
        "[Twitter](https://twitter.com/AmyMcGrathKY) \n\n "

        "[Map of Kentucky District 6](https://www.govtrack.us/congress/members/KY/6) \n\n"

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
