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

        <section id={'cars'} className={'car__article'}>

            {data.map((item, index) => (
                <article className={`car__item`}>
                    {/*<p  key={index}>{item.make} / {item.model} / {item.year} / {item.engine_type}*/}
                    {/*</p>*/}
                    <img alt={'car'} src={item.image}/>

                    <p>Make: {item.make}</p>
                    <p>Model: {item.model}</p>
                    <p>Year: {item.year}</p>
                    <p>Engine: {item.engine_type}</p>
                    <div className={'button__wrapper'}>
                        <button className={'buy__btn'}>BUY</button>
                        <button className={'rent__btn'}>RENT</button>
                    </div>
                </article>
            ))}
        </section>
    );
}

export default Cars;
