import "./topbar.css";
import logo from './logo.png';
import {Link} from "react-router-dom";

export default function topbar() {
  
  return (
    <div className='top'>
      <div className="topLeft">
      <a href="https://www.facebook.com/" >
        <i class="topIcon fa-brands fa-facebook-square"></i>
        </a>
        <a href="https://twitter.com/?lang=en">
        <i class="topIcon fa-brands fa-twitter-square"></i>
        </a>
        <a href="https://www.instagram.com/">
        <i class="topIcon fa-brands fa-instagram"></i>
        </a>
      </div>
      <div className="topCenter">
        <ul className="topList">
        
          <li className="topIcon topListItem">
          <Link to="/"> HOME </Link> 
          </li>

         

          <li className="topIcon topListItem">
          <Link to="/Contact"> CONTACT </Link>
           </li>

          <li className="topIcon topListItem"> 
          <Link to="/About">ABOUT </Link>
          </li>

          
        </ul>
      </div>
      <div className="topRight">
        
        <img className="topImg" src={logo}/>
        
        <i className="topSearchIcon fa-solid fa-magnifying-glass"></i>
        <button className="signInBtn">Sign Up</button>
      </div>
       
    </div>
  )
}
