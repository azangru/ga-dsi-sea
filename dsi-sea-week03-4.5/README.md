---
title: Web Crawlers pt. 1
duration: "3:00"
creator:
    name: Brad Zimmerman
    city: SEA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Web Crawlers pt. 1

## Introduction

Today you will be working with Hugh Man to create a rudimentary web crawler to compile data from a variable list of websites. This lab is very difficult. Do not be afraid ask questions!

## Notes

There are some differences between the web crawler we will be making today, and the web crawlers commonly found in production. Here are some things that can be done to improve the web crawler you are making today.

* Threading isn't implemented. We must make all of our calls serially instead of in parallel.
* We aren't changing our headers to get through certain error messages, so some websites will be blocked.
* We are using iPython, a very inefficient tool when it comes to doing this sort of thing. We should be using a dedicated Python IDE (Interactive Development Environment) or a script.
* We aren't templating. In layman's terms, we aren't providing an html structure for our web crawler to look for. This would drastically save time and space if we knew what we were looking for specifically.
* We are saving all of our data to variables in memory instead of a database. This slows down our program significantly.
* We are only using one computer to do all the crawling and processing. Usually these actions are done by a distributed network of computers working in parallel.
* Our pattern matching isn't super sophisticated. We won't be able to filter out our strings as well until we learn regular expressions a little better.

#### Requirements

- Finish all cells in the provided iPython notebook. There are a few empty cells, so make sure you get them all!
- There is a bonus for this lab. Try to do it if you finish early. It's a bonus because I don't think anyone will finish early.

#### Deliverable
- The ipython notebook from this lab
