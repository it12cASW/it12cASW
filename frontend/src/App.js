
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Login from './views/Login/Login';
import Register from './views/Register/Register';
import Panel from './views/Panel/Panel';


function App() {
  return (
    <Routes>
      <Route path="/" element={<Panel />} />    
    </Routes>
  );
}

export default App;
