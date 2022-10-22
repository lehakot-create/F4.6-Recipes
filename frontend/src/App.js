import axios from 'axios';
import {useEffect, useState} from "react";

function App() {
  const [category, SetCategory] = useState({});

  async function getCategory() {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/category/')
      console.log(response)
    } catch (error) {
      console.log(error);
    }

  }

  useEffect(() => {
    getCategory()
  }, []);

  return (
    <div>
      Hello from frontend!
    </div>
  );
}

export default App;
