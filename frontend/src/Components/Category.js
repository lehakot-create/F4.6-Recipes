import axios from "axios"
import { useEffect, useState } from "react"

import { Button } from "./Button"

export function Category(props) {
    const [recipes, setRecipes] = useState([])
    async function getRecipes() {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/v1/recipes/')
            console.log(response.data)
            setRecipes(response.data)
        } catch (error) {
            console.log(error)
        }
    }

    useEffect(() => {
        getRecipes()
        
    }, []);
    return (
        <div>
            <h2>{props.name}</h2>
            {recipes && recipes.map((item, index)=> <Button name={item.title}/>)}
        </div>
    )
}