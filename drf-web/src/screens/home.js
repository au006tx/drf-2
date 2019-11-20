import React from 'react';

import axios from 'axios';


class Home extends React.Component {
    constructor(props) {
        super(props) 
        this.state = {
            customer : []    
        }
    }
    // componentDidMount() {
    //     console.log('Fetching.....');
    //     fetch("http://127.0.0.1:8000/crm_app/", {
    //         method: 'GET',
    //         mode: 'no-cors',
    //     }).then(response => response.json()).then(data => {
    //             this.setState({
    //                 customer : data
    //             });
    //             console.log(data);
    //         })  
    //         .catch((e) => {
    //             console.log('Looks like there was a problem: \n', e);
    //         });
    // }; 

    componentDidMount() {
        axios.get("http://127.0.0.1:8000/tweet/")
            .then(response => response.data)
            .then(data => {
                this.setState({
                    customer: data
                }); 
            });
    }

    alldata() {
        return this.state.customer.map((item,index) => (            
            <div key={index}>
                <h1 style={{color: 'red'}}>
                {item.text}
                </h1>
                <div>
                    <h1>
                        {item.user_name}
                    </h1>
                </div>
            </div>  
            )            
        )
    }

    render(){
        console.log('checking....')
        const customer= this.state.customer; 
        console.log(customer)       
        return(
            <div>
                <h2> Data </h2>
                    <div>
                        {this.alldata()}
                    </div>
            </div>
        )
    };
}

export default Home;
