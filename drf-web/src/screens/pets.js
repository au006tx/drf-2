import React from 'react';


class Pets extends React.Component {
    constructor(props) {
        super(props) 
        this.state = {
            pets : []    
        }
    }


    componentDidMount() {
        console.log('Fetching.....');
        fetch("https://varunpsr.github.io/pets.json")
            .then(response => response.json())
            
            .then(data => {
                this.setState({
                    pets: data
                }) 
            })  
            .catch((e) => {
                console.log('Looks like there was a problem: \n', e);
            });
    }; 

    allpetsdata() {
        return this.state.pets.map((item,index) => (            
            <div key={index}>
                <h1>
                    {item.name}
                </h1>
  
            </div>
            
            
            )            
        )
    }


    render(){
        const pets = this.state.pets; 
        console.log(pets);
       
        return(
            <div>
                <h2> Data </h2>
                    <div>
                    {this.allpetsdata()}
                </div>
  
            </div>
        )
    };
}

export default Pets;
