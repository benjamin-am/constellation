import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import Welcome from "../components/Welcome/Welcome";
import Header from "../components/Header/Header";

import "../pages/HomePage.scss";

function generateStars(num) {
  const stars = [];
  for (let i = 0; i < num; i++) {
    const top = Math.random() * 100;
    const left = Math.random() * 100;
    stars.push(
      <div
        key={i}
        className="star"
        style={{
          top: `${top}%`,
          left: `${left}%`,
        }}
      />
    );
  }
  return stars;
}

function HomePage() {
  return (
    <section className="body">
      <div className="title__container">
        <p className="title">constellation</p>
        <button className="button button--large">
          <Link to="/notes"> Get Started </Link>
        </button>
      </div>
      <div className="constellation">{generateStars(70)}</div>
    </section>
  );
}

export default HomePage;
