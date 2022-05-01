import "./about.css"
 import React from 'react'
 import two from "./two.jpg"
 
 export default function About() {
   return (
     <div>
     
     <img className="Img" src={two}/>
     <div className="visagoword">VISAGO</div>
     
     <div className="transparent">
    
   <p> VISAGO is an application programming interface which improves the inter connection between the student and the teacher by providing many facilities to the both ends than other online learning platforms. VISAGO offers teachers an easy and efficient way to deliver lessons to students with various tools including attendance marking of the session and this application will provides the engagement level of the overall class
   </p>
     </div>
     
     </div>
   )
 }
 