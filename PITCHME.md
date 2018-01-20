# Reactive Native Code Test

### Using Language Hints

---

```
import React, { Component } from 'react';

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
