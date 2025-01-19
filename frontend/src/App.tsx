import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Input from "./pages/Input";

const Home = () => <h1>Home Page</h1>;
const About = () => <h1>About Page</h1>;
const Contact = () => <h1>Contact Page</h1>;

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Input />} />
      </Routes>
    </Router>
  );
};

export default App;
