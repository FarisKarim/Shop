import React from 'react';
import logo from './logo.svg';
import './App.css';
import Reviews from './components/Reviews';
import Products from './components/Products';
import {BrowserRouter, Routes, Route} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    <div className="App">
      <Routes>
        <Route path = '/products' element = {<Products />} />
        <Route path = '/reviews' element = {<Reviews />}/>
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;
