import React from 'react';

import './css/fetch.css';

class FetchApi extends React.Component{
    constructor(props){
        super(props)

        this.state = {
            items: []
        }
    }

    componentDidMount(props){
        fetch('http://127.0.0.1:8000/api/')
        .then(res=>res.json())
        .then(json=>{
            this.setState({
                items:json,
            })
        });

    }

    render(){
        const {items} = this.state;
        return(
            <div className='Cards'>
                {items.map(item=>
                    <div className='sub__class'>
                        <img className='img_class' src={item.image} />
                        <h1>{item.title}</h1>
                        <p>{item.description}</p>
                        
                        
                    </div>
                    )} 
                
            </div>
        )
    }
}

export default FetchApi;