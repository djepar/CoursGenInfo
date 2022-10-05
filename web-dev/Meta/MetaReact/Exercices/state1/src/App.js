import logo from './logo.svg';
import React, { useState } from 'react';
import './App.css';
import Heading from './Heading';

function App() {
  const [word, setWord] = React.useState('Eat')
  function handleClick(){
    setWord('Drink')

  }
  return(
    <div className="App">
      <Heading message={word + " at Little Lemon"}/>
      <button onClick={handleClick}>Click here</button>
    </div>
  );
}

export default App;
