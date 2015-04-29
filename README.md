# md\_browser

This is a simple tool to render the markdown docs in a chromium checkout
locally. It is written in Python and requires that the 'markdown' package
be installed.

It attempts to emulate the flavor of Markdown implemented by
[Gitiles](https://gerrit.googlesource.com/gitiles/+/master/Documentation/markdown.md).

Gitiles is the source browser running on https://chromium.googlesource.com,
and can be run locally, but to do so requires a Java install and a Buck
install, which can be slightly annoying to set up on Mac or Windows.

This is a lighterweight solution, which also allows you to preview uncommitted
changes (i.e., it just serves files out of the filesystem, and is not a
full Git repo browser like Gitiles is).

To run md\_browser:

1. cd to the repository you want to browse

2. run $PATH\_TO\_MD\_BROWSER

3. There is no step three.

This will run a local web server on port 8080 that points to the top
of the repo.

As noted above, it requires the `markdown` Python package to be installed
on your machine. If you don't have that installed, run

    % sudo pip install markdown

If you don't have `pip` installed, run:

    % sudo easy_install pip

(I do not yet have install instructions for Windows, but if you can
get a working copy of pymarkdown, md\_browser should work fine).
