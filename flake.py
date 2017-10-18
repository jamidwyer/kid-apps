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

local_subs = open("arizona.dat", "r")
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
            terms = ['^(?!.*snowflake).*flake.*$', 'sinema', 'Kelli Ward\'s Senate Campaign', 'GOP donors hearing new warnings about impeachment', 'Ajit Pai gets 4 more years as head of FCC', 'Ajit Pai gets new term on FCC despite protest', 'Senate Democrats voted to give Ajit Pai another term', 'Ajit Verizon Pai gets new term', 'Senators voted to reconfirm Ajit Pai', 'Senate reconfirms Ajit Pai as FCC chairman', 'Ajit Pai nomination confirmed', 't tearing themselves apart', 'Vulnerable GOP senator callously admits repeal bill', 'Congress Has Always Let Dreamers Down', 'The Republican Plan for a One-Party State', 'Republicans completely own Trump\'s Arpaio pardon', 'empty words against Trump', 'Against Trump, Republicans are all talk and no action']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://servicearizona.com/webapp/evoter/register?execution=e1s2) by July 30, 2018 \n\n"
            "[Sign up to vote by mail](https://www.vote.org/absentee-ballot/) \n\n\n"

            "[**Deedra Abboud**](http://deedra2018.com/) is running against Jeff Flake. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/deedra-2018) | "
            "[Facebook](https://www.facebook.com/Deedra2018/) | "
            "[Twitter](https://twitter.com/deedra2018) \n\n"
            "Abboud supports health care for all Americans, public schools, protecting Social Security, LGBTQ equality, and net neutrality. \n\n\n"

            "[**Kyrsten Sinema**](http://kyrstensinema.com/) is running against Jeff Flake. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/kyrstensinema) | "
            "[Facebook](https://www.facebook.com/ksinemaaz/) | "
            "[Twitter](https://twitter.com/kyrstensinema) \n\n"
            "Sinema supports renewable energy, increasing the minimum wage, protecting Social Security and Medicare, and equal pay for equal work. \n\n\n"

            "Primary Election: August 28, 2018 | General Election: November 6, 2018 \n\n"
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