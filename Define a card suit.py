def define_suit(card):
    if(card.endswith('C')):
        return 'clubs'
    elif(card.endswith('S')):
        return 'spades'
    elif(card.endswith('D')):
        return 'diamonds'
    else:
        return 'hearts'
    
print(define_suit('3C'))
