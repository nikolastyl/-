import instaloader

L = instaloader.Instaloader() 

usernameInst = input("dose enan dhmosio instagram logariasmo: ") 
profile = instaloader.Profile.from_username(L.context, usernameInst)  

posts = 0 
coommenters= [] 

for post in profile.get_posts():

    comments = post.get_comments() 

    for comment in comments: 
        coommenters.append(comment.owner.username)

    posts=posts+ 1
    if posts == 100: 
        break

if posts==0:
  print("aytos o logariasmos einai idiotikos h den exei kamia dhmosieysh")
elif coommenters[0]== None:
   print ("aytos o logariasmos den exei kanena sxolio")
else:   
 print( "Aytos poy exei kanei ta perissotera sxolia einai o/h: " + max(set(coommenters), key = coommenters.count))