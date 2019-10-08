new Vue({
    el: '#my-app',
    data : {
        message : 'app message',
        base_usl : 'http://127.0.0.1:8000',
        datamenu : [],
        nom: '',
        email:'',
        phone:'',
        days:'',
        heure:'',
        persone:1,
        messages:'',
    },
    components: {
        'my-menu': httpVueLoader('/static/vue/components/menu.vue'),
        'my-special': httpVueLoader('/static/vue/components/specialite.vue'),
        'my-plats': httpVueLoader('/static/vue/components/plats.vue'),
    },
    delimiters: ["${", "}"],
    mounted(){
        this.getdata();
    },

    methods:{
        getdata: function(){
            console.log('data getting')
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            var d = new Date();
            var n = d.getDay(); console.log(n)

            axios({
                url: this.base_usl + '/graphql',
                method: 'post',
                data: {
                    query: `
                    query{
                        allCategories(statut:true){
                            edges{
                                node{
                                    titre,
                                    platcateg(menu_Position:`+ n +`){
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
                        }
                    }
                    `
                }
            })
            .then(response => {
                result = response.data

                console.log('getting..')
                
                this.datamenu = result.data.allCategories.edges
                console.log(result.data.allCategories)
                //this.loading = false;
            })
            .catch((err) => {
                //this.loading = false;
                console.log(err);
            })
        },
        sendcode() {
            

            console.log(this.messages)
            // let data = JSON.stringify({
            //     code: code,
            //     id_exo: exoid,

            // })

            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'

            // axios.post(this.base_usl + '/add', data, {
            //         headers: {
            //             'Content-Type': 'application/json',
            //         }
            //     })
            //     .then((response) => {

            //         //resultats = JSON.parse(response.data)

            //     })
            //     .catch((err) => {
                    
            //         console.log(err);
            //     })

        },
    }
});