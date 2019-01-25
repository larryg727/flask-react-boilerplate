import React, { Component } from 'react';
import { Router, Route, Switch } from 'react-router-dom';
import history from './history';
import Index from './components/index';
import NotFound from './components/NotFound';
import Navbar from './components/Navbar';
import Register from './components/register/register';

class App extends Component {
    render() {
        return (
            <Router history={history}>
                <React.Fragment>
                    <Navbar />
                    <Switch>
                        <Route exact path="/" component={Index} />
                        <Route path="/register" component={Register} />
                        <Route component={NotFound} />
                    </Switch>
                </React.Fragment>
            </Router>
        );
    }
}

export default App;
