import { Routes, Route, Link } from 'react-router-dom';
import axios from "axios";
import { useEffect, useState } from 'react';
import './App.css';
import { Button } from './Components/Button';
import { Category } from './Components/Category';

function App() {
  const [category, setCategory] = useState([])

  async function getCategory() {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/category/')
      console.log(response.data);
      setCategory(response.data)
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    getCategory()
  }, []);

  return (
    <div className="App">
      <nav className='nav'>
        <Link to='/'>Home</Link>
      </nav>
      <h2>Все категории</h2>
      <div className='btn-category'>
        {category && category.map((item, index) => <Link to={item.name}>
          <Button name={item.name} key={index} />
        </Link>)}
      </div>

      <Routes>
        <Route path="/Десерты" element={<Category name="Десерты"/>}/>
        <Route path="/Пироги" element={<Category name="Пироги"/>}/>
      </Routes>
    </div>
  );
}

export default App;
