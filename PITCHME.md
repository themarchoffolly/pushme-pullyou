---?image=assets/image/ivan_televnyy.jpg

# Code Graffiti

### A GitPitch Presentation Template

---?image=assets/image/lukas_blazek.jpg

## About Presentation

---?code=src/go/server.go&title=Golang File

---?gist=onetapbeyond/494e0fecaf0d6a2aa2acadfb8eb9d6e8&title=Scala GIST

---?image=assets/image/maarten_deckers.jpg

@title[JavaScript Block]

JavaScript Block

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

  handleSubmit(e) {
    e.preventDefault();
    if (!this.state.text.length) {
      return;
    }
    const newItem = {
      text: this.state.text,
      id: Date.now()
    };
    this.setState(prevState => ({
      items: prevState.items.concat(newItem),
      text: ''
    }));
  }
}

class TodoList extends React.Component {
  render() {
    return (
      <ul>
        {this.props.items.map(item => (
          <li key={item.id}>{item.text}</li>
        ))}
      </ul>
    );
  }
}

ReactDOM.render(<TodoApp />, mountNode);
```

---?image=assets/image/clark_tibbs.jpg

@title[Fork this Repo!]

<br><br><br>
<br><br><br>
<br><br><br>

### Get started by forking this repo...

