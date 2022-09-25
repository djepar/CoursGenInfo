import Intro1 from "./components/Intro1"
function App() {
  function Heading() {
    return <h1>This is an h1 heading</h1>
  }
  return ( 
    <div className="App"> 
     <Intro1 firstname="Jeremie" />
    </div> 
  ); 
} 
 
export default App;