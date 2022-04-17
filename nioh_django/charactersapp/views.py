from django.shortcuts import render
from charactersapp.models import GameCharacter

def AllChars(request):
    allObjects = GameCharacter.objects.all()
    params = { "enemies":allObjects }
    return render(request, "all_chars.html", params)

def CurrentCharacter(request, charName):
    selected = GameCharacter.objects.all().filter(characterName=charName)
    character = selected[0]
    parameter = { "key_character" : character }

    return render(request, "single_character.html", parameter)