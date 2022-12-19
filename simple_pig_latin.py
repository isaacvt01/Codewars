def pig_it(text):
    text = text.split()
    new_list = []
    for item in text: 
        item = str(item)
        al_reves = item[1:] + item[0]
        new_list.append(al_reves)
    new_list = 'ay '.join(new_list)
    if new_list[-1] == '?' or new_list[-1] == '!':
        new_list = new_list.strip()
        return new_list
    else:
        new_list = new_list.strip()
        new_list = new_list + 'ay'
        return new_list
    








if __name__ == "__main__":
    assert pig_it("Quis custodiet ipsos custodes ?") == 'uisQay ustodietcay psosiay ustodescay ?'
    assert pig_it('This is my string') == 'hisTay siay ymay tringsay'