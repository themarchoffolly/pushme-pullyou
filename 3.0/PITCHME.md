## GitPitch

@snap[south span-100]
**3Test**
@snapend

---

[drag=50]
Grid 4.0 Syntax

---

@snap[north span-100]
Fenced Code Block w/Python-Markup
@snapend

```py
from cgi import escape
import sys, os
from flup.server.fcgi import WSGIServer

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    yield '<h1>FastCGI Environment</h1>'
    yield '<table>'
    for k, v in sorted(environ.items()):
        yield '<tr><th>%s</th><td>%s</td></tr>' % (escape(k), escape(v))
    yield '</table>'

WSGIServer(app).run()
```
@[8-12](This annotation directly follows the three-ticks.)

---

# The End

