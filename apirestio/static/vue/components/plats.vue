<template>
    <div class="menus d-flex align-items-center">
        <div class="menu-img rounded-circle">
            <img class="img-fluid" :src="'media/'+listplat.node.imageMenu" alt="">
        </div>
        <div class="text-wrap">
            <div class="row align-items-start">
                <div class="col-8">
                    <h4>${ listplat.node.titre }</h4>
                </div>
                <div class="col-4">
                    <h4 class="text-muted menu-price">${ listplat.node.prix }</h4>
                </div>
            </div>
            <p>${ listplat.node.ingredient }</p>
        </div>
    </div>
</template>



<script>

    module.exports = {
        data: function(){
            return {
                mess : " salut ",
            }
        },
        props:['listplat',],
        delimiters: ["${", "}"],
    }

</script>