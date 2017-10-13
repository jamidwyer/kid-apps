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
            terms = ['paul ryan', 'rep. ryan', 'congressman ryan', 'rep ryan', 'speaker ryan', '@speakerryan', '@IronStache', 's time to panic', 'tax plan gives the top 1 percent of households a ', 'savage fringe of the GOP is carefully advancing policies designed to enrich their true constituency', 'Challenges Pile Up for Republicans on Tax Reform', 'Ryan to Feuding Trump and Corker', 'Ryan urges ATF to fix', 'Ryan on Trump-Corker feud', 'You Better Learn Our Lesson', 'House Republicans shy away from action', 'only retiring Republicans will talk about Trump', 's Twitter Tantrum Threatens the G.O.P', 'tremendous compassion', 'Tax Break Repeal Will Kill GOP Plan', '\'moral courage\' on gun control legislation', 'swats away talk of gun control', 'Why the GOP tax plan could implode', 'It pays to be rich in the Trump era', 'Angry at Economists for Finding Their Tax Cuts Go to the Rich', 'lose your chance to take healthcare away from 16 million people', 'Middle-Class Tax Hike', 'About Gun Control We Refuse To Pass', 'promise middle class benefits or Trump tax returns while pushing tax reform', 's in the right place\' on race', 'have any congressional Republicans denounced the president’s tweets', 'An Act Of Political Domination By The Rich', 'Trump tax reform overhaul is a pipe dream', 'The Growth Effects of Tax Policy', 'Tax cuts don\'t equal growth', 'Tax Cuts Shrink Over Time for Everyone but the Richest', 'GOP tax plan would provide major gains for richest 1', 'Tax Cuts Would Go to Richest One Percent', 'A Very Taxing President', '1 billion under his tax plan', 'Republican-proposed changes to the tax plan', 'Trump and Republicans want to Repeal the Estate Tax', 'GOP tax plan would provide major gains for richest 1 percent', 'Republican tax plan', 'increase the Deficit by Six Trillion Dollars', 'Sell the GOP Tax Plan to Working-Class Americans', 'bonanza for the rich', 'gop tax plan is a lie', 'Most Sweeping Tax Overhaul in Decades', 'Trump\'s massive tax cut -- for the rich', 'GOP plan cuts corporate, individual taxes and repeals the estate tax', 'Tax Plan Is a Pointless Gift to the Wealthy', 'Trump and Ryan claimed victory on healthcare when the AHCA passed', 'Trillions in Tax Breaks for the Rich', 'GOP Tax plan could cost', 'GOP over tax cuts for the rich', 'and raise the bottom one', 'Republicans agree to raise bottom tax rate', 'Opinion of the Republican Party falls to all-time low', 'Trump to See Tax Plan That Targets', 'GOP to cut top rate to 35 percent', 'GOP eyes corporate tax rate of 20 percent', 'Republicans Can\'t Defend The Graham-Cassidy Health Care Bill', 'Even Pretending This Is About Healthcare Anymore', 'Republican Leaders Defy Bipartisan Opposition to Health Law Repeal', 'ObamaCare insurance fix difficult', 'GOP has hope for Obamacare repeal bill', 'To make their tax plan work', 'September and Republicans still can', 'Trump sides with Democrats over length of debt limit hike', 'GOP leaders made a huge wager', 'bipartisanship signals warning for GOP', 'Trump welcome to the resistance', 'Republican plans into chaos', 'GOP leaders don\'t have a plan', 'GOP Will Settle For The Usual Litany Of Tax Cuts', 'Freedom Caucus Member Blames GOP Leadership For Trump', 'Trump lashes out at GOP', 'distracted boyfriend meme of Trump checking out Schumer', 'Republicans Angry at Economists for Finding Their Tax Cuts Go to the Rich', 'Republicans Will Let America Burn', 'Wisconsin\'s First Congressional District']
            for term in terms:
                 search(term, submission);

def search(term, submission):
            if re.search(term, submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://myvote.wi.gov/en-us/registertovote) \n\n"
                    "[**Randy Bryce**](https://randybryceforcongress.com/) is running against Paul Ryan. \n\n"
                    "[Donate](https://secure.actblue.com/donate/randy-bryce-for-congress-1) | "
                    "[Reddit](https://www.reddit.com/r/RandyBryce) | "
                    "[Facebook](https://www.facebook.com/RandyBryce2018) | "
                    "[Twitter](https://twitter.com/IronStache) \n\n"
                    "Bryce supports universal health care, living wages, protecting Social Security and Medicare, affordable college, renewable energy, campaign finance reform, and DACA. \n\n\n"

                    "[**Cathy Myers**](https://cathymyersforcongress.com/) is running against Paul Ryan. \n\n"
                    "[Donate](https://secure.actblue.com/donate/cathy-for-congress-1?refcode=website) | "
                    "[Facebook](https://www.facebook.com/cathymyersforcongress/) \n\n"

                    "[Map of Wisconsin District 1](https://www.govtrack.us/congress/members/WI/1) \n\n"

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