
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Pizza from './pizza'; 
import Restaurants from './restaurants';
import Home from './home';
import RestaurantDetails from './Restaurant';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/pizzas" element={<Pizza />} />
        <Route path="/restaurants" element={<Restaurants />} />
        <Route path="/restaurants/:restaurantId" element={<RestaurantDetails/>} />
      </Routes>
    </Router>
  );
}

export default App;
