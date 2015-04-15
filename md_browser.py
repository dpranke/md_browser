#!/usr/bin/env python

# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Simple Markdown browser for a Git checkout."""

from __future__ import print_function

import SimpleHTTPServer
import SocketServer
import argparse
import codecs
import os
import socket
import subprocess
import sys


try:
  import markdown
except ImportError:
  print("markdown doesn't seem to be installed; ",
        "run 'sudo pip install markdown'", file=sys.stderr)
  sys.exit(1)


CURDIR = os.path.abspath(os.path.dirname(__file__))


def main(argv):
  parser = argparse.ArgumentParser(prog='md_browser')
  parser.add_argument('-p', '--port', type=int, default=8080,
                      help='port to run on (default = %(default)s)')
  args = parser.parse_args(argv)

  top_level = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'])
  s = Server(args.port, top_level.strip())

  try:
    s.serve_forever()
    s.shutdown()
    return 0
  except KeyboardInterrupt:
    return 130


class Server(SocketServer.TCPServer):
  def __init__(self, port, top_level):
    SocketServer.TCPServer.__init__(self, ('0.0.0.0', port), Handler)
    self.port = port
    self.top_level = top_level

  def server_bind(self):
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind(self.server_address)


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
    full_path = os.path.abspath(os.path.join(self.server.top_level,
                                             self.path[1:]))
    if not full_path.startswith(self.server.top_level):
      self._do_out_of_tree()
    elif not os.path.exists(full_path):
      self._do_not_found()
    elif self.path.endswith('.css'):
      self._do_css()
    elif self.path.endswith('.md'):
      self._do_md()
    else:
      self._do_unknown()

  def _do_css(self):
    if self.path == '/doc.css':
      contents = self._read(os.path.join(CURDIR, 'doc.css'))
    else:
      contents = self._read(self.path[1:])

    self.wfile.write(contents.encode('utf-8'))

  def _do_md(self):
    extensions = [
      'markdown.extensions.fenced_code',
      'markdown.extensions.tables',
      'markdown.extensions.toc',
    ]

    contents = self._read(self.path[1:])
    md_fragment = markdown.markdown(contents,
                             extensions=extensions,
                             output_format='html4').encode('utf-8')
    try:

      self.wfile.write(self._read(os.path.join(CURDIR, 'header.html'))
      self.wfile.write(md_fragment)
      self.wfile.write(self._read(os.path.join(CURDIR, 'footer.html'))
    except:
      raise

  def _do_not_found(self):
    self.wfile.write('<html><body>%s not found</body></html>' % self.path)

  def _do_unknown(self):
    self.wfile.write('<html><body>do not know how to serve %s</body></html>'
                     % self.path)

  def _read(self, path):
    if not path.startswith('/'):
      path = os.path.join(self.server.top_level, path)
    return codecs.open(path, mode='r', encoding='utf-8').read()



if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
