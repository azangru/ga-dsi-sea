---
title: My First Website
duration: "2:00"
creator:
    name: Brad Zimmerman
    city: SEA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) My First Website
Week 5 | Lesson 3.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Create a working website
- Move data from a website server to your browser
- Use APIs!
- Generally be a Boss

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Be a Boss
- Use 'for' loops and stuff

### LESSON GUIDE

| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 60 mins | Guided-practice](#guided-practice) | Walkthrough |
| 60 mins | Lab](#lab) | Lab |


<a name="walkthrough"></a>
## Walkthrough (60 mins)
Open up Django Setup.ipynb. We will be working with this file for a little bit to help us out with some steps. After we set up our initial server, we will be moving on to the enclosed lab. Take a peek at the lab section if you are curious about what we are building today...


<a name="lab"></a>
## Lab (60 mins)
<img src="/images/01.png"/ style="width: 400px;">
<br>
<img src="/images/02.png"/ style="width: 400px;">

A giphy generator! Our website is going to crawl the giphy api and give us results to put up on our page. We have already done 90% of the steps in class so far, but we have never taken those skills out of our ipython notebooks.

#### What we need to do
Since we are covering a lot of new stuff in a very limited span of time, I feel like we should start out slow. Let's take a look at your site. It was made following the tutorial on the Django website and will give a very good basic idea of how a website is made in python (For any references and help, see the Django tutorial on the bottom of the page). I have taken elements from things we already know, and applied them to this website. You will need to know regular expressions, json, html, routing, and maybe even css! Here are the steps:

* Take the image from your index.html file and copy it to your giphy.html file.
* Add a new route to your website/url.py file for your new view
* At the bottom of your website/views.py file, add a new function. Name it giphy. Make sure the names match in the website/url.py file. Here is an example of what a function like that might look like:

```
def giphy(request, giphy_search):
    #Query giphy api here
    giphy_json = API_Images_In_Array
    return render(request, 'site/giphy.html', {'giphy': giphy_json})
```

* Make sure you are grabbing the right urls when you query the api! Some of the urls aren't meant to be embedded in an image tag. [Here](https://media.giphy.com/media/EaMTsoYxfPpuw/giphy.gif) is an example of a url that works in an image tag. Play around with the giphy json in the chrome inspector if you are having trouble figuring out which image to use.
* Views return objects that look like this => _return render(request, 'site/giphy.html', {'giphy': giphy_json})_ . Make sure giphy_json contains a list of your giphy images.
* Django can create loops in html for you to use! Take advantage of this knowledge to loop through your images and print them out on your site. Look at how the loop is implemented in the results.html and index.html files to get some hints on what to do.
* You're pretty much done! Congrats! That wasn't too hard was it? If you are feeling awesome, add some css to the page. I left my styling for the images in the style.css file. All you have to do is add the giphy class to your image tag and see what happens! Feel free to add your own accent to clean up the site a bit. We will be using it again in future labs.


### ADDITIONAL RESOURCES

- [Django Tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)
- [HTML Helper](http://www.w3schools.com/html/)
- [Giphy API](https://github.com/Giphy/GiphyAPI)
