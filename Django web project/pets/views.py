from django.shortcuts import render, redirect

# Create your views here.
from pets.forms.comment_form import CommentForm
from pets.forms.pet_form import PetForm
from pets.models import Pet, Like, Comment


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),

    }
    return render(request, 'list_pets.html', context)


def show_pets_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        pet.likes_count = pet.like_set.count()
        context = {
            'pet': pet,
            'comment_form': CommentForm(),
        }
        return render(request, 'pets_details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                text=form.cleaned_data['text']
            )
            comment.pet = pet
            comment.save()
            return redirect('pet det', pk)

        pet.likes_count = pet.like_set.count()
        context = {
            'pet': pet,
            'comment_form': form,
        }
        return render(request, 'pets_details.html', context)


def persist_pet(request, pet, template_name):
    if request.method == 'GET':
        form = PetForm(instance=pet)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)
    else:
        form = PetForm(
            request.POST,
            instance=pet,
        )
        if form.is_valid():
            form.save()
            return redirect('pet det', pet.pk)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    return persist_pet(request, pet, 'pet_edit')


def create_pet(request):
    pet = Pet()
    return persist_pet(request, pet, 'pet_create')


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet
        }
        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('pets_details.html')


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect('pet det', pk)


def comment_pet(request, pk):
    pass
