### Why you should try React Native

<span class="subtitle">for your next mobile project.</span>

---

## Gwen Faraday

- Developer at Fusion Alliance
- freeCodeCamp Indy
<li><a href="https://github.com/gwenf">github.com/gwenf</a></li>
<li><a href="https://twitter.com/gwen_faraday">@gwen_faraday</a></li>
<li>gwenfaraday@gmail.com</li>

---

## What is React Native?

- Mobile Apps in JavaScript |
- Cross-platform |
- Declarative |
- Uses the React Paradigm |
- Learn once build anywhere |

---

@title[React - JSX]

```html
import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class App extends Component {
    render() {
        return (
            <div>
                <h1>Hello App!</h1>
            </div>
        );
    }
}
ReactDOM.render(<app></app>, document.getElementById('root'));
```

---

@title[React - JSX]

```html
import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class App extends Component {
    constructor () {
        super();
        this.state = {
            count: 0
        };
        this.add = this.add.bind(this);
    }

    add () {
        this.setState({
            count: this.state.count + 1
        });
    }

    render () {
        return (
            <div>
                <h1>Count = {this.state.count}</h1>
                <button>Add</button>
            </div>
        );
    }
}
ReactDOM.render(<app></app>, document.getElementById('root'));
```

---

@title[React Native - JSX]

```
import React, { Component } from 'react';
import { AppRegistry, View, Text } from 'react-native';

class App extends Component {
    render() {
        return (
            <view>
                <text>Hello App!</text>
            </view>
        );
    }
}
AppRegistry.registerComponent('AwesomeProject', () =&gt; App);
```

---

@title(React Native - JSX)

```
import React, { Component } from 'react';
import {
    AppRegistry,
    View,
    Text,
    TouchableOpacity
} from 'react-native';

class App extends Component {
    constructor () {
        super();
        this.state = {
            count: 0
        };
        this.add = this.add.bind(this);
    }

    add () {
        this.setState({
            count: this.state.count + 1
        });
    }

    render() {
        return (
            <view>
                <text>Count: {this.state.count}</text>
                <touchableopacity>
                <text>Add One</text>
                </touchableopacity>
            </view>
        );
    }
}
AppRegistry.registerComponent('AwesomeProject', () =&gt; App);
```

---

@title[Default Styling with Flexbox]

```yaml
display: 'flex'
flex-direction: 'column'
```

---

@title[Benefits of React Native]

- Fast Developer Iteration
- Cross-platform code sharing
- Native Views
- Performance
- Built in developers tools
- Re-use web skills

---

@title[Web Ecosystem]

- Geolocation
- Fetch
- WebGL
- NPM/JS Libraries

---

The End
