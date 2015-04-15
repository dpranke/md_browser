# md_browser

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
