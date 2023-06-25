import logo from './logo.svg';
import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Home from './components/Home';
import Contact from './components/Contact';
import Projects from './components/Projects';
import Header from './components/Header';

const App = () => {
  return (
    <Router>
        <Route exact path="/" component={Home} />
        <Route path="/contact" component={Contact} />
        <Route path="/projects" component={Projects} />
    </Router>
    <Header />
  );
};

export default App;
