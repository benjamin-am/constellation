import "./Header.scss";

function Header() {
    return(
        <header className="header">
            <div className="header__container">
                <div className="header__wrapper1">
                    <button className="button">
                        Current Notes
                    </button>
                    <button className="button">
                        Past Notes
                    </button>
                </div>
            </div>
        </header>
    )
}

export default Header;