"""
Export the email templates and inline the CSS

Usage: python export_email_templates.py /path/to/simple.css
or:    python export_email_templates.py --clean
"""

import os
import sys
import re
from distutils.dir_util import copy_tree
from shutil import rmtree

import pynliner

BASE = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = BASE + '/gidsy_template/gidsy_reply_template/'
TARGET_DIR = BASE + '/export/'


def clean():
    try:
        rmtree(TARGET_DIR)
    except OSError:
        pass


def export_templates(css_path):
    clean()

    css = u'<style type="text/css">\n%s\n</style>' % open(css_path).read()

    copy_tree(SOURCE_DIR, TARGET_DIR)

    for dirpath, dirnames, filenames in os.walk(TARGET_DIR):
        for fpath in (dirpath + f for f in filenames if f.endswith('.html')):
            contents = open(fpath).read()
            contents = re.sub(ur'''<style.+?</style>''', css, contents, 1)
            contents = pynliner.fromString(contents)
            with open(fpath, 'w') as f:
                f.write(contents.encode('utf-8'))


if __name__ == "__main__":
    if '--clean' in sys.argv:
        print "Cleaning..."
        clean()
    else:
        print "Exporting..."
        export_templates(sys.argv[1])
