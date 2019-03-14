import 'bootstrap';
import Vue from 'vue'
import GarageList from './components/garagelist.vue'

window.eventHub = new Vue();

Vue.component('modal', {
  template: '#modal-template',
  props: ['show'],
  data: function () {
    return {
      gname: '',
      gbrand: '',
      doge: ''
    };
  },
  methods: {
    saveGarage: function () {
      var self = this
      $.ajax({
          method: 'POST',
          url: '/garages',
          data: { name: this.gname, brand: this.gbrand },
          success: function() {
                console.log('dawawdadwadw');
                eventHub.$emit('refreshList');
                self.$emit('close');
          }
      });
    }
  },
  mounted: function () {
    document.addEventListener('keydown', function(e) {
      if (e.keyCode == 27) {
        this.$emit('close');
      }
    });
  }
});

new Vue({
    el: "#garages",
    data: {
      showModal: false
    },
    components: {
      GarageList
    }
});


// var a = [
//   "We're up all night 'til the sun",
//   "We're up all night to get some",
//   "We're up all night for good fun",
//   "We're up all night to get lucky"
// ];
// 
// // These two assignments are equivalent:
// 
// // Old-school:
// var superduper = a.map(function(s){ return s.length });
// console.log(superduper)
// 
// // ECMAscript 6 using arrow functions
// var superduper3 = a.map( s => s.length );
// console.log(superduper3)
// 
// let add = (x,y) => x + y;
// let result = add(1,1);
// console.log(result);

$('body').on('click', '.edit-garage', function() {
  alert('dwadawadw');
  //eventHub.$emit('refreshList');
});
