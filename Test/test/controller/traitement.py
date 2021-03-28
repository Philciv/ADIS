from ..data import bdd as b


# traitement: Mise à jour des champs table synopsis par javascript
def update_synopsis(request):
    print(request.form)
    id_synopsis = int(request.form['pk'])
    new_value = str(request.form['value'])
    champ = str(request.form['name'])
    msg = b.update_SynopsisData(champ, id_synopsis, new_value)
    print("update_SynopsisData (fonc update_synopsis): "+msg) #debug dans terminal
    return msg
