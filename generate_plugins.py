#!/usr/bin/python
# Copyright (c) 2012 Aravinda VK<mail@aravindavk.in>
# http://aravindavk.in

# MIT License
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

langs = (('Bengali', 'bn'),
         ('Gujarati', 'gu'),
         ('Hindi', 'hi'),
         ('Kannada', 'kn'),
         ('Malayalam', 'ml'),
         ('Marathi', 'mr'),
         ('Nepali', 'ne'),
         ('Oriya', 'or'),
         ('Punjabi', 'pa'),
         ('Sanskrit', 'sa'),
         ('Sindhi', 'sd'),
         ('Tamil', 'ta'),
         ('Telugu', 'te'))

tmpl = """<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/" xmlns:moz="http://www.mozilla.org/2006/browser/search/">
  <Author>Aravinda VK, mail@aravindavk.in</Author>
  <License>MIT</License>
  <ShortName>Wiktionary ({{LANG_CODE}})</ShortName>
  <Description>{{LANG_NAME}} Wiktionary Search Plugin</Description>
  <InputEncoding>UTF-8</InputEncoding>
  <Image width="16" height="16">data:image/icon;base64,AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAEAgQAhIOEAMjHyABIR0gA6ejpAGlqaQCpqKkAKCgoAPz9/AAZGBkAmJiYANjZ2ABXWFcAent6ALm6uQA8OjwAiIiIiIiIiIiIiI4oiL6IiIiIgzuIV4iIiIhndo53KIiIiB/WvXoYiIiIfEZfWBSIiIEGi/foqoiIgzuL84i9iIjpGIoMiEHoiMkos3FojmiLlUipYliEWIF+iDe0GoRa7D6GPbjcu1yIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</Image>
  <Url type="application/x-suggestions+json" method="GET" template="http://{{LANG_CODE}}.wiktionary.org/w/api.php">
    <Param name="action" value="opensearch"/>
    <Param name="search" value="{searchTerms}"/>
  </Url>
  <Url type="text/html" method="GET" template="http://{{LANG_CODE}}.wiktionary.org/wiki/Special:Search">
    <Param name="search" value="{searchTerms}"/>
    <Param name="sourceid" value="Mozilla-search"/>
  </Url>
  <SearchForm>http://{{LANG_CODE}}.wiktionary.org/wiki/Special:Search</SearchForm>
</OpenSearchDescription>"""


for lang in langs:
    op = tmpl.replace("{{LANG_NAME}}", lang[0]).replace("{{LANG_CODE}}", lang[1])
    f = open("plugins/" + lang[1] + ".xml", "w")
    f.write(op)
    f.close()
    print "\033[32m[OK]\033[0m Generated plugins/%s.xml" % lang[1]
