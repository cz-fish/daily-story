#!/usr/bin/python3.8

import datetime
import os
import re

BASE_DATES = {
    'spaceboy': datetime.date(2020, 11, 15),
    'unsorted': datetime.date(2020, 11, 15)
}
STORIES = list(BASE_DATES.keys())

produced_posts = set()


def make_story(story):
    global produced_posts
    pics = os.listdir(story)
    for pic in pics:
        m = re.search(r'(\d+) - (.*)\.png', pic)
        if m is None:
            continue

        number = int(m.group(1))
        if number > 1000:
            # the number is a date: YYMMDD
            year = number // 10000
            month = (number // 100) % 100
            day = number % 100
            date = datetime.date(2000 + year, month, day)
        else:
            # number is the offset from base date (starting at 1 on the base date)
            date = BASE_DATES[story] + datetime.timedelta(days=(number - 1))

        title = m.group(2)

        fname = f"_posts/{date.strftime('%Y-%m-%d')}-{title}.md"
        while fname in produced_posts:
            # When two different stories have the same word on the same day then
            # we would have a clash - two posts with the same name - so we have to
            # differentiate
            fname = fname[:-3] + "_.md"
        produced_posts.add(fname)

        title = title[0].upper() + title[1:]
        url = f"{story}/{pic.replace(' ', '%20')}"

        with open(fname, 'wt') as f:
            print(f"""---
layout: post
title:  "{title}"
date:   {date.strftime('%Y-%m-%d')} 00:00:00 +0000
categories: {story}
---

[![{title}]({{{{ site.baseurl }}}}/{url})]({{{{ site.baseurl }}}}/{url})
""",
                file=f)


for story in STORIES:
    make_story(story)
