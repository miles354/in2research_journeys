# in2research_journeys

## Adding yourself as an author

Create a new file under the `_authors` directory named as `short_name.md` where `short_name` is the same that the `short_name` tag in the example below.

```md
---
short_name: davidps
name: David PS
project: HPC
year: 2025
---

David is an astrophysicist interested in brains.

```


## Adding a new post

Create a new file with the following format `YYYY-MM-DD-authorname-title.md` under the `_posts/yyyy/mm/` directory.

The file should look like

```md
---
title: Your Title
date: 2025-06-11
time: "15:30:00"
author: your-short-author-name
categories: ["learning", "python", "introduction"] # This is optional, list of categories that you want to add
layout: post
---

Here you write your content on markdown. If you want to add an image, you can add them under
`images/yyyy/mm` and link them as:

![](/images/yyyy/mm/image-file.jpg)

or if you want to have control of its size, using HTML format:

<img height="200px" src="/images/yyyy/mm/image-file.jpg" />
```
