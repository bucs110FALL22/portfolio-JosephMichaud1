passage = "Once upon a time there was a dear little girl who was loved by every one who looked at her, but most of all by her grandmother, and there was nothing that she would not have given to the child.Once she gave her a little cap of red velvet, which suited her so well that she would never wear anything else. So she was always called Little Red Riding Hood."
wordreplace = {"little":"big", "red":"blue", "she":"he", "was":"was not"}
newPassage = passage[:]
print(newPassage)
print(" ")
for i in wordreplace:
    newPassage = newPassage.replace(i, wordreplace[i])
print(newPassage)