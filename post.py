#!/usr/bin/python3.8

import datetime
import os
import re

STORY = 'spaceboy'
BASE_DATE = datetime.date(2020, 11, 15)

pics = os.listdir(STORY)
for pic in pics:
    m = re.search(r'(\d+) - (.*)\.png', pic)
    if m is None:
        continue
    date = BASE_DATE + datetime.timedelta(days=(int(m.group(1)) - 1))
    title = m.group(2)
    fname = f"_posts/{date.strftime('%Y-%m-%d')}-{title}.md"
    title = title[0].upper() + title[1:]
    url = f"{STORY}/{pic.replace(' ', '%20')}"

    with open(fname, 'wt') as f:
        print(f"""---
layout: post
title:  "{title}"
date:   {date.strftime('%Y-%m-%d')} 00:00:00 +0000
categories: {STORY}
---

[![{title}]({{{{ site.baseurl }}}}/{url})]({{{{ site.baseurl }}}}/{url})
""",
            file=f)

