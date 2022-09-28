<template>
  <div>
    <div class="row">
      <label class="col-sm-4">Name</label>
      <input type="text" class="col-sm-8" v-model="myGarage.name" />
    </div>
    <div class="row">
      <label class="col-sm-4">Brand</label>
      <input type="text" class="col-sm-8" v-model="myGarage.brand" />
    </div>
    <div class="row">
      <label class="col-sm-4">Country</label>
      <input type="text" class="col-sm-8" v-model="myGarage.postal_country" />
    </div>
    <div class="row">
      <button class="pull-right btn btn-success" @click="save">Save</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "new-garage",
  props: {
    garage: {
      type: Object,
      required: false,
      default() {
        return {name:"",brand:"",postal_country:""};
      }
    },
  },
  data() {
    return {
      myGarage: {
        name: "",
        brand: "",
        postal_country: "",
      },
    };
  },
  methods: {
    save() {
      console.log(this.myGarage);
      console.log("hello");
      $.ajax({
        type: "POST",
        url: `/garages/`,
        contentType: "application/json",
        data: JSON.stringify(this.myGarage),
        timeout: 2000,
      })
        .then((data) => {
          this.$emit("change", data);
          console.log("to check if being set inside save");
          console.log(data);
          this.resetForm();
        })
        .always(() => {
          // this.loading = false
        });
    },
    resetForm() {
      if (this.myGarage.id) {
        Object.assign(this.myGarage, this.garage);
      } else {
        this.myGarage.name = "";
        this.myGarage.brand = "";
        this.myGarage.postal_country = "";
        console.log("are you being reset");
      }
    },
  },
};
</script>

<style scoped></style>
