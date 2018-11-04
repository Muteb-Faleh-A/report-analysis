
Logs Analysis Project
Building an informative summary from logs by sql database queries. Interacting with a live database both from the command line and from the python code. This project is a part of the Udacity's Full Stack Web Developer Nanodegree.

Technologies used
PostgreSQL
Writing Python code with DB-API
Linux-based virtual machine (VM) Vagrant
Project Requirements
Reporting tool should answer the following questions:

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?
Project follows good SQL coding practices: Each question should be answered with a single database query.
The code is error free and conforms to the PEP8 style recommendations.
The code presents its output in clearly formatted plain text.
System setup and how to view this project
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.

Download Vagrant and install.
Download Virtual Box and install.
Clone this repository to a directory of your choice.
Download the newsdata.sql (extract from newsdata.zip (not provided here though)) and newsdata.py files from the respository and move them to your vagrant directory within your VM.
Run these commands from the terminal in the folder where your vagrant is installed in:
vagrant up to start up the VM.
vagrant ssh to log into the VM.
cd /vagrant to change to your vagrant directory.
psql -d news -f newsdata.sql to load the data and create the tables.
python3 newsdata.py to run the reporting tool.

These queries are complicated. Where do I start?
One of the best ways to build complex queries is by starting with smaller pieces, and testing each of them in small steps. Here's a worked example —

Suppose we wanted to print out each article's title and author name.

Looking at the schema for articles (with \d articles) we can see there's an author and title column. But the author column doesn't have names in it — just numbers. To see this in your database, run:

select author from articles;
But the authors table has a name column, and a numeric id column. To see this, run:

select * from authors;
Those numeric id values match up with the articles.author column. And that means we can connect the two tables with a join:

select title, name
from articles join authors
on articles.author = authors.id;
or:

select title, name
from articles, authors
where articles.author = authors.id;
Try these queries on your news database! Look for other relationships that can work with join.




1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors
