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
            terms = ['Nevada gun shows tied to firearm violence in California', 'Gun Injuries Spike After Nevada Gun Shows', 'neo-Nazi Shooting', '500 Americans Were Shot Down in Vegas', 'gunshots', 'gun owner blames theft of', 'Las Vegas shooting was staged', 'the nra', 'no one is charged with gun-trafficking', 'Would Impeaching Trump Set Off a Citizens', 'police officer killed in massacre', 'lenient concealed carry laws linked with increases in homicide', 'Hell-Bent on Keeping Its Guns', 'nra whines', 'nra ad', 'most ruthless attack on a president', 'More Gun Violence Research', 'Shooting suspect arrested', '6 shot, 3 killed', 'request for protection from Edgewood, Maryland shooting suspect', 'Mass Killings Not On The Rise Over Past Decade', 'gun violence researchers discover', 'gun control debate', 'Insane Conspiracy Theories About the Vegas Shooter', 'shooting in Maryland', 'shooting at Maryland office park', 'active shooter', 'Americans Widely Support Tighter Regulations on Gun Sales', 'resolution honoring Las Vegas shooting victims', 'second shooter in Las Vegas', 'Shots fired at Plano office building', 'Concertgoers Became Medics', 'in the wake of the Las Vegas shooting', 'Dip in visitors', 'on lockdown after shooting on campus', 'Protects Gunmakers After Mass Shootings Like Las Vegas', 'lock down after shooting on campus', 'NRA spokeswoman', 'Las Vegas massacre', 'Two Guns Per Person', 'Shooting at Coastal Caroline University', 'gap between first shots and concert massacre', 'NRA Defends the Indefensible', 'Allow people with open arrest warrants to buy guns', 'suing bump-stock manufacturers', 'change allows some facing arrest to buy guns', 'daily gun death', 'Gun Rights Need Limits', 'empty words and moments of silence', 'doing Nothing Isn\'t Working', 'silence insults the dead', 'Call for blood donors', 'giving blood can save lives']
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