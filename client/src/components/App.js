// import { Router, Routes, Route, } from "react-router-dom";
// import './App.css';
// import Pizza from './pizza'; 
// import Restaurants from './restaurants';
// import Home from "./home";
// import { createBrowserHistory } from "history"

// const history = createBrowserHistory();

// function App() {

  
//   return (
//     <Router history={history}>
//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/pizzas" element={<Pizza />} />
//         <Route path="/restaurants" element={<Restaurants />} />
//       </Routes>
//     </Router>
//   );
// }

// export default App;
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Pizza from './pizza'; 
import Restaurants from './restaurants';
import Home from './home';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/pizzas" element={<Pizza />} />
        <Route path="/restaurants" element={<Restaurants />} />
      </Routes>
    </Router>
  );
}

export default App;
