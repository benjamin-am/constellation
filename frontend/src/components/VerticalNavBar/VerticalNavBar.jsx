import "./VerticalNavBar.scss";
import { Link } from "react-router-dom";

function VerticalNavBar({onSave}) {


    return(
     <nav className="nav">
        <ul>
            <button className="button">
                <Link to="/">Home Test</Link>
            </button>
            <button className="button"
             onClick={onSave}>
            <Link to="/pastNotes">Save Current Notes</Link>
            </button>
            <button className="button">
                <Link to="/pastNotes">Review Past Notes</Link>
            </button>
        </ul>
        </nav>
        
    )
}

export default VerticalNavBar;