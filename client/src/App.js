import React, { Component } from 'react';
import { Router, Route, Switch } from 'react-router-dom';
import history from './history';
import Index from './components/index';
import NotFound from './components/NotFound';

class App extends Component {
    render() {
        return (
            <Router history={history}>
                <Switch>
                    <Route exact path="/" component={Index} />

                    <Route component={NotFound} />
                </Switch>
            </Router>
        );
    }
}

export default App;
