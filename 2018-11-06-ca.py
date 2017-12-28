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

local_subs = open("california.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.selftext)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Can The Dems Take The House in 2018', 'We have to end the use of private prisons in the United States', 'Rackauckas', 'todd spitzer', 'orange county da ', 'orange county d.a.', 'orange county district attorney', 'gerrymandering, political reform, and saving democracy', 'A Serial Killer In Orange County', 'restorative justice for all those who had their lives destroyed', 'Southern California wildfire now largest in state history', 'with a Pen, 5 Seconds After Exiting His Patrol Car', 'progressive renaissance of 2018', 'CASEN 2018', 'Plot To Use Classified Information To Discredit', 'expansion of mass surveillance', 'polling results for 36 districts', 'Democrats Are Pulling Away in the Generic Ballot', 'NSA Expansion Bill', 'Ballot average gives Democrats highest advantage yet', 'Thomas Fire is on track to become the largest', 'Trump predicts Republicans will do', 'deny global warming all he wants, but the price can', 'full rights are restored to every American who spent time in jail for marijuana', 'we can do it in cd4', 'Coroner resigns due to sheriff interference', 'A Deep Vein of Poverty Runs Through the U.S.', 'mimi walters', 'Kia Hamadanchy', 'Putin Is Not Omnipotent', 'Climate change is part of California', 'congressional districts to target for 2018', 'much closer districts than the Alabama Senate Seat', 'Climate Change Has Come for Los Angeles', 'Kremlin Likes Him So Much It Gave Him a Code Name', 'GOP rushes ahead on taxes', 'lives ruined for smoking a joint', 'future climate favorable for wildfires', 'GOP tax bill would end deduction for wildfire and earthquake victims', 'exacerbate California droughts', 'The Feminist Case For Single Payer', 'Lakewood, California ', 'El Cajon Homeless Feeding Ban', 'says sheriff interferes in death investigations', 'devin nunez', 'Contempt Action Against FBI, DOJ', 'fully exposed in the Republican tax bill', 'looks like California Republicans are eager to lose their seats', 'chance of winning control of the U.S. House', 'Orange County Alt-Right', 'devin nunes', 'rep. nunes', 'congressman nunes', 'House Intel chief', '20 percent of our uranium', 'Journalist nails GOP\'s fake patriotism', 'Fake news Clinton story revived', 'desperately trying to shift blame to Clinton', 'The Evolution of a Right Wing Distraction', 'House panel says it will get bank records from firm behind Trump dossier', 'RUSSIA URANIUM ONE CONSPIRACY THEORY', 'Alt-Collusion to Defend Trump From Mueller', 'Russian uranium efforts', 'Someone Is Really Worried About the Trump', 'Republicans Leaking Confidential Info Like Crazy', 'Republicans look past Trump scandals, zero in on Hillary Clinton', 'Blowing Goats Instead Of Investigating', 'How Republicans Are Jumping on the New ', 'fund the Trump golden shower dossier', 'Republicans seize on dossier revelations to counter Russia probes', 'House Republicans investigating Obama', 'Russia Probe Just Blew Up', 'Russia Probe Not That Interested in Trump or Russia', 'GOP launches probes into Clinton, Obama controversies', 'era uranium deal', 'partisan split widening over Russia probe', 'Trump Singes Fingers Trying to Torch Dossier', 'House Intel Committee Have Enough Staff', 'Republican House intelligence committee members are coaching witnesses', 'Partisan feud undercuts Trump-Russia probe', 'Flat Earth" Report', 'clear abuse of power', 'Russia dossier balks at House subpoena', 'Firm behind Trump-Russia dossier subpoenaed', 'Nunes lunges back into Russia', 'dossier subpoenaed by House intelligence committee', 'Nunes Subpoenaed', 'Nunes signs off on new subpoenas', 'The Secrecy Undermining the Senate Intelligence Committee', 'House intel Democrat on Russia probe', 'California could flip the House, and these 13 races will make the difference', 'More smoking guns than Bonnie and Clyde', 'Republican attempt to deflect Trump-Russia probes', 'Republicans Trying to Discredit Mueller Investigation', 'rep nunes', 'House panel subpoenas Justice Dept. and FBI', 'Most California GOP House members vote to pass tax bill', 'darrell issa', 'rep. issa', 'rep issa', 'Decision Desk 2018 House ratings', '13 new candidates', 'Thirteen New Candidates', 'Justice Democrats launched 13 new candidates', 'Mike Pence pitches tax reform in Rancho Cordova', 'single-payer healthcare becomes a pivotal issue', 'Last California Republicans', 'states that will lose under Cassidy-Graham', 'Issa told to pay challenger for legal expenses in lawsuit', 's hottest congressional races, ranked', 'the california gop\'s last gasp', 'Republicans booed top White House officials', 'rohrabacher', 'michael kotick', '@danarohrabacher', 'rohrabracher', 'what is the plan to exploit it for midterms', 'Rep. Hill received memo', 'The Republican civil war, and why Trump is winning it', 'Brought Holocaust Denier To Capitol Meeting', 'Transcript of McCarthy', 'transcript of the conversation among GOP leaders obtained by The Post', 'congressman openly loyal to Russia', 'broken clock and all.', 'GOP Congressman Met in Moscow With Kremlin', 'pro-Russia congressman', 'lackey in Congress met with Veselnitskaya', 'This M.F. Has To Go!', 'Congressman calls Charlottesville protest', 'GOP Congressman Sought Trump Deal on WikiLeaks, Russia', 'GOP Rep Goes Full Crazy And Claims Charlottesville Nazis', 'White Nationalist Rally Was a Left-Wing Set-Up', 'left-wingers manipulating Civil War reenactors', 'pro-assange gop congressman', 'Republican congressman praises ISIS attack in Iran', 'Republican Congressman Meets With WikiLeaks Founder Julian Assange', 'Paid by Putin Meets With WikiLeaks Founder Julian Assange', 'pro-putin california congressman', 'Pro-Russia GOP Rep.', 'Putin\'s congressman', 'Assange meets U.S. congressman', 'rhorabacher', 'steve knight', 'rep. knight', 'congressman knight', 'rep knight', 'representative knight', 'ca-25', 'valadao', 'Mere weeks after Las Vegas, the GOP is quietly pushing', 'House passes 4.2 trillion budget that guts Medicare and Medicaid, gives tax cuts to the rich', 'who controls the House in 2018, especially in California', 'silencer, which the NRA wants to make easier to get']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("California 2018 Election \n\n"
            "[Primary Election Registration Deadline](http://registertovote.ca.gov/): May 16, 2018 \n\n"
            "[Primary Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): June 5, 2018 \n\n"
            "[General Election Registration Deadline](http://registertovote.ca.gov/): October 22, 2018 \n\n"
            "[General Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()