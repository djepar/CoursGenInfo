import logo from './logo.svg';
import './App.css';
import Title from './Title';
import Body from './Body';
import * as React from "react"; 
import {useState, useEffect} from 'react';

const Row = ({children, spacing}) => {
  const childStyle = {
    marginLeft: `${spacing}px`,
  };

  return (
    <div classname="Row">
      {React.Children.map(children, (child, index) => {
        return React.cloneElement(child, {
          style: {
            ...child.props.style,
            ...(index > 0 ? childStyle : {}),
          },
        });
      })}
    </div>
  );
};

const withMousePosition = (WrappedComponent) => {
  return (props) => {
    const [mousePosition, setMousePosition] = React.useState({
      x:0,
      y: 0,
    })

    useEffect(() => {
      const handleMousePositionChange = (e) => {
        setMousePosition({
          x: e.clientX,
          y: e.clientY,
        });
      };
      window.addEventListener("mousemove", handleMousePositionChange);
      return () => {
        window.removeEventListener("mouseover", handleMousePositionChange);
      }
    }, []);

    return <WrappedComponent {...props} mousePosition={mousePosition} />;
  }
}

const PanelMouseTracker = withMousePosition(PanelMouseLogger);
const PointMouseTracker = withMousePosition(PointMouseLogger);



function LiveOrders() {
  return (
      <div className="App">
          <Row spacing={32}>
              <p>Pizza Margarita</p>
              <p>2</p>
              <p>30$</p>
              <p>18:30</p>
              <p>John</p>
          </Row>
      </div>
  )
}


const PanelMouseLogger = ({ mousePosition}) => {
  if (!mousePosition) {
    return null;
  }

  return (
    <div className='BasicTracker'>
      <p>Mouse position :</p>
      ({mousePosition.x}, {mousePosition.y})
    </div>
  );
};
const PointMouseLogger = ({ mousePosition}) => {
  if (!mousePosition) {
    return null;
  }
  return (
    <p>
      ({mousePosition.x}, {mousePosition.y})
    </p>
  );
};



function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      
      <div>
      <PanelMouseTracker />
      <PointMouseTracker/>

      </div>
    


      <div>Bonjour</div>
      {/** JSX removes whitespaces at the beginning and end of a line, as well as blank lines  */}
      <div> No blank line     </div>
      <div>
          Neither here
      </div>

      {/** New lines adjacent to tags are removed */}
      <div>

            No new line here
      </div>

      {/** JSX condenses new lines that happen in the middle of string literals into a single space"  */}
    <div>
      New line that happen
      In the middle of a string literals
      into a single space
      
    </div>
      {/** You can provide JSX elements as children to display nested components */}
      <Body>
        <Title/>
      </Body>

      <Title/>

      <div />
    {/** false, null, undefined, and true are all valid children. They simply don't render anything. 
     * The bellow expression will all render the same things */}
    <div></div>

    <div>{false}</div>

    <div>{null}</div>

    <div>{undefined}</div>

    <div>{true}</div>
      
   

    </div>


  );
}

export default App;
