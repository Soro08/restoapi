new Vue({
    el: '#my-app',
    data : {
      message : 'app message',
      base_usl : 'http://127.0.0.1:8000'
    },
    components: {
      'my-menu': httpVueLoader('/static/vue/components/menu.vue'),
      'my-special': httpVueLoader('/static/vue/components/specialite.vue')
    },
    mounted(){
      this.getdata();
    },

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
                        allMenus(statut:true){
                            pageInfo{
                                hasNextPage,
                                hasPreviousPage,
                                startCursor,
                                endCursor
                            }
                            edges{
                            node{
                                jour,
                                statut
                            }
                            }
                        }
                    }
                    `
                }
            })
            .then(response => {
                myshop = response.data

                console.log('getting..')
                

                console.log(response.data)
                //this.loading = false;
            })
            .catch((err) => {
                //this.loading = false;
                console.log(err);
            })
        }
    }
});