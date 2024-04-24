from django.shortcuts import render,redirect
from .forms import ProfileForm,WorkExperienceForm,EducationForm
from .models import Profile,WorkExperience,Education,Project,Certification
# Create your views here.

def create_profile(request):
    profiles=Profile.objects.all()

    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()


    else:
        form =ProfileForm()

    return render(request,'create_profile.html',{'form':form,'profiles':profiles})


def listProfile(request):
    profiles=Profile.objects.all()

    return render(request,'list.html',{'profiles':profiles})


def detailsView(request,profile_id):
    profile=Profile.objects.get(id=profile_id)


    return render(request,'detailsview.html',{'profile':profile})


def updateProfile(request,profile_id):

    profile=Profile.objects.get(id=profile_id)

    if request.method=='POST':
        form=ProfileForm(request.POST,instance=profile)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form=ProfileForm(instance=profile)

    return render(request,'update.html',{'form':form})


def deleteView(request,profile_id):

    profile=Profile.objects.get(id=profile_id)

    if request.method=='POST':
        profile.delete()

        return redirect('/')

    return render(request,'deleteview.html',{'profile':profile})


def create_work_experience(request):

    work_experience = WorkExperience.objects.all()

    if request.method == "POST":
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the list view after work experience creation
    else:
        form = WorkExperienceForm()
    return render(request, 'create_work_experience.html', {'form': form, 'work_experience':work_experience})

# def work_details_view(request, work_experience_id):
#     work_experience = WorkExperience.objects.get(id=work_experience_id)
#     return render(request, 'work_details_view.html', {'work_experience': work_experience})
#
def list_work_experience(request):
    work_experiences = WorkExperience.objects.all()
    return render(request, 'list_work_experience.html', {'work_experiences': work_experiences})



def create_education(request):
    educations = Education.objects.all()

    if request.method=="POST":
        form=EducationForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()



    else:
        form = EducationForm()

    return render(request,'create_education.html',{'form':form,'educations':educations})


def list_education(request):
    educations = Education.objects.all()
    return render(request, 'list_education.html', {'educations': educations})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'project_detail.html', {'project': project})


def certification_list(request):
    certificates = Certification.objects.all()
    return render(request,'certificate_list.html',{'certificates':certificates})