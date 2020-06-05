import React from 'react';
import './css/footer.css'

function Footer(){
    return(
        <div className='footer__main'>
            <h1>PerceptronAI 2020</h1>

            <div className='footer__sub'>
                <h3>Contact Us</h3>
                <ul>
                    <li><a href='#'>LinkedIn</a></li>
                    <li><a href='#'>Github</a></li>
                    <li><a href='#'>Facebook</a></li>
                    <li><a href='#'>Twiiter</a></li>
                </ul>
            </div>
        </div>
    )
}

export default Footer;