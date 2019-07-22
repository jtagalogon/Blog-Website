from django.db import models
from datetime import datetime

class User(models.Model):
    userID = models.CharField(max_length =100, primary_key=True)
    username = models.CharField(max_length = 20, unique=True)
    firstName = models.CharField(max_length = 15)
    lastName = models.CharField(max_length = 15)
    email = models.EmailField(max_length = 50, unique=True)
    password = models.CharField(max_length = 30)

    #NOTES on Image Uploads:
      #in your settings file, you need to define a 'MEDIA_ROOT'
      #this will be equal to the full directory path for a folder you want django to store the images
      #next in settings, define 'MEDIA_URL' as the base public URL of the directory
      # you need to create subfolders in MEDIA root for appropriate image classes (i.e blog content, profle pic)
      # the the directory for the profile pic folder will be defined in the instance of the profilePic model below.

    #profilePic = models.ImageField(upload_to = rootSubdirectory)
    
    aboutMe = models.TextField(max_length = 200) 

    #When email is verified, if not then the account will be deleted in 7 days
    isActive = models.BooleanField()

    #When user wants a private account with no commenting by others ect.  
    isPrivate = models.BooleanField()

    created_on = models.DateTimeField(auto_now_add=True)

    def getPosts(self):
        blog = UserBlog.objects.get(author = self.userID)
        return blog.getPostsIds()


class Blog(models.Model):
    blogID = models.CharField(max_length = 100, primary_key=True)
    blogTitle = models.CharField(max_length = 40)

def __str__(self):
    return self.blog_title

class UserBlog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, primary_key =True)

    def getPostsIds(self):
        posts = Blog_Post.objects.filter(blogID = self.blog)
        allPosts = set()
        for post in posts:
           q = Post.objects.get(postID = post.post_id)
           allPosts.add(q)
        return allPosts


class Post(models.Model):
    postID = models.CharField(max_length = 100, primary_key=True)
    postTitle = models.CharField(max_length = 40)
    text = models.TextField(max_length = 2000)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.post_title

class Comment(models.Model):
    commentID = models.CharField(max_length = 100, primary_key=True)
    commentBody = models.CharField(max_length = 200)
    isReply = models.BooleanField()
    likes = models.IntegerField()
    dislikes = models.IntegerField() 
    created_on = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    replyID = models.CharField(max_length = 100, primary_key=True)
    replyBody = models.CharField(max_length = 200)
    isReply = models.BooleanField()
    likes = models.IntegerField()
    dislikes = models.IntegerField() 
    created_on = models.DateTimeField(auto_now_add=True)

#this is needed because we need to keep track of comment hierarchy 
#So if the comment id has appeared as a reply id then the comment is also a reply 
#and the is_reply boolean must be true
class CommentReply(models.Model):
    commentID = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)
    replyID = models.ForeignKey('Reply', on_delete=models.CASCADE, null=True)


class User_Likes(models.Model):
    userID = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    postID = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    like = models.BooleanField()
    

#if user does like then the boolean will be true if the user does dislike the boolean 
#will be false. Both cannot be true at the same time. This prevents multiple 
#likes/dislikes for one user
class User_Comment(models.Model):
    userID = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    commentID = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)
       

class Tag(models.Model):
    tagID = models.CharField(max_length = 100, primary_key=True)
    tag = models.CharField(max_length = 15)


class Tag_Post(models.Model):
    postID = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    tagID = models.ForeignKey('Tag', on_delete=models.CASCADE, null=True)


class Blog_Post(models.Model):
    blogID = models.ForeignKey('Blog', on_delete=models.CASCADE, null=True)
    postID = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)


class Comment_Post(models.Model):
    commentID = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)
    postID = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)













