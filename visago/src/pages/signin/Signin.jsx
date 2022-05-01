import "./signin.css";
import two from "./two.jpg";
import three from "./three.webp";

export default function Signin() {
  return (
    
    <div className="signin">
    
    <img className="signinImg" src={three}/>
    
        <span className="signintitle">SIGN IN</span>
        
        <div className="trans"/>
    <form className="signinform">
    
    
    
    <div className="space"/>
        <label>Batch level</label>
        <input type="text" className="signinput" placeholder="Enter the batch level..."/>
        <div className="space"/>
        <label>Level</label>
        <input type="text" className="signinput" placeholder="Enter the level..."/>
        <div className="space"/>
        <label>Subject</label>
        <input type="text" className="signinput" placeholder="Enter the subject..."/>
        <div className="space"/>
        <label>Student ID</label>
        <input type="text" className="signinput" placeholder="Enter the student ID..."/>
        <div className="space"/>
        <label>Session</label>
        <input type="text" className="signinput" placeholder="Enter the session..."/>
        <div className="space"/>
        <button className="signinbtn">SIGN IN</button>
        
    </form>
      
    </div>
  )
}
