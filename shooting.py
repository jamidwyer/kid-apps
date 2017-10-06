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
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Superstition helps explain how people think about gun laws', 'silence insults the dead', 'God Killed Those People\' Who Died In Las Vegas', 'Surprising as NRA Urges Less Restrictive Gun Laws After Las Vegas', 'Las Vegas shooting motive eludes investigators', 'Just how gun owners think', 'How Las Vegas Shattered Country Music', 'Afraid to Talk About Guns', 'Mass Shooter\'s Bizarre Behavior', 'the NRA is safe', 'Las Vegas survivors furious', 'Conspiracy Theories About The Vegas Shooting', 'Las Vegas shooting unlikely to move Congress on gun control', 'like a ghost when he came in', 'calling shooting a hoax', '1518 mass shootings', 'america is at war with itself', 'is starting to sound so profane', 'Pat Robertson Blames Las Vegas Massacre', '\"end of everything\" if Trump supports gun controls', 'Trump calls for unity after Las Vegas, then retweets media attacks', 'Trump retweets media attacks by Hannity', 'On gun control, Donald Trump has lost his marbles', 'theres actually zero difference between good', 'Top Trump Ally Met With Putin', 'What happened in Las Vegas is in many ways a miracle', 'Gun Toting Maniacs', 'NRA poured more than', 'Thank you NRA', 'America Used to Be Good at Gun Control', 'Democrats Lament Inability to Pass Gun Restrictions', 'Mass Shootings Are a Bad Way to Understand Gun Violence', 'thoughts and prayers\" is slowly becoming a meme', 'accepted the rage of white men', 'Gun Controls Pose a Greater Threat Than Terrorism', 'Yes, Pat Robertson blamed the Vegas shooting on', 'gerrymandering keeps Congress from passing gun control laws', 'Republican senator blames the culture of', 'Mass Shootings Are Not The Price Of Freedom, They Are The Price Of Stupidity', 'stocks rise after Las Vegas shooting', 'research gun violence because of NRA lobbying', 'Call for blood donors', 'giving blood can save lives']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[Give Blood](http://www.redcross.org/give-blood) | [Contact your state legislator](https://openstates.org/find_your_legislator/)")
        print("Bot replying to : ", submission.title)
        submission.reply(text)
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