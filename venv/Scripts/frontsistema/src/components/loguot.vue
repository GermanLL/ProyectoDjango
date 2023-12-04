<template>
    <div>
        <h1 class="display-1 text-center">Logout</h1>
        
    </div>
    </template>
    
    <script>
    import axios from "axios"
    export default {
        //////
      name: 'Logout',
      data() {
          return {
              username: "",
              password: "",
          }
      },
      ///////
      methods: {
          loguear() {
            axios({
                  url: 'http://127.0.0.1:8000/auth/token/login/',
                  headers: {Authorization : "token" + this.$tore.getters.getToken},
                  method: 'POST'
            }).then((response) => {
                //console.log(response.data);
                this.$store.comit('unLogUser');
                this.$router.push('/');
            });
          },
      },
      mounted() {
          //
      },
    };
    </script>