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

local_subs = open("pennsylvania.dat", "r")
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
            terms = ['Trump asks that supporters not hurt protesters', 'Failing in Wisconsin, Pennsylvania and Michigan', 'pittsburgh public schools', 'philadelphia workers', 'Gunmen Run Around Van Shooting at Each Other', 'philly student climate strike', 'pennsylvania state sen', 'now ban ar-15s', 'Sanders 746k individual donors', 'universal background checks are off the table', 'trump says pennsylvania chemical plant', 'Shell Workers Had To Attend Trump Speech', 'Same Lie for the 80th Time', 'pa rally', 'trumpsbodycount', 'data on white supremacist terrorism', 'white nationalist killers', 'law lets pennsylvania', 'freed after 27 years in prison', 'person of color. I\'m white', 'White GOP congressman says he isn', 'political power from urban pennsylvania', 'robber returns money to philly store', 'FBI and ICE use DMV photos', 'courthouse in hanover, pa', 'pa-10', 'senatormuth', 'Ten cities say Trump owes them money', 'legislation that would benefit victims of child sex abuse', 'Sunday collections on political lobbying', 'economic patriotism', 'nfL player aims to destigmatize marijuana use', 'pennsylvania transgender', 'Trump Would Have Lost Election Without Russian Help', 'key states like pennsylvania', 'philadelphia prosecutor', 'trump would beat biden', 'ajit pai gets a whopping', 'poll numbers in pennsylvania', 'dropped a bomb on a black neighborhood', 'haircuts to the homeless in the middle of a busy street', 'synagogue massacre', 'atrocities like pittsburgh', 'pittsburgh massacre', 'tree of life synagogue', 'pittsburgh shoot', 'robert bowers', 'jews in pittsburgh', 'pennsylvania rally', 'pa-17', 'pa-01', 'bob casey', 'brendan boyle', 'pa-7', 'pa-07', '^(?!.*john meehan).*meehan.*$', 'pa hd150', 'pa-7', 'pa state rep', 'pennsylvania primaries', 'pennsylvania governor', 'primary in Pennsylvania', 'primaries in pennsylvania', 'pa34', 'summer lee', 'progressives in pennsylvania', 'innamorto', 'pa state house', 'pa hd-178', 'socialists in pennsylvania', 'terri mitko', 'fetterman', 'pa 184', 'candidate in pennsylvania', 'pa11', 'house race in pennsylvania', 'impeach PA Supreme Court', 'santorum', 'pa01', 'pennsylvania Republican state legislator', 'larry krasner', 'pa gerrymandering', 'Women Run in Pennsylvania', 'nick miccarelli', 'saccone', 'conor lamb', 'pa.\'s redistricting', 'christina hartman', 'rep costello', 'congressman costello', 'representative costello', 'rep. costello', 'New Congressional Map in Pennsylvania', 'Pennsylvania\'s Gerrymandered Congressional Map', 'Daryl Metcalfe', 'pennsylvania voters', 'PA\'s new congressional map', 'New map for Pennsylvania', 'Pennsylvania House District', 'hal english', 'pennsylvania voting map', 'new Pennsylvania map', 'pa. congress', 'turzai', 'Pennsylvania congress', 'Pennsylvania GOP lawmaker', 'pa redistricting', 'Pennsylvania GOP\'s leading Senate candidate', 'Pa. governor', 'lou barletta', 'marijuana in PA.', 'Vincent Hughes', 'PA\'s 16th Congressional', 'stable genius act', 'Pennsylvania redistricting', 'pennsylvania state senate', 'smucker', 'pa-16', 'joe billie', 'pennsylvania gerrymandering', 'ryan costello']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        # No early voting
        text = ("Pennsylvania 2020 Election \n\n"
            "[Register to Vote](https://www.pavoterservices.pa.gov/Pages/VoterRegistrationApplication.aspx) \n\n"
            "[Primary Election](https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx): April 28, 2020 \n\n"
            "[General Election](https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx): November 3, 2020 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()