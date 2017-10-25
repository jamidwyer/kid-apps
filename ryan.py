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
            terms = ['paul ryan', 'rep. ryan', 'congressman ryan', 'rep ryan', 'speaker ryan', '@speakerryan', '@IronStache', 'house speaker', 'Trump, GOP senators appear united on fighting for tax cuts', 'Ruse to Make Their Tax Plan Look Tough on Millionaires', 'Not a single GOP representative is rushing to defend Myeshia Johnson', 'Minimum Wage Is Poverty Trap for Millions of Americans', 'GOP tax plan would give foreign investors a', 'Why both major US parties look doomed', 'Tax reform has a long way to go', 'GOP has found an innovative way to steal', 'like tax reform bill on his desk closer to Thanksgiving', 'GOP Tax Plan Will Have Fourth Bracket for Top Earners, Could Lower Retirement Deductions', 'Tax Cuts for Wealthy a Bad Deal for Most Americans', 'Republican tax scam', 'Republicans are celebrating tax cuts', 'I hope no one lets him forget this in 2018', 'which tweets I will have to pretend that I didn\'t see', 'comedy routine for NY elite', 'Senate Approves Budget Plan That Smooths Path Toward Tax Cut', 'friends flee as frustration with Trump grows', 'the perils of doing a healthcare deal with Trump', '24 hours later, Senate health deal all but completely dead', 'Health care plan sponsor says Trump offers encouragement', 'Ryan opposes ObamaCare', 'posh hideaway bankrolled by secret corporate cash', 'Tax Myths And Republicans Are Taking Advantage Of It', 'Independent economists on why they aren\'t buying Trump', 'No Party for Honest Men', 'actually help the middle class. Here', 'Bernie Sanders wrote an opinion piece in the Guardian', 'John Kasich denounces Trump', 'robin hood in reverse', 'Every single thing GOP says about its tax plan is a flat lie', 'Trump Allies Worry that Losing the House Means Impeachment', 'Conservative army bolsters Trump on tax cuts', 'Mad When He Finds Out What His Policies Actually Do', 'Tax Cuts Are Bound to Increase the National', 'tax reform plans favor the wealthy', 'tax reform plans favor wealthy', 'Hill GOP touts tax reform before 2018', 'The G.O.P. Is a Mess', 'Biggest Enemy on Tax Reform', 'aimed at giving breaks to the middle class, not high-income earners', 'NRA opposes bump fire stocks bills in Congress', 's time to panic', 'tax plan gives the top 1 percent of households a ', 'savage fringe of the GOP is carefully advancing policies designed to enrich their true constituency', 'Challenges Pile Up for Republicans on Tax Reform', 'Ryan to Feuding Trump and Corker', 'Ryan urges ATF to fix', 'Ryan on Trump-Corker feud', 'You Better Learn Our Lesson', 'House Republicans shy away from action', 'only retiring Republicans will talk about Trump', 's Twitter Tantrum Threatens the G.O.P', 'tremendous compassion', 'Tax Break Repeal Will Kill GOP Plan', '\'moral courage\' on gun control legislation', 'swats away talk of gun control', 'Why the GOP tax plan could implode', 'It pays to be rich in the Trump era', 'Angry at Economists for Finding Their Tax Cuts Go to the Rich', 'Middle-Class Tax Hike', 'GOP tax plan would provide major gains for richest 1', 'Tax Cuts Would Go to Richest One Percent', 'Wisconsin\'s First Congressional District']
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