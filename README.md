# md\_browser

This is a simple tool to render the markdown docs in a chromium checkout
locally. It is written in Python and uses the Python 'markdown' package,
which is pulled in via a git submodule:

    % git clone --recursive https://github.com/dpranke/py_markdown

(If you have 'markdown' installed locally, you can skip the --recursive step.)

md\_browser attempts to emulate the flavor of Markdown implemented by
[Gitiles](https://gerrit.googlesource.com/gitiles/+/master/Documentation/markdown.md).

Gitiles is the source browser running on https://chromium.googlesource.com,
and can be run locally, but to do so requires a Java install and a Buck
install, which can be slightly annoying to set up on Mac or Windows.

This is a lighterweight solution, which also allows you to preview uncommitted
changes (i.e., it just serves files out of the filesystem, and is not a
full Git repo browser like Gitiles is).

To run md\_browser:

1. cd to the repository you want to browse

2. run `$PATH\_TO\_MD\_BROWSER\_CHECKOUT/md_browser.py`

3. There is no step three.

This will run a local web server on port 8080 that points to the top
of the repo.  You can specify a different port with the `-p` flag
