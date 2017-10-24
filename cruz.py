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
            terms = ['ted cruz', 'sen. cruz', 'senator cruz', 'ted. cruz', 'middle-class Americans, including Texans, will see a tax increase', 't Work So Well for F.D.R.', 'Republicans Are Unsure What Trump Wants on Health Care', 'Texas Voters Familiar With Cruz', 'Cruz claims repealing the estate tax', 'Bernie calls GOP tax plan a \'Robin Hood proposal in reverse', 'Sanders, Cruz spar', 'Ted Lies Again', 'tedcruz', 'sanders vs. cruz', 'Bernie Sanders Tax Reform debate MegaThread', 'tries to sell tax reform to Democrats', 'for at Least 3rd Time in Two Months', 'Republicans Worry They\'ll Lose Congress', 'Republicans fear a \'bloodbath\' in midterm elections', 'Cruz: GOP could face', 'Watergate-level blowout', 'Cruz warns Koch donors re', 'CRUZ: MAYBE NEXT YEAR', 'Sanders, Cruz to Square Off Over in a Debate Over GOP', 'except Cruz', 'Cruz, Sanders to debate Trump', 'Cruz town hall debate on taxes', 'Where GOP senators stand on President Trump', 'Austin political consultant worked for Germany', 'Favorite Meme-Maker is Now Helping the Far-Right in Germany', 'Cruz grapples with GOP inaction under Trump', 'what democrats must do', 'morally repugnant and bad economic policy', 'collapse escalates Republican infighting', 'Republicans look to next year for Obamacare repeal', 'GOP already eyeing next chance', 'guts Obamacare even more', 'But They Just Might, Anyway', 'Al Franken keeps jabbing at Ted Cruz', 'outlines four-step plan to Medicare for all', 'pass this final test before it can come to a vote', 'GOP takes heavy fire over pre-existing conditions', 'insurer bailout could turn Texas blue', 'PolitiFact: Cruz and O', 'dis cruz', 'Cruz Bill Eases Revocations of U.S. Citizenship Without Due Process', 'states like Texas to request federal assistance after Harvey', 'Texas Congressmen voted against Sandy relief, now are begging for Harvey relief', 'hypocrisy on Harvey aid', 'Texas Lawmakers Who Voted Against Relief for Hurricane Sandy', 'Texas Republicans voted against aid', 'Socialist After a Natural Disaster', 'Cruz, Cornyn back Texas Gov\'s request for disaster declaration']
            for term in terms:
                search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.votetexas.gov/register-to-vote/) \n\n"
        "[**Beto O\'Rourke**](https://www.betofortexas.com/) is running against Ted Cruz. \n\n "
        "[Donate](https://secure.actblue.com/contribute/page/beto-homepage) | "
        "[Reddit](https://www.reddit.com/r/BetoORourke/) | "
        "[Facebook](https://www.facebook.com/betoorourke) | "
        "[Twitter](https://twitter.com/betoorourke) \n\n "
        "O\'Rourke supports universal health care, renewable energy, campaign finance reform, net neutrality, protecting Social Security, equal pay for equal work, LGBT equality, voting rights, and DACA.\n\n "

        "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")
        print("Bot replying to : ", submission.id, submission.title)
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

text_file.close()
local_subs.close()