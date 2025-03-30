import "./Header.scss";
import { Link } from "react-router-dom";


function Header() {
    return(
        <header className="header">
            <div className="header__container">
                <div className="header__wrapper1">
                    <button className="button">
                        <Link to="/">Home</Link>
                    </button>
                    <button className="button">
                        <Link to="/notes">Take Notes</Link>
                    </button>
                </div>
            </div>
        </header>
    )
}

export default Header;