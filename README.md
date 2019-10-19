# restoapi
 Exercice graphql et vue js

# Use axios to get graphQl data

## Structure

```bash
methods:{
        getdata: function(){
            this.base_url = '127.0.0.1:8000'
            console.log('data getting')
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            

            axios({
                url: this.base_url + '/graphql',
                method: 'post',
                data: {
                    query: `
                    
                        # Your query her !
                        # copier et coller la query içi !
                    `
                }
            })
            .then(response => {
            
                result = response.data
                # get different data
                
                
            })  
            .catch((err) => {
               
                console.log(err);
            })
        },
}

```

## Aplication
```bash

methods:{
        getdata: function(){
            console.log('data getting')
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            

            axios({
                url: this.base_usl + '/graphql',
                method: 'post',
                data: {
                    query: `
                    query{
                        allCategories(statut:true){
                            edges{
                                node{
                                    id
                                    titre,
                                    platcateg(menu_Position:1){
                                    edges{
                                        node{
                                            titre,
                                            imageMenu,
                                            ingredient,
                                            prix,
                                            }
                                        }
                                    }
                                }
                            }
                    },
                    allAcceuils(first:1, statut:true){
                        edges{
                            node{
                                titre,
                                videoUrl,
                            }
                            }
                        },
                        allImgacceuils(statut:true){
                            edges{
                            node{
                                image,
                            }
                            }
                        },
                        
                        allAbouts(statut:true, first:1){
                            edges{
                            node{
                                titre,
                                description,
                                image,
                            }
                            }
                        },
                        
                        allTestimonials(statut:true){
                            edges{
                            node{
                                message,
                                user,
                                role
                            }
                            }
                        },
                        
                            allHorraires(statut:true, first:6){
                            edges{
                            node{
                                jour,
                                heureDebut,
                                heureFin
                            }
                            }
                        }
                    }
                    `
                }
            })
            .then(response => {
            
                result = response.data
                this.datamenu = result.data.allCategories.edges
                this.dataacceuil = result.data.allAcceuils.edges[0].node
                this.dataabout = result.data.allAbouts.edges[0].node
                this.dataaccimage = result.data.allImgacceuils.edges
                this.datatesti = result.data.allTestimonials.edges
                
                
            })  
            .catch((err) => {
               
                console.log(err);
            })
        },
}

```
