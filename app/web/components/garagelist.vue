<template>
	<div>
		<h1>Garages</h1>
		<ul>
		    <li v-for="g in garagelist">{{ g.name }} <button type="button" class="btn btn-primary edit-garage">Edit</button></li>
		</ul>
	</div>
</template>

<script>
	//import eventHub from './eventHub.vue'
    export default {
      name: 'garage-list',
      data: function () {
        return {
            garagelist: []
        }
      },
      methods: {
        getList: function() {
            var self = this
            $.ajax({url:'/garages',
                success: function(data) {
                    self.garagelist = data
                }
            });
        }
      },
      created: function() {
        this.getList();
				eventHub.$on('refreshList', this.getList);
      }
    }


</script>

<style>
	.edit-garage { float:right; }
</style>
