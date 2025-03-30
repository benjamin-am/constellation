import "./Header.scss";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";


function Header() {
     const navigate = useNavigate();
    
     const handleGoHome = () => {
        navigate("/");
      };
    return(
        <nav className="nav">
           <ul>
               <button className="button" onClick={handleGoHome}>
                 Home
               </button>
               {/* <button className="button">
                   <Link to="/notes">Write Notes</Link>
               </button>
               <button className="button">
                   <Link to="/pastNotes">Review Past Notes</Link>
               </button> */}
           </ul>
           </nav>
           
       )
}

export default Header;