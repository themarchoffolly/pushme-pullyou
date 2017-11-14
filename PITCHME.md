---?image=assets/image/ivan_televnyy.jpg

# Code Graffiti

### A GitPitch Presentation Template

---?image=assets/image/lukas_blazek.jpg

## Template Features

- Code Presenting
  + Repo Source
  + GIST
  + Static Block
- Default Background Image
- Slide-specific Background Images
- Custom CSS Styling
- Custom TOC Titles
- Custom Logo & Footnotes

---?code=src/go/server.go&title=Golang File

@[1,3-6](Present code found within any repo source file.)
@[8-18](Without ever leaving your slideshow.)
@[19-28](Using GitPitch code-presenting with annotations.)

---?gist=onetapbeyond/494e0fecaf0d6a2aa2acadfb8eb9d6e8&title=Scala GIST

@[1,3-6](Present code found within any GitHub GIST.)
@[8-18](Have GIST source beautifully rendered on your slides.)
@[19-28](Again, all this without ever leaving your slideshow.)

---?image=assets/image/maarten_deckers.jpg

@title[JavaScript Block]

<p><span class="slide-title">JavaScript Block</span></p>

```javascript
// Include http module.
var http = require("http");

// Create the server. Function passed as parameter is called on every request made.
// request variable holds all request parameters
// response variable allows you to do anything with response sent to the client.
http.createServer(function (request, response) {
	// Attach listener on end event.
	// This event is called when client sent all data and is waiting for response.
	request.on("end", function () {
		// Write headers to the response.
		// 200 is HTTP status code (this one means success)
		// Second parameter holds header fields in object
		// We are sending plain text, so Content-Type should be text/plain
		response.writeHead(200, {
			'Content-Type': 'text/plain'
		});
		// Send data and end response.
		response.end('Hello HTTP!');
	});
// Listen on the 8080 port.
}).listen(8080);
```

@[2-7](Present code inlined within markdown on any slide.)
@[13-21](With code-syntax highlighting as good as any IDE.)
@[26-28](And all this works seamlessly both online and offline.)

---?image=assets/image/clark_tibbs.jpg

@title[Fork this Repo!]

<br><br><br>
<br><br><br>
<br><br><br>

### Get started by forking this repo...

