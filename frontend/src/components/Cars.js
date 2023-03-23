import './Cars.css';
import React, {useState, useEffect} from "react";
import axios from 'axios';

function Cars() {
    const [data, setData] = useState([])
    useEffect(() => {
        axios.get('http://127.0.0.1:8000/cars/api')
            .then(response => setData(response.data))
            .catch(error => console.log(error))
    }, []);
    return (
        <div>
            {data.map((item, index) => (
                <p key={index}>{item.make} / {item.model} / {item.year} / {item.engine_type}</p>
            ))}
        </div>
    );
}

export default Cars;
