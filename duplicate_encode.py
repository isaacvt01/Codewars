    encoded = {}
    for character in word:
        if character.lower() in encoded:
            encoded[character.lower()] = ')'
        else:
            encoded[character.lower()] = '('

    orderedEncoded = ""
    for character in word:
        orderedEncoded = orderedEncoded + encoded[character.lower()]
    
    return orderedEncoded

