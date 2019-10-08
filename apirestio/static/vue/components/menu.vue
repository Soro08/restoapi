<template>

    <div class="col-lg-4 menu-wrap">
        <div class="heading-menu">
            <h3 class="text-center mb-5">${ todo.node.titre }</h3>
        </div>
        <my-plats
            v-for="plat in todo.node.platcateg.edges"
            v-bind:listplat="plat"
            v-bind:key="plat.id"
        ></my-plats>
    </div>

</template>


<script>

    module.exports = {
        data: function(){
            return {
                mess : " salut ",
            }
        },
        props:['todo',],
        delimiters: ["${", "}"],
        components: {
            'my-plats': httpVueLoader('/static/vue/components/plats.vue'),
        },
    }

</script>