import { Link } from "react-router-dom";
import Welcome from "../components/Welcome/Welcome";
import Header from "../components/Header/Header"

import "../pages/HomePage.scss";

function HomePage() {

    return(
        <section className="body">
            <div className="title__container">
                <p className="title">
                    constallation
                </p>
            </div>
        <button className="button">
         <Link to="/notes">  Get Started </Link>
        </button>
        </section>
 
    )
}

export default HomePage;
