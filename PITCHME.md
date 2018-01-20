# Reactive Native Code Test

### Using Language Hints

---

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

```html
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
