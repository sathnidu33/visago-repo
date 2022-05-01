import Header from "../../header/header"
import Posts from "../../posts/Posts"
import SideBar from "../../sidebar/SideBar"
import "./home.css"

export default function home() {
  return (
    <>
    <Header/>
    <div className="home">
      
      <Posts/>
      <SideBar/>
    </div>
    </>
  )
}
