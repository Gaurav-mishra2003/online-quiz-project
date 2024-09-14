from django.shortcuts import render
from testapp import forms
from . forms import signupform
from testapp.models import addquiz_model,answer_model
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def upload_quiz_view(request):

    if request.method=='POST':
        form=forms.quiz_form(request.POST)
        if form.is_valid():
            question=form.cleaned_data['question']
            option1=form.cleaned_data['opption1']
            option2=form.cleaned_data['opption2']
            option3=form.cleaned_data['opption3']
            option4=form.cleaned_data['opption4']
            answer=form.cleaned_data['answer']
            addquiz=addquiz_model(ques=question,A=option1,B=option2,C=option3,D=option4,Ans=answer)
            addquiz.save()

    form=forms.quiz_form()

    return render(request,'testapp/upload_question.html',{'form':form})

@login_required    
def studentquiz_view(request):
        
           data_list=addquiz_model.objects.all()

        #    paginator concept
           p=Paginator(addquiz_model.objects.all(),1)
           page=request.GET.get('page')
           p_items=p.get_page(page)
           last=True
           print(p_items.next_page_number)

           if request.method=='POST':
                 form=forms.answer_form(request.POST)
                 if form.is_valid():
                       answer=form.cleaned_data['Answer']
                   
                       ans_model=answer_model(Selected_ans=answer,)
                       ans_model.save()
    # #  after submitting answer redirect to score page 
           form=forms.answer_form()     
           return render(request,'testapp/quiz.html',{'form':form ,'data_list':data_list,'p_items':p_items})


def show_result_score(request):
      selcted_answer_data=answer_model.objects.all()
      stored_answer=addquiz_model.objects.all()
      count=0

      for stored_data in stored_answer:
            for items in selcted_answer_data:
              if stored_data.Ans==items.Selected_ans:
                   count=count+1
                   print(count)
                
              else:
                  pass
      
      return render(request,'testapp/result.html',{'count':count})

def home_page_view(request):
     return render(request,'testapp/home.html')

def privacy_view(request):
     return render(request,'testapp/privacy_condition.html')
@login_required
def conditions_view(request):
     return render(request,'testapp/notice.html')

def signupform_view(request):
     form=signupform()
     if request.method=='POST':
          form=signupform(request.POST)
          user=form.save()
          user.set_password(user.password)
          user.save()
          return HttpResponseRedirect('/accounts/login')   
     return render(request,'testapp/signup.html',{'form':form})