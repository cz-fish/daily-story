# Daily Story blog

https://cz-fish.github.io/daily-story/#

This is built with Jekyll and only slightly modified default template.

## Posting new update
Due to the nature of the blog, all posts are just a single image. To not copy paste the same post each day, there is a script, `post.py`, which scans the directory with the images (`spaceboy`) and regenerates all the posts.

## Running locally
Install Jekyll. Run `jekyll build` in the root directory to rebuild the generated site (all files go to `_site`). There is also a way to make jekyll continuously monitor the files and rebuild automatically.

To host the site, it would be enough to just go to the `_site` directory and start the Python webserver. But because on github the site will be under /daily-story subdir, we have to have the same local layout as well, so that absolute URLs work. For that reason there is `local/daily-story` symlink, so enter `local` and serve from there.

```
cd local
python3.8 -m http.server
```

Note that because `jekyll build` includes the `local` symlink in the built `_site`, things can sometimes get weird and the build fails with

```
jekyll 3.1.6 | Error:  No such file or directory @ rb_file_s_stat - <some file under local/>
```

Just deleting `_site/local` and running `jekyll build` again seems to do the trick.

TODO: it seems that there might also be `jekyll serve` command which might solve these difficulties.

## Serving on Github

Github supports Jekyll and would be able to build the HTML pages directly from master branch, but it doesn't allow running Ruby plugins. Since the blog is now using jekyll-archives plugin to show each story separately, it cannot be served from master branch any more.

Instead, run `jekyll build --future` locally, switch to the `gh-pages` branch and move contents of `_site/` over to the root in this branch; then push `gh-pages` branch.
(Note that `--future` flag to `jekyll build` will also include posts scheduled for the future)

## Notes
By default, the width of the images is limited on the index page. To make the images clickable / expandable, I use [lightbox plugin](https://jekyllcodex.org/without-plugin/lightbox). It only works on links, so every picture in every post is wrapped in a link. The script itself is included in the footer. It is included by a relative path that might not work on all pages, but works on the index. That is required when testing locally, but for github deployment, it could have the full path.
