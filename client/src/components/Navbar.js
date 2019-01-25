import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';

class Navbar extends Component {
    state = {};
    render() {
        return (
            <div className="navbar">
                <NavLink exact to="/" activeClassName="active">
                    Home
                </NavLink>
                <NavLink to="/register" activeClassName="active">
                    Register
                </NavLink>
            </div>
        );
    }
}

export default Navbar;
