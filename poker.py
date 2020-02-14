import random
import itertools


def print_hand(l):
	txt=""
	for c in l:
		txt+=str(c[0])+str(c[1])+","
	txt=txt[:-1]
	return txt





def card_ranks(hand):
    "epistrefei mia lista me tis ajies toy xerioy apo th megalyterh syh mikroterh"
    ranks = ['--23456789TJQK1'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    if ranks == [14,5,4,3,2]:
       ranks = [5,4,3,2,1]
    return ranks

def kind(n, ranks):
    for i in ranks:
        if ranks.count(i) == n:
            return i

def straight(ranks):
    #ginetai alhthia an yparxei kenta
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    #epistrefei alhtheia an exei ginei flush
    suits = [s for r,s in hand]
    for i in range(len(suits)-1):
        if suits[i] != suits[i+1]:
            return False
    return True


#kathe elegxos poy bgainei althhs epistrefei enen arithmo poy antistoixei se enan syndiasmo
def hand_rank(hand):
    ranks = card_ranks(hand)
    #elenxei an exei ginei  kenta xroma
    if straight(ranks) and flush(hand):            
        return (7, max(ranks))
    #elenxei an exei ginei 4 of a king
    elif kind(4, ranks):                           
        return (6, kind(4, ranks), kind(1, ranks))
    #elenxei an exei ginei full house    
    elif kind(3, ranks) and kind(2, ranks):        
        return (5, kind(3, ranks), kind(2,ranks))
    #elenxei an exei ginei flush
    elif flush(hand):                              
        return (4, [ranks])
        #elenxei an exei ginei kenta
    elif straight(ranks):                          
        return (3, max(ranks))
    #elenxei an yparxoyn mono 3 idia fylla kai den exei ginei full house(3 of a king)
    elif kind(3, ranks):                           
        return (2, kind(3, ranks), [ranks])
    #elenxei an yparxei ena zeygari    
    elif kind(2, ranks):        
        return (1, kind(2, ranks), [ranks])
    #epistrefei th megalyterh karta an den yparxei kapoios syndiasmos    
    else:                                          
        return (0, [ranks])


#mia lista me kleidia toys arithmoys poy epistrefontai apo thn parapanv def kai odhgei sthn onomasia kathe syndiasmoy 
hand_names = {0:'high card',1:'pair',2:'3 of a kind',3:'straight',4:'flush',5:'full house',6:'4 of a kind',7:'straight flush'}


cards=[str(i) for i in range(1,10)] 
cards+=["T","J","Q","K"] 
suits=["S","H","D","C"] 
deck=itertools.product(cards,suits) 
deck=list(deck) #Ας τα έχω σε μία λίστα...


random.shuffle(deck)
hand=[]
hand2=[]

for i in range(5):
	hand+=[deck.pop()]
	hand2+=[deck.pop()]



print ("Τα χαρτιά του player_1 είναι: ",print_hand(hand))
print ("Τα χαρτιά του player_2 είναι: ",print_hand(hand2))



h1=hand_rank(hand)
h2=hand_rank(hand2)


print("Player_1 has ",hand_names[h1[0]],"with: ",h1[1])
print("Player_2 has ",hand_names[h2[0]],"with: ",h2[1])




if h1[0]>h2[0]:
  print("PLAYER_1 WIN!!")
elif h1[0]<h2[0]:
  print("PLAYER_2 WIN!!")
else:
  if h1[1]>h2[1]:
   print("PLAYER_1 WIN!!")
  elif h1[1]<h2[1]:
   print("PLAYER_2 WIN!!")







