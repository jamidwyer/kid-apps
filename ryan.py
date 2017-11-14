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

local_subs = open("wisconsin.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['paul ryan', 'rep. ryan', 'congressman ryan', 'rep ryan', 'speaker ryan', '@speakerryan', 'IronStache', 'house speaker', 'Republican leaders are placing tribal loyalty ahead of their constitutional responsibility', 'The Mueller investigation is making the Republican tax plan rollout', '5.8 Trillion Bank Heist', 'forget we still have all the Hillary activity', 'Gearing Up for War on the Rule of Law', 'The Huge Tax Heist', 'The Ignorance of Trump', 'dossier documents to Congress next week', 'Republicans see need for speed', 'Ryan finds new ways to downplay concerns about Trump', 'Trump-GOP tax plan', 'GOP tax plan would cost', 'new gilded age', 'disaster for American children and families', 'tax reform push is already in bad shape', 'far from sufficient', 'House narrowly passes budget', '1.5 trillion tax cut', '1.8 trillion in health care cuts', 'huge vote on tax reform', 'New Polls Suggest Trump and the GOP', 'GOP tax plan declares war on everyone who isn', 'The Republican budget is disgraceful', '700 Billion Gift to Wealthy Foreigners', 'The American oligarchy prepares a new tax windfall for the rich', 'Trump tax plan benefits rich, companies', 'Endangering His Prized Tax Cuts', 'Trying to Get Taxes Cut', 'Trump, GOP senators appear united on fighting for tax cuts', 'Ruse to Make Their Tax Plan Look Tough on Millionaires', 'Not a single GOP representative is rushing to defend Myeshia Johnson', 'Minimum Wage Is Poverty Trap for Millions of Americans', 'GOP tax plan would give foreign investors a', 'Why both major US parties look doomed', 'Tax reform has a long way to go', 'GOP has found an innovative way to steal', 'like tax reform bill on his desk closer to Thanksgiving', 'GOP Tax Plan Will Have Fourth Bracket for Top Earners, Could Lower Retirement Deductions', 'Tax Cuts for Wealthy a Bad Deal for Most Americans', 'Republican tax scam', 'Republicans are celebrating tax cuts', 'I hope no one lets him forget this in 2018', 'which tweets I will have to pretend that I didn\'t see', 'comedy routine for NY elite', 'Senate Approves Budget Plan That Smooths Path Toward Tax Cut', 'friends flee as frustration with Trump grows', 'the perils of doing a healthcare deal with Trump', '24 hours later, Senate health deal all but completely dead', 'Health care plan sponsor says Trump offers encouragement', 'Ryan opposes ObamaCare', 'posh hideaway bankrolled by secret corporate cash', 'Middle-Class Tax Hike', 'Wisconsin\'s First Congressional District']
            for term in terms:
                 search(term, submission);

def search(term, submission):
            if re.search(term, submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("Wisconsin 2018 Election \n\n"
                    "[Voter Registration Deadline](https://myvote.wi.gov/en-us/registertovote): August 14, 2018 \n\n"
                    "[Primary Election](https://myvote.wi.gov/en-us/FindMyPollingPlace): August 14, 2018 \n\n"
                    "[General Election](https://myvote.wi.gov/en-us/FindMyPollingPlace): November 6, 2018 \n\n")
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