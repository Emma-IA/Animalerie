
from django.db import models




class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)
    def __str__(self):
        return self.id_equip


class Animal(models.Model):
    id_animal = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def logique(self,lieu):
        if self.etat=='affamé' and lieu.id_equip=='mangeoire' :
            self.etat = 'repus'
            return ''
        elif self.etat == 'fatigué' and lieu.id_equip=='nid': 
            self.etat = 'endormi'
            return ''
        elif self.etat == 'endormi' and lieu.id_equip=='litière': 
            self.etat = 'affamé'
            return ''
        elif self.etat == 'repus' and lieu.id_equip=='roue': 
            self.etat = 'fatigué'
            return ''
        elif self.etat=='affamé' and lieu.id_equip!='mangeoire':
            return "et pourquoi pas la mangeoire ?"
        elif self.etat == 'fatigué' and lieu.id_equip!='nid': 
            return "notre ami ferait mieux de dormir ..."
        elif self.etat == 'endormi' and lieu.id_equip!='litière':
            return "et si on le réveillait ? "
        elif self.etat == 'repus' and lieu.id_equip!='roue': 
            return "un peu d'exercice ne lui ferait pas de mal ..."
        else : return 'erreur'




    def deplacer(self,lieu):
        reason = self.logique(lieu)
        if lieu.id_equip == 'litière':
            if  not reason :
                self.lieu = lieu
                return self
            else : 
                return 'error_impossible'
        else :
            if lieu.disponibilite == 'libre':
                if not reason :
                    self.lieu = lieu
                    return self
                else : 
                    return 'error_impossible'
            else:
                return 'error_not_empty'

    def message(self, lieu) :
        if self.deplacer(lieu) == 'error_impossible' :
            return self.logique(lieu)



   
    def __str__(self):
        return self.id_animal


