import './Contact.css'
import React, {useState} from 'react';

function Contacts() {
    const [email, setEmail] = useState('');
    const [name, setName] = useState('');
    const [text, setText] = useState('');
    const [error, setError] = useState()

    function isValidEmail(email) {
        return /\S+@\S+\.\S+/.test(email);
    }

    const handleChange = event => {
        if (!isValidEmail(event.target.value)) {
            setError('Invalid Email address');
        } else {
            setError(null);
        }

        setEmail(event.target.value);
    };
    const handleSubmit = (e) => {
        // e.preventDefault();
        alert('You have submitted');
        const email = e.target[0].value
        const name = e.target[1].value
        const text = e.target[2].value


        fetch('http://127.0.0.1:8000/contact/api', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({email: `${email}`, name: `${name}`, text: `${text}`}),
        })
            .then(response => response.json())
            .then(data => {

            })
            .catch(error => {
                // Handle errors here
            });
        e.target.reset();

    }
    return (
        <div className={'contact__form'} id={'contact'}>
            <h2>Contact us</h2>
            <form className='form' onSubmit={handleSubmit}>
                <div className='form-control'>
                    <label htmlFor='firstName'>Email: </label>
                    <input
                        type='text'
                        id='firstName'
                        name='firstName'
                        value={email}
                         onChange={handleChange}
                        // onChange={(e) => setEmail(e.target.value)}
                    />
                    {error && <h2 style={{color: 'red'}}>{error}</h2>}
                    <label htmlFor='firstName'>Name: </label>
                    <input
                        type='text'
                        id='firstName'
                        name='firstName'
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                    <label htmlFor='firstName'>Text: </label>
                    <input
                        type='text'
                        id='firstName'
                        name='firstName'
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                    />
                </div>
                <button type='submit'>Submit Request</button>
            </form>
        </div>
    )
}

export default Contacts