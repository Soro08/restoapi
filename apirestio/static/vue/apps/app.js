var app = new Vue({
    el: '#my-app',
    data : {
        message : 'app message',
        base_usl : 'http://127.0.0.1:8000',
        datamenu : [],
        dataacceuil:[],
        dataaccimage:[],
        dataabout:[],
        datatesti:[],
        datateam:[],
        nom: '',
        email:'',
        phone:'',
        days:'',
        heure:'',
        persone:1,
        messages:'',
        loaddata:true,
    },
    components: {
        'my-menu': httpVueLoader('/static/vue/components/menu.vue'),
        'my-special': httpVueLoader('/static/vue/components/specialite.vue'),
        'my-plats': httpVueLoader('/static/vue/components/plats.vue'),
    },
    delimiters: ["${", "}"],
    mounted(){
        this.getdata();
        //jQuery(this.$refs.carousel_or_anything).owlCarousel();
    },
    // ready: function() {
        
    //     Vue.nextTick(function () {
    //         this.installOWLcarousel();
    //     }.bind(this))
    //  },
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

                console.log('getting..')
                
                this.datamenu = result.data.allCategories.edges
                this.dataacceuil = result.data.allAcceuils.edges[0].node
                this.dataabout = result.data.allAbouts.edges[0].node
                this.dataaccimage = result.data.allImgacceuils.edges
                this.datatesti = result.data.allTestimonials.edges
                //this.datateam = result.data.allImgacceuils.edges
                console.log(result.data.allAcceuils.edges[0].node)
                this.loaddata = false;
                //this.loading = false;
                var vm = this; //declare this just BEFORE calling axios();
                // The below are inside axios.then()
                
                Vue.nextTick(function(){
                    $(".hero-carousel").owlCarousel({
                        loop:!0,
                        margin:10,
                        nav:!0,
                        dots:!1,
                        responsive:{
                            0:{
                                items:1
                            },
                            600:{
                                items:1
                            }
                        },
                        nav:!0,
                        navText:['<span class="lnr lnr-chevron-left"></span>','<span class="lnr lnr-chevron-right"></span>']
                    });
                    $(".testi-carousel").owlCarousel({
                        loop:!0,margin:10,autoplay:!0,nav:!1,dots:!0,
                        dotSpeed:1e3,autoplay:!0,autoplaySpeed:1e3,items:1
                    });
                    $('.owl-user').owlCarousel({
                        rtl:true,
                        loop:true,
                        margin:10,
                        autoplay:!0,nav:!1,dots:!0,
                        dotSpeed:1e3,autoplay:!0,autoplaySpeed:1e3,
                        nav:false,
                        responsive:{
                            0:{
                                items:1
                            },
                            600:{
                                items:2
                            },
                            1000:{
                                items:2
                            }
                        }
                    })

                })
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
    },
    directives: {
        
    }
});