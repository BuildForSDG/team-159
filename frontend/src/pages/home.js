import React from 'react';

const Home = () => {
  
  function sayHello() {
    console.log('Hello, World!');
  }
  
  return (
    <button onClick={sayHello}>Click me!</button>
  );
};

export default Home;