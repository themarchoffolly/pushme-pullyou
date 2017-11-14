---?image=assets/image/patrick-tomasso.jpg

# Code Graffiti

### A GitPitch Presentation Template

---?image=assets/image/kimberly-farmer.jpg

## Template Features

- Code Presenting
  + Repo Source
  + GIST
  + Static Block
- Custom CSS Styling
- Custom TOC Titles
- Custom Logo & Footnotes
- Default Background Image
- Slide-specific Background Images

---?code=src/go/server.go&title=Golang File

@[1,3-6](Present code found within any repo source file.)
@[8-18](Without ever leaving your slideshow.)
@[19-28](Using GitPitch code-presenting with annotations.)

---?gist=onetapbeyond/494e0fecaf0d6a2aa2acadfb8eb9d6e8&title=Scala GIST

@[1,3-6](Present code found within any GitHub GIST.)
@[8-18](Have GIST source beautifully rendered on your slides.)
@[19-28](Again, all this without ever leaving your slideshow.)

---?image=assets/image/simon-matzinger.jpg&opacity=50

@title[JavaScript Block]

<p><span class="slide-title">JavaScript Block</span></p>

```javascript
// Include http module.
var http = require("http");

// Create the server. Function passed as parameter
// is called on every request made.
http.createServer(function (request, response) {
  // Attach listener on end event.  This event is
  // called when client sent, awaiting response.
  request.on("end", function () {
    // Write headers to the response.
    // HTTP 200 status, Content-Type text/plain.
    response.writeHead(200, {
      'Content-Type': 'text/plain'
    });
    // Send data and end response.
    response.end('Hello HTTP!');
  });

// Listen on the 8080 port.
}).listen(8080);
```

@[1,2](Present code inlined within markdown on any slide.)
@[9-17](With code-syntax highlighting as good as any IDE.)
@[19-20](And all of this works seamlessly, both online and offline.)

---?image=assets/image/kimberly-farmer.jpg

## Template Help

- [Code Presenting](https://github.com/gitpitch/gitpitch/wiki/Code-Presenting)
  + [Repo Source](https://github.com/gitpitch/gitpitch/wiki/Code-Delimiter-Slides)
  + [GIST](https://github.com/gitpitch/gitpitch/wiki/GIST-Slides)
  + [Static Block](https://github.com/gitpitch/gitpitch/wiki/Code-Slides)
- [Custom CSS Styling](https://github.com/gitpitch/gitpitch/wiki/Slideshow-Custom-CSS)
- [Custom TOC Titles](https://github.com/gitpitch/gitpitch/wiki/Table-of-Contents)
- [Custom Logo & Footnotes](https://github.com/gitpitch/gitpitch/wiki/Footnote-Setting)
- [Default Background Image](https://github.com/gitpitch/gitpitch/wiki/Background-Setting)
- [Slide-specific Background Images](https://github.com/gitpitch/gitpitch/wiki/Image-Slides#background)

---?image=assets/image/clark_tibbs.jpg

@title[Fork this Repo!]

<br><br><br>
<br><br><br>
<br><br><br>

### Get started, <a target="_blank" href="https://github.com/gitpitch/template-code-graffiti-wood">fork this presentation template <i class="fa fa-external-link" style="margin-left: 10px" aria-hidden="true"></i></a>

