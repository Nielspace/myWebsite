import React from 'react';
import './App.css';
import FetchApi from './components/fetch';
import Nav from './components/nav';
import Home from './components/home';
import Quote from './components/quote';
import Footer from './components/footer';
import Featured from './components/featuredPost';
import Subfeatured from './components/subPost';



class App extends React.Component{
  render(){
    
      return(
        
        <div>
          <Nav />
          <Home />
          <Quote />
          <Featured />
          <Subfeatured />
          <FetchApi/>
          <Footer />
        </div>
      );
    }
    
      

  }


export default App;
