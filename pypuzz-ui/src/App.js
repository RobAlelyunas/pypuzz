import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          PyPuzz UI initial checkin
        </p>
        <a
          className="App-link"
          href="http://pypuzz-pilot.us-east-2.elasticbeanstalk.com/anagrams"
          target="_blank"
          rel="noopener noreferrer"
        >
          Server side page
        </a>
      </header>
    </div>
  );
}

export default App;
