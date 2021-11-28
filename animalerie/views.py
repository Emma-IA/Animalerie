


from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, Equipement
from .forms import MoveForm


def animal_list(request):
    animals = Animal.objects.all()
    equipements = Equipement.objects.all()
    return render(request, 'animalerie/animal_list.html', {'animals': animals,'equipements': equipements})

def equipement_list(request):
    equipements = Equipement.objects.all()
    return render(request, 'animalerie/animal_list.html', {'equipements': equipements})


def animal_detail(request, id_animal,error=None):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    if request.method == "POST":
        form = MoveForm(request.POST)
        if form.is_valid():
            ancien_lieu = get_object_or_404(Equipement, id_equip=animal.lieu)
            post = form.save(commit=False)
            nouveau_lieu = get_object_or_404(Equipement, id_equip=post.lieu)
            modif = get_object_or_404(Animal, id_animal=id_animal).deplacer(nouveau_lieu)
            logique = get_object_or_404(Animal, id_animal=id_animal).message(nouveau_lieu)
            if modif=='error_not_empty' :
                return redirect('animal_detail_mes', id_animal=id_animal, error='Ce lieu est déjà occupé !')
            elif modif =="error_impossible":
                return redirect('animal_detail_mes', id_animal=id_animal, error='Hum, ' + logique)
            else :
                ancien_lieu.disponibilite = 'libre'
                ancien_lieu.save()
                modif.save()   
                nouveau_lieu.disponibilite = 'occupé'
                nouveau_lieu.save()
            return redirect('animal_detail', id_animal=id_animal)
    else:
         form = MoveForm()
    lieu = animal.lieu
    if error==None:
        return render(request,
                    'animalerie/animal_detail.html',
                    {'animal': animal, 'lieu': lieu, 'form': form})
    else:
        return render(request,
                    'animalerie/animal_detail.html',
                    {'animal': animal, 'lieu': lieu, 'form': form, 'error':error})