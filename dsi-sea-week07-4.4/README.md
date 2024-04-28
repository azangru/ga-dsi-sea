---
title: The Language of Us
duration: "3:00"
creator:
    name: Brad Zimmerman
    city: SEA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) The Language of Us

## Introduction

The language of us refers to the concept that music and art encompass a universal way of communicating. A great Russian painting or musical composition doesn't need to be translated into English to be understood. It just needs to be created.

Today we are going to do a little bit of creating on our own. We have been working on the top imdb movies in the past few projects. Why not work with all the movies this time? Use your new future skills to crawl through any movie's page and pull the top 3 user comments for the flick. We are then going to then vectorize the text and pull out the significant words. From there we are going to use each of those words to query giphy and return an image. Once we have all of our images, we are going to put them up on our website!

[Here is my URL](https://peaceful-badlands-42479.herokuapp.com/site/imdb/lang/tt2488496/)

<img src="./images/screen01.png" alt="Title" style="border: 5px solid #000000; padding: 10px; height: 500px;"/>
<img src="./images/screen02.png" alt="Title" style="border: 5px solid #000000; padding: 10px; height: 500px;"/>

That sounds kind of confusing. Let's break apart those steps real quick.
* Make a new route when a url is queried on your site
    * Example: imdb/lang/**movie_id**
* When you receive the id, look at the top user comments.
* Vectorize the top 3 comments. Pull out the significant words.
* Use the significant words and query the giphy api for each
* Show the giphy images on your website

#### Requirements
- Use futures to pull information from multiple sources. Show the images.

#### Side Note
- Text blob is a little bit weird with how it can be pushed up to heroku due to it's associated libraries. Follow the instructions [Here](http://stackoverflow.com/questions/18385303/how-to-install-nltk-modules-in-heroku) to push the library up successfully.

#### Deliverable
- Edit this readme. Add your url with the finished page.

## https://obscure-hollows-37474.herokuapp.com/site/imdb/lang/tt0111161/
