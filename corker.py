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

local_subs = open("tennessee.dat", "r")
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
            terms = ['How Republicans Got Trump Catastrophically Wrong', 'Trump-Corker spat complicates drive for tax reform', 'bob corker', 'sen. corker', 'mackler', 'blackburn', 'corker\'s u.s. senate seat', 'replace corker', 'Senate narrowly passes 2018 budget', 'Participated in Normalizing', 'TWITTER shuts down anti-abortion campaign video', 'disgusting lies about Planned Parenthood', 'Senate candidate from advertising false claim about Planned Parenthood', 'Corker fight', 'baby body parts', 'Twitter takes down GOP lawmaker', 'alliance with powerful Republican senator broke down into verbal warfare', 'become an adult day care center', 'announces her bid by trashing the Republican Senate', 'Berke considering run', 'Budget battles loom on Capitol Hill', 'tax reform will make health care look like', 'peyton manning', 'andy ogles', 'senator corker', 'Corkers seat', '1.5 Trillion Revenue-Losing Tax Cut', 'Republicans vs. Economists', 'debt. Republicans have a plan to make it worse', 'White House plan for tax cuts moves forward', '1.5 Trillion Tax Cut', 'senate foreign relations committee chairman', 'GOP tentatively agrees to $1.5 trillion plan on tax cuts', 'Senate votes down bipartisan push for new']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://ovr.govote.tn.gov/Registration/#BM) by July 3, 2018 \n\n"
        "[**Justin Kanew**](http://www.kanewforcongress.com/) is running to represent Tennessee in the United States Senate. \n\n"

        "[Facebook](https://www.facebook.com/KanewforCongress/) | [Twitter](https://twitter.com/kanew) | [Volunteer](http://www.kanewforcongress.com/volunteer) | [Donate](https://secure.actblue.com/donate/kanew-for-congress-1) \n\n"

        "Kanew supports Medicare for all, public schools, affordable college, universal pre-K, paid family leave and child care assistance, equal pay for equal work, renewable energy, campaign finance reform, LGBTQ equality, net neutrality, and legalizing medical marijuana. \n\n"

        "[**Bill Bailey**](http://www.electbillbailey.com) is running to represent Tennessee in the United States Senate. \n\n "
        "[Facebook](https://www.facebook.com/Bill-Bailey-for-Senate-137311173532373/) | "
        "[Twitter](https://www.twitter.com/officialbbailey) | "
        "[Volunteer](https://electbillbailey.com/volunteer) | "
        "[Donate](https://www.crowdpac.com/campaigns/335068/bill-bailey) \n\n"
        "Bailey supports Medicare for all, protecting Social Security, and affordable college. \n\n\n"

        "[**James Mackler**](https://www.jamesmackler.com/) is running to represent Tennessee in the United States Senate. \n\n "
        "[Facebook](https://www.facebook.com/JamesMacklerForSenate/) | "
        "[Twitter](https://twitter.com/james_mackler) | "
        "[Volunteer](https://www.jamesmackler.com/action/) | "
        "[Donate](https://secure.actblue.com/donate/james-mackler-1) \n\n"
        "Mackler supports universal health care, public schools, and affordable college. \n\n\n"

        "Primary Election: August 2, 2018 | General Election: November 6, 2018 \n\n"
        "[Find your polling place](http://web.go-vote-tn.elections.tn.gov/) \n\n"

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

text_file.close()
local_subs.close()