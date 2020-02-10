<template>
    <div>
        <h1>Home</h1>
        <h2>{{ msg }}</h2>
        <router-link to="/garages">Garages</router-link>
    </div>
</template>

<script>
    export default {
        name: "Home",
        data () {
            return {
                msg: 'Welcome to Your Appengine/Vue app the garage'
            }
        }
    }
</script>

<style scoped>

</style>