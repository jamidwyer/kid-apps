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

subs = ['enoughtrumpspam', 'orangecounty', 'political_revolution', 'worldnews', 'bluemidterm2018', 'california_politics', 'politicaltweets', 'technology', 'impeach_trump', 'autotldr', 'esist', 'indepthstories', 'keepournetfree', 'democrats', 'thehillauto', 'democracy', 'waexauto', 'unremovable', 'badgovnofreedom', 'thenewcoldwar', 'politicalvideo', 'autonewspaper', 'chapotraphouse', 'sandersforpresident', 'environment', 'keep_track', 'liberal', 'women', 'cornbreadliberals', 'greed', 'watchingcongress', 'restorethefourth', 'libs', 'indivisibleguide', 'politicalrevolutionca', 'goodlongposts', 'theconstitution', 'reddit.com', 'wayofthebern', 'climate', 'cnet_all_rss', 'pancakepalpatine', 'nottheonion', 'skydtech', 'PoliticalVideos', 'huffpoauto', 'geprnotes', 'politicalcalifornia', 'trussiagate']

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=2000):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            if re.search("rohrabacher", submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://registertovote.ca.gov/) \n\n"
                    "[**Tony Zarkades**](https://www.tonyzforcongress.org/on-the-issues) is running against Dana Rohrabacher. \n\n"
                    "[Donate](https://secure.actblue.com/contribute/page/tonyzforcongress) | "
                    "[Facebook](https://www.facebook.com/tonyzforcongress/) | "
                    "[Twitter](https://twitter.com/tonyz4congress) \n\n"
                    "Zarkades supports single-payer health care, living wages, paid family leave, Social Security, Medicare, "
                    "affordable college, equal pay for equal work, renewable energy, common-sense gun control, funding "
                    "science and the EPA, DACA, and a path to citizenship for hard-working, law-abiding people, while "
                    "deporting criminals. \n\n\n"

                    "[**Laura Oatman**](https://www.tonyzforcongress.org/on-the-issues) is running against Dana Rohrabacher. \n\n"
                    "[Donate](https://act.myngp.com/Forms/4363798847687232000) | "
                    "[Facebook](https://www.facebook.com/OatmanforCongress/) | "
                    "[Twitter](https://twitter.com/Laura_Oatman) \n\n"
                    "Oatman supports single-payer health care, public schools, IDEA, "
                    "affordable college, equal pay for equal work, and renewable energy. \n\n\n"

                    "[**Harley Rouda**](https://harleyforcongress.com/issues/) is running against Dana Rohrabacher. \n\n"
                    "[Donate](https://secure.actblue.com/contribute/page/rouda) | "
                    "[Facebook](https://www.facebook.com/HarleyforCongress/) | "
                    "[Twitter](https://twitter.com/HarleyRouda) \n\n"
                    "Rouda supports universal health care coverage, "
                    "equal pay for equal work, renewable energy, standing with our international "
                    "allies, LGBTQ equality, and funding science. \n\n\n"

                    "[**Michael Kotick**](http://kotickforcongress.com/priorities/) is running against Dana Rohrabacher. \n\n"
                    "[Donate](https://www.crowdpac.com/campaigns/264265/michael-kotick-for-us-congress) | "
                    "[Facebook](https://www.facebook.com/KotickForCongress/) | "
                    "[Twitter](https://twitter.com/Kotick4Congress) \n\n"
                    "Kotick supports universal health care coverage, Medicare, "
                    "equal pay for equal work, renewable energy, LGBTQ equality, funding science, and a path to "
                    "citizenship for hard-working, law-abiding people, while deporting criminals. \n\n\n"

                    "Map of California District 48: https://www.govtrack.us/congress/members/CA/48 \n\n"

                    "^(I'm a bot and I'm learning. Let me know if I can do better. It's a lot of "
                    "work to add all this info, but if you prefer a different candidate, let me know, and I'll add them.)")
                submission.reply(text)
                print("Bot replying to : ", submission.title)

                # Store the current id into our list
                posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
