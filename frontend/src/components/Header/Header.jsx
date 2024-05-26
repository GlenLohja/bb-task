import React, { useState } from "react";
import PropTypes from "prop-types";
import reactImg from "../../assets/bb.png";

const MobileMenuButton = ({ isOpen, onClick }) => (
  <button
    type="button"
    className="inline-flex p-2 text-white transition-all duration-200 rounded-md lg:hidden focus:bg-gray-100 hover:bg-gray-100"
    onClick={onClick}
    aria-expanded={isOpen}
    aria-controls="mobile-menu"
  >
    {isOpen ? (
      <svg
        className="block w-6 h-6"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M6 18L18 6M6 6l12 12"
        />
      </svg>
    ) : (
      <svg
        className="block w-6 h-6"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M4 8h16M4 16h16"
        />
      </svg>
    )}
  </button>
);

MobileMenuButton.propTypes = {
  isOpen: PropTypes.bool.isRequired,
  onClick: PropTypes.func.isRequired,
};

const NavLink = ({ href, children }) => (
  <a
    href={href}
    title={children}
    className="text-base font-medium text-white transition-all duration-200 hover:text-customHoverYellow focus:text-customHoverYellow"
  >
    {children}
  </a>
);

NavLink.propTypes = {
  href: PropTypes.string.isRequired,
  children: PropTypes.node.isRequired,
};

const MobileNavLink = ({ href, children }) => (
  <a
    href={href}
    title={children}
    className="inline-flex py-2 text-base font-medium text-black transition-all duration-200 hover:text-blue-600 focus:text-blue-600"
  >
    {children}
  </a>
);

MobileNavLink.propTypes = {
  href: PropTypes.string.isRequired,
  children: PropTypes.node.isRequired,
};

const Header = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <header className="pb-6 bg-customBlue lg:pb-0">
      <div className="px-4 mx-auto max-w-7xl pt-2 sm:pt-0 sm:px-6 lg:px-8">
        <nav className="flex items-center justify-between h-16 lg:h-20">
          <div className="flex-shrink-0">
            <a href="#" title="Home" className="flex">
              <img
                className="w-auto h-16 lg:h-12"
                src={reactImg}
                alt="b&b logo"
              />
            </a>
          </div>

          <MobileMenuButton
            isOpen={isMobileMenuOpen}
            onClick={toggleMobileMenu}
          />

          <div className="hidden lg:flex lg:items-center lg:ml-auto lg:space-x-10">
            <NavLink href="#">Home</NavLink>
          </div>
        </nav>

        {isMobileMenuOpen && (
          <nav
            id="mobile-menu"
            className="pt-4 pb-6 bg-white border border-gray-200 rounded-md shadow-md lg:hidden"
          >
            <div className="flow-root">
              <div className="flex flex-col px-6 -my-2 space-y-1">
                <MobileNavLink href="#">Home</MobileNavLink>
              </div>
            </div>
          </nav>
        )}
      </div>
    </header>
  );
};

export default Header;
