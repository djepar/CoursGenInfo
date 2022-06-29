def winner(deck_steve, deck_josh):
    cardDict = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
    StevePoint = 0
    JoshPoint = 0
    for i in range(0, len(deck_steve)):
        if cardDict.get(deck_steve[i]) < cardDict.get(deck_josh[i]):
            JoshPoint += 1
        elif cardDict.get(deck_steve[i]) > cardDict.get(deck_josh[i]):
            StevePoint += 1
    if JoshPoint < StevePoint:
        return "Steve wins {} to {}".format(StevePoint, JoshPoint)
    elif JoshPoint > StevePoint:
        return "Josh wins {} to {}".format(JoshPoint, StevePoint)
    else:
        return "Tie"