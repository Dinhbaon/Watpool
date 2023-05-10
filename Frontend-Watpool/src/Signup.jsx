import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import { useEffect } from 'react'

export default function Signup() {

    const [emailValid, setEmailValid] = useState(true)
    console.log(emailValid)

    const loginSubmit = (e) =>{
      e.preventDefault();
      // Read the form data
      const form = e.target;
      const formData = new FormData(form); 
      const formJson = Object.fromEntries(formData.entries());
      let idx = formJson.email.indexOf('@')
      if (idx > -1 && formJson.email.slice(idx + 1) === 'uwaterloo.ca'){
        setEmailValid(true); 
        console.log(formJson);
        const requestOptions = {
          method: 'POST',
          headers:  {
            'Content-Type': 'application/json',
            'accept': 'application/json',
        },
          body: JSON.stringify(formJson),
          mode: 'cors'
        }
        fetch('http://127.0.0.1:8000/api/register/', requestOptions).then(response => response.json())
        .then(data => {
          console.log('Success:', data);
        })
        .catch(error => {
          console.error('Error:', error);
        });
      }else{
        setEmailValid(false)
        return
      }
  }
    return (
        <div>
        <form method="post" id='login-form' onSubmit={loginSubmit}>
          <div><input type = "text" id="email" name="email"/></div>
          <div><input type = "text" id = "password" name="password"/></div>
          <button type='submit'>Submit</button>
      {emailValid ? null : <div>Please Enter Your Uwaterloo Email</div> }
        </form>
      </div>
    )
}
