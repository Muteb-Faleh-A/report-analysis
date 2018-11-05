#!/usr/bin/env python3

import psycopg2

topArticles = """SELECT articles.title, count(*)
    as countNum FROM log, articles WHERE
    log.status='200 OK' and articles.slug=
    substr(log.path, 10) group by articles.title
    order by countNum desc limit 3;"""

popularAuthors = """SELECT authors.name,
    count(*) as countNum FROM articles,
    authors, log WHERE log.status='200 OK'
    and authors.id = articles.author and
    articles.slug = substr(log.path, 10)
    group by authors.name order by
    countNum desc limit 3;"""

requestsErrors = """SELECT TO_CHAR(date1,'Mon DD, YYYY')
    , reqsts_sent, err1,100.0
    * err1 / reqsts_sent as pert FROM (select date_trunc
    ('day', time) as reqdate, count(*) as reqsts_sent FROM
    log group by reqdate)as requests,(select date_trunc
    ('day', time) as date1,count(*)as err1 FROM log WHERE
    status = '404 NOT FOUND'group by date1)as errors WHERE
    reqdate = date1 and errors.err1 > 0.01 *
    requests.reqsts_sent order by date1 desc;"""


def dbNws(query):
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def the_title(title):
    print("\n" + title + "\n")


def topmost_articles():
    topmost_articles = dbNws(topArticles)
    the_title("(Q1)--> The most popular three articles of all time.")
    for title, num in topmost_articles:
        print(" |{}| --> {} views".format(title, num))


def topmost_authors():
    topmost_authors = dbNws(popularAuthors)
    the_title("(Q2)--> The most popular article authors of all time.")
    for name, num in topmost_authors:
        print(" |{}        | --> {} views".format(name, num))


def errors():
    errors = dbNws(requestsErrors)
    # Print results
    the_title("(Q3)-->Days more than 1% of requests lead to errors.")
    for date1, reqsts_sent, err1, pert in errors:
        print("\t{:} --> {:.3f}% \n\tGood".format(date1, pert))


if __name__ == '__main__':
    topmost_articles()
    topmost_authors()
    errors()
    print ''
