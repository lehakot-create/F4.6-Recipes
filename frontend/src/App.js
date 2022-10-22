import axios from 'axios';
import { useEffect, useState } from "react";

function App() {
  const [category, setCategory] = useState([]);

  async function getCategory() {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/category/')
      console.log(response)
      setCategory(response.data)
    } catch (error) {
      console.log(error);
    }

  }

  useEffect(() => {
    getCategory()
  }, []);

  return (
    <div>
      Категории
      {category && category.map((item, index) => <button key={index}>{item.name}</button>)}
    </div>
  );
}

export default App;
