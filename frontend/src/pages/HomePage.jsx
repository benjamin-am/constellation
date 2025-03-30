import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import Welcome from "../components/Welcome/Welcome";
import Header from "../components/Header/Header"

import "../pages/HomePage.scss";

function HomePage() {
    const navigate = useNavigate();
    const handleNotes = () => {
        navigate("/notes");
      };
    return(
        <section className="body">
            <div className="title__container">
                <p className="title">
                    constallation
                </p>
            </div>
        <button className="button" onClick={handleNotes}>
        Get Started
        </button>
        </section>
 
    )
}

export default HomePage;
