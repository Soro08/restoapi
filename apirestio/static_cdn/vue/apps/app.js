new Vue({
    el: '#my-app',
    data : {
      message : 'app message',
    },
    components: {
      'my-comp': httpVueLoader('my-comp.vue')
    }
  });