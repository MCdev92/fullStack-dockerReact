import './App.css';
import axios from 'axios';
import {useState, useEffect} from 'react'; 

function App() {

  const [recipe, setRecipe] = useState([]);

  useEffect(() => {
    axios.get('/api').then(res => setRecipe(res.data)); 
  }, []);

  return recipe.map((r, index)=> {
    return <p key={index}>{r.id} {r.title} {r.instructions} </p>
  })
    

}

export default App;
