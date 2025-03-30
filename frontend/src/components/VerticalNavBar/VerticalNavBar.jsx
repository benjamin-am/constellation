import "./VerticalNavBar.scss";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import { useEffect } from "react";
import axios from "axios";

function VerticalNavBar({onSave, onAnalyze}) {
    const navigate = useNavigate();

    const handleSaveAndNavigate = () => {
        onSave(); 
        navigate("/pastNotes"); 
      };

      const handleGoHome = () => {
        navigate("/");
      };

      const handlePastNotes = () => {
        navigate("/pastNotes");
      };
    return(
     <nav className="nav">
        <ul>
            <button className="button" onClick={handleGoHome}>
            Home
            </button>
            <button className="button" onClick={handlePastNotes}>
            Review Past Notes
            </button>
            <button className="button"
             onClick={handleSaveAndNavigate}>
            Save Current Notes
            </button>
            <button className="button" onClick={onAnalyze}>
                Analyze
            </button>

            
        </ul>
        </nav>
        
    )
}

export default VerticalNavBar;