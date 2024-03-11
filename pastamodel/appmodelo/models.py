from django.db import models
classComentario(models.Model):


    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    texto=models.TextField()  
    data=models.DateTimeField(auto_now_add=True)
    hora=models.TimeField(auto_now_add=True)
