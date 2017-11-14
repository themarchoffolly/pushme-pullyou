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

```js
class TodoApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = { items: [], text: '' };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  render() {
    return (
      <div>
        <h3>TODO</h3>
        <TodoList items={this.state.items} />
        <form onSubmit={this.handleSubmit}>
          <input
            onChange={this.handleChange}
            value={this.state.text}
          />
          <button>
            Add #{this.state.items.length + 1}
          </button>
        </form>
      </div>
    );
  }

  handleChange(e) {
    this.setState({ text: e.target.value });
  }
}
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

