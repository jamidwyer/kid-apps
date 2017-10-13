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

text_file = open("standardsubs.dat", "r")
subs = text_file.read().split('\n')

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['gun giveaway fundraiser 2 weeks after Las Vegas massacre', 'Two Guns Per Person', 'Shooting at Coastal Caroline University', 'gap between first shots and concert massacre', 'NRA Defends the Indefensible', 'Allow people with open arrest warrants to buy guns', 'suing bump-stock manufacturers', 'change allows some facing arrest to buy guns', 'daily gun death', '64 Percent Support Stricter Gun Laws After Vegas Massacre', 'Girlfriend Got More Media Coverage Than the Shooter Himself', 'How Chicago gets its guns', 'memorializing Las Vegas shooting victims', 'Gun Rights Need Limits' 'Texas Tech Active Sooter', 'gunman shot security guard', 'For anyone with strong opinions on guns', 'Victims of Las Vegas massacre struggle', 'NRA opposes outright U.S. ban on gun devices used by Las Vegas killer', 'NRA opposes outright U.S. ban on gun devices used by Las Vegas killer', 'mum over gun issues after Vegas deaths', 'Celebrated the Las Vegas Massacre', 'we want to shoot at police and military if we decide to', 'empty words and moments of silence', 'doing Nothing Isn\'t Working', 'Superstition helps explain how people think about gun laws', 'silence insults the dead', 'God Killed Those People\' Who Died In Las Vegas', 'Surprising as NRA Urges Less Restrictive Gun Laws After Las Vegas', 'Las Vegas shooting motive eludes investigators', 'Just how gun owners think', 'How Las Vegas Shattered Country Music', 'Afraid to Talk About Guns', 'Mass Shooter\'s Bizarre Behavior', 'the NRA is safe', 'Las Vegas survivors furious', 'like a ghost when he came in', 'Gun Toting Maniacs', 'NRA poured more than', 'research gun violence because of NRA', 'Call for blood donors', 'giving blood can save lives']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[Give Blood](http://www.redcross.org/give-blood) | [Contact your state legislator](https://openstates.org/find_your_legislator/)")
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