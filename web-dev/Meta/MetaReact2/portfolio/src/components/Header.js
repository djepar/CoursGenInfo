import React from 'react';
import { Link } from 'react-router-dom';
import { FaFacebook, FaTwitter, FaInstagram } from 'react-icons/fa';

const Header = () => {
  return (
    <header>
      <div className="logo">Logo</div>
      <nav>
        <ul className="social-media">
          <li><a href="https://www.facebook.com"><FaFacebook /></a></li>
          <li><a href="https://www.twitter.com"><FaTwitter /></a></li>
          <li><a href="https://www.instagram.com"><FaInstagram /></a></li>
        </ul>
        <ul className="menu">
          <li><Link to="/contact">Contact</Link></li>
          <li><Link to="/projects">Projects</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
