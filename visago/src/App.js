import TopBar from "./topbar/TopBar.jsx"
import Footer from "./footer/Footer.jsx"
import Home from "./pages/home/Home.jsx"
import Signin from "./pages/signin/Signin.jsx"
import About from "./pages/about/About.jsx"
import Contact from "./pages/contact/Contact.jsx"

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";

function App() {
  
  return (
    <Router>
    <TopBar />
   
    <Routes>

      <Route path="/" element={<Home/>}/>      
      <Route path="/signin" element={<Signin/>}/>  
      <Route path="/about" element={<About/>}/>
      <Route path="/contact" element={<Contact/>}/>

    </Routes>
   
    <Footer/>
    </Router>
  );
}

export default App;
