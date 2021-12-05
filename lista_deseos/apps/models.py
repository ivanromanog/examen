from django.db import models
# Create your models here.

#manager admmin

class ItemManager(models.Manager):
    def createItem(self, postData, username):
        item = Item.objects.create(
            name= postData['item'],
            creator=User.objects.get(username=username)
        )
    def deleteItem(self, item_id):
        delete = Item.objects.get(id=item_id)
        delete.delete()

class UserManager(models.Manager):
    def register(self, postData):
        print(postData)
        user = User.objects.create(
			name = postData['name'],  
			username= postData['username'],
			password= postData['password'],
            date_hired= postData['datehired']
        )
    def login(self, postData):
        user = User.objects.get(username=postData['username'])

#los modelos

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_hired = models.DateField()
    objects = UserManager()

class Item(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='listed')
    date_created = models.DateTimeField(auto_now_add=True)
    objects = ItemManager()


