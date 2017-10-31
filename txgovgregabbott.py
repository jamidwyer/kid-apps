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

local_subs = open("texas.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['greg abbott', 'texas governor', 'TX\'s next governor ', 'Texans are more open to legalizing marijuana', 'Harvey Relief Program Nixes Requirement to Not Boycott Israel', 'caveat is the result of a strange new state law', 'Abbott Plan to Amend Constitution', 'Texas Is No Longer Feeling Miraculous', 'The Racist Map Wins', 'Democrats Must Take a Shot at Texas', 'Federal Judge Blocks Texas', 'rolando pablos', 'Texas Republican turns down donated blankets', 'Judge blocks provisions in Texas law punishing \'sanctuary cities\'', 'bill restricting insurance coverage of abortion', 'governor of texas', 'tx gov', 'runs for governor in Texas', '@gregabbott_tx', 'Texas crackdown on sanctuary cities', 'sb-4', 'sb4', 'sb 4', 'Senate Bill 4', 'rape insurance', 'Texas\' redistricting fight', 'tx governor\'s']
            for term in terms:
                blend_in = 0
                if subreddit == "twoxchromosomes":
                    blend_in = 1
                fb_link = 1
                if subreddit == "twoxchromosomes":
                    fb_link = 0
                twitter_link = 1
                if subreddit == "twoxchromosomes":
                    twitter_link = 0
                donate_link = 1
                if subreddit == "twoxchromosomes":
                    donate_link = 0
                search(term, submission, blend_in, fb_link, twitter_link, donate_link);

def search(term, submission, blend_in, fb_link, twitter_link, donate_link):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post

        vote_link = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.votetexas.gov/register-to-vote/where-to-get-an-application-2.html) \n\n")

        if blend_in:
            vote_link = ("[Register To Vote](http://www.votetexas.gov/register-to-vote/where-to-get-an-application-2.html) \n\n")

        dems = ("[**Jeffrey Payne**](http://www.jeffrey4texas.com/) is running to be Governor of Texas. \n\n"
            "[Donate](https://secure.actblue.com/donate/jeffrey4texas) | "
            "[Facebook](https://www.facebook.com/Jeffrey4Texas/) | "
            "[Twitter](https://twitter.com/Jeffrey4Texas) \n\n"
            "Payne supports renewable energy, public schools, living wages, equal pay for equal work, and LGBTQ equality. \n\n\n")

        # This disclaimer works
        disclaimer = ("^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")

        text = '\n'.join([vote_link, dems, disclaimer])

        print("Bot replying to : ", submission.title)
        submission.reply(text)

        # Store the current id into our list
        posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

text_file.close()
local_subs.close()