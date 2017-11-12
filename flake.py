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
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:


            # Do a case insensitive search
            terms = ['^(?!.*snowflake).*flake.*$', '@jeffflake', 'sinema', 'Kelli Ward', 'No Reason To Think Republicans Will Be In Better Shape', 'Most and Least Popular Senators', 'GOP senators dismiss calls for bill to protect Mueller from Trump', 'Congress can stop Trump from starting World War', 'Millennials will shape future of GOP', 'Conservatives to Trump critic McSally', 'Democrats are split on whether to support Trump', 'thank you for saying mean things to the bad man', 'fake things true and true things fake', 'The Happy Hooker Conservatives', 'Republicans won\'t quit Trump', 'GOP braces for what’s next amid Corker, Flake tumult', 'Republicans Need a Better Response Besides Quitting', 'Republican senators attacks on Donald Trump', 'Welcome to the Senate Mr. Arpaio', 'Female candidates are targeting 3 key Senate seats in 2018', 'As midterms approach, GOP', 'GOP donors hearing new warnings about impeachment', 'Ajit Pai gets 4 more years as head of FCC', 'Ajit Pai gets new term on FCC despite protest', 'Senate Democrats voted to give Ajit Pai another term', 'Ajit Verizon Pai gets new term', 'Senators voted to reconfirm Ajit Pai', 'Senate reconfirms Ajit Pai as FCC chairman', 'Ajit Pai nomination confirmed', 't tearing themselves apart', 'Vulnerable GOP senator callously admits repeal bill', 'Congress Has Always Let Dreamers Down', 'The Republican Plan for a One-Party State', 'Republicans completely own Trump\'s Arpaio pardon', 'empty words against Trump', 'Against Trump, Republicans are all talk and no action']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
            text = ("Arizona 2018 Election \n\n"
                "[Voter Registration Deadline](https://servicearizona.com/webapp/evoter/register?execution=e1s2): July 30, 2018 \n\n"
                "[Primary Election](https://www.vote.org/absentee-ballot/): August 28, 2018 \n\n"
                "[General Election](https://www.vote.org/absentee-ballot/): November 6, 2018 \n\n")
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