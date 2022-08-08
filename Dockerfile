FROM python:3
WORKDIR /django/Django_Instagram

#Step2 git clone
RUN git clone https://github.com/kosaf1996/Django_Instagram.git /django/Django_Instagram
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

#STEP3 Run the application on the port 8080
EXPOSE 80

#STEP4 django project run 
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
