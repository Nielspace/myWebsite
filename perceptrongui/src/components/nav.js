import React from 'react'
import './css/nav.css'


function Nav(){
    return(
        <header>
            <h3 className='brand'>PerceptronAI</h3>
            <nav>
                
                <ul className='nav__links'>
                    <li><a href='#'>Home</a></li>
                    <li><a href='#'>About</a></li>
                    <li><a href='#'>Work</a></li>
                    <li><a href='#'>Education</a></li>
                    <li><a href='#'>Machine Learning</a></li>
                    <li><a href='#'>Blog</a></li>
                    <li>.</li>
                </ul>
            </nav>
        </header>
    )
}

export default  Nav;