import React from 'react';
import axios from 'axios';

const Login = () => {

    function myfunction() {

        // quiero pasarle 2 parametros a la request que hace el axios.get
        // el primero es el email y el segundo es el password
        // pero no se como hacerlo
        

        axios.get('http://127.0.0.1:8000/polls/register', {
            params: {
                name: 'name',
                email: 'email',
                password: 'password',
            }
        })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });   
    }

    return (
        <div styles={ styles.mainContainer }>
            <input type="text" placeholder='email'/>
            <input type="password" placeholder='password'/>

            <button onClick={myfunction}>Click me</button>
        </div>
    );
};



export default Login;

const styles = {

    mainContainer: {
        display: 'flex',
        flexDirection: 'column',
    },
};