import React,{ useState }from 'react'
import './css/nav.css'


const Nav = ({open})=>{
    
    return(
        <header>
            <h3 className='brand'>PerceptronAI.</h3>
            <nav>
                
                <ul className='nav__links' open={open}>
                    <li><a href='#'>Home</a></li>
                    <li><a href='#'>About</a></li>
                    <li><a href='#'>Work</a></li>
                    <li><a href='#'>Education</a></li>
                    <li><a href='#'>Machine Learning</a></li>
                    <li><a href='#'>Blog</a></li>
                    <li>.</li>
                </ul>
                <div className="burger">
                    <div className="line1"></div>
                    <div className="line1"></div>
                    <div className="line1"></div>
                </div>
                
            </nav>


        </header>
        
 )

}

export default  Nav;


