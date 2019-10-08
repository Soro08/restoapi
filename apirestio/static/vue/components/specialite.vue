<template>
    <div class="hello container">Hello {{ who }}  {{ message }}</div>
</template>
 
<script>
module.exports = {
    data: function() {
        return {
            who: 'world',
        }
    },
    props: ['message'],
}

</script>



<style>
.hello {
    background-color: #ffe;
}
</style>