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

local_subs = open("kansas.dat", "r")
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
            terms = ['brownback', 'kobach', 'colyer', 'kansas governor', 'governor in kansas', 'State workers at site of shooting had guards, security until Kansas', 'Trump\'s Voter Fraud Commission', 'waging war on the right to vote', 'GOP Is Plowing Ahead with an Audacious Effort to Hijack the VotexR', 'Voter Commission Reveals Its Bias', 'voter-fraud propandist', 'GOP to Latinos: Drop Dead', 'testify at Trump voter commission meeting', 'Voter Fraud Commission Clashes Over New Hampshire Count', 'Trump official accused 5,000 people of voter fraud with no proof', 'Lawsuits, Falsehoods, and a Lot of White Men', 'kansas republican governance experiment', 'Voter Fraud Panel, No Stranger to Controversy', 'Trump adviser caught in gleeful, racist tirade', 'house minority leader jim ward', 'Trump Voter Fraud Probe', '\"election integrity commission\"', 'Trump\'s voter-fraud panel', 'Trump\'s election commission co-chair', '\'election integrity\' panel', 'The Trump Administration Is Planning an Unprecedented Attack on Voting Rights', 'Trump voting panel', 'Trump voter fraud panel head', 'punishing public officials who disenfranchise voters']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://www.kdor.ks.gov/apps/voterreg/default.aspx) by July 17, 2018 \n\n"
            "[Sign up to vote by mail](http://www.kssos.org/forms/elections/AV1.pdf) \n\n\n"

            "[**Jim Ward**](https://kansasforward.com) is running to be Governor of Kansas. \n\n"
            "[Donate](https://secure.actblue.com/donate/kansasforward) | "
            "[Facebook](https://www.facebook.com/RepJimWard/) | "
            "[Twitter](https://twitter.com/repjimward) \n\n"
            "Ward supports universal health care, public schools, LGBTQ equality, protecting Medicare, and voting rights. \n\n\n"

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

            "Primary Election: August 7, 2018 | General Election: November 6, 2018 \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")
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

text_file.close()
local_subs.close()