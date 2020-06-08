import React from 'react';
import './css/footer.css'

function Footer(){
    return(
        <div className='footer__main'>
            <h1>PerceptronAI</h1>
            <div className='footer__main__div'>
                <div className='footer__sub'>
                    <h3>Contact Us</h3>
                    <ul>
                        <li><a href='#'>LinkedIn</a></li>
                        <li><a href='#'>Github</a></li>
                        <li><a href='#'>Facebook</a></li>
                        <li><a href='#'>Twiiter</a></li>
                    </ul>
                    
                </div>
                <div className='footer__legal'>
                    <h3>Important Resources</h3>
                    <ul>
                        <li><a href='#'>Privacy Policy</a></li>
                        <li><a href='#'>Terms and Condition</a></li>
                    </ul>
                </div>

                <div className='footer__important__resources'>
                    <h3>Blogs</h3>
                    <ul>
                        <li><a href='#'>Machine Learning</a></li>
                        <li><a href='#'>Fiction</a></li>
                        <li><a href='#'>Non-Fiction</a></li>
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default Footer;