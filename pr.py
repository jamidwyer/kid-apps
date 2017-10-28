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
            terms = ['full toll on puerto rico', 'astonishingly corrupt', 'puerto rico contract', 'puerto rico is burning its dead', 'uncle was flying from DC to PR', 'Puerto Rico is not alone', 'Nurses returning from Puerto Rico', 'puerto rico is slipping', 'Puerto Rican hurricane survivors', 'Puerto Rican Telecommunications Alliance warns', 'surgery by flashlight', 'Sanders to visit Puerto Rico', 'Trump:Golf', 'Puerto Rico is still without power', 'Appeal backed by former presidents raises', 'raising money for hurricane relief', 'Puerto Rico governor', 'die en masse in Puerto Rico', 'hurricane relief concert', 'hurricane aid concert', '1.5 Million Meals To Hungry Puerto Ricans', 'puerto rico delegate', 'Puerto Rico response a 10', 't sure Puerto Ricans should', 'Puerto Rico mayor: ​for US response', 'alternative reality world', 'San Juan mayor grades Trump', 'American citizens need America’s resources', 'more hot meals in Puerto Rico than the Red Cross', 'response to Puerto Rico in Hurricane Maria', 'perfect grade for Puerto Rico', 'Sanders to visit Puerto Rico', '10 out of 10', 'to go to Puerto Rico', 'make trip to Puerto Rico', 'I\'d give myself a 10', 'Puerto Rico handling a 10', 'Sanders to visit Puerto Rico', 'Trump gave himself a \'10\' on Puerto Rico. Then he tried to get its governor to do the same', 'Thousands of Pets Behind in Puerto Rico', 'Puerto Rican Secretary Of State Blows Whistle On Hurricane Relief Fraud', 'The unrelenting crisis in Puerto Rico', 'month after Hurricane Maria', 'Video Shows Where Puerto Rico', 'Tracked Down 10 of the Biggest Vulture Firms', 'Tweets About Puerto Rico', 'Same Problems Are Happening in Puerto Rico', 'american crisis', 'firefighter raising money for Puerto Rico', 'Puerto Ricans get short shrift', 'Trump blames difficulty accessing water in Puerto Rico', 'How Data Can Save Us From The Trumpocalypse', 'Utuado, Puerto Rico have NO water', 'should not have to help with food, water distribution in Puerto Rico', 'approval rating on hurricanes', 'must help Puerto Rico', 'health faces prolonged recovery', 'like they are disposable', 'Congresswoman Nydia Velazquez Blast', 'ravaged puerto rico', 'Fake News Of Puerto Rico Truck Strike', 'American Disasters.', 'Exploiting Puerto Rico Tragedy', 'enormously high cost of doing nothing', 'Racist Supreme Court rulings created Puerto Rico', 'spin Puerto Rico to the media', 'Puerto Rico, Disconnection and Chaos', 'Puerto Ricans given drinking water pumped from a hazardous', 'Puerto Ricans given water from hazardous site', 'Puerto Rico distributes water from Superfund site', 'Desperate Puerto Ricans', 'three weeks after Hurricane Maria', 'Not even hospitals in Puerto Rico know how many people have died', 'Started Paying Attention To Puerto Rico', 'message Puerto Rico did not want to hear', 'While people are dying in Puerto Rico', 'Puerto Rico tweets were response to San Juan mayor', 'hater-in-chief', 'trump attacks puerto rico', 'FEMA, first responders can', 'hater in chief', 'San Juan mayor fires back after Trump', 'criticism for Puerto Rico tweet', 'only for help getting back to a comparable pre-disaster state as was done in Houston', 'threatens to end disaster relief for Puerto Ricans', 'Puerto Rico have become political opponents for Trump', 'threatens to abandon Puerto Rico', 'pull out of Puerto Rico already', 'pull FEMA from Puerto Rico', 'Not Their Job to Distribute Food and Water to Hurricane Victims in Puerto Rico', 'Puerto Rico crisis into catastrophe', 'Puerto Ricans are drinking water from hazardous waste sites', 'FEMA dodges questions about Puerto Rico', 'Dead in Puerto Rico', 'Drinking Water From Wells at Hazardous Waste', 'Puerto Rico city Trump visited is still without power', 'Puerto Rico city Trump visited is still without power', 'Puerto Rico Needs A Major Military Rescue Operation Now', 'Only one ship headed to Puerto Rico', 'Most of Puerto Rico has been in the dark for 21 days', 'Three Weeks After Maria', 'Weeks After Hurricane, Puerto Rico Lacks Water, Working Hospitals, Electricity', '3 weeks after Hurricane Maria', ' give a damn', 'Playing Defense on Hurricane Maria', 'Three weeks after Hurricane Maria hit Puerto Rico just 10', 'San Juan Mayor Carmen Yulin Cruz on Trump exchange', 'FEMA has been deleting facts', 'deaths in Puerto Rico is at odds with the official count', 'Trump Pushes More Loans on Devastated Puerto Rico', 'Puerto Rico Relief', 'trump\'s katrina', 'update on Puerto Rico', 'big water']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[Project Hope](http://www.projecthope.org/) | [ConPRmetidos](https://www.generosity.com/emergencies-fundraising/maria-puerto-rico-real-time-recovery-fund) | [Direct Relief](https://secure.directrelief.org/site/Donation2) | [Hispanic Federation](https://hispanicfederation.org/unidos/) | [World Central Kitchen](https://www.worldcentralkitchen.org/donate) \n\n"
        "[^(Charity Navigator)](https://www.charitynavigator.org/index.cfm?compare=4367%2C3626%2C4997&bay=search.compare) \n\n")
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