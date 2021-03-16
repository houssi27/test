<template>
  <div id="app">
    <Todos v-bind:todos="todos"/>
  </div>
</template>

<script> 
import Todos from "./components/Todos"
import Todos from './components/Todos.vue';
export default {
  name: 'App',
  components: {
    Todos
  },

  data () {
    return {
      todos:[
       {
          id: 1,
          title: "Todo One",
          completed: false  
       },
       {
          id: 2,
          title: "Todo Two",
          completed: true  
       },
       {
          id: 3,
          title: "Todo Three",
          completed: false  
       },
      ]
    }
  }
};
</script>
