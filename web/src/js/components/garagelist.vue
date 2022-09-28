<template>
  <div class="grid-container">
    <div class="title">
      <h1>Garages</h1>
      <new-garage @change="garageList.push($event)"></new-garage>
    </div>
    <ul class="list-group">
      <li v-for="g in garageList" :key="g.id" class="list-group-item">
        <!-- when a garage item is deleted it will raise change event and return the new list, so the $event is basically the data of the new list that was passed when change was raised -->
        <garage-list-item :garage="g" @change="garageList.splice(garageList.findIndex(x=> x.id === g.id), 1)">hello</garage-list-item>
        <!-- @change="garageList = $event" -->
      </li>
    </ul>
  </div>
</template>

<script>
import GarageListItem from "./garage-list-item";
import GarageForm from "./garage-form";
import NewGarage from "./new-garage";

export default {
  name: "garage-list",
  components: { NewGarage, GarageListItem, GarageForm },
  data: function () {
    return {
      garageList: [],
      garageDialog: true,
    };
  },
  methods: {
 
    load() {
      $.ajax({
        type: "GET",
        url: `/garages/`,
        contentType: "application/json",
        timeout: 60000,
      })
        .then((data) => {
          console.log("this is data");
          console.log(data);
          this.garageList = data;
          console.log(this.garageList);
        })
        .always(() => {
          // this.loading = false
        });
    },
  },
  created: function () {
    this.load();
  },
};
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: 2fr 6fr;
  grid-gap: 10px;
  grid-auto-rows: min-content;
  grid-template-areas: "title garage-list ";
}

.title {
  grid-area: title;
  margin-right: 20px;
}
.list-group {
  grid-area: garage-list;
}
.add-garage {
  margin: 4px;
}
</style>
