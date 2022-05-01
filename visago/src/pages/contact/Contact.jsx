import "./contact.css"
import React from 'react'
import six from "./six.jpg"

import nine from "./nine.jpg"



export default function Contact() {
  return (
    <div className="b">
      <img className="contactImg" src={six}/>
      <div className="leftBox">
       <h5>Contact Information</h5>
       <div className="space"></div>
       <p>To get register contacct us...</p>
       <div className="spacemore"></div>
       <div className="icons">
       <i class="fa-solid fa-phone"><span className="span">+94 75 470 0840</span></i>
       <div className="spacemore"></div>
       <i class="fa-solid fa-envelope"><span className="span">visago@gmail.com</span></i>
       <div className="spacemore"></div>
       <i class="fa-solid fa-location-dot"><span className="span">   Visago, Colombo 7</span></i>
       </div>
      </div>
      
    </div>
    
  )
}
