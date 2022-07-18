<template>
    <div class="about">
        <h1>Garage list</h1>

        <hr
            style="margin: 10px;"
        >
        <form
            class="form-col"
            >
            <label>
                <span>Naam</span>
                <input
                    v-model="newGarage.name"
                />
            </label>
        </form>
    </div>
</template>

<script>
    export default {
        name: "Garage",
        data() {
            return {
                garages: [],
                newGarage: {}
            }
        }
    }
</script>

<style scoped>

</style>