import "./VerticalNavBar.scss";

function VerticalNavBar() {
    return(
     <nav className="nav">
        <ul>
            <button className="button">
            Current Notes
            </button>
            <button className="button">
            Past Notes
            </button>
        </ul>
        </nav>
        
    )
}

export default VerticalNavBar;