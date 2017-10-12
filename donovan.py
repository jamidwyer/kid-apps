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

local_subs = open("newyork.dat", "r")
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
            terms = ['daniel donovan', 'dan donovan', 'ny-11', 'rep. donovan', 'rep donovan', 'representative donovan', 'congressman donovan', 'michael grimm', 'GOP incumbent over Grimm']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://voterreg.dmv.ny.gov/MotorVoter/) \n\n"
            "[Find your poll site](https://nyc.pollsitelocator.com/search)\n\n"

            "[**Mike DeCillis**](http://mikedecillis.com/) is running to represent New York House District 11. \n\n"
            "[Facebook](https://www.facebook.com/mikedecillis/) | "
            "[Twitter](https://twitter.com/Mike_DeCillis) | "
            "[Volunteer](http://mikedecillis.com/join.php) | "
            "[Donate](https://secure.actblue.com/donate/mike-decillis-for-congress-1) \n\n"
            "DeCillis supports single-payer health care, public schools, a living wage, paid family leave, affordable child care, equal pay for equal work, renewable energy, LGBTQ equality, DACA, public transportation, and community policing. \n\n\n"

            "[**Michael DeVito**](https://www.devitoforcongress.com/) is running to represent New York House District 11. \n\n"
            "[Facebook](https://www.facebook.com/michaeldevitojr/) | "
            "[Twitter](https://twitter.com/mdevitojr) | "
            "[Volunteer](https://www.devitoforcongress.com/get-involved) | "
            "[Donate](https://secure.actblue.com/donate/devitoforcongress) \n\n"
            "DeVito supports single-payer health care, public schools, a living wage, protecting Social Security, equal pay for equal work, renewable energy, and LGBTQ equality. \n\n\n"

            "[**Omar Vaid**](https://www.omarvaid.com/) is running to represent New York House District 11. \n\n"
            "[Facebook](https://www.facebook.com/omarvaid) | "
            "[Twitter](https://twitter.com/omarvaid) | "
            "[Volunteer](https://www.omarvaid.com/volunteer/) | "
            "[Donate](https://secure.actblue.com/donate/omarvaid) \n\n"
            "Vaid supports Medicare for all, public schools, protecting Social Security, renewable energy, and net neutrality. \n\n\n"

            "[Map of New York House District 11](https://www.govtrack.us/congress/members/NY/11) \n\n"

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