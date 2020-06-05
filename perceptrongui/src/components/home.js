import React from 'react'
import './css/home.css'

function Home(){
    return(

        <main class='main__class'>
            <div class='Intro'>
                
            </div>

            <div class='section'> 
                <div class='Intro_work'>
                    <h1>Work</h1>
                    <p>Find out what we do.</p>
                </div>

                <div class='Intro_education'>
                    <h1>Education</h1>
                    <p>Learn about our courses.</p>
                </div>

                <div class='Intro_ml'>
                    <h1>Artificial Intelligence</h1>
                    <p>Data Viz and AI archive.</p>
                </div>

                <div class='Intro_blog'>
                    <h1>Blog</h1>
                    <p>We share what we percieve.</p>
                </div>
            </div>
        </main>


    )
}

export default Home;