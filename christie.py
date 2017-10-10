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

local_subs = open("newjersey.dat", "r")
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
            terms = ['chris christie', 'guadagno', 'n.j. governor', 'new jersey governor', 'nj gubernatorial', 'NJ\'s next governor ', 'governor of new jersey', 'nj gov', 'nj governor', 'Mark Kelly to Lawmakers Opposing Gun Laws', 'The Independents: New Jersey', 'Do you think this gov election will be a referendum on Trump', 'close governor\'s beach house during shutdowns', 'loyal enough to Trump after Billy Bush tape', 'Seth Kaper-Dale: Don', '\"Access Hollywood\" tape was a \"litmus test\"', 'response to lewd Trump tape', 'christie\'s secret attorney fee']
            for term in terms:
                include_green = 1
                if subreddit == "bluemidterm2018":
                    include_green = 0

                search(term, submission, include_green);

def search(term, submission, include_green):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        vote_link = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.state.nj.us/state/elections/voting-information.html) by October 17, 2017 \n\n")
        election_date = ("Election: November 7, 2017 | [Sign up to vote by mail](http://www.njelections.org/voting-information-vote-by-mail.html) \n\n")

        green = ""

        if include_green:
            green = ("[**Seth Kaper-Dale**](https://www.kaperdaleforgovernor.com/) is running to be Governor of New Jersey. \n\n"
                "[Donate](https://www.kaperdaleforgovernor.com/donate/) | "
                "[Reddit](https://www.reddit.com/r/SethKaperDale/) | "
                "[Facebook](https://www.facebook.com/kaperdaleforgovernor) | "
                "[Twitter](https://twitter.com/KaperDaleForGov) \n\n"
                "Kaper-Dale supports single payer Medicare for all, renewable energy, public schools, living wages, paid sick leave, affordable college, equal pay for equal work, LGBTQ equality, DACA, and legalizing marijuana. \n\n\n")

        dems = ("[**Phil Murphy**](https://www.murphy4nj.com/issues) is running to be Governor of New Jersey. \n\n"
            "[Donate](https://act.myngp.com/Forms/2599649002085616384) | "
            "[Facebook](https://www.facebook.com/PhilMurphyNJ) | "
            "[Twitter](https://twitter.com/PhilMurphyNJ) \n\n"
            "Murphy supports renewable energy, public schools, living wages, paid sick leave, affordable college, equal pay for equal work, LGBTQ equality, background checks on all gun sales, and legalizing marijuana. \n\n\n")

        with open('disclaimer.txt', 'r') as myfile:
            disclaimer=myfile.read().replace('\n', '')

        text = '\n'.join([vote_link, election_date, green, dems, disclaimer])
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