import {useState, useEffect} from 'react'; 
import api from './api'

// "useState" hook allows to keep state within react, so we know when state changes (shift and change pieces of data).
const App = () => {
  const [recipes, setRecipes] = useState([]);
  const [formData, setFormData] = useState({
    title: '',
    ingredients: '',
    directions:''
  });

// "fetRecipes" gets all our recipes from the fastAPI application
const fetchRecipes = async () => {
  const response = await api.get('/recipes/');
  setRecipes(response.data);
}

// "useEffect" hook : when this component loads (app.js), we'll fetch the "fetchRecipes"
useEffect(() => {
  fetchRecipes();
}, []);

 // Line 38: this will prevent form defaulting to submit the form, so we can handle the action of submitting.
  // line 40: when a new transaction is submitted, app will recall all transactions from db to keep application up-to-date in frontend
  // line 42: this will allow when the user fill the form and click submit to keep the data becasue the form submission will overwrite 
  const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api.post('/recipes/', formData);
    fetchRecipes();
    setFormData({
      title: '',
      ingredients: '',
      directions:''
    });
  };

  return (
    <div>
      {/* Your navigation bar code here */}
      <div className="container">
        <form onSubmit={handleFormSubmit}>
          {/* Your input fields for title, ingredients, and directions */}
        </form>

        <table className="table table-striped table-bordered table-hover">
          <thead>
            <tr>
              <th>Title</th>
              <th>Ingredients</th>
              <th>Directions</th>
            </tr>
          </thead>
          <tbody>
            {recipes.map((recipe) => (
              <tr key={recipe.id}>
                <td>{recipe.title}</td>
                <td>{recipe.ingredients}</td>
                <td>{recipe.directions}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default App;
