<template>
    <dialog
        title="New garage"
    >
        <new-garage></new-garage>
    </dialog>
</template>

<script>
    import Modal from './modal'
    import NewGarage from "./new-garage";
    export default {
        name: "new-garage-dialog",
        components: {
            NewGarage,
            Modal
        }
    }
</script>

<style scoped>

</style>