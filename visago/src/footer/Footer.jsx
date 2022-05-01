import React from 'react'
import "./footer.css"
import {BottomNavigation, BottomNavigationAction} from '@material-ui/core'
import FacebookIcon from '@material-ui/icons/Facebook';
import TwitterIcon from '@material-ui/icons/Twitter';
import InstagramIcon from '@material-ui/icons/Instagram';
import YouTubeIcon from '@material-ui/icons/YouTube';

function Footer() {
    return (
      
      
        <BottomNavigation>
        <div className='footer'>
          <a href="https://www.facebook.com/">
          <BottomNavigationAction color="red" label="Facebook" value="recents" icon={<FacebookIcon  style={{fill: "#3b5998"}}/>} />
          </a>
          <a href="https://twitter.com/?lang=en">
          <BottomNavigationAction label="Twitter" value="favorites" icon={<TwitterIcon  style={{fill: "#1DA1F2"}}/>} />
          </a>
          <a href="https://www.instagram.com/">
          <BottomNavigationAction label="Instagram" value="nearby" icon={<InstagramIcon  style={{fill: " #C13584"}}/>} />
          </a>
          <a href="https://www.youtube.com/">
          <BottomNavigationAction label="YouTube" value="folder" icon={<YouTubeIcon  style={{fill: "#c4302b"}}/>} />
          </a>
        </div>
        </BottomNavigation>
       
        
)
}

export default Footer
